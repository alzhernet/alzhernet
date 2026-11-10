from fastapi import FastAPI, Header, HTTPException
from pydantic_settings import BaseSettings, SettingsConfigDict
import secrets

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    bridge_api_token: str = ""

settings = Settings()
app = FastAPI(title="Alzher Net Cloud Bridge", version="0.1.0")

def require_token(authorization: str | None):
    if not settings.bridge_api_token:
        raise HTTPException(status_code=503, detail="Bridge authentication is not configured")
    expected = f"Bearer {settings.bridge_api_token}"
    if not authorization or not secrets.compare_digest(authorization, expected):
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/health")
def health():
    return {"status": "ok", "service": "alzher-net-cloud-bridge", "router_connected": False}

@app.get("/v1/router/status")
def router_status(authorization: str | None = Header(default=None)):
    require_token(authorization)
    # Intentionally unavailable until a private VPN route and least-privilege
    # RouterOS read-only account are configured and tested.
    return {
        "connected": False,
        "mode": "read-only",
        "message": "Router VPN connection is not configured yet"
    }
