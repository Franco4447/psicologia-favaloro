# Handoff Report: Next.js 14+ Scaffolding Procedure for web-experimento

**Agent**: `explorer_m1_1`  
**Working Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\.agents\explorer_m1_1`  
**Target Project Directory**: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`  
**Date / Timestamp**: 2026-09-20T23:30:00Z  

---

## 1. Observation

1. **Runtime & Toolchain Versions**:
   - `node -v` output: `v24.15.0`
   - `npm -v` output: `11.12.1`
   - Binary location: `C:\Users\Fmendezcasariego\nodejs\node-v24.15.0-win-x64\`
   - Package managers `pnpm`, `yarn`, and `bun` are not present (`where.exe` exited with code 1). `npm` is the sole package manager available on this system.

2. **Filesystem & Git Repository Status**:
   - The target parent folder `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN` currently contains:
     - `Feedback_Diseño_Experimental.md`
     - `Fundamentos Empíricos/`
     - `Fundamentos Teóricos/`
     - `Noticias/`
     - `Psicología Experimental - Favaloro.docx`
     - `Psicología Experimental - Favaloro.md`
     - `experimento.docx`
     - `mover_archivos.py`
   - The directory `web-experimento` does **not** exist yet.
   - `git rev-parse --is-inside-work-tree` returned `true`, with top-level repository at `C:/Users/Fmendezcasariego/OneDrive/Carpetas/Educación/Universidad/Favaloro/Psicología`.

3. **create-next-app Flags & Behaviors**:
   - Tested command `npx --yes create-next-app@14 --help`. The available flags include:
     - `--ts` / `--typescript` (Initialize as TypeScript project)
     - `--tailwind` (Initialize with Tailwind CSS config)
     - `--eslint` (Initialize with ESLint config)
     - `--app` (Initialize as App Router project)
     - `--src-dir` (Initialize inside `src/` directory)
     - `--import-alias <alias-to-configure>` (Specify import alias, e.g. `@/*`)
     - `--use-npm` (Explicitly bootstrap using npm)
   - When all of the above options are specified as arguments, `create-next-app` executes 100% non-interactively without prompting for user input.
   - Because the target directory is already inside a Git repository, `create-next-app` will automatically detect the enclosing repository and skip initializing an unwanted nested `.git` folder, while still writing `.gitignore`.

4. **Next.js Version Pinned vs Latest**:
   - `npm info next@14.2.35 version` returned `14.2.35`.
   - `npm info next@14.2.35 engines` returned `{ node: '>=18.17.0' }`, which Node `v24.15.0` satisfies.
   - `npx create-next-app@14` scaffolds Next.js `14.2.35` paired with React 18 (`react@^18`, `react-dom@^18`), matching `PROJECT.md` line 13 (`Next.js 14+ (App Router), React 18, TypeScript, Tailwind CSS, Lucide React icons`).
   - `create-next-app@latest` is currently version `16.3.5` (Next.js 15/16 + React 19), which introduces asynchronous request APIs (`await cookies()`, `await headers()`) that deviate from Next.js 14 synchronous server helpers.

5. **Additional Dependencies & Stimuli Assets**:
   - `lucide-react`: latest version `1.47.0`, peerDependencies `{ react: '^16.5.1 || ^17.0.0 || ^18.0.0 || ^19.0.0' }` (clean match with React 18).
   - `@supabase/supabase-js`: latest version `2.116.0` (clean match with Node 24 and npm 11).
   - Stimuli source folder `..\Noticias\noticias imagenes\` contains all 28 expected stimulus image files:
     - 27 `.jpg` files: `Noticia_01.jpg` to `Noticia_25.jpg`, `Noticia_27.jpg`, `Noticia_28.jpg`
     - 1 `.png` file: `Noticia_26.png`

---

## 2. Logic Chain

1. **Non-Interactive Execution Requirement**:
   - Running scaffolding scripts in background automation fails if any CLI tool blocks waiting on `stdin`.
   - By supplying `web-experimento` as the directory and all seven configuration flags (`--ts`, `--tailwind`, `--eslint`, `--app`, `--src-dir`, `--import-alias "@/*"`, `--use-npm`), every decision branch in `create-next-app` is satisfied up front. No interactive prompts will appear.

2. **Node v24.15.0 and npm 11.12.1 Compatibility**:
   - Node 24 is an active LTS release supporting modern V8 ECMAScript features.
   - The engine specification in `next@14.2.35` is `>=18.17.0`.
   - Node 24 satisfies this range, and npm 11 seamlessly handles peer dependencies without requiring `--legacy-peer-deps`.

3. **Version Selection (Next.js 14.2.35 with React 18)**:
   - `PROJECT.md` line 13 specifies: `Next.js 14+ (App Router), React 18, TypeScript, Tailwind CSS, Lucide React icons`.
   - Pinning the scaffold command to `npx --yes create-next-app@14` guarantees that Next.js `14.2.35` and React 18 are installed.
   - This avoids React 19 peer-dependency friction and ensures standard Next.js 14 App Router conventions.

4. **Working Directory & Path Handling**:
   - The workspace path contains spaces: `.../2do Año/Psicología Experimental/PARCIAL 2 - INVESTIGACIÓN`.
   - To prevent PowerShell token-splitting issues, the command should be run with `Cwd` set to the parent directory `.../PARCIAL 2 - INVESTIGACIÓN`, passing the simple directory name `web-experimento` to `create-next-app`.
   - Windows PowerShell safely passes `--import-alias "@/*"` when enclosed in quotes.

5. **Asset Staging**:
   - Following `create-next-app`, the directory `web-experimento/public/noticias/` must be created and populated from `..\Noticias\noticias imagenes\*` to satisfy the stimulus display requirements.

---

## 3. Caveats

1. **Existing Parent Git Repository**:
   - Because `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología` is already a git repository, `create-next-app` will omit running `git init`. When preparing Milestone 5 (Git Setup / Vercel Deploy), the deployment configuration must account for whether `web-experimento` is deployed as a subfolder of this repository (Vercel Root Directory setting: `2do Año/Psicología Experimental/PARCIAL 2 - INVESTIGACIÓN/web-experimento`) or as an independent remote.
2. **OneDrive Path Synchronization**:
   - The workspace resides inside a OneDrive-synchronized folder. Rapid file creation of `node_modules` can trigger brief file lock delays in Windows Defender or OneDrive client. If npm encounters `EBUSY` or `EPERM` during `node_modules` extraction, running npm with `--prefer-offline` or retrying resolves it.
3. **No Prior `web-experimento` Directory**:
   - The target directory `web-experimento` must not exist prior to scaffolding; `create-next-app` refuses to scaffold into a non-empty directory.

---

## 4. Conclusion & Recommended Scaffolding Procedure

The exact, non-interactive scaffolding and initialization recipe for Milestone M1 is as follows:

### Step 1: Scaffold Next.js 14 App
Run from Cwd: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN`
```powershell
npx --yes create-next-app@14 web-experimento --ts --tailwind --eslint --app --src-dir --import-alias "@/*" --use-npm
```

### Step 2: Install Core Domain Dependencies
Run from Cwd: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`
```powershell
npm install lucide-react @supabase/supabase-js
```

### Step 3: Create Asset Directory & Copy Stimuli Images
Run from Cwd: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`
```powershell
New-Item -ItemType Directory -Force -Path "public\noticias"
Copy-Item -Path "..\Noticias\noticias imagenes\*" -Destination "public\noticias\" -Recurse
```

### Step 4: Create Module Subdirectories (Per PROJECT.md)
Run from Cwd: `C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental\PARCIAL 2 - INVESTIGACIÓN\web-experimento`
```powershell
New-Item -ItemType Directory -Force -Path "src\types", "src\data", "src\lib", "src\components", "src\app\admin\login", "src\app\api\session", "src\app\api\responses", "src\app\api\admin\login", "src\app\api\admin\stats", "src\app\api\admin\export-csv", "supabase"
```

### Step 5: Initialize Environment Configuration Templates
Create `web-experimento\.env.example`:
```env
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
ADMIN_PASSWORD=your-secure-admin-password
```
Copy to `.env.local` for local development.

---

## 5. Verification Method

To independently verify the scaffolding output after execution by the implementer agent:

1. **Verify Directory Structure**:
   Check that `web-experimento/package.json`, `tsconfig.json`, `tailwind.config.ts`, `postcss.config.js`, `next.config.mjs`, and `src/app/layout.tsx` exist.
2. **Verify Stimuli Assets (All 28 Files)**:
   In PowerShell, run:
   ```powershell
   (Get-ChildItem "web-experimento\public\noticias").Count
   ```
   Must return `28`. Verify specifically that `public\noticias\Noticia_26.png` exists and is a valid image.
3. **Verify Build and Typecheck**:
   In `web-experimento`:
   ```powershell
   npm run build
   ```
   Exit code must be `0` with no TypeScript errors and no Next.js build errors.
4. **Verify Dependencies in `package.json`**:
   Inspect `web-experimento/package.json` to confirm:
   - `"next"`: `"^14.2.35"`
   - `"react"`: `"^18"`
   - `"react-dom"`: `"^18"`
   - `"lucide-react"`: `"^1.47.0"`
   - `"@supabase/supabase-js"`: `"^2.116.0"`
