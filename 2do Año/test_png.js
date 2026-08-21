const fs = require("fs");
const buffer = fs.readFileSync("C:\\Users\\Fmendezcasariego\\OneDrive\\Carpetas\\Educación\\Universidad\\Favaloro\\Psicología\\2do Año\\Psicoanálisis\\3_Guias_de_Estudio\\_media\\mermaid_1787090597470_1.png");
if (buffer.toString("ascii", 1, 4) === "PNG") {
    const widthPx = buffer.readUInt32BE(16);
    console.log("Width px: " + widthPx);
    const idealPt = widthPx * (72/96) * (14/24);
    console.log("Ideal Pt: " + Math.round(idealPt));
}
