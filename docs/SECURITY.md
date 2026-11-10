# Security and rollout

1. Keep WinBox, SSH, and the RouterOS API off the public internet.
2. Establish a private VPN route from this server to the router before enabling router queries.
3. Create a dedicated RouterOS account with the minimum read-only permissions needed.
4. Store VPN keys and API tokens only in the server secret store or local .env file.
5. Keep the agent-facing API behind HTTPS, bearer authentication, and rate limiting.
6. Return only the minimum data needed by the voice agent; redact customer identifiers where possible.
7. Do not implement write operations, reboot, disconnect, or configuration changes in this project.

The current router endpoint is deliberately a placeholder and reports disconnected until the VPN and RouterOS read-only account are configured and verified.
