# BRIEFING — 2026-09-20T23:23:10Z

## Mission
Investigate technical stack, target folder, Node.js/npm environment, Supabase schema and configuration, balanced randomization algorithm, CSV export structure, admin dashboard, git and deployment pipeline for the Psychology Experiment platform.

## 🔒 My Identity
- Archetype: explorer
- Roles: investigation, synthesis
- Working directory: C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_survey_3
- Original parent: a385a74f-853a-4974-829a-239ecab00da0
- Milestone: survey and technical architecture investigation

## 🔒 Key Constraints
- Read-only investigation — do NOT implement
- Investigation focus: technical stack, target folder, Node/npm, Supabase schema/config, balanced randomization algorithm, CSV export, admin dashboard, git & deployment

## Current Parent
- Conversation ID: a385a74f-853a-4974-829a-239ecab00da0
- Updated: not yet

## Investigation State
- **Explored paths**: `PARCIAL 2 - INVESTIGACIÓN`, `Noticias/noticias imagenes`, `NOTICIAS TRADUCIDAS.docx`, git repo origin, node/npm/python versions, env variables.
- **Key findings**:
  - Target folder `web-experimento` does not exist yet; must be scaffolded.
  - All 28 stimuli found in `Noticias/noticias imagenes` (27 JPEG, 1 PNG `Noticia_26.png`).
  - Node `v24.15.0`, npm `11.12.1`, git `2.53.0`, python `3.13.14` installed. Git repo is `Franco4447/psicologia-favaloro`.
  - Recommended stack: Next.js 14+ (App Router) + TypeScript + Tailwind CSS for secure server actions, secret admin routes, and 1-click Vercel deploy.
  - Min-fill algorithm with Postgres transactional advisory lock mathematically guarantees group difference <= 1 (strictly <= 2).
  - Designed complete Supabase DDL with RLS, indexes, and RPC function.
  - Designed RFC 4180 CSV export schema in Long format (20 rows per participant) with UTF-8 BOM.
  - Designed protected admin dashboard with HTTP-only cookie authentication.
- **Unexplored areas**: None within scope. All objectives completed.

## Key Decisions Made
- Chose Next.js App Router over Vite SPA for server-side secret isolation (service role key, admin password) and native Vercel optimization.
- Proved and modeled the balanced randomization algorithm via Python simulation and PostgreSQL RPC with `pg_advisory_xact_lock`.

## Artifact Index
- DISPATCH.md — Assignment instructions
- BRIEFING.md — Persistent working memory
- progress.md — Liveness heartbeat
- handoff.md — Comprehensive technical architecture report
