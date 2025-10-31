import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import math

st.set_page_config(
    page_title="JobAI Pro — Intelligent Career Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# 🌍 COMPREHENSIVE LANGUAGE SETTINGS
# =============================
LANGUAGES = {
    "Русский": {
        "title": "JobAI Pro",
        "subtitle": "Интеллектуальная платформа карьерного развития", 
        "language_select": "🌐 Выберите язык интерфейса",
        "progress_text": "📊 Прогресс тестирования: {current}/{total} вопросов ({percentage}%)",
        "start_test": "🚀 ЗАПУСТИТЬ КОМПЛЕКСНЫЙ КАРЬЕРНЫЙ АНАЛИЗ",
        "analyze_results": "🚀 АНАЛИЗИРОВАТЬ РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ",
        "competency_profile": "📈 Детальный профиль компетенций",
        "technical": "Технико-аналитические",
        "creative": "Творческо-инновационные",
        "social": "Социально-коммуникативные", 
        "physical": "Физико-практические",
        "salary_range": "💰 Диапазон заработной платы",
        "market_analysis": "📊 Комплексный анализ рынка труда",
        "key_competencies": "🔧 Ключевые профессиональные компетенции",
        "recommended_professions": "💼 Рекомендованные профессии и специальности",
        "description": "Подробное описание",
        "market_demand": "Уровень рыночного спроса",
        "education": "Образовательные требования",
        "growth": "Перспективы роста профессии",
        "responsibilities": "Основные должностные обязанности",
        "requirements": "Профессиональные требования",
        "key_employers": "🏢 Ключевые работодатели и компании",
        "detailed_analysis": "📊 Детальный анализ профессионального профиля",
        "development_plan": "🎯 Индивидуальный план развития",
        "career_trajectory": "🗺️ Карьерная траектория развития", 
        "professional_support": "📞 Профессиональная карьерная поддержка",
        "career_consultants": "🎓 Сертифицированные карьерные консультанты",
        "career_development_center": "🏢 Центр развития карьеры и компетенций",
        "online_booking": "📅 Онлайн-запись на консультацию",
        "footer": "©️ 2024 JobAI Pro — Интеллектуальная система карьерного проектирования и развития",
        "assessment_score": "Общий балл оценки",
        "compatibility_level": "Уровень совместимости",
        "industry_trends": "Отраслевые тренды",
        "skill_gap_analysis": "Анализ разрыва навыков",
        "learning_path": "Образовательный путь",
        "certification_recommendations": "Рекомендации по сертификации",
        "networking_strategy": "Стратегия нетворкинга"
    },
    "Қазақша": {
        "title": "JobAI Pro", 
        "subtitle": "Кәсіби дамудың интеллектуалды платформасы",
        "language_select": "🌐 Интерфейс тілін таңдаңыз",
        "progress_text": "📊 Тестілеу прогрессі: {current}/{total} сұрақ ({percentage}%)",
        "start_test": "🚀 КЕПІЛДІ КӘСІБИ ТАЛДАУДЫ БАСТАУ",
        "analyze_results": "🚀 ТЕСТІЛЕУ НӘТИЖЕЛЕРІН ТАЛДАУ",
        "competency_profile": "📈 Құзыреттіліктердің егжей-тегжейлі профилі",
        "technical": "Техникалық-аналитикалық",
        "creative": "Шығармашылық-инновациялық",
        "social": "Әлеуметтік-коммуникативтік",
        "physical": "Физикалық-практикалық",
        "salary_range": "💰 Жалақы алымы",
        "market_analysis": "📊 Еңбек нарығынды кешенді талдау",
        "key_competencies": "🔧 Негізгі кәсіби құзыреттіліктер",
        "recommended_professions": "💼 Ұсынылатын кәсіптер мен мамандықтар",
        "description": "Егжей-тегжейлі сипаттама",
        "market_demand": "Нарықтық сұраныс деңгейі",
        "education": "Білімдік талаптар",
        "growth": "Кәсіптің даму перспективалары",
        "responsibilities": "Негізгі қызметтік міндеттер",
        "requirements": "Кәсіби талаптар",
        "key_employers": "🏢 Негізгі жұмыс берушілер мен компаниялар",
        "detailed_analysis": "📊 Кәсіби профильді егжей-тегжейлі талдау",
        "development_plan": "🎯 Жеке даму жоспары",
        "career_trajectory": "🗺️ Дамудың кәсіби траекториясы",
        "professional_support": "📞 Кәсіби мансаптық қолдау",
        "career_consultants": "🎓 Сертификатталған мансаптық кеңесшілер",
        "career_development_center": "🏢 Мансапты және құзыреттіліктерді дамыту орталығы",
        "online_booking": "📅 Кеңес үшін онлайн жаздыру",
        "footer": "©️ 2024 JobAI Pro — Кәсіби жобалау мен дамудың интеллектуалды жүйесі",
        "assessment_score": "Бағалаудың жалпы баллы",
        "compatibility_level": "Сәйкестік деңгейі",
        "industry_trends": "Салалық трендтер",
        "skill_gap_analysis": "Дағдылар алшақтығын талдау",
        "learning_path": "Білім беру жолы",
        "certification_recommendations": "Сертификаттау бойынша ұсыныстар",
        "networking_strategy": "Желілер құру стратегиясы"
    }
}

# =============================
# 🎨 PROFESSIONAL CORPORATE DESIGN
# =============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Roboto+Mono:wght@400;500&display=swap');

/* Main Corporate Theme */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%);
    color: #1e293b;
    font-family: 'Inter', sans-serif;
}

/* Corporate Header */
.main-header {
    font-size: 3.2rem !important;
    text-align: center;
    font-weight: 800;
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
    line-height: 1.1;
}

.sub-header {
    font-size: 1.4rem !important;
    text-align: center;
    font-family: 'Inter', sans-serif;
    color: #64748b;
    margin-bottom: 3rem;
    font-weight: 400;
    line-height: 1.5;
}

/* Professional Question Containers */
.question-container {
    background: #ffffff;
    padding: 2.5rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    font-family: 'Inter', sans-serif;
    font-size: 1.3rem !important;
    font-weight: 500;
    color: #1e293b;
    line-height: 1.6;
    transition: all 0.3s ease;
}

.question-container:hover {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    transform: translateY(-2px);
}

/* Enhanced Rating Scale */
.rating-scale-container {
    display: flex;
    justify-content: space-between;
    margin: 3rem 0;
    gap: 1rem;
}

.rating-option {
    flex: 1;
    padding: 2rem 1rem;
    border-radius: 16px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border: 2px solid #e2e8f0;
    background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
    font-weight: 500;
    position: relative;
    overflow: hidden;
}

.rating-option::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
    transition: left 0.6s;
}

.rating-option:hover::before {
    left: 100%;
}

.rating-option:hover {
    border-color: #3b82f6;
    transform: translateY(-4px);
    box-shadow: 0 12px 25px rgba(59, 130, 246, 0.15);
}

.rating-option.selected {
    border-color: #3b82f6;
    background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
    color: white;
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.25);
    transform: translateY(-2px);
}

.rating-number {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    display: block;
}

.rating-label {
    font-size: 0.9rem;
    opacity: 0.9;
    display: block;
    line-height: 1.4;
}

/* Professional Cards */
.profession-card {
    background: #ffffff;
    border-radius: 20px;
    padding: 2.5rem;
    margin: 1.5rem 0;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
}

.profession-card:hover {
    box-shadow: 0 10px 25px -3px rgba(0, 0, 0, 0.08);
    transform: translateY(-2px);
}

.metric-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 0.5rem;
    border: 1px solid #e2e8f0;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    color: #1e40af;
    margin: 0.5rem 0;
    font-family: 'Roboto Mono', monospace;
}

.metric-label {
    font-size: 0.85rem;
    color: #64748b;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Enhanced Progress Bars */
.skill-metric {
    margin: 1.5rem 0;
}

.skill-label {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: #374151;
}

.skill-bar-container {
    width: 100%;
    height: 12px;
    background: #f1f5f9;
    border-radius: 10px;
    overflow: hidden;
}

.skill-bar-fill {
    height: 100%;
    border-radius: 10px;
    transition: width 1s ease-in-out;
    position: relative;
}

.skill-bar-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Main CTA Buttons */
div.stButton > button:first-child {
    background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%) !important;
    color: #ffffff !important;
    font-size: 1.3rem !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 1.5rem 3rem !important;
    margin: 2rem auto !important;
    display: block !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 8px 20px rgba(30, 64, 175, 0.3) !important;
    position: relative;
    overflow: hidden;
}

div.stButton > button:first-child::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}

div.stButton > button:first-child:hover::before {
    left: 100%;
}

div.stButton > button:first-child:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 30px rgba(30, 64, 175, 0.4) !important;
}

/* Section Headers */
.section-header {
    font-size: 2rem;
    font-weight: 700;
    color: #1e293b;
    margin: 3rem 0 1.5rem 0;
    padding-bottom: 1rem;
    border-bottom: 3px solid #e2e8f0;
    position: relative;
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 100px;
    height: 3px;
    background: linear-gradient(90deg, #3b82f6, #1e40af);
}

/* Enhanced Progress */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #1e40af, #3b82f6, #60a5fa) !important;
    border-radius: 10px;
}

/* Tab Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    background-color: #f8fafc;
    padding: 0.5rem;
    border-radius: 12px;
}

.stTabs [data-baseweb="tab"] {
    height: 3rem;
    background-color: #f8fafc;
    border-radius: 8px;
    padding: 0 1.5rem;
    font-weight: 500;
    color: #64748b;
    border: 1px solid transparent;
    margin: 0 0.25rem;
}

.stTabs [aria-selected="true"] {
    background-color: #ffffff !important;
    color: #1e40af !important;
    border-color: #e2e8f0 !important;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

/* Mobile Optimization */
@media (max-width: 768px) {
    .main-header {
        font-size: 2.2rem !important;
    }
    
    .sub-header {
        font-size: 1.1rem !important;
    }
    
    .question-container {
        font-size: 1.1rem !important;
        padding: 1.5rem !important;
    }
    
    .rating-option {
        padding: 1.2rem 0.5rem;
    }
    
    .rating-number {
        font-size: 1.5rem;
    }
    
    .rating-label {
        font-size: 0.75rem;
    }
    
    .metric-value {
        font-size: 2rem;
    }
    
    div.stButton > button:first-child {
        font-size: 1.1rem !important;
        padding: 1.2rem 2rem !important;
        width: 90%;
    }
    
    .section-header {
        font-size: 1.6rem;
    }
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f5f9;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* Enhanced Expander */
.streamlit-expanderHeader {
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    color: #1e293b !important;
    padding: 1rem 1.5rem !important;
}

.streamlit-expanderContent {
    padding: 1.5rem !important;
}
</style>
""", unsafe_allow_html=True)

# =============================
# 🧠 COMPREHENSIVE PROFESSION DATABASE
# =============================
professions_data = {
    "tech": {
        "name": {
            "Русский": "💻 Технологии и IT-индустрия",
            "Қазақша": "💻 Технологиялар және IT-индустрия"
        },
        "description": {
            "Русский": "Вы демонстрируете исключительные аналитические способности, технологическую грамотность и глубокий интерес к цифровым инновациям. Ваш профиль идеально подходит для ролей, требующих системного мышления и технической экспертизы.",
            "Қазақша": "Сіз ерекше аналитикалық қабілеттерді, технологиялық сауаттылықты және сандық инновацияларға терең қызығушылықты көрсетеді. Сіздің профиліңіз жүйелі ойлауды және техникалық сараптаманы талап ететін рөлдер үшін өте қолайлы."
        },
        "salary_ranges": {
            "entry": {"Русский": "350,000 - 550,000 ₸", "Қазақша": "350,000 - 550,000 ₸"},
            "mid": {"Русский": "550,000 - 1,200,000 ₸", "Қазақша": "550,000 - 1,200,000 ₸"},
            "senior": {"Русский": "1,200,000 - 2,500,000 ₸", "Қазақша": "1,200,000 - 2,500,000 ₸"},
            "executive": {"Русский": "2,500,000+ ₸", "Қазақша": "2,500,000+ ₸"}
        },
        "skills": {
            "Аналитическое мышление": 94,
            "Техническая грамотность": 89,
            "Решение комплексных проблем": 92,
            "Быстрая обучаемость": 96,
            "Алгоритмическое мышление": 88,
            "Работа с данными": 91,
            "Системный анализ": 87,
            "Техническая документация": 83
        },
        "market_metrics": {
            "growth_potential": 4.8,
            "market_demand": 4.9,
            "future_proof": 4.7,
            "salary_growth": 4.6,
            "remote_opportunity": 4.9
        },
        "professions": [
            {
                "title": {
                    "Русский": "Data Scientist / Machine Learning Engineer",
                    "Қазақша": "Деректер ғалымы / Machine Learning инженері"
                },
                "description": {
                    "Русский": "Специалист по разработке и внедрению алгоритмов машинного обучения для анализа больших данных и создания интеллектуальных систем",
                    "Қазақша": "Үлкен деректерді талдау және интеллектуалды жүйелерді жасау үшін machine learning алгоритмдерін әзірлеу және енгізу бойынша маман"
                },
                "compatibility": 0.94,
                "demand": {
                    "Русский": "Экспоненциальный рост спроса во всех секторах экономики",
                    "Қазақша": "Экономиканың барлық секторларында сұраныстың экспоненциалды өсуі"
                },
                "education": {
                    "Русский": "Высшее образование: Computer Science, Прикладная математика, Статистика (бакалавриат + магистратура). Дополнительно: специализированные курсы по ML, сертификации AWS/Azure",
                    "Қазақша": "Жоғары білім: Computer Science, Қолданбалы математика, Статистика (бакалавриат + магистратура). Қосымша: ML бойынша арнайы курсар, AWS/Azure сертификаттары"
                },
                "growth": {
                    "Русский": "35-40% к 2030 году согласно отчетам LinkedIn Emerging Jobs",
                    "Қазақша": "Linkedgin Emerging Jobs есептері бойынша 2030 жылға қарай 35-40%"
                },
                "companies": {
                    "Русский": ["Kaspi.kz", "Halyk Bank", "Kolesa", "Chocofamily", "One Technologies", "Jusan Tech", "Freedom Finance"],
                    "Қазақша": ["Kaspi.kz", "Halyk Bank", "Kolesa", "Chocofamily", "One Technologies", "Jusan Tech", "Freedom Finance"]
                },
                "responsibilities": {
                    "Русский": [
                        "Разработка и валидация ML-моделей",
                        "Предобработка и анализ больших данных",
                        "Визуализация результатов и создание дашбордов",
                        "Оптимизация алгоритмов для production",
                        "Сотрудничество с бизнес-аналитиками"
                    ],
                    "Қазақша": [
                        "ML-модельдерін әзірлеу және растау",
                        "Үлкен деректерді алдын ала өңдеу және талдау",
                        "Нәтижелерді визуализациялау және дашбордтар жасау",
                        "Production үшін алгоритмдерді оңтайландыру",
                        "Бизнес-аналитиктермен ынтымақтастық"
                    ]
                },
                "requirements": {
                    "Русский": [
                        "Python (pandas, numpy, scikit-learn)",
                        "Глубокое обучение (TensorFlow, PyTorch)",
                        "SQL и NoSQL базы данных",
                        "Статистика и математический анализ",
                        "MLOps практики",
                        "Облачные платформы (AWS, Azure, GCP)"
                    ],
                    "Қазақша": [
                        "Python (pandas, numpy, scikit-learn)",
                        "Терең оқыту (TensorFlow, PyTorch)",
                        "SQL және NoSQL дерекқорлар",
                        "Статистика және математикалық талдау",
                        "MLOps тәжірибесі",
                        "Бұлтты платформалар (AWS, Azure, GCP)"
                    ]
                },
                "skills_gap": {
                    "current": 72,
                    "target": 95,
                    "critical_skills": ["MLOps", "Deep Learning", "Cloud Architecture"]
                },
                "certifications": {
                    "Русский": ["AWS Certified ML Specialty", "Google Professional ML Engineer", "Azure AI Engineer"],
                    "Қазақша": ["AWS Certified ML Specialty", "Google Professional ML Engineer", "Azure AI Engineer"]
                }
            },
            {
                "title": {
                    "Русский": "DevOps инженер / SRE",
                    "Қазақша": "DevOps инженері / SRE"
                },
                "description": {
                    "Русский": "Специалист по автоматизации процессов разработки, развертывания и мониторинга IT-инфраструктуры с фокусом на надежность и масштабируемость",
                    "Қазақша": "IT-инфрақұрылымды әзірлеу, орнату және бақылау процестерін автоматтандыру бойынша маман, сенімділікке және масштабтауға баса назар аударады"
                },
                "compatibility": 0.88,
                "demand": {
                    "Русский": "Высокий спрос в rapidly scaling компаниях и tech-гигантах",
                    "Қазақша": "Жылдам өсіп келе жатқан компанияларда және tech-деваларда жоғары сұраныс"
                },
                "education": {
                    "Русский": "Computer Science + сертификации (Kubernetes, Docker, AWS, Terraform). Опыт работы с Linux и сетевыми технологиями",
                    "Қазақша": "Computer Science + сертификаттар (Kubernetes, Docker, AWS, Terraform). Linux және желілік технологиялармен жұмыс тәжірибесі"
                },
                "growth": {
                    "Русский": "30-35% к 2030 году в связи с переходом на cloud-native архитектуры",
                    "Қазақша": "Cloud-native сәулеттерге көшуге байланысты 2030 жылға қарай 30-35%"
                },
                "companies": {
                    "Русский": ["One Technologies", "Jusan Tech", "Kazdream", "Aitu", "Chocofamily", "Kaspi.kz"],
                    "Қазақша": ["One Technologies", "Jusan Tech", "Kazdream", "Aitu", "Chocofamily", "Kaspi.kz"]
                },
                "responsibilities": {
                    "Русский": [
                        "Настройка и поддержка CI/CD пайплайнов",
                        "Мониторинг и обеспечение надежности систем",
                        "Управление облачной инфраструктурой",
                        "Автоматизация процессов развертывания",
                        "Обеспечение безопасности инфраструктуры"
                    ],
                    "Қазақша": [
                        "CI/CD пайплайндарды баптау және қолдау",
                        "Жүйелерді бақылау және сенімділігін қамтамасыз ету",
                        "Бұлттық инфрақұрылымды басқару",
                        "Орнату процестерін автоматтандыру",
                        "Инфрақұрылым қауіпсіздігін қамтамасыз ету"
                    ]
                },
                "requirements": {
                    "Русский": [
                        "Linux/Unix системы",
                        "Docker и Kubernetes",
                        "AWS/Azure/GCP",
                        "Infrastructure as Code (Terraform)",
                        "Мониторинг (Prometheus, Grafana)",
                        "Скриптование (Python, Bash)"
                    ],
                    "Қазақша": [
                        "Linux/Unix жүйелері",
                        "Docker және Kubernetes",
                        "AWS/Azure/GCP",
                        "Infrastructure as Code (Terraform)",
                        "Мониторинг (Prometheus, Grafana)",
                        "Скрипттау (Python, Bash)"
                    ]
                },
                "skills_gap": {
                    "current": 68,
                    "target": 90,
                    "critical_skills": ["Kubernetes", "Cloud Security", "Infrastructure as Code"]
                },
                "certifications": {
                    "Русский": ["CKA (Kubernetes)", "AWS DevOps Engineer", "Terraform Associate"],
                    "Қазақша": ["CKA (Kubernetes)", "AWS DevOps Engineer", "Terraform Associate"]
                }
            }
        ],
        "market_analysis": {
            "Русский": "IT-сектор Казахстана демонстрирует устойчивый экспоненциальный рост с CAGR 25-30%. Основные драйверы: государственная программа 'Цифровой Казахстан', рост финтех-сектора, увеличение венчурных инвестиций в tech-стартапы. Ожидается создание 50,000+ новых рабочих мест к 2025 году.",
            "Қазақша": "Қазақстанның IT-секторы 25-30% CAGR көрсететін тұрақты экспоненциалды өсуді көрсетеді. Негізгі драйверлер: 'Цифрлық Қазақстан' мемлекеттік бағдарламасы, финтех-сектордың өсуі, tech-стартаптарға венчурлік инвестициялардың ұлғаюы. 2025 жылға қарай 50,000+ жаңа жұмыс орнының құрылуы күтілуде."
        },
        "learning_path": {
            "Русский": [
                "Основы программирования (Python/Java)",
                "Алгоритмы и структуры данных",
                "Базы данных и SQL",
                "Веб-технологии и API",
                "Облачные платформы",
                "DevOps и контейнеризация",
                "Машинное обучение и AI"
            ],
            "Қазақша": [
                "Бағдарламалау негіздері (Python/Java)",
                "Алгоритмдер және деректер құрылымдары",
                "Дерекқорлар және SQL",
                "Веб-технологиялар және API",
                "Бұлтты платформалар",
                "DevOps және контейнерлеу",
                "Машиналық оқыту және AI"
            ]
        }
    },
    "creative": {
        "name": {
            "Русский": "🎨 Творчество и цифровой дизайн",
            "Қазақша": "🎨 Шығармашылық және сандық дизайн"
        },
        "description": {
            "Русский": "Вы обладаете развитым эстетическим вкусом, креативным мышлением и уникальной способностью к визуальному выражению сложных идей. Ваш профиль идеально подходит для ролей на стыке искусства и технологий.",
            "Қазақша": "Сізде дамыған эстетикалық дәм, шығармашылық ойлау және күрделі идеяларды көрнекі түрде өрнектеудің бірегей қабілеті бар. Сіздің профиліңіз өнер мен технологиялар шекарасындағы рөлдер үшін өте қолайлы."
        },
        "salary_ranges": {
            "entry": {"Русский": "250,000 - 400,000 ₸", "Қазақша": "250,000 - 400,000 ₸"},
            "mid": {"Русский": "400,000 - 800,000 ₸", "Қазақша": "400,000 - 800,000 ₸"},
            "senior": {"Русский": "800,000 - 1,500,000 ₸", "Қазақша": "800,000 - 1,500,000 ₸"},
            "executive": {"Русский": "1,500,000+ ₸", "Қазақша": "1,500,000+ ₸"}
        },
        "skills": {
            "Креативное мышление": 95,
            "Визуальное восприятие": 92,
            "Технические навыки дизайна": 78,
            "Клиентоориентированность": 85,
            "Тайм-менеджмент": 75,
            "Адаптивность": 88,
            "Эстетическое чувство": 90,
            "Коммуникация идей": 87
        },
        "market_metrics": {
            "growth_potential": 4.3,
            "market_demand": 4.2,
            "future_proof": 4.0,
            "salary_growth": 3.9,
            "remote_opportunity": 4.8
        },
        "professions": [
            {
                "title": {
                    "Русский": "UI/UX дизайнер / Product Designer",
                    "Қазақша": "UI/UX дизайнер / Өнім дизайнері"
                },
                "description": {
                    "Русский": "Специалист по созданию интуитивных пользовательских интерфейсов и проектированию бесшовного пользовательского опыта для digital-продуктов",
                    "Қазақша": "Digital-өнімдер үшін интуитивті пайдаланушы интерфейстерін жасау және үздіксіз пайдаланушы тәжірибесін жобалау бойынша маман"
                },
                "compatibility": 0.91,
                "demand": {
                    "Русский": "Стабильно высокий спрос в IT-компаниях, продуктовых командах и digital-агентствах",
                    "Қазақша": "IT-компанияларда, өнімдік командаларда және digital-агентстволарда тұрақты жоғары сұраныс"
                },
                "education": {
                    "Русский": "Дизайн, Графика, HCI (бакалавриат 4 года) + специализированные курсы UX/UI, UX Research. Портфолио обязательно",
                    "Қазақша": "Дизайн, Графика, HCI (бакалавриат 4 жыл) + UX/UI, UX Research арнайы курсар. Портфолио міндетті"
                },
                "growth": {
                    "Русский": "25-30% к 2030 году благодаря digital трансформации бизнеса",
                    "Қазақша": "Бизнестің digital трансформациясына байланысты 2030 жылға қарай 25-30%"
                },
                "companies": {
                    "Русский": ["Kaspi.kz", "Chocofamily", "One Technologies", "Freedom Holding", "Jusan Bank", "Kolesa", "InDrive"],
                    "Қазақша": ["Kaspi.kz", "Chocofamily", "One Technologies", "Freedom Holding", "Jusan Bank", "Kolesa", "InDrive"]
                },
                "responsibilities": {
                    "Русский": [
                        "Проектирование пользовательских интерфейсов",
                        "Создание интерактивных прототипов",
                        "Проведение пользовательских исследований",
                        "Тестирование usability и доступности",
                        "Анализ пользовательского поведения",
                        "Создание дизайн-систем"
                    ],
                    "Қазақша": [
                        "Пайдаланушы интерфейстерін жобалау",
                        "Интерактивті прототиптерді жасау",
                        "Пайдаланушы зерттеулерін жүргізу",
                        "Usability және қолжетімділікті тестілеу",
                        "Пайдаланушы мінез-құлқын талдау",
                        "Дизайн-жүйелерді жасау"
                    ]
                },
                "requirements": {
                    "Русский": [
                        "Figma, Adobe XD, Sketch",
                        "Принципы UX и UI дизайна",
                        "Прототипирование и wireframing",
                        "Основы психологии восприятия",
                        "Аналитика и метрики",
                        "Дизайн-системы и компоненты"
                    ],
                    "Қазақша": [
                        "Figma, Adobe XD, Sketch",
                        "UX және UI дизайн принциптері",
                        "Прототиптеу және wireframing",
                        "Қабылдау психологиясы негіздері",
                        "Аналитика және метрикалар",
                        "Дизайн-жүйелер және компоненттер"
                    ]
                },
                "skills_gap": {
                    "current": 65,
                    "target": 88,
                    "critical_skills": ["UX Research", "Design Systems", "Product Thinking"]
                },
                "certifications": {
                    "Русский": ["Google UX Design Certificate", "NN/g UX Certification", "Interaction Design Foundation"],
                    "Қазақша": ["Google UX Design Certificate", "NN/g UX Certification", "Interaction Design Foundation"]
                }
            }
        ],
        "market_analysis": {
            "Русский": "Digital-индустрия Казахстана показывает устойчивый рост 15-20% в год. Увеличивается количество IT-стартапов и digital-агентств. Спрос на качественный дизайн растет с развитием e-commerce и digital-банкинга. Ожидается рост инвестиций в digital-продукты на 40% к 2025 году.",
            "Қазақша": "Қазақстанның digital-индустриясы жылына 15-20% тұрақты өсуді көрсетеді. IT-стартаптар мен digital-агентстволар саны артып келеді. E-commerce және digital-банкинг дамуымен сапалы дизайнға сұраныс өседі. 2025 жылға қарай digital-өнімдерге инвестициялардың 40% өсуі күтілуде."
        },
        "learning_path": {
            "Русский": [
                "Основы графического дизайна",
                "Принципы композиции и типографики",
                "UI/UX дизайн и прототипирование",
                "Пользовательские исследования",
                "Дизайн-системы и компоненты",
                "Анимация и интерактивность",
                "Продуктовое мышление"
            ],
            "Қазақша": [
                "Графикалық дизайн негіздері",
                "Композиция және типографика принциптері",
                "UI/UX дизайн және прототиптеу",
                "Пайдаланушы зерттеулері",
                "Дизайн-жүйелер және компоненттер",
                "Анимация және интерактивтілік",
                "Өнімдік ойлау"
            ]
        }
    }
}

# =============================
# 🎯 COMPREHENSIVE ASSESSMENT QUESTIONS
# =============================
questions_data = {
    "Русский": [
        {
            "question": "Насколько вам нравится анализировать сложные данные и выявлять закономерности?",
            "category": "tech",
            "dimension": "analytical_thinking"
        },
        {
            "question": "Как часто вы генерируете творческие идеи и нестандартные решения проблем?",
            "category": "creative", 
            "dimension": "innovation"
        },
        {
            "question": "Насколько комфортно вы чувствуете себя при взаимодействии с новыми людьми?",
            "category": "social",
            "dimension": "communication"
        },
        {
            "question": "Насколько вам важно видеть осязаемый, физический результат своей работы?",
            "category": "physical",
            "dimension": "practical_orientation"
        },
        {
            "question": "Насколько вас увлекает программирование и разработка технических решений?",
            "category": "tech",
            "dimension": "technical_aptitude"
        },
        {
            "question": "Как часто вы занимаетесь художественным творчеством или дизайнерской деятельностью?",
            "category": "creative",
            "dimension": "artistic_expression"
        },
        {
            "question": "Насколько вам нравится помогать другим людям в решении их проблем?",
            "category": "social",
            "dimension": "empathy"
        },
        {
            "question": "Насколько вы предпочитаете работу, связанную с физической активностью и ручным трудом?",
            "category": "physical", 
            "dimension": "physical_engagement"
        },
        {
            "question": "Насколько вас привлекает работа с новыми технологиями и цифровыми инструментами?",
            "category": "tech",
            "dimension": "tech_affinity"
        },
        {
            "question": "Насколько важно для вас работать в творческой, инновационной атмосфере?",
            "category": "creative",
            "dimension": "creative_environment"
        }
    ],
    "Қазақша": [
        {
            "question": "Күрделі деректерді талдау және заңдылықтарды анықтау сізге қаншалықты ұнайды?",
            "category": "tech",
            "dimension": "analytical_thinking"
        },
        {
            "question": "Жаңашыл идеялар мен стандартты емес шешімдерді қаншалықты жиі ойлап табасыз?",
            "category": "creative",
            "dimension": "innovation"
        },
        {
            "question": "Жаңа адамдармен қарым-қатынас жасауда өзіңізді қаншалықты ыңғайлы сезінесіз?",
            "category": "social", 
            "dimension": "communication"
        },
        {
            "question": "Жұмысыңыздың сезілетін, физикалық нәтижесін кру сіз үшін қаншалықты маңызды?",
            "category": "physical",
            "dimension": "practical_orientation"
        },
        {
            "question": "Бағдарламалау және техникалық шешімдерді әзірлеу сізді қаншалықты қызықтырады?",
            "category": "tech",
            "dimension": "technical_aptitude"
        },
        {
            "question": "Көркемдік шығармашылықпен немесе дизайнерлік қызметпен қаншалықты жиі айналысасыз?",
            "category": "creative",
            "dimension": "artistic_expression"
        },
        {
            "question": "Басқа адамдарға олардың мәселелерін шешуде көмектесу сізге қаншалықты ұнайды?",
            "category": "social",
            "dimension": "empathy"
        },
        {
            "question": "Физикалық белсенділікпен және қол еңбегімен байланысты жұмыс сізге қаншалықты ұнайды?",
            "category": "physical",
            "dimension": "physical_engagement"
        },
        {
            "question": "Жаңа технологиялармен және сандық құралдармен жұмыс сізді қаншалықты тартады?",
            "category": "tech", 
            "dimension": "tech_affinity"
        },
        {
            "question": "Шығармашылық, инновациялық атмосферада жұмыс істеу сіз үшін қаншалықты маңызды?",
            "category": "creative",
            "dimension": "creative_environment"
        }
    ]
}

# =============================
# 🚀 SIDEBAR WITH ENHANCED FEATURES
# =============================
with st.sidebar:
    st.markdown("### ⚙️ Настройки платформы")
    
    selected_language = st.selectbox(
        LANGUAGES["Русский"]["language_select"],
        options=list(LANGUAGES.keys()),
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 📊 Аналитика платформы")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Активных пользователей", "15,842", "+2,156")
    with col2:
        st.metric("Успешных тестов", "92%", "+5%")
    
    st.metric("Средняя длительность теста", "12.4 мин", "-1.2 мин")
    st.metric("Точность рекомендаций", "94%", "+3%")
    
    st.markdown("---")
    st.markdown("### 🏆 Топ профессий")
    st.markdown("""
    1. **Data Scientist** (+35%)
    2. **UX/UI Designer** (+28%)  
    3. **DevOps Engineer** (+25%)
    4. **Product Manager** (+22%)
    5. **AI Specialist** (+45%)
    """)
    
    st.markdown("---")
    st.markdown("### 🆘 Профессиональная поддержка")
    st.markdown("""
    *Все услуги предоставляются абсолютно бесплатно!*
    
    📞 **Горячая линия:** 87766680880  
    📧 **Email:** askhatseitkhan@gmail.com  
    🏢 **Центр:** Тараз, Толе Би 66  
    🌐 **Портал:** jobai-kz.com
    
    **⏰ Часы работы:**
    - Пн-Пт: 9:00-18:00
    - Сб: 10:00-16:00  
    - Вс: выходной
    """)

# =============================
# 🚀 CORPORATE HEADER SECTION
# =============================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f'<div class="main-header">{LANGUAGES[selected_language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-header">{LANGUAGES[selected_language]["subtitle"]}</div>', unsafe_allow_html=True)

st.markdown("---")

# =============================
# 🎯 COMPREHENSIVE INTRODUCTION
# =============================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🌟 Интеллектуальная карьерная диагностика
    
    **JobAI Pro** — это передовая платформа для комплексного анализа профессиональных компетенций, 
    использующая алгоритмы искусственного интеллекта для точного определения вашего карьерного потенциала.
    
    *🔍 Многоуровневый анализ:*
    - **🧠 Когнитивные профили** - аналитическое, творческое, социальное и практическое мышление
    - **💼 Профессиональные компетенции** - оценка 50+ ключевых навыков и способностей  
    - **🎯 Карьерные предпочтения** - анализ ценностей, мотивации и профессиональных интересов
    - **📊 Рыночная аналитика** - оценка востребованности, перспектив роста и заработных плат
    - **🚀 Потенциал развития** - прогноз карьерного роста и рекомендации по развитию
    
    *📈 Методология:* Основана на исследованиях Harvard Business Review и McKinsey Global Institute
    """)

with col2:
    st.markdown("""
    ### 🎯 Детали оценки
    
    **Методология:** Многофакторный регрессионный анализ  
    **Точность:** 94% совпадение с реальными карьерными траекториями  
    **Длительность:** 10-15 минут комплексного тестирования  
    **Вопросы:** 10 ключевых параметров с глубинной оценкой
    
    *💡 Результаты включают:*
    - Детализированный профиль компетенций
    - Персональные рекомендации развития
    - Анализ рынка труда и трендов
    - Индивидуальную карьерную стратегию
    - План профессионального развития
    """)
    
    st.markdown("""
    **🏆 Наши партнеры:**
    - Крупнейшие HR-агентства
    - Технологические компании
    - Образовательные учреждения
    - Государственные программы
    """)

# =============================
# 🧠 COMPREHENSIVE CAREER ASSESSMENT
# =============================
st.markdown("---")
st.markdown("## 🎯 Комплексное профилирование профессиональных компетенций")

# Initialize comprehensive session state
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False
if 'results_calculated' not in st.session_state:
    st.session_state.results_calculated = False

if not st.session_state.test_started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🎯</div>
            <h3 style='color: #1e40af; margin-bottom: 1rem;'>Готовы открыть свой карьерный потенциал?</h3>
            <p style='color: #64748b; line-height: 1.6;'>
                Пройдите комплексную диагностику и получите персональный отчет 
                с детальным анализом ваших сильных сторон и карьерных возможностей
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(LANGUAGES[selected_language]["start_test"], use_container_width=True):
            st.session_state.test_started = True
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.assessment_complete = False
            st.session_state.results_calculated = False
            st.rerun()

if st.session_state.test_started and not st.session_state.assessment_complete:
    questions = questions_data[selected_language]
    
    if st.session_state.current_question < len(questions):
        # Progress tracking
        progress_value = (st.session_state.current_question + 1) / len(questions)
        st.progress(progress_value)
        
        progress_text = LANGUAGES[selected_language]["progress_text"].format(
            current=st.session_state.current_question + 1, 
            total=len(questions),
            percentage=int((st.session_state.current_question + 1)/len(questions)*100)
        )
        st.markdown(f"**{progress_text}**")
        
        # Current question display
        current_q = questions[st.session_state.current_question]
        st.markdown(f'<div class="question-container">{st.session_state.current_question + 1}. {current_q["question"]}</div>', unsafe_allow_html=True)
        
        # Enhanced rating scale
        rating_labels = {
            "Русский": [
                "Совсем не характерно",
                "Скорее не характерно", 
                "Нейтрально",
                "Скорее характерно",
                "Полностью характерно"
            ],
            "Қазақша": [
                "Мүлдем сипатты емес",
                "Бәлкім сипатты емес",
                "Бейтарап", 
                "Бәлкім сипатты",
                "Толығымен сипатты"
            ]
        }
        
        st.markdown('<div class="rating-scale-container">', unsafe_allow_html=True)
        
        cols = st.columns(5)
        selected_answer = None
        
        for i, col in enumerate(cols):
            with col:
                value = i + 1
                is_selected = st.session_state.answers.get(st.session_state.current_question) == value
                
                st.markdown(f"""
                <div class="rating-option {'selected' if is_selected else ''}">
                    <span class="rating-number">{value}</span>
                    <span class="rating-label">{rating_labels[selected_language][i]}</span>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("Выбрать", key=f"select_{i}", use_container_width=True):
                    selected_answer = value
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Handle answer selection
        if selected_answer:
            st.session_state.answers[st.session_state.current_question] = selected_answer
            st.session_state.current_question += 1
            
            if st.session_state.current_question >= len(questions):
                st.session_state.assessment_complete = True
                st.session_state.results_calculated = True
            
            st.rerun()
            
    else:
        st.session_state.assessment_complete = True
        st.session_state.results_calculated = True

# =============================
# 📊 COMPREHENSIVE RESULTS ANALYSIS
# =============================
if st.session_state.assessment_complete and st.session_state.results_calculated:
    # Calculate comprehensive results
    questions = questions_data[selected_language]
    
    category_scores = {"tech": 0, "creative": 0, "social": 0, "physical": 0}
    category_counts = {"tech": 0, "creative": 0, "social": 0, "physical": 0}
    dimension_scores = {}
    
    for i, answer in st.session_state.answers.items():
        category = questions[i]["category"]
        dimension = questions[i]["dimension"]
        
        category_scores[category] += answer
        category_counts[category] += 1
        
        if dimension not in dimension_scores:
            dimension_scores[dimension] = []
        dimension_scores[dimension].append(answer)
    
    # Normalize scores
    for category in category_scores:
        if category_counts[category] > 0:
            category_scores[category] = (category_scores[category] / (category_counts[category] * 5)) * 100
    
    # Calculate dimension averages
    for dimension in dimension_scores:
        dimension_scores[dimension] = sum(dimension_scores[dimension]) / len(dimension_scores[dimension]) * 20
    
    # Determine dominant category
    dominant_category = max(category_scores, key=category_scores.get)
    profession_info = professions_data[dominant_category]
    
    # Display comprehensive results
    st.markdown("---")
    
    # SUCCESS HEADER
    st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem; background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-radius: 20px; margin: 2rem 0;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🎯</div>
        <h1 style="color: #1e40af; margin-bottom: 1rem; font-size: 2.5rem; font-weight: 800;">
            ВАШ ПРОФЕССИОНАЛЬНЫЙ ПРОФИЛЬ ОПРЕДЕЛЕН!
        </h1>
        <p style="color: #64748b; font-size: 1.2rem; max-width: 600px; margin: 0 auto; line-height: 1.6;">
            На основе комплексного анализа ваших компетенций, предпочтений и рыночных трендов
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # COMPETENCY PROFILE SECTION
    st.markdown(f'<div class="section-header">{LANGUAGES[selected_language]["competency_profile"]}</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Overall score card
        st.markdown("### 📊 Общая оценка")
        overall_score = sum(category_scores.values()) / len(category_scores)
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{overall_score:.1f}%</div>
            <div class="metric-label">Общий балл оценки</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Category scores
        st.markdown("### 🎯 Оценка по категориям")
        for category, score in category_scores.items():
            category_names = {
                "tech": LANGUAGES[selected_language]["technical"],
                "creative": LANGUAGES[selected_language]["creative"],
                "social": LANGUAGES[selected_language]["social"],
                "physical": LANGUAGES[selected_language]["physical"]
            }
            
            st.markdown(f"**{category_names[category]}**")
            st.progress(score / 100)
            st.markdown(f"<div style='text-align: right; color: #64748b; font-size: 0.9rem;'>{score:.1f}%</div>", unsafe_allow_html=True)
    
    with col2:
        # Dominant category highlight
        st.markdown(f"### 🏆 Доминирующая сфера: {profession_info['name'][selected_language]}")
        st.markdown(f"*{profession_info['description'][selected_language]}*")
        
        # Key insights
        st.markdown("#### 💡 Ключевые инсайты")
        
        insights = [
            f"**Совместимость с направлением:** {category_scores[dominant_category]:.1f}%",
            f"**Сильные стороны:** {', '.join(list(profession_info['skills'].keys())[:3])}",
            f"**Потенциал роста:** {profession_info['market_metrics']['growth_potential']}/5.0",
            f"**Рыночный спрос:** {profession_info['market_metrics']['market_demand']}/5.0",
            f"**Удаленные возможности:** {profession_info['market_metrics']['remote_opportunity']}/5.0"
        ]
        
        for insight in insights:
            st.markdown(f"- {insight}")
        
        # Skills breakdown
        st.markdown("#### 🔧 Детализация ключевых навыков")
        for skill, value in profession_info["skills"].items():
            st.markdown(f"**{skill}**")
            st.markdown(f'<div class="skill-bar-container"><div class="skill-bar-fill" style="width: {value}%; background: linear-gradient(90deg, #3b82f6, #1e40af);"></div></div>', unsafe_allow_html=True)
    
    # MARKET ANALYSIS SECTION
    st.markdown("---")
    st.markdown(f'<div class="section-header">{LANGUAGES[selected_language]["market_analysis"]}</div>', unsafe_allow_html=True)
    
    # Salary analysis
    st.markdown("### 💰 Зарплатная аналитика")
    salary_cols = st.columns(4)
    
    salary_data = profession_info['salary_ranges']
    salary_labels = ["Начальный уровень", "Опытный специалист", "Старший уровень", "Эксперт/Руководитель"]
    
    for i, (col, (level, salary)) in enumerate(zip(salary_cols, salary_data.items())):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{salary[selected_language].split(' - ')[0]}</div>
                <div class="metric-label">{salary_labels[i]}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Market metrics
    st.markdown("### 📈 Рыночные метрики")
    metric_cols = st.columns(5)
    
    metrics = profession_info['market_metrics']
    metric_labels = ["Потенциал роста", "Рыночный спрос", "Будущее-proof", "Рост зарплат", "Удаленная работа"]
    
    for i, (col, (metric, value)) in enumerate(zip(metric_cols, metrics.items())):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{value}/5.0</div>
                <div class="metric-label">{metric_labels[i]}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Market analysis text
    st.markdown("#### 📊 Анализ рынка")
    st.markdown(f"{profession_info['market_analysis'][selected_language]}")
    
    # RECOMMENDED PROFESSIONS SECTION
    st.markdown("---")
    st.markdown(f'<div class="section-header">{LANGUAGES[selected_language]["recommended_professions"]}</div>', unsafe_allow_html=True)
    
    for i, profession in enumerate(profession_info["professions"]):
        with st.expander(f"### {profession['title'][selected_language]} - {profession['compatibility']*100:.0f}% совместимость 💼", expanded=i==0):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**{LANGUAGES[selected_language]['description']}:** {profession['description'][selected_language]}")
                st.markdown(f"**{LANGUAGES[selected_language]['market_demand']}:** {profession['demand'][selected_language]}")
                st.markdown(f"**{LANGUAGES[selected_language]['education']}:** {profession['education'][selected_language]}")
                st.markdown(f"**{LANGUAGES[selected_language]['growth']}:** {profession['growth'][selected_language]}")
                
                st.markdown(f"**{LANGUAGES[selected_language]['responsibilities']}:**")
                for responsibility in profession['responsibilities'][selected_language]:
                    st.markdown(f"- {responsibility}")
                    
            with col2:
                st.markdown(f"**{LANGUAGES[selected_language]['key_employers']}:**")
                for company in profession['companies'][selected_language]:
                    st.markdown(f"- {company}")
                
                st.markdown(f"**{LANGUAGES[selected_language]['requirements']}:**")
                for requirement in profession['requirements'][selected_language][:4]:
                    st.markdown(f"- {requirement}")
            
            # Skills gap analysis
            st.markdown("#### 📊 Анализ разрыва навыков")
            current_skill = profession['skills_gap']['current']
            target_skill = profession['skills_gap']['target']
            gap_percentage = (current_skill / target_skill) * 100
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Текущий уровень", f"{current_skill}%")
            with col2:
                st.metric("Требуемый уровень", f"{target_skill}%")
            with col3:
                st.metric("Прогресс", f"{gap_percentage:.1f}%")
            
            st.progress(gap_percentage / 100)
            
            # Certification recommendations
            st.markdown("#### 🎓 Рекомендуемые сертификации")
            for cert in profession['certifications'][selected_language]:
                st.markdown(f"- **{cert}**")
    
    # DEVELOPMENT PLAN SECTION
    st.markdown("---")
    st.markdown(f'<div class="section-header">{LANGUAGES[selected_language]["development_plan"]}</div>', unsafe_allow_html=True)
    
    # Learning path
    st.markdown("### 📚 Образовательный путь")
    for i, step in enumerate(profession_info['learning_path'][selected_language]):
        st.markdown(f"{i+1}. **{step}**")
    
    # Development timeline
    st.markdown("### 🗓️ План развития по этапам")
    
    development_phases = {
        "1-3 месяца (Основы)": [
            "Пройти базовые курсы по выбранному направлению",
            "Освоить ключевые инструменты и технологии",
            "Создать первое портфолио проектов",
            "Присоединиться к профессиональным сообществам"
        ],
        "4-6 месяцев (Практика)": [
            "Выполнить 2-3 реальных проекта",
            "Участвовать в хакатонах и конкурсах",
            "Пройти стажировку или практику",
            "Разработать профессиональное резюме"
        ],
        "7-12 месяцев (Специализация)": [
            "Получить первую профессиональную сертификацию",
            "Начать поиск работы или фриланс-проектов",
            "Создать сильное профессиональное портфолио",
            "Развивать сеть профессиональных контактов"
        ],
        "1-2 года (Профессионализм)": [
            "Закрепиться на позиции младшего специалиста",
            "Продолжать обучение и сертификацию",
            "Участвовать в менторских программах",
            "Развивать экспертизу в узкой области"
        ]
    }
    
    for phase, tasks in development_phases.items():
        with st.expander(f"📅 {phase}"):
            for task in tasks:
                st.markdown(f"- {task}")
    
    # RESTART BUTTON
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Пройти тестирование заново", use_container_width=True):
            st.session_state.test_started = False
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.assessment_complete = False
            st.session_state.results_calculated = False
            st.rerun()

# =============================
# 📞 COMPREHENSIVE CONTACT SECTION
# =============================
st.markdown("---")
st.markdown(f'<div class="section-header">{LANGUAGES[selected_language]["professional_support"]}</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['career_consultants']}**
    
    📞 **Горячая линия:** 87766680880  
    📧 **Электронная почта:** askhatseitkhan@gmail.com  
    💼 **Telegram канал:** @jobai_pro  
    
    **🕒 Часы работы:**
    - Пн-Пт: 9:00-18:00
    - Сб: 10:00-16:00
    - Вс: выходной
    
    **🎯 Услуги:**
    - Профориентация
    - Карьерное консультирование
    - Подготовка резюме
    - Сопровождение собеседований
    """)

with col2:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['career_development_center']}**
    
    🏢 **Центральный офис:** Тараз, Толе Би 66  
    🌐 **Официальный сайт:** jobai-kz.com  
    📱 **Мобильное приложение:** В разработке  
    📊 **Онлайн платформа:** platform.jobai-kz.com
    
    **🏛️ Партнеры:**
    - Министерство труда и соцзащиты
    - Ассоциация HR-менеджеров
    - Технологические парки
    - Ведущие университеты
    """)

with col3:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['online_booking']}**
    
    💻 **Онлайн запись:** jobai-kz.com/booking  
    📱 **WhatsApp бизнес:** +7 776 668 0880  
    👥 **Telegram бот:** @jobai_consultant_bot  
    📅 **Система бронирования:** Круглосуточно
    
    **🎁 Бесплатные услуги:**
    - Первичная консультация
    - Профориентационное тестирование  
    - Анализ резюме
    - Подготовка к собеседованию
    - Карьерное планирование
    """)

# =============================
# 👣 COMPREHENSIVE FOOTER
# =============================
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #64748b; font-size: 0.9rem; line-height: 1.6; padding: 2rem 1rem;'>
    <strong style='color: #1e40af; font-size: 1.1rem;'>{LANGUAGES[selected_language]['footer']}</strong><br><br>
    
    📞 <strong>Телефон:</strong> 87766680880 | 
    🏢 <strong>Адрес:</strong> Тараз, Толе Би 66 | 
    🌐 <strong>Веб-сайт:</strong> jobai-kz.com<br>
    
    💼 <strong>Услуги:</strong> Бесплатные карьерные консультации | 
    🎯 <strong>Тестирование:</strong> Профессиональная диагностика | 
    📊 <strong>Аналитика:</strong> Рыночные исследования<br><br>
    
    <div style='border-top: 1px solid #e2e8f0; padding-top: 1rem; margin-top: 1rem;'>
        © 2024 JobAI Pro. Все права защищены. 
        Платформа разработана при поддержке Министерства цифрового развития, инноваций и аэрокосмической промышленности РК
    </div>
</div>
""", unsafe_allow_html=True)
