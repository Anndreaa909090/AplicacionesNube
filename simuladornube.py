import streamlit as st
import random
import pandas as pd
from datetime import datetime
from collections import defaultdict

# ============================================
# 1. CARGAR Y ESTRUCTURAR LAS PREGUNTAS
# ============================================

def cargar_preguntas():
    """Estructura todas las preguntas sobre Aplicaciones en la Nube"""
    
    preguntas = [
        # Pregunta 1
        {
            "pregunta": "¿Qué es Lambda?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Un servicio de computación sin servidor que permite ejecutar código sin la necesidad de administrar servidores",
                "Un servicio de pago que envía mensajes y correos",
                "Un servicio computacional que requiere gran manejo de servidores y servicios",
                "Ninguna de las anteriores"
            ],
            "respuesta": "Un servicio de computación sin servidor que permite ejecutar código sin la necesidad de administrar servidores"
        },
        # Pregunta 2
        {
            "pregunta": "Una organización quiere innovar mediante las tecnologías más recientes, pero también tiene necesidades de cumplimiento en las que se especifica que los datos se deben almacenar en ubicaciones determinadas. ¿Cuál enfoque de nube debería satisfacer sus necesidades?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Nube privada",
                "Nube pública",
                "Nube híbrida",
                "Nube comunitaria"
            ],
            "respuesta": "Nube híbrida"
        },
        # Pregunta 3
        {
            "pregunta": "Una organización quiere innovar mediante las tecnologías más recientes, pero también tiene necesidades de cumplimiento en las que se especifica que los datos se deben almacenar en ubicaciones determinadas. ¿Cuál enfoque de nube debería satisfacer sus necesidades? La respuesta es Nube híbrida",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 4
        {
            "pregunta": "AWS Management Console es una consola de administración de AWS, es una interfaz web para AWS y se utiliza para acceder a servicios de AWS como de Azure.",
            "tipo": "true_false",
            "respuesta": False
        },
        # Pregunta 5
        {
            "pregunta": "¿Qué significa API en el contexto de AWS? Interfaz de Programación de Aplicaciones, es un conjunto de reglas, protocolos y herramientas que permiten a diferentes aplicaciones comunicarse entre sí, especialmente para interactuar con los servicios en la nube de Amazon Web Services.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 6
        {
            "pregunta": "En la nube de AWS, una VPC es una Virtual Private Cloud",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 7
        {
            "pregunta": "Un bucket es un contenedor de almacenamiento en Amazon S3 donde se guardan archivos (objetos). Es similar a una carpeta o directorio, pero a nivel del sistema de almacenamiento en la nube.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 8
        {
            "pregunta": "Relacione lo correcto con respecto a las características de computación en la Nube",
            "tipo": "unir_conceptos",
            "conceptos": {
                "Elasticidad": "A las aplicaciones se les permite solicitar los recursos que necesitan usar de una forma rápida y cambiante (elástica)",
                "Amplio acceso a la red": "Los recursos están disponibles desde la red y se acceden a ellos a través de mecanismos estándares desde multitud de plataformas clientes",
                "Servicios bajo demanda": "De manera similar, una aplicación puede requerir ciertos servicios, por ejemplo de almacenamiento, computación o hosting, y los puede solicitar cuando los requiera",
                "Medición de servicios": "Las plataformas ofrecen herramientas para monitorizar el uso de estos recursos y que se puedan controlar por parte de los usuarios",
                "Conjunto de recursos": "Los recursos físicos (hardware) y los virtuales (software) se van asignando y reasignando según los requisitos de los usuarios y sus aplicaciones"
            }
        },
        # Pregunta 9
        {
            "pregunta": "Azure App Service es un servicio de computación en la nube de Microsoft Azure que permite crear, alojar y escalar aplicaciones web, API RESTful y backends móviles de forma sencilla y rápida.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 10
        {
            "pregunta": "Otra forma de desplegar aplicaciones en Azure es a través de extensiones disponibles para Azure y App Service, las cuales se instalan para conectarse a la suscripción de Azure y luego al servicio de aplicación correcto y cargar el código fuente de la aplicación directamente desde el código.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 11
        {
            "pregunta": "AWS Global Infrastructure. La infraestructura global de AWS es masiva y está dividida en regiones geográficas. Las regiones geográficas se dividen en zonas de disponibilidad separadas.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 12
        {
            "pregunta": "¿DynamoDB utiliza el modelo de almacenamiento clave-valor y documentos?",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 13
        {
            "pregunta": "¿Qué es API Gateway? API Gateway es un servicio de administración de API completamente automatizado que permite crear, publicar, mantener, monitorear y proteger APIs RESTful.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 14
        {
            "pregunta": "En una nube pública, los proveedores externos de servicios en la nube suministran los recursos como un servicio completamente administrado.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 15
       {
    "pregunta": "Marque las afirmaciones correctas respecto a Microsoft Azure:",
    "tipo": "opcion_multiple_multiple",
    "opciones": [
        "Una categoría son las aplicaciones web y los sistemas de bases de datos como SQL Server, MariaDB, PostgreSQL y NoSQL como Cosmos DB",
        "Otra categoría es IaaS, donde se incluyen servicios de infraestructura como máquinas virtuales",
        "Otra categoría son los servicios para comunicación, conexión y seguridad en redes",
        "Azure es una plataforma en la nube para implementar aplicaciones empresariales organizadas en múltiples categorías de servicios",
        "Otra categoría son los servicios para proteger datos, identidades y entornos"
    ],
    "respuesta": [
        "Una categoría son las aplicaciones web y los sistemas de bases de datos como SQL Server, MariaDB, PostgreSQL y NoSQL como Cosmos DB",
        "Otra categoría es IaaS, donde se incluyen servicios de infraestructura como máquinas virtuales",
        "Otra categoría son los servicios para comunicación, conexión y seguridad en redes",
        "Azure es una plataforma en la nube para implementar aplicaciones empresariales organizadas en múltiples categorías de servicios",
        "Otra categoría son los servicios para proteger datos, identidades y entornos"
    ]
        },

        # Pregunta 16
        {
            "pregunta": "Las implementaciones en la nube pública son complejas y requieren mucho tiempo. Necesitan una importante inversión inicial en infraestructura y recursos humanos. Se tienen que contratar equipos con conocimientos avanzados de codificación e ingeniería para configurar el entorno de nube privada.",
            "tipo": "true_false",
            "respuesta": False
        },
        # Pregunta 17
        {
            "pregunta": "Una forma de desplegar aplicaciones en la nube de Azure es: Emplear el usuario de cliente FTP, para conectarse a Azure App Service a través de sus credenciales y luego a través del cliente FTP, y así poder ir a cargar los paquetes de la aplicación en el servicio de la aplicación.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 18
        {
            "pregunta": "Marque los Modelos de Servicio que se manejan en la nube:",
            "tipo": "opcion_multiple",
            "opciones": [
                "IP, DNS, HTTP",
                "PaaS, SaaS, IaaS",
                "TCP, UDP, FTP",
                "SSL, TLS, VPN"
            ],
            "respuesta": "PaaS, SaaS, IaaS"
        },
        # Pregunta 19
        {
            "pregunta": "Cloud Privada: En la Cloud Privada, la infraestructura se usa solo dentro de una única organización. En una nube privada, una única organización controla y mantiene la infraestructura subyacente para suministrar los recursos de TI.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 20
        {
            "pregunta": "El centro de implementación del portal de Azure es una de las formas de implementar aplicaciones, esta opción se habilita mediante el uso de acciones de GitHub.",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 21
        {
            "pregunta": "¿Qué clave se utiliza para establecer relaciones entre tablas?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Clave primaria",
                "Clave foránea",
                "Clave candidata",
                "Clave compuesta"
            ],
            "respuesta": "Clave foránea"
        },
        # Pregunta 22
        {
            "pregunta": "¿Es cierto que las bases de datos de grafos son ideales para modelar relaciones jerárquicas y conexiones complejas entre datos?",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 23
        {
            "pregunta": "Las bases de datos documentales almacenan datos como pares clave-valor",
            "tipo": "true_false",
            "respuesta": False
        },
        # Pregunta 24
        {
            "pregunta": "¿Cuáles son los elementos básicos en el modelo relacional?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Nodos, aristas y grafos",
                "Tablas, filas y columnas",
                "Documentos, colecciones y campos",
                "Claves, valores y buckets"
            ],
            "respuesta": "Tablas, filas y columnas"
        },
        # Pregunta 25
        {
            "pregunta": "¿Es cierto que las bases de datos de documentos almacenan información en formatos como JSON o BSON?",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 26
        {
            "pregunta": "¿Cuál de los siguientes servicios ofrece gestión de bases de datos relacionales?",
            "tipo": "opcion_multiple",
            "opciones": [
                "AWS Lambda y Azure Functions",
                "AWS RDS y Google Cloud SQL",
                "AWS S3 y Azure Blob Storage",
                "DynamoDB y MongoDB Atlas"
            ],
            "respuesta": "AWS RDS y Google Cloud SQL"
        },
        # Pregunta 27
        {
            "pregunta": "¿Qué característica principal tienen las bases de datos NoSQL orientadas a columnas?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Almacenan datos en formato JSON",
                "Organizan los datos por columnas en lugar de filas",
                "Solo permiten consultas SQL",
                "Requieren esquemas fijos"
            ],
            "respuesta": "Organizan los datos por columnas en lugar de filas"
        },
        # Pregunta 28
        {
            "pregunta": "¿Es cierto que el comando SELECT en SQL se utiliza para realizar consultas?",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 29
        {
            "pregunta": "¿Es cierto que SQL es un lenguaje estándar para interactuar con bases de datos relacionales?",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 30
        {
            "pregunta": "¿Qué motores de bases de datos soporta AWS RDS?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Solo MySQL",
                "MySQL, PostgreSQL y SQL Server",
                "Solo MongoDB",
                "Solo Oracle"
            ],
            "respuesta": "MySQL, PostgreSQL y SQL Server"
        },
        # Pregunta 31
        {
            "pregunta": "¿Qué define principalmente a las bases de datos NoSQL?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Solo funcionan con SQL",
                "Están diseñadas para datos no estructurados y escalabilidad horizontal",
                "Requieren esquemas rígidos",
                "Solo se usan en aplicaciones móviles"
            ],
            "respuesta": "Están diseñadas para datos no estructurados y escalabilidad horizontal"
        },
        # Pregunta 32
        {
            "pregunta": "¿Cuáles son ejemplos de tipos de bases de datos NoSQL?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Solo SQL Server",
                "Clave-valor, Documentos y Columnas",
                "Solo MySQL",
                "Solo PostgreSQL"
            ],
            "respuesta": "Clave-valor, Documentos y Columnas"
        },
        # Pregunta 33
        {
           "pregunta": "Marque lo correcto en relación a las bases de datos documentales:",
           "tipo": "opcion_multiple_multiple",
           "opciones": [
               "Almacenan información en formatos como JSON, BSON o XML",
               "Cada documento es una unidad de datos estructurada con campos clave y valores",
               "La flexibilidad permite esquemas variados",
               "Ninguna de las anteriores"
            ],
         "respuesta": [
              "Almacenan información en formatos como JSON, BSON o XML",
              "Cada documento es una unidad de datos estructurada con campos clave y valores",
              "La flexibilidad permite esquemas variados"
            ]
        },

        # Pregunta 34
        {
            "pregunta": "EC2 permite a los usuarios alquilar capacidad de informática virtual en la nube desplegando y ejecutando aplicaciones en:",
            "tipo": "opcion_multiple",
            "opciones": [
                "Contenedores",
                "Instancias",
                "Buckets",
                "Funciones"
            ],
            "respuesta": "Instancias"
        },
        # Pregunta 35
        {
            "pregunta": "¿Cómo es el pago de AWS Lambda?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Por hora completa de uso",
                "El tiempo de ejecución en milisegundos",
                "Por cantidad de servidores",
                "Mensualmente fijo"
            ],
            "respuesta": "El tiempo de ejecución en milisegundos"
        },
        # Pregunta 36
        {
            "pregunta": "Fmt es una librería clave en Go para formatear y mostrar datos en la consola",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 37
        {
            "pregunta": "Marque las razones del por qué usar Go para Scripts de automatización es beneficioso:",
            "tipo": "opcion_multiple",
            "opciones": [
                "Solo por su sintaxis simple",
                "Rendimiento y eficiencia",
                "Solo porque es nuevo",
                "Solo por popularidad"
            ],
            "respuesta": "Rendimiento y eficiencia"
        },
        # Pregunta 38
        {
            "pregunta": "Relacione los beneficios de Docker Compose:",
            "tipo": "unir_conceptos",
            "conceptos": {
                "Configuración": "Definir servicios en un archivo YAML",
                "Separación de servicios": "Cada servicio se ejecuta de forma aislada",
                "Escalabilidad": "Permite escalar servicios fácilmente",
                "Gestión simplificada": "Comandos simples para múltiples contenedores"
            }
        },
        # Pregunta 39
        {
            "pregunta": "¿Qué es Docker?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Un sistema operativo",
                "Docker es una plataforma que permite empaquetar aplicaciones en contenedores",
                "Un lenguaje de programación",
                "Un editor de código"
            ],
            "respuesta": "Docker es una plataforma que permite empaquetar aplicaciones en contenedores"
        },
        # Pregunta 40
        {
            "pregunta": "Relacione el comando de Docker con la acción correspondiente:",
            "tipo": "unir_conceptos",
            "conceptos": {
                "docker rmi": "Eliminar una imagen específica",
                "docker build": "Construye una imagen desde un Dockerfile",
                "docker pull": "Descarga una imagen desde Docker Hub",
                "docker images": "Lista las imágenes disponibles en el sistema"
            }
        },
        # Pregunta 41
        {
            "pregunta": "¿En qué tecnología se basa Docker?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Máquinas virtuales",
                "Contenedores",
                "Cloud computing",
                "Blockchain"
            ],
            "respuesta": "Contenedores"
        },
        # Pregunta 42
        {
            "pregunta": "Relacione el concepto de Docker con su significado:",
            "tipo": "unir_conceptos",
            "conceptos": {
                "Registro de Docker": "Almacén de imágenes (Docker Hub)",
                "Cliente Docker": "Herramienta de línea de comandos",
                "Contenedores Docker": "Unidades de ejecución",
                "Daemon de Docker": "Servicio que ejecuta en segundo plano",
                "Imágenes de Docker": "Plantillas de contenedores"
            }
        },
        # Pregunta 43
        {
            "pregunta": "Relacione los componentes principales de Docker con su función:",
            "tipo": "unir_conceptos",
            "conceptos": {
                "Volúmenes": "Definen la persistencia de datos entre reinicios de contenedores",
                "Redes": "Permiten que los contenedores se comuniquen entre sí",
                "Servicios": "Definen los contenedores que se ejecutarán, incluyendo la imagen a usar y las configuraciones específicas"
            }
        },
        # Pregunta 44
        {
            "pregunta": "¿Cuáles opciones son parte de la configuración de un Dockerfile?",
            "tipo": "opcion_multiple",
            "opciones": [
                "Solo comandos básicos",
                "Agregar, Puertos, Volúmenes y Configuración",
                "Solo el sistema operativo",
                "Solo las dependencias"
            ],
            "respuesta": "Agregar, Puertos, Volúmenes y Configuración"
        },
        # Pregunta 45
        {
            "pregunta": "Relacione el concepto de Docker con su significado:",
            "tipo": "unir_conceptos",
            "conceptos": {
                "Dockerfile": "Script para crear imágenes Docker",
                "Registro": "Almacén de imágenes Docker",
                "Docker Hub": "Registro público más conocido",
                "Imagen": "Plantilla inmutable de un contenedor",
                "Contenedor": "Instancia en ejecución de una imagen"
            }
        },
        # Pregunta 46
        {
            "pregunta": "Los volúmenes hacen que los datos sean volátiles y desaparezcan con la eliminación de contenedores.",
            "tipo": "true_false",
            "respuesta": False
        },
        # Pregunta 47
        {
            "pregunta": "Con Docker Compose, se puede usar un archivo YAML para configurar los servicios de una aplicación",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 48
        {
            "pregunta": "Relacione el concepto con la definición de Docker:",
            "tipo": "unir_conceptos",
            "conceptos": {
                "Máximo rendimiento de los recursos": "Eficiencia",
                "Despliegue de aplicaciones en tiempos cortos": "Rapidez",
                "Ejecuta aplicaciones en cualquier lugar": "Portabilidad",
                "Fácil ampliación de un sistema": "Escalabilidad",
                "Los contenedores son independientes": "Aislamiento"
            }
        },
        # Pregunta 49
        {
            "pregunta": "Verifique si el enunciado es verdadero. Docker se utiliza en entornos de integración continua y despliegue continuo (CI/CD):",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 50
        {
            "pregunta": "Docker se utiliza para despliegue y gestión de aplicaciones de microservicios",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 51
        {
            "pregunta": "Docker permite ejecutar múltiples aplicaciones en el mismo servidor sin conflictos",
            "tipo": "true_false",
            "respuesta": True
        },
        # Pregunta 52
        {
            "pregunta": "Docker se utiliza para migrar aplicaciones de entornos Windows a entornos Mac",
            "tipo": "true_false",
            "respuesta": False
        }
    ]
    
    # Asignar IDs únicos
    for i, pregunta in enumerate(preguntas):
        pregunta["id_unico"] = i
    
    return preguntas

# ============================================
# 2. FUNCIONES DE GESTIÓN DE SESIÓN
# ============================================

def inicializar_sesion():
    """Inicializa las variables de sesión de Streamlit"""
    if 'inicializado' not in st.session_state:
        todas_preguntas = cargar_preguntas()
        
        st.session_state.banco_completo_preguntas = todas_preguntas.copy()
        st.session_state.preguntas_usadas = set()
        st.session_state.historial_tests = []
        st.session_state.test_actual = None
        st.session_state.estado = "inicio"
        st.session_state.inicializado = True

def obtener_preguntas_disponibles():
    """Retorna preguntas que no han sido usadas"""
    disponibles = [
        p for p in st.session_state.banco_completo_preguntas 
        if p["id_unico"] not in st.session_state.preguntas_usadas
    ]
    return disponibles

def reiniciar_banco_preguntas():
    """Reinicia el banco de preguntas cuando se agoten"""
    st.session_state.preguntas_usadas = set()
    st.success("🔄 Se ha reiniciado el banco de preguntas. Puedes continuar con el test.")

# ============================================
# 3. FUNCIONES DEL TEST
# ============================================

def crear_nuevo_test():
    """Crea un nuevo test con TODAS las preguntas disponibles"""
    preguntas_disponibles = obtener_preguntas_disponibles()
    
    # Validar si hay preguntas disponibles
    if len(preguntas_disponibles) == 0:
        # Reiniciar automáticamente si no hay preguntas disponibles
        reiniciar_banco_preguntas()
        preguntas_disponibles = obtener_preguntas_disponibles()
    
    # Tomar TODAS las preguntas disponibles (sin límite)
    preguntas_seleccionadas = preguntas_disponibles.copy()
    
    # Mezclarlas aleatoriamente
    random.shuffle(preguntas_seleccionadas)
    
    # Marcar como usadas
    for pregunta in preguntas_seleccionadas:
        st.session_state.preguntas_usadas.add(pregunta["id_unico"])
    
    # Crear objeto de test
    test = {
        "id": len(st.session_state.historial_tests) + 1,
        "fecha_inicio": datetime.now(),
        "preguntas": preguntas_seleccionadas,
        "respuestas": {},
        "indice_actual": 0,
        "completado": False,
        "fecha_finalizacion": None,
        "puntaje": None,
        "detalle_resultados": None,
        "total_preguntas": len(preguntas_seleccionadas)
    }
    
    return test

def validar_respuesta(pregunta, respuesta_usuario):
    resultado = {
        "correcta": False,
        "puntos": 0,
        "respuesta_usuario": respuesta_usuario,
        "respuesta_correcta": None,
        "explicacion": ""
    }

    if respuesta_usuario is None:
        resultado["explicacion"] = "❌ No respondiste esta pregunta."
        return resultado

    # ==========================
    # VERDADERO / FALSO
    # ==========================
    if pregunta["tipo"] == "true_false":
        resultado["respuesta_correcta"] = pregunta["respuesta"]
        if respuesta_usuario == pregunta["respuesta"]:
            resultado["correcta"] = True
            resultado["puntos"] = 1
            resultado["explicacion"] = "✅ Correcto."
        else:
            resultado["explicacion"] = "❌ Incorrecto."

    # ==========================
    # OPCIÓN MÚLTIPLE (UNA)
    # ==========================
    elif pregunta["tipo"] == "opcion_multiple":
        resultado["respuesta_correcta"] = pregunta["respuesta"]
        if respuesta_usuario == pregunta["respuesta"]:
            resultado["correcta"] = True
            resultado["puntos"] = 1
            resultado["explicacion"] = "✅ Correcto."
        else:
            resultado["explicacion"] = f"❌ Incorrecto. Respuesta correcta: {pregunta['respuesta']}"

    # ==========================
    # OPCIÓN MÚLTIPLE (VARIAS)
    # ==========================
    elif pregunta["tipo"] == "opcion_multiple_multiple":
        correctas = set(pregunta["respuesta"])
        usuario = set(respuesta_usuario)

        resultado["respuesta_correcta"] = list(correctas)

        if usuario == correctas:
            resultado["correcta"] = True
            resultado["puntos"] = 1
            resultado["explicacion"] = "✅ Correcto. Seleccionaste todas las opciones correctas."
        else:
            resultado["explicacion"] = (
                f"❌ Incorrecto.\n\n"
                f"✔️ Correctas: {', '.join(correctas)}\n"
                f"❌ Tu selección: {', '.join(usuario) if usuario else 'Ninguna'}"
            )

    # ==========================
    # UNIR CONCEPTOS
    # ==========================
    elif pregunta["tipo"] == "unir_conceptos":
        aciertos = 0
        total = len(pregunta["conceptos"])
        detalles = []

        for concepto, correcta in pregunta["conceptos"].items():
            if respuesta_usuario.get(concepto) == correcta:
                aciertos += 1
                detalles.append(f"✅ {concepto}")
            else:
                detalles.append(f"❌ {concepto}")

        if aciertos == total:
            resultado["correcta"] = True
            resultado["puntos"] = 1
        elif aciertos >= total / 2:
            resultado["puntos"] = 0.5

        resultado["explicacion"] = "\n".join(detalles)

    return resultado


def calcular_resultados(test):
    """Calcula los resultados finales del test"""
    puntaje_total = 0
    detalle = []
    
    for i, pregunta in enumerate(test["preguntas"]):
        respuesta_usuario = test["respuestas"].get(i)
        resultado = validar_respuesta(pregunta, respuesta_usuario)
        
        puntaje_total += resultado["puntos"]
        
        detalle.append({
            "numero": i + 1,
            "pregunta": pregunta["pregunta"],
            "tipo": pregunta["tipo"],
            "seccion": pregunta.get("seccion", "Sin categoría"),
            "correcta": resultado["correcta"],
            "puntos": resultado["puntos"],
            "explicacion": resultado["explicacion"],
            "respuesta_usuario": resultado["respuesta_usuario"],
            "respuesta_correcta": resultado["respuesta_correcta"]
        })
    
    total_preguntas = len(test["preguntas"])
    correctas = sum(1 for d in detalle if d["correcta"])
    incorrectas = total_preguntas - correctas
    porcentaje = (puntaje_total / total_preguntas) * 100
    aprobado = porcentaje >= 75
    
    errores_por_seccion = defaultdict(int)
    total_por_seccion = defaultdict(int)
    
    for item in detalle:
        seccion = item["seccion"]
        total_por_seccion[seccion] += 1
        if not item["correcta"]:
            errores_por_seccion[seccion] += 1
    
    resultados = {
        "puntaje_total": puntaje_total,
        "total_preguntas": total_preguntas,
        "correctas": correctas,
        "incorrectas": incorrectas,
        "porcentaje": porcentaje,
        "aprobado": aprobado,
        "detalle": detalle,
        "errores_por_seccion": dict(errores_por_seccion),
        "total_por_seccion": dict(total_por_seccion)
    }
    
    return resultados

# ============================================
# 4. FUNCIONES DE INTERFAZ
# ============================================

def mostrar_pregunta(pregunta, indice, test):
    """Muestra una pregunta según su tipo"""
    total = test.get('total_preguntas', len(test['preguntas']))
    st.markdown(f"### 📝 Pregunta {indice + 1} de {total}")
    st.markdown(f"**Categoría:** {pregunta.get('seccion', 'General')}")
    st.write("")

    with st.container():
        st.markdown(f"**{pregunta['pregunta']}**")
        st.write("")

        # ==========================
        # VERDADERO / FALSO
        # ==========================
        if pregunta["tipo"] == "true_false":
            respuesta_actual = test["respuestas"].get(indice)
            index_actual = 0 if respuesta_actual is True else 1 if respuesta_actual is False else None

            respuesta = st.radio(
                "Selecciona tu respuesta:",
                ["Verdadero", "Falso"],
                index=index_actual,
                key=f"pregunta_{indice}_{pregunta['id_unico']}"
            )

            test["respuestas"][indice] = (respuesta == "Verdadero")

        # ==========================
        # OPCIÓN MÚLTIPLE (UNA)
        # ==========================
        elif pregunta["tipo"] == "opcion_multiple":
            opciones = pregunta["opciones"].copy()

            random.seed(pregunta["id_unico"])
            random.shuffle(opciones)
            random.seed()

            respuesta_actual = test["respuestas"].get(indice)
            index_actual = opciones.index(respuesta_actual) if respuesta_actual in opciones else None

            respuesta = st.radio(
                "Selecciona la opción correcta:",
                opciones,
                index=index_actual,
                key=f"pregunta_{indice}_{pregunta['id_unico']}"
            )

            test["respuestas"][indice] = respuesta

        # ==========================
        # OPCIÓN MÚLTIPLE (VARIAS) - CORRECCIÓN APLICADA
        # ==========================
        elif pregunta["tipo"] == "opcion_multiple_multiple":
            opciones = pregunta["opciones"]
            respuesta_actual = test["respuestas"].get(indice, [])

            respuesta = st.multiselect(
                "Selecciona todas las opciones correctas:",
                opciones,
                default=respuesta_actual,
                key=f"pregunta_{indice}_{pregunta['id_unico']}"
            )

            test["respuestas"][indice] = respuesta

        # ==========================
        # UNIR CONCEPTOS - CORRECCIÓN CLAVE
        # ==========================
        elif pregunta["tipo"] == "unir_conceptos":
            st.write("**Relaciona cada concepto con su definición:**")
            st.write("")

            conceptos = list(pregunta["conceptos"].keys())
            todas_definiciones = list(pregunta["conceptos"].values())

            respuestas_unir = test["respuestas"].get(indice, {})
            if not isinstance(respuestas_unir, dict):
                respuestas_unir = {}

            for concepto in conceptos:
                st.markdown(f"**{concepto}**")

                definicion_correcta = pregunta["conceptos"][concepto]
                
                # CORRECCIÓN: Solo mostrar TODAS las definiciones posibles
                # sin mezclar ni limitar, para que siempre estén disponibles
                opciones_def = todas_definiciones.copy()
                
                # Mezclar usando seed para consistencia
                random.seed(pregunta["id_unico"] + hash(concepto))
                random.shuffle(opciones_def)
                random.seed()

                respuesta_actual = respuestas_unir.get(concepto)
                index_actual = opciones_def.index(respuesta_actual) if respuesta_actual in opciones_def else 0

                seleccion = st.selectbox(
                    f"Definición para {concepto}:",
                    opciones_def,
                    index=index_actual,
                    key=f"unir_{indice}_{pregunta['id_unico']}_{concepto}"
                )

                respuestas_unir[concepto] = seleccion

            test["respuestas"][indice] = respuestas_unir


def mostrar_navegacion_preguntas(test):
    """Muestra navegación visual de las preguntas"""
    st.write("---")
    st.markdown("### 🗺️ Navegación Rápida")
    
    total_preguntas = test.get('total_preguntas', len(test['preguntas']))
    
    # Calcular número de columnas (máximo 15 por fila)
    num_cols = min(15, total_preguntas)
    num_filas = (total_preguntas + num_cols - 1) // num_cols
    
    for fila in range(num_filas):
        cols = st.columns(num_cols)
        for col_idx in range(num_cols):
            i = fila * num_cols + col_idx
            if i < total_preguntas:
                with cols[col_idx]:
                    if i in test["respuestas"]:
                        emoji = "✅"
                    else:
                        emoji = "⬜"
                    
                    if i == test["indice_actual"]:
                        emoji = "👉"
                    
                    if st.button(f"{i+1}", key=f"nav_{i}", use_container_width=True):
                        test["indice_actual"] = i
                        st.rerun()

def mostrar_resultados(test, resultados):
    """Muestra los resultados del test"""
    st.title("🎯 Resultados del Test")
    st.write(f"**Test N°:** {test['id']}")
    st.write(f"**Fecha:** {test['fecha_finalizacion'].strftime('%d/%m/%Y %H:%M')}")
    st.write("")
    
    total = test.get('total_preguntas', len(test['preguntas']))
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Puntaje", f"{resultados['puntaje_total']:.1f}/{total}")
    with col2:
        st.metric("Porcentaje", f"{resultados['porcentaje']:.1f}%")
    with col3:
        st.metric("✅ Correctas", resultados['correctas'])
    with col4:
        st.metric("❌ Incorrectas", resultados['incorrectas'])
    
    st.progress(resultados['porcentaje'] / 100)
    st.write("")
    
    puntaje_minimo = total * 0.75
    
    if resultados['aprobado']:
        st.success("### ✅ ¡APROBADO! ¡Felicidades! 🎉")
        st.balloons()
    else:
        st.error(f"### ❌ NO APROBADO")
        st.info(f"Necesitas al menos {puntaje_minimo:.1f} puntos (75%). Te faltaron {puntaje_minimo - resultados['puntaje_total']:.1f} puntos.")
    
    st.write("---")
    
    # Análisis por sección
    if resultados['errores_por_seccion']:
        st.markdown("### 📊 Análisis por Categoría")
        
        df_secciones = pd.DataFrame([
            {
                "Categoría": seccion,
                "Total": resultados['total_por_seccion'][seccion],
                "Errores": errores,
                "Aciertos": resultados['total_por_seccion'][seccion] - errores,
                "% Acierto": f"{((resultados['total_por_seccion'][seccion] - errores) / resultados['total_por_seccion'][seccion] * 100):.1f}%"
            }
            for seccion, errores in sorted(
                resultados['errores_por_seccion'].items(), 
                key=lambda x: x[1], 
                reverse=True
            )
        ])
        
        st.dataframe(df_secciones, use_container_width=True, hide_index=True)
    
    st.write("---")
    
    # Revisión detallada
    st.markdown("### 📋 Revisión Detallada")
    
    filtro = st.selectbox(
        "Filtrar preguntas:",
        ["Todas las preguntas", "Solo incorrectas ❌", "Solo correctas ✅"],
        key="filtro_resultados"
    )
    
    detalle_filtrado = resultados['detalle']
    if filtro == "Solo incorrectas ❌":
        detalle_filtrado = [d for d in resultados['detalle'] if not d['correcta']]
    elif filtro == "Solo correctas ✅":
        detalle_filtrado = [d for d in resultados['detalle'] if d['correcta']]
    
    if not detalle_filtrado:
        st.info("No hay preguntas que mostrar con el filtro seleccionado.")
    else:
        st.write(f"**Mostrando {len(detalle_filtrado)} preguntas**")
        st.write("")
        
        for item in detalle_filtrado:
            icono = "✅" if item['correcta'] else "❌"
            titulo = f"{icono} Pregunta {item['numero']}: {item['pregunta'][:60]}..."
            
            with st.expander(titulo, expanded=False):
                st.markdown(f"**Categoría:** {item['seccion']}")
                st.markdown(f"**Tipo:** {item['tipo'].replace('_', ' ').title()}")
                
                st.write("")
                st.markdown("**Pregunta:**")
                st.info(item['pregunta'])
                
                st.markdown("**Explicación:**")
                st.write(item['explicacion'])

def finalizar_test(test):
    """Finaliza el test y calcula los resultados"""
    test["completado"] = True
    test["fecha_finalizacion"] = datetime.now()
    
    resultados = calcular_resultados(test)
    
    test["puntaje"] = resultados["puntaje_total"]
    test["detalle_resultados"] = resultados
    
    st.session_state.historial_tests.append(test)
    st.session_state.estado = "resultados"
    st.rerun()

# ============================================
# 5. INTERFAZ PRINCIPAL
# ============================================

def main():
    st.set_page_config(
        page_title="Simulador - Aplicaciones en la Nube",
        page_icon="☁️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    inicializar_sesion()
    
    st.title("☁️ Simulador de Aplicaciones en la Nube")
    st.markdown("*Bases de Datos, AWS, Docker y Programación Go*")
    st.write("")
    
    # Sidebar
    with st.sidebar:
        st.header("📊 Panel de Control")
        
        total_banco = len(st.session_state.banco_completo_preguntas)
        usadas = len(st.session_state.preguntas_usadas)
        disponibles = total_banco - usadas
        
        st.metric("Total en Banco", total_banco)
        st.metric("Preguntas Disponibles", disponibles)
        st.metric("Preguntas Usadas", usadas)
        st.metric("Tests Realizados", len(st.session_state.historial_tests))
        
        st.write("")
        st.progress(usadas / total_banco if total_banco > 0 else 0)
        st.caption(f"{(usadas/total_banco*100):.1f}% del banco utilizado")
        
        st.write("---")
        
        if st.session_state.historial_tests:
            st.subheader("📜 Historial")
            for test_hist in reversed(st.session_state.historial_tests[-5:]):
                if test_hist.get('completado'):
                    resultados = test_hist.get('detalle_resultados')
                    if resultados:
                        icono = "✅" if resultados['aprobado'] else "❌"
                        total = test_hist.get('total_preguntas', len(test_hist.get('preguntas', [])))
                        st.write(f"{icono} Test #{test_hist['id']}: {resultados['puntaje_total']:.1f}/{total}")
        
        st.write("---")
        
        with st.expander("ℹ️ Información", expanded=False):
            st.markdown("""
            **Características:**
            - Todas las preguntas disponibles por test
            - Preguntas sin repetición entre tests
            - Puntaje mínimo: 75%
            - Análisis detallado
            
            **Tipos de preguntas:**
            - Verdadero/Falso
            - Opción múltiple
            - Relacionar conceptos
            
            **Temas:**
            - Bases de Datos
            - AWS y Servicios Cloud
            - Docker y Contenedores
            - Programación Go
            """)
        
        st.write("")
        if st.button("🔄 Reiniciar Todo", type="secondary", use_container_width=True):
            if st.session_state.get('confirmar_reinicio', False):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
            else:
                st.session_state.confirmar_reinicio = True
                st.warning("⚠️ Presiona nuevamente para confirmar")
    
    # Contenido principal
    if st.session_state.estado == "inicio":
        mostrar_pantalla_inicio()
    elif st.session_state.estado == "test_activo":
        mostrar_pantalla_test()
    elif st.session_state.estado == "resultados":
        mostrar_pantalla_resultados()

def mostrar_pantalla_inicio():
    """Pantalla inicial del simulador"""
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 🎯 Bienvenido al Simulador")
        st.write("Este simulador te ayudará a prepararte con preguntas sobre aplicaciones en la nube, bases de datos, Docker y más.")
        
        st.write("")
        st.markdown("### 📚 Categorías Disponibles:")
        
        categorias = [
            "💾 Bases de Datos (Relacionales y NoSQL)",
            "☁️ AWS y Servicios en la Nube",
            "🐳 Docker y Contenedores",
            "🔷 Programación en Go",
            "🔍 SQL y Consultas",
        ]
        
        for cat in categorias:
            st.write(f"• {cat}")
        
        st.write("")
        st.write("---")
        
        disponibles = len(obtener_preguntas_disponibles())
        
        if disponibles == 0:
            st.info("🔄 Todas las preguntas han sido utilizadas. El banco se reiniciará al comenzar un nuevo test.")
        else:
            st.success(f"✅ {disponibles} preguntas disponibles para el próximo test")
        
        if st.button("🚀 Comenzar Nuevo Test", type="primary", use_container_width=True):
            test = crear_nuevo_test()
            if test:
                st.session_state.test_actual = test
                st.session_state.estado = "test_activo"
                st.rerun()
    
    with col2:
        st.markdown("### 📋 Instrucciones")
        st.info("""
        **Cómo funciona:**
        
        1️⃣ Cada test usa **todas las preguntas disponibles**
        
        2️⃣ Las preguntas **no se repiten** entre tests
        
        3️⃣ Puntaje mínimo: **75%** de aprobación
        
        4️⃣ Puedes **navegar** entre preguntas
        
        5️⃣ Las respuestas se **guardan automáticamente**
        
        6️⃣ Al finalizar verás un **análisis detallado**
        
        7️⃣ Cuando completes todos los tests, el banco se **reinicia automáticamente**
        """)
        
        st.write("")
        
        if st.session_state.historial_tests:
            mejor_puntaje = max(
                [t.get('puntaje', 0) for t in st.session_state.historial_tests if t.get('completado', False)],
                default=0
            )
            mejor_total = 0
            for t in st.session_state.historial_tests:
                if t.get('completado', False) and t.get('puntaje', 0) == mejor_puntaje:
                    mejor_total = t.get('total_preguntas', len(t.get('preguntas', [])))
                    break
            
            if mejor_total > 0:
                st.metric("🏆 Mejor Puntaje", f"{mejor_puntaje:.1f}/{mejor_total}")

def mostrar_pantalla_test():
    """Pantalla donde se realiza el test"""
    test = st.session_state.test_actual
    
    if not test:
        st.error("❌ Error: No hay test activo")
        st.session_state.estado = "inicio"
        st.rerun()
        return
    
    total_preguntas = test.get('total_preguntas', len(test['preguntas']))
    
    progreso = (test["indice_actual"] + 1) / total_preguntas
    st.progress(progreso)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown(f"**Progreso:** {test['indice_actual'] + 1}/{total_preguntas} preguntas")
    with col2:
        respondidas = len(test["respuestas"])
        st.markdown(f"**Respondidas:** {respondidas}/{total_preguntas}")
    with col3:
        faltantes = total_preguntas - respondidas
        if faltantes > 0:
            st.markdown(f"**⚠️ Faltan:** {faltantes}")
        else:
            st.markdown(f"**✅ Todas respondidas**")
    
    st.write("")
    
    pregunta_actual = test["preguntas"][test["indice_actual"]]
    mostrar_pregunta(pregunta_actual, test["indice_actual"], test)
    
    st.write("")
    st.write("---")
    
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 2])
    
    with col1:
        if test["indice_actual"] > 0:
            if st.button("⬅️ Anterior", use_container_width=True):
                test["indice_actual"] -= 1
                st.rerun()
        else:
            st.button("⬅️ Anterior", disabled=True, use_container_width=True)
    
    with col2:
        if test["indice_actual"] < total_preguntas - 1:
            if st.button("Siguiente ➡️", use_container_width=True):
                test["indice_actual"] += 1
                st.rerun()
        else:
            st.button("Siguiente ➡️", disabled=True, use_container_width=True)
    
    with col3:
        if st.button("🔄 Primera", use_container_width=True):
            test["indice_actual"] = 0
            st.rerun()
    
    with col4:
        if st.button("⏭️ Última", use_container_width=True):
            test["indice_actual"] = total_preguntas - 1
            st.rerun()
    
    with col5:
        todas_respondidas = len(test["respuestas"]) == total_preguntas
        
        if todas_respondidas:
            if st.button("✅ Finalizar Test", type="primary", use_container_width=True):
                finalizar_test(test)
        else:
            sin_responder = total_preguntas - len(test["respuestas"])
            if st.button(f"⚠️ Finalizar ({sin_responder} sin responder)", type="secondary", use_container_width=True):
                if st.session_state.get('confirmar_finalizar', False):
                    finalizar_test(test)
                else:
                    st.session_state.confirmar_finalizar = True
                    st.warning(f"⚠️ Tienes {sin_responder} preguntas sin responder. Presiona nuevamente para confirmar.")
    
    mostrar_navegacion_preguntas(test)
    
    sin_responder = total_preguntas - len(test["respuestas"])
    if sin_responder > 0:
        st.info(f"ℹ️ Tienes {sin_responder} pregunta(s) sin responder. Las preguntas sin respuesta contarán como incorrectas.")

def mostrar_pantalla_resultados():
    """Pantalla de resultados del test"""
    test = st.session_state.test_actual
    
    if not test or not test.get("completado"):
        st.error("❌ Error: No hay resultados para mostrar")
        st.session_state.estado = "inicio"
        st.rerun()
        return
    
    resultados = test["detalle_resultados"]
    
    if not resultados:
        st.error("❌ Error: No se pudieron calcular los resultados")
        st.session_state.estado = "inicio"
        st.rerun()
        return
    
    mostrar_resultados(test, resultados)
    
    st.write("")
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔄 Realizar Otro Test", type="primary", use_container_width=True):
            st.session_state.test_actual = None
            st.session_state.estado = "inicio"
            if 'confirmar_finalizar' in st.session_state:
                del st.session_state.confirmar_finalizar
            st.rerun()
    
    with col2:
        if st.button("📊 Ver Historial", use_container_width=True):
            mostrar_historial_completo()
    
    with col3:
        if st.button("🏠 Volver al Inicio", use_container_width=True):
            st.session_state.test_actual = None
            st.session_state.estado = "inicio"
            if 'confirmar_finalizar' in st.session_state:
                del st.session_state.confirmar_finalizar
            st.rerun()

def mostrar_historial_completo():
    """Muestra el historial completo de tests realizados"""
    st.write("---")
    st.markdown("### 📜 Historial Completo de Tests")
    
    if not st.session_state.historial_tests:
        st.info("No hay tests realizados aún.")
        return
    
    datos_historial = []
    for test in st.session_state.historial_tests:
        if test.get("completado"):
            resultados = test.get("detalle_resultados")
            if resultados:
                total = test.get('total_preguntas', len(test.get('preguntas', [])))
                datos_historial.append({
                    "Test #": test["id"],
                    "Fecha": test["fecha_finalizacion"].strftime("%d/%m/%Y %H:%M"),
                    "Puntaje": f"{resultados['puntaje_total']:.1f}/{total}",
                    "Porcentaje": f"{resultados['porcentaje']:.1f}%",
                    "Estado": "✅ Aprobado" if resultados['aprobado'] else "❌ Reprobado",
                    "Correctas": resultados['correctas'],
                    "Incorrectas": resultados['incorrectas']
                })
    
    if datos_historial:
        df_historial = pd.DataFrame(datos_historial)
        st.dataframe(df_historial, use_container_width=True, hide_index=True)
        
        st.write("")
        st.markdown("### 📈 Estadísticas Generales")
        
        total_tests = len(datos_historial)
        aprobados = sum(1 for t in st.session_state.historial_tests if t.get("completado") and t.get("detalle_resultados", {}).get("aprobado", False))
        
        puntajes = [t.get("detalle_resultados", {}).get("puntaje_total", 0) for t in st.session_state.historial_tests if t.get("completado")]
        promedio = sum(puntajes) / len(puntajes) if puntajes else 0
        mejor = max(puntajes) if puntajes else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Tests", total_tests)
        with col2:
            st.metric("Aprobados", f"{aprobados}/{total_tests}")
        with col3:
            st.metric("Mejor Puntaje", f"{mejor:.1f}")

if __name__ == "__main__":
    main()
