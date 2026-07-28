# Post-Commit Evidence Boundary

The R11 commit SHA, parent, push output, final live remote SHA, and final clean
tree are reported after the single remediation commit is created and pushed.
They cannot be embedded truthfully inside that same commit without changing its
SHA. The committed evidence package contains the reproducible commands and all
precommit evidence; the implementation result supplies the resulting post-commit
values.
