const fs = require("fs");
const path = require("path");

const mediaDir = "C:\\Users\\Fmendezcasariego\\OneDrive\\Carpetas\\Educación\\Universidad\\Favaloro\\Psicología\\2do Año\\Psicoanálisis\\3_Guias_de_Estudio\\_media";
const files = fs.readdirSync(mediaDir).filter(f => f.endsWith(".png"));

for (const file of files) {
    const filePath = path.join(mediaDir, file);
    const buffer = fs.readFileSync(filePath);
    if (buffer.toString('ascii', 1, 4) === 'PNG') {
        const widthPx = buffer.readUInt32BE(16);
        const idealPt = widthPx * (72/96) * (14/24);
        if (idealPt > 500) {
            console.log(`Wide image: ${file} -> ${Math.round(idealPt)}pt`);
        }
    }
}
