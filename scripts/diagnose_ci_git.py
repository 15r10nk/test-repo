"""Print only Git metadata needed to validate the changelog hook in CI."""

import os
import subprocess

for name in (
    "CI", "PRE_COMMIT", "PRE_COMMIT_FROM_REF", "PRE_COMMIT_TO_REF",
    "PRE_COMMIT_REMOTE_NAME",
):
    print(f"{name}={os.environ.get(name, '<unset>')}", flush=True)

for args in (
    ("rev-parse", "--is-shallow-repository"),
    ("rev-list", "--count", "HEAD"),
    ("log", "--max-count=8", "--format=%h %p"),
    ("for-each-ref", "--format=%(refname)"),
    ("merge-base", "HEAD", "origin/main"),
    ("merge-base", "HEAD", "main"),
):
    print(f"\n$ git {' '.join(args)}", flush=True)
    result = subprocess.run(["git", *args], capture_output=True, text=True)
    print(f"exit={result.returncode}")
    print(result.stdout.strip())
    print(result.stderr.strip())
