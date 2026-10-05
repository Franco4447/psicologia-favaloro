import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import assert from 'assert';

const WORKSPACE_DIR = 'C:/Users/Fmendezcasariego/OneDrive/Carpetas/Educación/Universidad/Favaloro/Psicología';
const WEB_DIR = path.join(WORKSPACE_DIR, '2do Año/Psicología Experimental/PARCIAL 2 - INVESTIGACIÓN/web-experimento');
const ORIGINAL_IMG_DIR = path.join(WORKSPACE_DIR, '2do Año/Psicología Experimental/PARCIAL 2 - INVESTIGACIÓN/Noticias/noticias imagenes');

console.log('--- FORENSIC INTEGRITY AUDIT - MILESTONE 1 ---');
console.log('Inspecting target:', WEB_DIR);

let totalChecks = 0;
let passedChecks = 0;
let failedChecks = 0;
const failureDetails = [];

function check(name, fn) {
  totalChecks++;
  try {
    fn();
    console.log(`[PASS] ${name}`);
    passedChecks++;
  } catch (err) {
    console.error(`[FAIL] ${name}: ${err.message}`);
    failedChecks++;
    failureDetails.push({ name, error: err.message, stack: err.stack });
  }
}

// ----------------------------------------------------------------------------
// 1. Source Code Inspection & Stimuli Authenticity
// ----------------------------------------------------------------------------
check('Source file stimuli.ts exists and has substantive content', () => {
  const filePath = path.join(WEB_DIR, 'src/data/stimuli.ts');
  assert(fs.existsSync(filePath), 'src/data/stimuli.ts does not exist');
  const content = fs.readFileSync(filePath, 'utf-8');
  assert(content.length > 15000, `stimuli.ts content suspiciously short: ${content.length} bytes`);
  assert(!content.includes('Lorem ipsum'), 'stimuli.ts contains placeholder text "Lorem ipsum"');
  assert(!content.includes('Dummy'), 'stimuli.ts contains placeholder word "Dummy"');
  assert(!content.includes('Mock'), 'stimuli.ts contains placeholder word "Mock"');
  assert(!content.includes('TODO'), 'stimuli.ts contains incomplete "TODO" annotations');
});

// Import the actual module dynamically or evaluate via Node
// Since Next.js uses tsconfig paths and TS, we can inspect stimuli.ts content structurally or import compiled/transpiled
check('Verbatim stimuli inventory contains 28 authentic items with mirror pairs', () => {
  const content = fs.readFileSync(path.join(WEB_DIR, 'src/data/stimuli.ts'), 'utf-8');

  // Verify all 28 IDs exist in STIMULI
  for (let i = 1; i <= 28; i++) {
    const idRegex = new RegExp(`id:\\s*${i},`);
    assert(idRegex.test(content), `Stimulus ID ${i} not found in STIMULI`);
  }

  // Check Noticia_26.png distinction
  assert(content.includes("'Noticia_26.png'") || content.includes('"Noticia_26.png"'), 'Noticia_26.png not explicitly referenced');

  // Check mirror pairs in code
  const mirrorPairs = [
    [13, 21], [14, 22], [15, 23], [16, 24],
    [17, 25], [18, 26], [19, 27], [20, 28]
  ];
  for (const [a, b] of mirrorPairs) {
    // Check that pair a has mirrorPairId: b and b has mirrorPairId: a
    const regexA = new RegExp(`id:\\s*${a}[\\s\\S]*?mirrorPairId:\\s*${b}`);
    const regexB = new RegExp(`id:\\s*${b}[\\s\\S]*?mirrorPairId:\\s*${a}`);
    assert(regexA.test(content), `Mirror pair definition missing or incorrect for ${a} -> ${b}`);
    assert(regexB.test(content), `Mirror pair definition missing or incorrect for ${b} -> ${a}`);
  }
});

// ----------------------------------------------------------------------------
// 2. Asset Integrity & Cryptographic Hash Verification
// ----------------------------------------------------------------------------
check('All 28 assets in public/noticias match source assets bit-for-bit', () => {
  const publicNoticias = path.join(WEB_DIR, 'public/noticias');
  assert(fs.existsSync(publicNoticias), 'public/noticias folder missing');

  for (let i = 1; i <= 28; i++) {
    const padded = String(i).padStart(2, '0');
    const filename = i === 26 ? 'Noticia_26.png' : `Noticia_${padded}.jpg`;

    const srcFile = path.join(ORIGINAL_IMG_DIR, filename);
    const destFile = path.join(publicNoticias, filename);

    assert(fs.existsSync(srcFile), `Original source file missing: ${srcFile}`);
    assert(fs.existsSync(destFile), `Target asset missing: ${destFile}`);

    const srcBuf = fs.readFileSync(srcFile);
    const destBuf = fs.readFileSync(destFile);

    assert.strictEqual(destBuf.length, srcBuf.length, `Byte length mismatch in ${filename}`);

    const srcHash = crypto.createHash('sha256').update(srcBuf).digest('hex');
    const destHash = crypto.createHash('sha256').update(destBuf).digest('hex');

    assert.strictEqual(destHash, srcHash, `SHA-256 hash mismatch in ${filename}`);

    // Check magic bytes
    if (i === 26) {
      assert.strictEqual(destBuf[0], 0x89, 'Noticia_26.png invalid byte 0');
      assert.strictEqual(destBuf[1], 0x50, 'Noticia_26.png invalid byte 1');
      assert.strictEqual(destBuf[2], 0x4E, 'Noticia_26.png invalid byte 2');
      assert.strictEqual(destBuf[3], 0x47, 'Noticia_26.png invalid byte 3');
    } else {
      assert.strictEqual(destBuf[0], 0xFF, `${filename} invalid JPEG magic byte 0`);
      assert.strictEqual(destBuf[1], 0xD8, `${filename} invalid JPEG magic byte 1`);
      assert.strictEqual(destBuf[2], 0xFF, `${filename} invalid JPEG magic byte 2`);
    }
  }
});

// ----------------------------------------------------------------------------
// 3. Facade & Bypass Detection
// ----------------------------------------------------------------------------
check('No hardcoded test mocks or facades in stimuli.ts and assets.ts', () => {
  const stimuliCode = fs.readFileSync(path.join(WEB_DIR, 'src/data/stimuli.ts'), 'utf-8');
  const assetsCode = fs.readFileSync(path.join(WEB_DIR, 'src/lib/assets.ts'), 'utf-8');

  // Check evaluateInclusion implementation
  assert(stimuliCode.includes('demographics.age < 18'), 'evaluateInclusion does not check age < 18');
  assert(stimuliCode.includes('!demographics.studiesPsychology'), 'evaluateInclusion does not check studiesPsychology');
  assert(stimuliCode.includes("demographics.therapeuticOrientation === 'Otros'"), 'evaluateInclusion does not check orientation Otros');

  // Check getParticipantNewsDeck
  assert(stimuliCode.includes('PSA_CONGRUENT_FAKE_IDS'), 'getParticipantNewsDeck does not use PSA_CONGRUENT_FAKE_IDS');
  assert(stimuliCode.includes('EBP_CONGRUENT_FAKE_IDS'), 'getParticipantNewsDeck does not use EBP_CONGRUENT_FAKE_IDS');
  assert(stimuliCode.includes('TRUE_NEWS_IDS'), 'getParticipantNewsDeck does not use TRUE_NEWS_IDS');
  assert(stimuliCode.includes('shuffleArray'), 'getParticipantNewsDeck does not shuffle stimuli');

  // Ensure no test-specific bypass like if (test) return ...
  assert(!stimuliCode.includes('if (test)'), 'stimuli.ts has suspicious test conditional');
  assert(!assetsCode.includes('if (test)'), 'assets.ts has suspicious test conditional');
});

// ----------------------------------------------------------------------------
// 4. Type Definitions Conformance with PROJECT.md
// ----------------------------------------------------------------------------
check('Types in src/types/experiment.ts conform strictly to PROJECT.md specification', () => {
  const typesContent = fs.readFileSync(path.join(WEB_DIR, 'src/types/experiment.ts'), 'utf-8');

  const requiredTypes = [
    'export type InductionGroup',
    "'racional' | 'emocional' | 'control'",
    'export type TherapeuticOrientation',
    "'Psicoanálisis'",
    "'Basada en Evidencia Científica'",
    "'Otros'",
    'export type FakeNewsSet',
    'export interface StimulusItem',
    'export interface TrialStimulus',
    'export type ResponseCode = 1 | 2 | 3 | 4',
    'export interface ParticipantSession',
    'export interface TrialRecord',
    'export interface CsvExportRow',
    'export interface AdminDashboardStats'
  ];

  for (const item of requiredTypes) {
    assert(typesContent.includes(item), `Type definition missing or non-conforming: ${item}`);
  }
});

console.log('\n====================================================');
console.log(`AUDIT RESULTS: ${passedChecks} passed, ${failedChecks} failed out of ${totalChecks} checks.`);
if (failedChecks > 0) {
  console.error('VERDICT: INTEGRITY VIOLATION');
  process.exit(1);
} else {
  console.log('VERDICT: CLEAN (Phase 1)');
}
