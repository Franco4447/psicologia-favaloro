import assert from 'assert';
import {
  STIMULI,
  STIMULI_BY_ID,
  TRUE_NEWS_IDS,
  PSA_CONGRUENT_FAKE_IDS,
  EBP_CONGRUENT_FAKE_IDS,
  evaluateInclusion,
  getParticipantNewsDeck,
  classifyResponse,
  getStimulusImagePath,
  getStimulusById
} from '../../2do Año/Psicología Experimental/PARCIAL 2 - INVESTIGACIÓN/web-experimento/src/data/stimuli';
import {
  getStimulusImageFileName,
  getStimulusAlternativePath
} from '../../2do Año/Psicología Experimental/PARCIAL 2 - INVESTIGACIÓN/web-experimento/src/lib/assets';

console.log('--- INDEPENDENT DEEP LOGIC & ADVERSARIAL STRESS TEST ---');

let passed = 0;
let failed = 0;

function runTest(name: string, fn: () => void) {
  try {
    fn();
    console.log(`[PASS] ${name}`);
    passed++;
  } catch (err: any) {
    console.error(`[FAIL] ${name}: ${err.message}`);
    failed++;
  }
}

// 1. evaluateInclusion Boundary Tests
runTest('evaluateInclusion: boundary and edge cases', () => {
  // Under 18
  assert.strictEqual(evaluateInclusion({ age: 17, studiesPsychology: true, therapeuticOrientation: 'Psicoanálisis' }).isIncluded, false);
  assert.strictEqual(evaluateInclusion({ age: 17, studiesPsychology: true, therapeuticOrientation: 'Psicoanálisis' }).exclusionReason, 'menor_de_edad');
  assert.strictEqual(evaluateInclusion({ age: 0, studiesPsychology: true, therapeuticOrientation: 'Psicoanálisis' }).isIncluded, false);
  assert.strictEqual(evaluateInclusion({ age: -5, studiesPsychology: true, therapeuticOrientation: 'Psicoanálisis' }).isIncluded, false);

  // Exactly 18
  const at18 = evaluateInclusion({ age: 18, studiesPsychology: true, therapeuticOrientation: 'Psicoanálisis' });
  assert.strictEqual(at18.isIncluded, true);
  assert.strictEqual(at18.exclusionReason, null);

  // Non-psychology student
  const nonPsych = evaluateInclusion({ age: 25, studiesPsychology: false, therapeuticOrientation: 'Psicoanálisis' });
  assert.strictEqual(nonPsych.isIncluded, false);
  assert.strictEqual(nonPsych.exclusionReason, 'no_estudia_psicologia');

  // Orientation 'Otros'
  const otros = evaluateInclusion({ age: 30, studiesPsychology: true, therapeuticOrientation: 'Otros' });
  assert.strictEqual(otros.isIncluded, false);
  assert.strictEqual(otros.exclusionReason, 'orientacion_otros');

  // Valid Evidence-based
  const ebp = evaluateInclusion({ age: 22, studiesPsychology: true, therapeuticOrientation: 'Basada en Evidencia Científica' });
  assert.strictEqual(ebp.isIncluded, true);
  assert.strictEqual(ebp.exclusionReason, null);
});

// 2. getParticipantNewsDeck Simulation Stress Tests
runTest('getParticipantNewsDeck: PSA 200 simulations', () => {
  const firstItemIds = new Set<number>();
  for (let i = 0; i < 200; i++) {
    const deck = getParticipantNewsDeck('Psicoanálisis', true);
    assert.strictEqual(deck.length, 20, 'Deck must have 20 items');
    
    // Check no duplicate IDs
    const ids = deck.map(d => d.id);
    const uniqueIds = new Set(ids);
    assert.strictEqual(uniqueIds.size, 20, 'Deck contains duplicate stimuli');

    // Check true items
    const trueItems = deck.filter(d => !d.isFake);
    assert.strictEqual(trueItems.length, 12, 'Must have 12 true items');
    trueItems.forEach(t => assert(t.id >= 1 && t.id <= 12));

    // Check fake items
    const fakeItems = deck.filter(d => d.isFake);
    assert.strictEqual(fakeItems.length, 8, 'Must have 8 fake items');
    fakeItems.forEach(f => {
      assert(PSA_CONGRUENT_FAKE_IDS.includes(f.id), `Invalid PSA fake ID: ${f.id}`);
      assert(!EBP_CONGRUENT_FAKE_IDS.includes(f.id), `EBP fake ID found in PSA deck: ${f.id}`);
    });

    firstItemIds.add(deck[0].id);
  }
  // Order must vary across 200 runs
  assert(firstItemIds.size > 5, 'Presentation order appears static or unrandomized');
});

runTest('getParticipantNewsDeck: EBP 200 simulations', () => {
  for (let i = 0; i < 200; i++) {
    const deck = getParticipantNewsDeck('Basada en Evidencia Científica', true);
    assert.strictEqual(deck.length, 20);

    const ids = deck.map(d => d.id);
    assert.strictEqual(new Set(ids).size, 20);

    const trueItems = deck.filter(d => !d.isFake);
    assert.strictEqual(trueItems.length, 12);

    const fakeItems = deck.filter(d => d.isFake);
    assert.strictEqual(fakeItems.length, 8);
    fakeItems.forEach(f => {
      assert(EBP_CONGRUENT_FAKE_IDS.includes(f.id), `Invalid EBP fake ID: ${f.id}`);
      assert(!PSA_CONGRUENT_FAKE_IDS.includes(f.id), `PSA fake ID found in EBP deck: ${f.id}`);
    });
  }
});

runTest('getParticipantNewsDeck: Excluded participants 200 simulations & mirror pair collision check', () => {
  let psaCount = 0;
  let ebpCount = 0;

  for (let i = 0; i < 200; i++) {
    const deck = getParticipantNewsDeck('Otros', false);
    assert.strictEqual(deck.length, 20);

    const fakeItems = deck.filter(d => d.isFake);
    assert.strictEqual(fakeItems.length, 8);

    const isAllPsa = fakeItems.every(f => PSA_CONGRUENT_FAKE_IDS.includes(f.id));
    const isAllEbp = fakeItems.every(f => EBP_CONGRUENT_FAKE_IDS.includes(f.id));

    assert(isAllPsa || isAllEbp, 'Excluded participant received mixed fake set with potential mirror collisions');
    if (isAllPsa) psaCount++;
    if (isAllEbp) ebpCount++;

    // Mirror collision check: no item and its mirror pair can exist in the same deck
    const idSet = new Set(deck.map(d => d.id));
    deck.forEach(item => {
      if (item.mirrorPairId) {
        assert(!idSet.has(item.mirrorPairId), `Mirror collision detected! Deck contains both ${item.id} and ${item.mirrorPairId}`);
      }
    });
  }

  // 50/50 balance across 200 runs
  assert(psaCount > 60 && psaCount < 140, `Excluded set distribution skewed: PSA=${psaCount}, EBP=${ebpCount}`);
});

// 3. classifyResponse Exhaustive Truth Table
runTest('classifyResponse truth table', () => {
  assert.deepStrictEqual(classifyResponse(true, 1), { isFalseMemory: true, isFalseBelief: false, isTrueMemory: false });
  assert.deepStrictEqual(classifyResponse(true, 2), { isFalseMemory: false, isFalseBelief: true, isTrueMemory: false });
  assert.deepStrictEqual(classifyResponse(true, 3), { isFalseMemory: false, isFalseBelief: false, isTrueMemory: false });
  assert.deepStrictEqual(classifyResponse(true, 4), { isFalseMemory: false, isFalseBelief: false, isTrueMemory: false });

  assert.deepStrictEqual(classifyResponse(false, 1), { isFalseMemory: false, isFalseBelief: false, isTrueMemory: true });
  assert.deepStrictEqual(classifyResponse(false, 2), { isFalseMemory: false, isFalseBelief: false, isTrueMemory: false });
  assert.deepStrictEqual(classifyResponse(false, 3), { isFalseMemory: false, isFalseBelief: false, isTrueMemory: false });
  assert.deepStrictEqual(classifyResponse(false, 4), { isFalseMemory: false, isFalseBelief: false, isTrueMemory: false });
});

// 4. Asset Path Resolvers
runTest('Asset path resolvers for all 28 items', () => {
  for (let id = 1; id <= 28; id++) {
    const filename = getStimulusImageFileName(id);
    const primaryPath = getStimulusImagePath(id);
    const altPath = getStimulusAlternativePath(id);

    if (id === 26) {
      assert.strictEqual(filename, 'Noticia_26.png');
      assert.strictEqual(primaryPath, '/noticias/Noticia_26.png');
      assert.strictEqual(altPath, '/noticias/Noticia_26.jpg');
    } else {
      const padded = String(id).padStart(2, '0');
      assert.strictEqual(filename, `Noticia_${padded}.jpg`);
      assert.strictEqual(primaryPath, `/noticias/Noticia_${padded}.jpg`);
      assert.strictEqual(altPath, `/noticias/Noticia_${padded}.png`);
    }

    const item = getStimulusById(id);
    assert.strictEqual(item.id, id);
    assert.strictEqual(getStimulusImagePath(item), primaryPath);
  }
});

// 5. Immutability / Freezing
runTest('Dataset freezing against tampering', () => {
  assert(Object.isFrozen(STIMULI), 'STIMULI array is not frozen');
  assert(Object.isFrozen(TRUE_NEWS_IDS), 'TRUE_NEWS_IDS is not frozen');
  assert(Object.isFrozen(PSA_CONGRUENT_FAKE_IDS), 'PSA_CONGRUENT_FAKE_IDS is not frozen');
  assert(Object.isFrozen(EBP_CONGRUENT_FAKE_IDS), 'EBP_CONGRUENT_FAKE_IDS is not frozen');
  assert(Object.isFrozen(STIMULI_BY_ID), 'STIMULI_BY_ID is not frozen');
});

console.log(`\nDEEP LOGIC AUDIT: ${passed} passed, ${failed} failed.`);
if (failed > 0) {
  process.exit(1);
}
