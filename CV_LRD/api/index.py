from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="CV - Luis Alberto Ruiz Diaz")

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

CV_DATA = {
    "nombre": "Luis Alberto Ruiz Diaz",
    "titulo": "Analista Funcional & de Datos | BI, SQL & Automatización",
    "subtitulo": "+15 años optimizando operaciones Telecom/NOC, evolucionando hacia Ingeniería de Datos, Business Intelligence (BigQuery / Power BI) e IA Aplicada.",
    "ubicacion": "Ciudadela, Buenos Aires, Argentina",
    "email": "luiggi.ruiz.diaz@gmail.com",
    "linkedin": "https://www.linkedin.com/in/lrd70",
    "github": "https://github.com/Lwiggi",
    "kpis": [
        {"valor": "+15 años", "etiqueta": "Experiencia en Telecom / NOC"},
        {"valor": "ETL & BI", "etiqueta": "BigQuery, SQL, Power BI & Looker"},
        {"valor": "+20", "etiqueta": "Certificaciones en Datos, Dev e IA"},
        {"valor": "Key User", "etiqueta": "Ticketeras OSS, ITSM & Product Backlog"},
    ],
    "resumen": (
        "Profesional con sólida trayectoria en operaciones técnicas de misión crítica (NOC), logística de materiales "
        "y soporte funcional en Telecomunicaciones. Especializado en transformar datos operativos dispersos en indicadores "
        "ejecutivos mediante procesos ETL, consultas avanzadas en SQL/BigQuery y tableros de Business Intelligence. "
        "Nexo efectivo entre áreas de negocio, operación y desarrollo (Product Backlog / OSS), complementado con "
        "formación en desarrollo web (Python, Django, React) y flujos modernos con Inteligencia Artificial (RAG, Agentes, MCP)."
    ),
    "skills": {
        "Datos & Business Intelligence": [
            "SQL (Modelado & Conditional JOINs)",
            "Google BigQuery",
            "Power BI & SQL Server",
            "Looker Studio (Data Studio)",
            "Procesos ETL & KPIs Ejecutivos",
            "Data Analytics & Data Science",
            "Microsoft Access / Excel Avanzado",
        ],
        "Análisis Funcional & Operaciones": [
            "Análisis Funcional & Mejora Continua",
            "Gestión de Product Backlog",
            "Key User OSS / Ticketeras",
            "BMC Helix ITSM",
            "Salesforce (CoNext / ECO)",
            "SAP CRM & Auditoría de Stock",
        ],
        "Desarrollo & IA Aplicada": [
            "Python (FastAPI / Django)",
            "JavaScript / React / Node.js",
            "HTML5 / CSS3 / Git",
            "Prompt Engineering & Contexto",
            "Agentes IA, RAG, Embeddings & MCP",
        ],
    },
    "experiencia": [
        {
            "rol": "Analista Sr. Funcional, Datos y Administración Técnica NOC",
            "empresa": "Personal (Telecom Argentina)",
            "periodo": "Ene 2011 – Actualidad",
            "ubicacion": "C.A.B.A., Argentina",
            "logros": [
                "Diseño y ejecución de procesos ETL para la generación de indicadores ejecutivos y tableros de gestión operativa del área NOC.",
                "Analista funcional y Key User de plataformas de ticketing (BMC Helix ITSM / Salesforce), liderando soporte a la operación y mejora continua.",
                "Stakeholder de negocio frente a equipos de desarrollo OSS y gestión de Product Backlog para evolución de herramientas internas.",
                "Control analítico de abastecimiento, trazabilidad de stock de equipamiento Spare en Bases Técnicas y seguimiento de servicios técnicos.",
            ],
        },
        {
            "rol": "Analista de Auditoría de Materiales y Stock",
            "empresa": "Cablevisión – Fibertel",
            "periodo": "Jul 2008 – Dic 2010",
            "ubicacion": "C.A.B.A., Argentina",
            "logros": [
                "Análisis de inventarios, conciliación de diferencias y carga/control de movimientos de stock en SAP CRM.",
                "Elaboración de informes técnicos de auditoría en Bases Técnicas para reducción de desvíos operativos.",
            ],
        },
        {
            "rol": "Coordinador y Despachante de Operaciones Técnicas",
            "empresa": "Cablevisión – Fibertel (PRIMA)",
            "periodo": "Oct 2004 – Jul 2008",
            "ubicacion": "AMBA e Interior, Argentina",
            "logros": [
                "Planificación de hojas de ruta, coordinación de visitas técnicas domiciliarias y seguimiento de KPIs de cumplimiento en CRM.",
                "Control de recupero y disponibilidad de equipamiento técnico en campo.",
            ],
        },
        {
            "rol": "Trayectoria Técnica Previa (Telecomunicaciones & Soporte IT)",
            "empresa": "ITETE, INANCON, Sirti Argentina, Clínica Privada Provincial",
            "periodo": "1992 – 2004",
            "ubicacion": "Buenos Aires, Argentina",
            "logros": [
                "Soporte técnico en área Sistemas (redes, bases de datos y terminales), implementación de servicios ADSL y mantenimiento de infraestructura de telecomunicaciones.",
            ],
        },
    ],
    "proyectos": [
        {
            "nombre": "Dashboard Ejecutivo en Looker Studio",
            "categoria": "Business Intelligence",
            "descripcion": "Reporte interactivo de visualización de métricas y análisis de datos construido en Google Looker Studio (Data Studio).",
            "url": "https://datastudio.google.com/reporting/a44ab54d-f0c4-4798-86a5-abb6981a8fab",
            "repo": None,
            "tags": ["Looker Studio", "BI", "Visualización de Datos"],
        },
        {
            "nombre": "Gestor de Reclamos",
            "categoria": "Desarrollo Web",
            "descripcion": "Aplicación web para registro, seguimiento y gestión de reclamos desplegada en Vercel.",
            "url": "https://gestordereclamos.vercel.app/",
            "repo": "https://github.com/Lwiggi/gestordereclamos",
            "tags": ["Web App", "Vercel", "Gestión de Tickets"],
        },
        {
            "nombre": "Portfolio / Proyecto Web Frontend",
            "categoria": "Desarrollo Web",
            "descripcion": "Sitio web responsive desarrollado y desplegado en Netlify como práctica de arquitectura frontend.",
            "url": "https://com2017lrdiaz.netlify.app/",
            "repo": None,
            "tags": ["HTML/CSS/JS", "Netlify"],
        },
    ],
    "certificaciones": [
        {"titulo": "Advanced Data - Conditional JOINs en BigQuery", "categoria": "Datos", "anio": "2026"},
        {"titulo": "Programa Completo Data Analytics (Módulos 1 a 5 + Certificación)", "categoria": "Datos", "anio": "2026"},
        {"titulo": "Advanced Analytics | Mobility Insights", "categoria": "Datos", "anio": "2026"},
        {"titulo": "Data Science vs Data Analytics", "categoria": "Datos", "anio": "2026"},
        {"titulo": "Especialización en IA: Agentes, MCP, RAG y Embeddings, Skills, Prompts y NotebookLM", "categoria": "IA", "anio": "2026"},
        {"titulo": "Imaginá, creá y escalá con MásIA", "categoria": "IA", "anio": "2026"},
        {"titulo": "Introducción a SQL para BigQuery", "categoria": "Datos", "anio": "2025"},
        {"titulo": "Data Modeler - Fundamentos de SQL", "categoria": "Datos", "anio": "2025"},
        {"titulo": "Google Data Studio (Looker Studio)", "categoria": "Datos", "anio": "2025"},
        {"titulo": "Certificación Interna - Product Backlog", "categoria": "Funcional", "anio": "2023"},
        {"titulo": "Inteligencia de Negocios con Power BI y SQL Server 2019", "categoria": "Datos", "anio": "2022"},
        {"titulo": "Codo a Codo - React", "categoria": "Dev", "anio": "2022"},
        {"titulo": "Python Full Stack (EAALV) & BA Aprende Django", "categoria": "Dev", "anio": "2022"},
        {"titulo": "Master en JavaScript, Angular 8 y NodeJS (Udemy)", "categoria": "Dev", "anio": "2019"},
        {"titulo": "Microsoft Access Básico e Intermedio / Introducción a Programación (UNTREF)", "categoria": "Datos", "anio": "2010"},
    ],
    "educacion": [
        {
            "titulo": "Bachiller en Gestión y Administración con Orientación en Comercio Exterior",
            "institucion": "Instituto Educativo Argentino",
            "periodo": "2013 – 2015",
        },
        {
            "titulo": "Técnico Mecánico (Nivel Secundario)",
            "institucion": "E.N.E.T. N° 25 'Tte. 1ro. de Artillería Fray Luis Beltrán'",
            "periodo": "1983 – 1987",
        },
    ],
}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "cv": CV_DATA})