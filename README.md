# daddieshinor-backend

FastAPI backend service for daddieshinor.com

### Overview

- **Purpose**: Headless API layer supporting a Next.js blog frontend
- **Architecture**: Serverless (Vercel Functions)
- **Key Endpoints**:
  - `/api/wp-proxy` → proxied WordPress REST API requests (posts, embeds, etc.)
  - Health & monitoring routes (`/api/health`)
  - Extensible for future features (authentication, webhooks, custom queries)
- **Integration**: Next.js consumes via relative paths (`/api/...`) — no CORS needed in production

### Features

- Type-safe endpoints with Pydantic models
- Automatic OpenAPI/Swagger docs (`/docs`)
- Middleware: CORS (development-friendly)
- Minimal footprint for fast cold starts

### Project Goals

- Keep blog frontend lightweight (static-first + API calls)
- Enable easy content management via WordPress admin
- Prepare for future extensions (user features, analytics ingestion, AI tools)

### Setup

```bash
# Install deps
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload
