// Lista los PNG de una carpeta _media cuyo ancho, insertados en Word, supera el límite.
// Uso: node Scripts/check_wide.js "<carpeta _media>" [limite_pt=500]
// Ej.: node Scripts/check_wide.js "2do Año/Psicoanálisis/3_Guias_de_Estudio/_media"
const fs = require("fs");
const path = require("path");

const [mediaDir, limitArg] = process.argv.slice(2);
if (!mediaDir) {
    console.error('Uso: node check_wide.js "<carpeta _media>" [limite_pt=500]');
    process.exit(1);
}
const limitPt = Number(limitArg ?? 500);
const files = fs.readdirSync(mediaDir).filter(f => f.toLowerCase().endsWith(".png"));

for (const file of files) {
    const buffer = fs.readFileSync(path.join(mediaDir, file));
    if (buffer.toString('ascii', 1, 4) === 'PNG') {
        const widthPx = buffer.readUInt32BE(16);
        // px -> pt a 96 dpi, escalado por la relación de fuente 14/24 usada al exportar
        const idealPt = widthPx * (72/96) * (14/24);
        if (idealPt > limitPt) {
            console.log(`Wide image: ${file} -> ${Math.round(idealPt)}pt`);
        }
    }
}
