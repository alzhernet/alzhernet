# Alzher Net Cloud Bridge

A small, security-first service intended to connect the Alzher Net ElevenLabs voice agent to a MikroTik RouterOS 7 CCR2116 through a private VPN.

## Current status

This is a deployment scaffold, **not a live router integration**. The service currently exposes:
- `GET /health` — liveness check.
- `GET /v1/router/status` — authenticated placeholder that explicitly reports the router as disconnected.

No router credentials, VPN keys, or API secrets belong in this repository. No public WinBox, SSH, or RouterOS API exposure is required or supported.

## Deploy on Ubuntu 24.04 with Docker

1. Install Docker Engine and the Docker Compose plugin on your VPS.
2. Clone this repository:
   `git clone https://github.com/alzhernet/alzhernet.git && cd alzhernet`
3. Create a private environment file:
   `cp .env.example .env`
4. Generate a strong token and place it in `.env`:
   `openssl rand -hex 32`
5. Start the service:
   `docker compose up -d --build`
6. Check locally on the VPS:
   `curl http://127.0.0.1:8000/health`

The Compose configuration binds the API to localhost only. Put it behind a correctly configured HTTPS reverse proxy before connecting ElevenLabs. Do not expose port 8000 directly to the internet.

## Router connection plan

The intended path is:

`ElevenLabs agent -> HTTPS reverse proxy -> Cloud Bridge -> private VPN -> CCR2116`

Before enabling router queries:
1. Establish and test a private VPN route from the VPS to the router. Do not assume the MikroTik Back To Home relay automatically provides a server-to-router route; verify the actual topology and supported client/server mode.
2. Create a dedicated RouterOS account with narrowly scoped read-only permissions.
3. Keep VPN keys and RouterOS credentials in a server-side secret store or private `.env`, never in Git.
4. Add and test specific read-only operations, then expose only those operations as ElevenLabs tools.

## Security boundaries

- Read-only scope only; no reboot, disconnect, write, or configuration operations.
- No router management ports exposed publicly.
- API token required for protected endpoints.
- Compose binds to `127.0.0.1`; HTTPS termination is expected at a reverse proxy.
- Return the minimum data required by the voice agent and redact customer-identifying information.
- Add rate limiting, audit logging, and monitoring before production use.

See [docs/SECURITY.md](docs/SECURITY.md) and [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md).
