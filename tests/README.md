# Tests

The initial service is intentionally a scaffold. Before production deployment, add automated tests for:
- `/health` liveness.
- Rejection of missing and invalid bearer tokens.
- The router status placeholder returning `connected: false` until VPN and read-only RouterOS access are configured.
- Input validation, rate limits, and redaction of subscriber data before adding any router tools.
