import os

lista=[
'1_1_Cálculo_Diferencial',
'1_2_Programación_Básica',
'1_3_Física_I_Mecánica_Newtoniana',
'1_4_Cátedra_Francisco_José_de_Caldas',
'1_5_Producción_y_Comprensión_de_Textos',
'1_6_Seminario_de_Ingeniería',
'2_10_Programación_Orientada_a_Objetos',
'2_13_Física_II_Electromagnetismo',
'2_14_Análisis_de_Circuitos_I_y_Laboratorio',
'2_7_Cálculo_Integral',
'2_8_Historia_y_Cultura_Colombiana',
'2_9_Álgebra_Lineal',
'3__Electiva_Extrínseca_I',
'3_12_Cátedra_Democracia_y_Ciudadanía',
'3_16_Cálculo_Multivariado',
'3_17_Análisis_de_Circuitos_II_y_Laboratorio',
'3_20_Física_III_Ondas_y_Física_Moderna',
'3_88_Ecuaciones_Diferenciales',
'3_91_Electrónica_I',
'4_23_Probabilidades_y_Estadística',
'4_24_Variable_Compleja',
'4_25_Electrónica_II',
'4_26_Programación_Aplicada',
'4_27_Campos_Electromagnéticos',
'4_28_Fundamentos_de_Circuitos_Digitales',
'4_Segunda_Lengua_I',
'5_29_Ondas_Electromagnéticas',
'5_30_Análisis_de_Fourier_Wavelets',
'5_31_Transformadores',
'5_32_Electrónica_III',
'5_33_Análisis_y_Diseño_de_Microprocesadores',
'6__Electiva_Extrínseca_III',
'6__Segunda_Lengua_II',
'6_35_Comunicaciones_Analógicas',
'6_36_Motores_y_Generadores',
'6_37_Diseño_Digital_con_Microcontroladores',
'6_38_Señales_y_Sistemas',
'6_40_Cátedra_de_Contexto',
'7__Segunda_Lengua_III',
'7_41_Comunicaciones_Digitales',
'7_42_Física_de_Semiconductores',
'7_43_Hombre_Sociedad_y_Ecologia',
'7_44_Sistemas_Dinámicos',
'7_45_Electrónica_de_Potencia',
'7_47_Economía',
'8_48_Telecomunicaciones_I',
'8_49_Telemática_I',
'8_50_Control_I',
'8_51_Instrumentación_Industrial',
'8_52_Bioingeniería_I',
'8_53_Ingeniería_Económica',
'9_19_Trabajo_de_Grado_I',
'9_54_Televisión',
'9_57_Bioingeniería_II',
'9_58_Control_II',
'9_59_Nanotecnología_I',
'9_61_DSP',
'9_62_Telecomunicaciones_II',
'9_64_Inteligencia_Computacional_I',
'9_65_Sistemas_Embebidos_I',
'10_67_Electrónica_Industrial',
'10_68_Bioingeniería_III',
'10_69_Control_III',
'10_70_Nanotecnología_II',
'10_71_Telemática_III',
'10_72_Procesamiento_Digital_de_Imágenes',
'10_73_Telecomunicaciones_III',
'10_74_Televisión_Digital',
'10_75_Inteligencia_Computacional_II',
'10_78_Robótica_móvil',
]

import os

def crear_html(nombre_curso):
    # Crear el directorio si no existe
    #os.makedirs(nombre_curso, exist_ok=True)
    
    # Path del archivo index.html
    archivo_html = os.path.join(nombre_curso, "index.html")
    
    # Contenido del archivo HTML
    contenido_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{nombre_curso}</title>
</head>
<body>
    <h1> {nombre_curso}</h1>
  <h2>Recursos del Curso</h2>
        <ul>
            <li><a href="lecturas.html">Lecturas Recomendadas</a></li>
            <li><a href="videos.html">Videos Explicativos</a></li>
        </ul>   
</body>
</html>"""

    # Escribir el contenido en el archivo index.html
    with open(archivo_html, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_html)
    
    print(f"Archivo {archivo_html} creado con éxito.")

# Ejemplo de uso de la función
#nombre_curso = "1_1_Cálculo_Diferencial"
#crear_directorio_y_html(nombre_curso)

for nombre in lista:
    #path = os.path.join(directorio_base, nombre)
    #os.makedirs(nombre, exist_ok=True)
    #print(f"Directorio creado: {path}")
    crear_html(nombre)