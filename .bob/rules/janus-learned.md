# Rules learned by Janus

These rules were written by Janus after fixing real drift in this project.
Every mode must follow them.

## Config / Secrets
- Never leave a secret in source code; replace hardcoded values with `os.environ.get("KEY", "")` and add the key (empty) to `.env.example` and every deploy config with a comment `# set in the secret manager`.
- Every env var used anywhere in the code must appear in `.env.example`; every deploy config must carry all production vars.

## Docs
- README env var names must exactly match the names read by the code (e.g. `DATABASE_URL`, not `DB_URL`).
- The README start command must reference a file that actually exists; use the real invocation when the entry-point file is absent.
- README port numbers must match the value in config/code, not an assumed default.
- Do not document phantom endpoints; remove them from the README.
- Every route that exists in the code must be documented in the README.

## Tests
- Every undocumented endpoint found by janus must get at least one happy-path test covering status code and response shape.
