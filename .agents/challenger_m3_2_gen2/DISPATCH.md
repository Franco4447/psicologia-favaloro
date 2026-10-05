# Dispatch — challenger_m3_2_gen2

## Mission: Adversarial Stress Testing of API Routes, Data Validation & Client Sync Resiliency
You are `challenger_m3_2_gen2`. Adversarially challenge the API route handlers (`/api/session`, `/api/responses`) and client sync (`src/lib/sync.ts`).

## Challenge Objectives
1. Input fuzzing: invalid HTTP methods, missing required fields, age < 18, malformed UUIDs, newsId outside 1..28, responseOption outside 1..4, negative latencies.
2. Construct derivation correctness: verify that `is_false_memory = 1` ONLY when `is_fake = true` AND `response_option = 1`, and `is_false_belief = 1` ONLY when `is_fake = true` AND `response_option = 2`.
3. Offline queue resilience: simulate browser going offline, queuing 20 responses, browser reopening/coming online, flushing the queue, verifying no data loss and no duplicate rows via idempotent upserting.
4. Stress timing impact: verify sync requests do not block JavaScript main thread or affect `performance.now()` precision.

## Working Directory
`C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\challenger_m3_2_gen2`

## Output
Write `handoff.md` with explicit verdict: `APPROVE` or `REJECT`. Include code of adversarial scripts and run outputs.
