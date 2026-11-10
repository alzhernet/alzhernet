# VPS deployment (Ubuntu 24.04)

## Before you begin
You need an Ubuntu 24.04 VPS with Docker Engine and the Docker Compose plugin installed. DNS and an HTTPS reverse proxy are separate deployment steps.

## Configure
```bash
git clone https://github.com/alzhernet/alzhernet.git
cd alzhernet
cp .env.example .env
openssl rand -hex 32
```

Put the generated value into `BRIDGE_API_TOKEN` in the server's `.env` file. Keep this file private; never commit it or send it in chat.

## Start and verify
```bash
docker compose up -d --build
docker compose ps
curl http://127.0.0.1:8000/health
```

The API listens only on the VPS loopback interface. Configure a reverse proxy with HTTPS and authentication protections before allowing ElevenLabs to call it. Do not open TCP 8000 publicly.

## Router VPN
Do not configure RouterOS API access until a private tunnel from the VPS to the CCR2116 has been established and tested. Back To Home being enabled on the router does not, by itself, prove that this VPS can join that tunnel. Confirm supported client topology first.

Create a dedicated RouterOS read-only user and store its credentials only on the VPS. Then implement and test narrowly scoped read-only API calls.
