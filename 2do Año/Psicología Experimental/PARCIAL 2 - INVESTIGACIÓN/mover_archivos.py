import os
import shutil

# Rutas base
base_dir = r"C:\Users\Fmendezcasariego\OneDrive\Carpetas\Educación\Universidad\Favaloro\Psicología\2do Año\Psicología Experimental"
origen_dir = os.path.join(base_dir, "2_Textos_Extraidos")
empiricos_dir = os.path.join(base_dir, "PARCIAL 2 - INVESTIGACIÓN", "Fundamentos Empíricos")
teoricos_dir = os.path.join(base_dir, "PARCIAL 2 - INVESTIGACIÓN", "Fundamentos Teóricos")

# Mapa de archivos empíricos
archivos_empiricos = {
    "P2_LeonEtAl_FakeNewsFalseMemory_Crudo.md": "emp 1 - Fake news and false memory formation in the psychology debate - Leon et al (2023).md",
    "P2_FrendaEtAl_FalseMemoriesPolitical_Crudo.md": "emp 2 - frenda2013.md",
    "P2_MartelEtAl_RelianceOnEmotion_Crudo.md": "emp 3 - Reliance on emotion promotes belief in fake news.md",
    "P2_PerezSantangeloSolovey_UnderstandingBelief_Crudo.md": "emp 4 - Understanding belief in political statements.md",
    "P2_Murphy_AttitudesTowardsFeminism_Crudo.md": "emp 5 - Murphy - Attitudes towards feminism predict susceptibility to feminism-related fake.md",
    "P2_BagoRandPennycook_FakeNewsFastAndSlow_Crudo.md": "emp 6 - Bago Rand Pennycook Fake News Fast and Slow.md",
    "P2_TrevorsEtAl_ExperimentallyInducedEmotions_Crudo.md": "emp 7 - Trevors Experimentally Induced Emotions.md",
    "P2_GradyEtAl_PartisanshipPersisted_Crudo.md": "emp 8 - Nevertheless, partisanship persisted.md"
}

# Mapa de archivos teóricos
archivos_teoricos = {
    "P2_Nickerson_ConfirmationBias_Crudo.md": "teo 1 - Nickerson, R. S. (1998). Confirmation Bias.md",
    "P2_GreifenederEtAl_PsychologyOfFakeNews_Crudo.md": "teo 2 - The Psychology of Fake News.md",
    "P2_JohnsonEtAl_SourceMonitoring_Crudo.md": "teo 3 - Source Monitoring - Johnson et al (1993).md",
    "P2_PennycookRand_PsychologyOfFakeNews_Crudo.md": "teo 4 - Pennycook Rand Psychology of Fake News.md",
    "P2_EckerEtAl_PsychologicalDrivers_Crudo.md": "teo 5 - Ecker Psychological drivers.md"
}

def mover_y_renombrar(mapa_archivos, destino_dir):
    for archivo_origen, nuevo_nombre in mapa_archivos.items():
        ruta_origen = os.path.join(origen_dir, archivo_origen)
        ruta_destino = os.path.join(destino_dir, nuevo_nombre)
        
        if os.path.exists(ruta_origen):
            try:
                shutil.move(ruta_origen, ruta_destino)
                print(f"✅ Movido: {archivo_origen} -> {nuevo_nombre}")
            except Exception as e:
                print(f"❌ Error al mover {archivo_origen}: {e}")
        else:
            print(f"⚠️ No encontrado: {archivo_origen} (quizás ya fue movido)")

print("Moviendo artículos empíricos...")
mover_y_renombrar(archivos_empiricos, empiricos_dir)

print("\nMoviendo artículos teóricos...")
mover_y_renombrar(archivos_teoricos, teoricos_dir)

print("\n¡Proceso completado!")
