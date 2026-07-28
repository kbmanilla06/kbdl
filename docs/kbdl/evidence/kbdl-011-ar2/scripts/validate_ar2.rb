#!/usr/bin/env ruby

require "csv"
require "open3"

ROOT = File.expand_path("../../../../..", __dir__)
BASE = "a6b416e20f1b0c933aa75fe1c4dd0e04c9118179"
RECOVERY = File.join(ROOT, "docs/kbdl/evidence/kbdl-011-authority-recovery")

def fail!(message)
  warn "FAIL: #{message}"
  exit 1
end

def git(*args)
  out, err, status = Open3.capture3("git", *args, chdir: ROOT)
  fail!("git #{args.join(' ')}: #{err}") unless status.success?
  out
end

ledger_path = File.join(RECOVERY, "authority-recovery-ledger.csv")
mapping_path = File.join(RECOVERY, "artifacts/requirement-authority-mapping.csv")
review_path = File.join(RECOVERY, "project-owner-review.md")
packet_path = File.join(RECOVERY, "authority-recovery-packet.md")
gaps_path = File.join(RECOVERY, "authority-gaps.csv")
decision_path = File.join(RECOVERY, "project-owner-authority-confirmations.md")

ledger = CSV.read(ledger_path, headers: true)
mapping = CSV.read(mapping_path, headers: true)
gaps = CSV.read(gaps_path, headers: true)
review = File.read(review_path)
packet = File.read(packet_path)
decision = File.read(decision_path)

ids = (1..11).map { |n| format("KBDL-%03d", n) }
fail!("ledger prompt IDs are not exactly KBDL-001 through KBDL-011") unless ledger.map { |r| r["Prompt ID"] } == ids
fail!("decision count") unless ledger.count { |r| r["Project-owner decision"] == "CONFIRM CURRENT AUTHORITY" } == 11
fail!("decision date") unless ledger.all? { |r| r["Decision date"] == "2026-07-28" }
fail!("durable evidence") unless ledger.all? { |r| r["Decision evidence"].include?("project-owner-authority-confirmations.md") }
fail!("recovery classification") unless ledger.all? { |r| r["Recovery status"] == "CONFIRMED — CURRENT NON-RETROACTIVE AUTHORITY" }
fail!("original commands changed") unless ledger.all? { |r| r["Approval command recovered"] == "NO" }
fail!("selected review options") unless review.scan(/- \[x\] CONFIRM CURRENT AUTHORITY/).length == 11
fail!("unexpected selected option") unless review.scan(/- \[x\]/).length == 11
fail!("pending decision remains") if review.include?("____________________") || packet.include?("Project-owner decision: PENDING")
fail!("packet confirmations") unless packet.scan(/Project-owner decision: CONFIRM CURRENT AUTHORITY/).length == 11
fail!("packet effective dates") unless packet.scan(/Decision date:\*\* 2026-07-28 \(Asia\/Manila\)/).length == 11
fail!("durable decision enumeration") unless ids.all? { |id| decision.include?("`#{id}: CONFIRM CURRENT AUTHORITY`") }

baseline_csv = git("show", "#{BASE}:docs/kbdl/evidence/kbdl-011-authority-recovery/authority-recovery-ledger.csv")
baseline = CSV.parse(baseline_csv, headers: true)
before_sets = baseline.to_h { |r| [r["Prompt ID"], r["Requirements relying on the prompt"]] }
after_sets = ledger.to_h { |r| [r["Prompt ID"], r["Requirements relying on the prompt"]] }
fail!("AR1 relying-requirement sets changed") unless before_sets == after_sets

fail!("mapping count") unless mapping.length == 137
fail!("mapping prompt coverage") unless (mapping.map { |r| r["Prompt ID"] }.uniq.sort == ids)
fail!("mapping confirmation date") unless mapping.all? { |r| r["Confirmation date"] == "2026-07-28 (Asia/Manila)" }
fail!("mapping decision source") unless mapping.all? { |r| r["Durable decision source"].include?("KBDL-DEC-016") }
sole = mapping.count { |r| r["Authority dependency"] == "SOLE PROMPT" }
mixed = mapping.count { |r| r["Authority dependency"] == "MIXED" }
fail!("sole/mixed totals") unless [sole, mixed] == [113, 24]

fail!("historical gap count") unless gaps.count { |r| r["Gap ID"] != "KBDL-AR-GAP-012" } == 11
fail!("historical gap status") unless gaps.all? { |r| r["Blocking status"] == "HISTORICAL GAP OPEN; CURRENT AUTHORITY RESOLVED" }
gap12 = gaps.find { |r| r["Gap ID"] == "KBDL-AR-GAP-012" }
fail!("KBDL-005 scope separation") unless gap12 && gap12["Required project-owner action"].include?("preserve DEC-014 separation")

changed = git("diff", "--name-only", BASE).lines.map(&:strip)
allowed = [
  "docs/kbdl/README.md",
  "docs/kbdl/decision-register.md",
  "docs/kbdl/traceability-matrix.md",
  "docs/kbdl/validation.md"
]
fail!("normative or unrelated files changed") unless changed.all? { |p| allowed.include?(p) || p.start_with?("docs/kbdl/evidence/kbdl-011-authority-recovery/") || p.start_with?("docs/kbdl/evidence/kbdl-011-ar2/") }
fail!("traceability metadata changed") unless git("diff", "--quiet", BASE, "--", "docs/kbdl/traceability-metadata.csv").empty?

puts <<~SUMMARY
  Prompt confirmations recorded: 11
  Missing confirmations: 0
  Duplicate confirmations: 0
  Pending owner decisions: 0
  Current non-retroactive confirmations: 11

  Requirement-authority mappings: 137
  Unresolved current-authority mappings: 0
  Sole-prompt mappings: #{sole}
  Mixed-authority mappings: #{mixed}

  Original approval commands recovered: 0
  Historical approval records still unrecovered: 11
  Backdated approval claims: 0
  KBDL-005 scope conflations: 0

  Normative requirement changes: 0
  Lifecycle changes: 0
  Provenance changes: 0
  Validation-status promotions: 0
  Recommendation promotions: 0
  Deferred promotions: 0
  Accepted limitations: 0
  Readiness approvals: 0
  Completion approvals: 0

  Implementation conformance: NOT VERIFIED
  Project completion: PENDING
SUMMARY
