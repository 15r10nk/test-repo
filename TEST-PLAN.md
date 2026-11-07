# Changelog hook experiment

This branch tests the Git context actually provided by pre-commit.ci.
The diagnostic hook prints only selected environment variables and Git metadata.
The changelog hook is copied from the locally prepared pre-commit-checks 0.2.0.
Both hooks use the normal pre-commit stage so the hosted service can run them.

Cases:

1. A feat commit without a fragment must fail.
2. A fragment committed separately must make the check pass.
3. Removing that fragment in a later push must make the check fail again.
4. A docs-only branch without a fragment must pass.
5. A pull request targeting a branch other than main must use its actual base.

The first PR intentionally starts with case 1. No changes need to be merged.
