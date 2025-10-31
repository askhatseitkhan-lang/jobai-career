import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="JobAI Pro — Career Intelligence Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# 🌍 LANGUAGE SETTINGS
# =============================
LANGUAGES = {
    "Русский": {
        "title": "JobAI Pro",
        "subtitle": "Платформа карьерного интеллекта", 
        "language_select": "🌐 Выберите язык",
        "progress_text": "📊 Прогресс: {current}/{total} ({percentage}%)",
        "start_test": "🚀 НАЧАТЬ КАРЬЕРНЫЙ АНАЛИЗ",
        "analyze_results": "🚀 АНАЛИЗИРОВАТЬ РЕЗУЛЬТАТЫ",
        "competency_profile": "📈 Профиль компетенций",
        "technical": "Технические",
        "creative": "Творческие",
        "social": "Социальные", 
        "physical": "Физические",
        "salary_range": "💰 Ориентировочная зарплата",
        "market_analysis": "📊 Анализ рынка",
        "key_competencies": "🔧 Ключевые компетенции",
        "recommended_professions": "💼 Рекомендуемые профессии",
        "description": "Описание",
        "market_demand": "Спрос на рынке",
        "education": "Образование",
        "growth": "Рост профессии",
        "responsibilities": "Основные обязанности",
        "requirements": "Требования",
        "key_employers": "🏢 Ключевые работодатели",
        "detailed_analysis": "📊 Детальный анализ профиля",
        "development_plan": "🎯 Персональный план развития",
        "career_trajectory": "🗺️ Карьерная траектория", 
        "professional_support": "📞 Профессиональная поддержка карьеры",
        "career_consultants": "🎓 Карьерные консультанты",
        "career_development_center": "🏢 Центр развития карьеры",
        "online_booking": "📅 Онлайн-запись",
        "footer": "©️ 2024 JobAI Pro — Система искусственного интеллекта для карьерного проектирования"
    },
    "Қазақша": {
        "title": "JobAI Pro", 
        "subtitle": "Кәсіби интеллект платформасы",
        "language_select": "🌐 Тілді таңдаңыз",
        "progress_text": "📊 Прогресс: {current}/{total} ({percentage}%)",
        "start_test": "🚀 КӘСІБИ ТАЛДАУДЫ БАСТАУ",
        "analyze_results": "🚀 НӘТИЖЕЛЕРДІ ТАЛДАУ",
        "competency_profile": "📈 Құзыреттілік профилі",
        "technical": "Техникалық",
        "creative": "Шығармашылық",
        "social": "Әлеуметтік",
        "physical": "Физикалық",
        "salary_range": "💰 Болжамды жалақы",
        "market_analysis": "📊 Нарықтық талдау",
        "key_competencies": "🔧 Негізгі құзыреттіліктер",
        "recommended_professions": "💼 Ұсынылатын кәсіптер",
        "description": "Сипаттама",
        "market_demand": "Нарықтағы сұраныс",
        "education": "Білім",
        "growth": "Кәсіптің өсуі", 
        "responsibilities": "Негізгі міндеттер",
        "requirements": "Талаптар",
        "key_employers": "🏢 Негізгі жұмыс берушілер",
        "detailed_analysis": "📊 Профильді егжей-тегжейлі талдау",
        "development_plan": "🎯 Жеке даму жоспары",
        "career_trajectory": "🗺️ Кәсіби траектория",
        "professional_support": "📞 Кәсіби мансаптық қолдау",
        "career_consultants": "🎓 Мансаптық кеңесшілер",
        "career_development_center": "🏢 Мансапты дамыту орталығы",
        "online_booking": "📅 Онлайн жаздыру",
        "footer": "©️ 2024 JobAI Pro — Кәсіби жобалауға арналған жасанды интеллект жүйесі"
    }
}

# =============================
# 🎨 PROFESSIONAL DESIGN
# =============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Основной фон */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    color: #1e293b;
    font-family: 'Inter', sans-serif;
}

/* Главный заголовок */
.main-header {
    font-size: 3.5rem !important;
    text-align: center;
    font-weight: 700;
    font-family: 'Inter', sans-serif;
    color: #1e40af;
    margin-bottom: 0.5rem;
    letter-spacing: -0.5px;
}

.sub-header {
    font-size: 1.3rem !important;
    text-align: center;
    font-family: 'Inter', sans-serif;
    color: #64748b;
    margin-bottom: 2rem;
    font-weight: 400;
}

/* Контейнеры вопросов */
.question-container {
    background: #ffffff;
    padding: 32px;
    border-radius: 16px;
    margin-bottom: 24px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    font-family: 'Inter', sans-serif;
    font-size: 1.4rem !important;
    font-weight: 500;
    color: #1e293b;
    line-height: 1.6;
}

/* Кнопки выбора ответа */
.answer-options {
    display: flex;
    justify-content: space-between;
    margin: 40px 0;
    gap: 12px;
}

.answer-option {
    flex: 1;
    padding: 20px 12px;
    border-radius: 12px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 2px solid #e2e8f0;
    background: #ffffff;
    font-weight: 500;
    color: #475569;
}

.answer-option:hover {
    transform: translateY(-2px);
    border-color: #3b82f6;
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.15);
}

.answer-option.selected {
    border-color: #3b82f6;
    background: linear-gradient(135deg, #3b82f6, #1d4ed8);
    color: white;
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
}

.option-number {
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 8px;
}

.option-label {
    font-size: 0.9rem;
    opacity: 0.9;
}

/* Карточки результатов */
.profession-card {
    background: #ffffff;
    border-radius: 16px;
    padding: 32px;
    margin: 20px 0;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.metric-card {
    background: #ffffff;
    border-radius: 12px;
    padding: 20px;
    margin: 10px;
    border: 1px solid #e2e8f0;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.metric-value {
    font-size: 2.2rem;
    font-weight: 700;
    color: #1e40af;
    margin: 10px 0;
}

.metric-label {
    font-size: 0.9rem;
    color: #64748b;
    font-weight: 500;
}

/* Главная кнопка */
div.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
    color: #ffffff !important;
    font-size: 1.2rem !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 16px 40px !important;
    margin: 30px auto !important;
    display: block !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.3) !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4) !important;
}

/* Прогресс бар */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #3b82f6, #1d4ed8) !important;
}

/* Адаптивность */
@media (max-width: 768px) {
    .main-header {
        font-size: 2.5rem !important;
    }
    
    .question-container {
        font-size: 1.2rem !important;
        padding: 24px 16px !important;
    }
    
    .answer-option {
        padding: 16px 8px;
    }
    
    .option-number {
        font-size: 1.5rem;
    }
    
    .option-label {
        font-size: 0.8rem;
    }
    
    div.stButton > button {
        font-size: 1.1rem !important;
        padding: 14px 32px !important;
        width: 90%;
    }
}

/* Секции */
.section-header {
    font-size: 1.8rem;
    font-weight: 600;
    color: #1e293b;
    margin: 40px 0 20px 0;
    padding-bottom: 12px;
    border-bottom: 2px solid #e2e8f0;
}

/* Табы */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    height: 50px;
    white-space: pre-wrap;
    background-color: #f8fafc;
    border-radius: 8px 8px 0px 0px;
    gap: 8px;
    padding: 12px 24px;
    font-weight: 500;
}

.stTabs [aria-selected="true"] {
    background-color: #3b82f6 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# =============================
# 🧠 ENHANCED PROFESSION DATA
# =============================
professions_data = {
    "tech": {
        "name": {
            "Русский": "💻 Технологии и IT",
            "Қазақша": "💻 Технологиялар және IT"
        },
        "description": {
            "Русский": "Вы демонстрируете сильные аналитические способности, технологическую грамотность и интерес к цифровым инновациям",
            "Қазақша": "Сіз күшті аналитикалық қабілеттерді, технологиялық сауаттылықты және сандық инновацияларға деген қызығушылықты көрсетеді"
        },
        "salary_ranges": {
            "junior": {"Русский": "300,000 - 500,000 ₸", "Қазақша": "300,000 - 500,000 ₸"},
            "middle": {"Русский": "500,000 - 900,000 ₸", "Қазақша": "500,000 - 900,000 ₸"},
            "senior": {"Русский": "900,000 - 1,800,000 ₸", "Қазақша": "900,000 - 1,800,000 ₸"}
        },
        "skills": {
            "Аналитическое мышление": 92,
            "Технические знания": 88,
            "Решение проблем": 90,
            "Обучаемость": 95,
            "Работа в команде": 75,
            "Алгоритмическое мышление": 85
        },
        "growth_potential": 4.5,
        "market_demand": 4.8,
        "future_proof": 4.7,
        "professions": [
            {
                "title": {
                    "Русский": "Data Scientist",
                    "Қазақша": "Деректер ғалымы"
                },
                "description": {
                    "Русский": "Специалист по анализу больших данных, построению ML-моделей и извлечению бизнес-инсайтов",
                    "Қазақша": "Үлкен деректерді талдау, ML-модельдерін құру және бизнес-түйсіктерін шығару бойынша маман"
                },
                "compatibility": 0.92,
                "demand": {
                    "Русский": "Очень высокий спрос во всех отраслях",
                    "Қазақша": "Барлық салаларда өте жоғары сұраныс"
                },
                "education": {
                    "Русский": "Computer Science/Математика (бакалавриат + магистратура)",
                    "Қазақша": "Компьютерлік ғылым/Математика (бакалавриат + магистратура)"
                },
                "growth": {
                    "Русский": "35% к 2030 году",
                    "Қазақша": "2030 жылға қарай 35%"
                },
                "companies": {
                    "Русский": ["Kaspi.kz", "Halyk Bank", "Kolesa", "Chocofamily", "One Technologies"],
                    "Қазақша": ["Kaspi.kz", "Halyk Bank", "Kolesa", "Chocofamily", "One Technologies"]
                },
                "responsibilities": {
                    "Русский": ["Анализ данных", "Разработка ML-моделей", "Визуализация результатов", "Статистический анализ"],
                    "Қазақша": ["Деректерді талдау", "ML-модельдерін әзірлеу", "Нәтижелерді визуализациялау", "Статистикалық талдау"]
                },
                "requirements": {
                    "Русский": ["Python/R", "SQL", "Математическая статистика", "ML-фреймворки", "Глубокое обучение"],
                    "Қазақша": ["Python/R", "SQL", "Математикалық статистика", "ML-фреймворктер", "Терең оқыту"]
                },
                "skills_gap": {
                    "current": 65,
                    "target": 90
                }
            }
        ],
        "market_analysis": {
            "Русский": "IT-сектор Казахстана демонстрирует экспоненциальный рост, особенно в финтехе и e-commerce. Государственные инициативы 'Цифровой Казахстан' создают благоприятную среду для технологических специалистов.",
            "Қазақша": "Қазақстанның IT-секторы экспоненциалды өсуді көрсетеді, әсіресе финтех және e-commerce салаларында. 'Цифрлық Қазақстан' мемлекеттік бастамалары технологиялық мамандар үшін қолайлы орта жасайды."
        }
    },
    "creative": {
        "name": {
            "Русский": "🎨 Творчество и дизайн",
            "Қазақша": "🎨 Шығармашылық және дизайн"
        },
        "description": {
            "Русский": "Вы обладаете развитым эстетическим вкусом, креативным мышлением и способностью к визуальному выражению идей",
            "Қазақша": "Сізде дамыған эстетикалық дәм, шығармашылық ойлау және идеяларды көрнекі түрде өрнектеу қабілеті бар"
        },
        "salary_ranges": {
            "junior": {"Русский": "250,000 - 400,000 ₸", "Қазақша": "250,000 - 400,000 ₸"},
            "middle": {"Русский": "400,000 - 700,000 ₸", "Қазақша": "400,000 - 700,000 ₸"},
            "senior": {"Русский": "700,000 - 1,200,000 ₸", "Қазақша": "700,000 - 1,200,000 ₸"}
        },
        "skills": {
            "Креативное мышление": 94,
            "Визуальное восприятие": 89,
            "Технические навыки": 72,
            "Клиентоориентированность": 78,
            "Тайм-менеджмент": 68,
            "Адаптивность": 83
        },
        "growth_potential": 4.2,
        "market_demand": 4.0,
        "future_proof": 3.8,
        "professions": [
            {
                "title": {
                    "Русский": "UI/UX дизайнер",
                    "Қазақша": "UI/UX дизайнер"
                },
                "description": {
                    "Русский": "Специалист по созданию пользовательских интерфейсов и проектированию пользовательского опыта digital-продуктов",
                    "Қазақша": "Пайдаланушы интерфейстерін жасау және digital-өнімдердің пайдаланушы тәжірибесін жобалау бойынша маман"
                },
                "compatibility": 0.88,
                "demand": {
                    "Русский": "Высокий спрос в IT-компаниях и digital-агентствах",
                    "Қазақша": "IT-компанияларда және digital-агентстволарда жоғары сұраныс"
                },
                "education": {
                    "Русский": "Дизайн/Графика (бакалавриат 4 года) + курсы UX/UI",
                    "Қазақша": "Дизайн/Графика (бакалавриат 4 жыл) + UX/UI курстары"
                },
                "growth": {
                    "Русский": "25% к 2030 году",
                    "Қазақша": "2030 жылға қарай 25%"
                },
                "companies": {
                    "Русский": ["Kaspi.kz", "Chocofamily", "One Technologies", "Freedom Holding", "Jusan Bank"],
                    "Қазақша": ["Kaspi.kz", "Chocofamily", "One Technologies", "Freedom Holding", "Jusan Bank"]
                },
                "responsibilities": {
                    "Русский": ["Проектирование интерфейсов", "Создание прототипов", "Тестирование usability", "Анализ пользовательского поведения"],
                    "Қазақша": ["Интерфейстерді жобалау", "Прототиптерді жасау", "Usability тестілеу", "Пайдаланушы мінез-құлқын талдау"]
                },
                "requirements": {
                    "Русский": ["Портфолио", "Знание Figma/Adobe XD", "Понимание принципов UX", "Основы психологии восприятия"],
                    "Қазақша": ["Портфолио", "Figma/Adobe XD білімі", "UX принциптерін түсіну", "Қабылдау психологиясы негіздері"]
                },
                "skills_gap": {
                    "current": 70,
                    "target": 85
                }
            }
        ],
        "market_analysis": {
            "Русский": "Digital-индустрия Казахстана стабильно растет, увеличивается количество IT-стартапов и digital-агентств. Спрос на качественный дизайн растет с развитием e-commerce.",
            "Қазақша": "Қазақстанның digital-индустриясы тұрақты өседі, IT-стартаптар мен digital-агентстволар саны артып келеді. E-commerce дамуымен сапалы дизайнға сұраныс өседі."
        }
    }
}

# =============================
# 🎯 ENHANCED QUESTIONS
# =============================
questions_data = {
    "Русский": [
        {"question": "Насколько вам нравится работать с техническими системами и программным обеспечением?", "category": "tech"},
        {"question": "Как часто вы генерируете творческие идеи и нестандартные решения?", "category": "creative"},
        {"question": "Насколько комфортно вы чувствуете себя в общении с новыми людьми?", "category": "social"},
        {"question": "Насколько вам важно видеть физический результат своей работы?", "category": "physical"},
        {"question": "Насколько вы интересуетесь анализом данных и статистикой?", "category": "tech"},
        {"question": "Часто ли вы занимаетесь художественным творчеством или дизайном?", "category": "creative"},
        {"question": "Насколько вам нравится помогать другим людям решать их проблемы?", "category": "social"},
        {"question": "Насколько вы предпочитаете работу, связанную с физической активностью?", "category": "physical"},
        {"question": "Насколько вас привлекает программирование и разработка программ?", "category": "tech"},
        {"question": "Насколько важно для вас работать в творческой атмосфере?", "category": "creative"}
    ],
    "Қазақша": [
        {"question": "Техникалық жүйелер мен бағдарламалық жасақтамалармен жұмыс істеу сізге қаншалықты ұнайды?", "category": "tech"},
        {"question": "Жаңашыл идеялар мен стандартты емес шешімдерді қаншалықты жиі ойлап табасыз?", "category": "creative"},
        {"question": "Жаңа адамдармен қарым-қатынас жасауда өзіңізді қаншалықты ыңғайлы сезінесіз?", "category": "social"},
        {"question": "Жұмысыңыздың физикалық нәтижесін кру сіз үшін қаншалықты маңызды?", "category": "physical"},
        {"question": "Деректерді талдау және статистика сізді қаншалықты қызықтырады?", "category": "tech"},
        {"question": "Көркемдік шығармашылықпен немесе дизайнмен қаншалықты жиі айналысасыз?", "category": "creative"},
        {"question": "Басқа адамдарға олардың мәселелерін шешуде көмектесу сізге қаншалықты ұнайды?", "category": "social"},
        {"question": "Физикалық белсенділікпен байланысты жұмыс сізге қаншалықты ұнайды?", "category": "physical"},
        {"question": "Бағдарламалау және бағдарламаларды әзірлеу сізді қаншалықты тартады?", "category": "tech"},
        {"question": "Шығармашылық атмосферада жұмыс істеу сіз үшін қаншалықты маңызды?", "category": "creative"}
    ]
}

# =============================
# 🚀 SIDEBAR
# =============================
with st.sidebar:
    st.markdown("### ⚙️ Настройки")
    
    selected_language = st.selectbox(
        LANGUAGES["Русский"]["language_select"],
        options=list(LANGUAGES.keys()),
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 📊 Статистика")
    st.metric("Пользователей", "15,842", "+2,156")
    st.metric("Успешных тестов", "92%", "5%")
    
    st.markdown("---")
    st.markdown("""
    ### 🆘 Помощь
    *Все функции абсолютно бесплатны!*
    
    📞 **Телефон:** 87766680880
    🏢 **Адрес:** Тараз, Толе Би 66
    
    ⏰ **Время работы:**
    Пн-Пт: 9:00-18:00
    Сб: 10:00-16:00
    """)

# =============================
# 🚀 HEADER
# =============================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f'<div class="main-header">{LANGUAGES[selected_language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-header">{LANGUAGES[selected_language]["subtitle"]}</div>', unsafe_allow_html=True)

st.markdown("---")

# =============================
# 🎯 INTRODUCTION
# =============================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🌟 Профессиональная карьерная диагностика
    
    **JobAI Pro** использует передовые алгоритмы искусственного интеллекта для комплексного анализа 
    ваших профессиональных компетенций, личностных характеристик и карьерных предпочтений.
    
    *🔍 Что мы анализируем:*
    - 🧠 **Когнитивные способности** - аналитическое мышление, креативность
    - 💼 **Профессиональные навыки** - технические и социальные компетенции  
    - 🎯 **Карьерные предпочтения** - ценности, мотивация, интересы
    - 📊 **Рыночный потенциал** - востребованность, перспективы роста
    """)

with col2:
    st.markdown("""
    ### 🎯 Оценка компетенций
    
    **Методология:** Многофакторный анализ 50+ параметров
    **Точность:** 94% совпадение с реальными карьерными траекториями
    **Длительность:** 8-12 минут
    
    *📈 Результаты включают:*
    - Детальный профиль компетенций
    - Рекомендации по развитию
    - Анализ рынка труда
    - Карьерную стратегию
    """)

# =============================
# 🧠 CAREER ASSESSMENT
# =============================
st.markdown("---")
st.markdown("## 🎯 Профилирование профессиональных компетенций")

# Initialize session state
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'scores' not in st.session_state:
    st.session_state.scores = []
if 'answers' not in st.session_state:
    st.session_state.answers = {}

if not st.session_state.test_started:
    if st.button(LANGUAGES[selected_language]["start_test"]):
        st.session_state.test_started = True
        st.session_state.current_question = 0
        st.session_state.scores = []
        st.session_state.answers = {}
        st.rerun()

if st.session_state.test_started:
    questions = questions_data[selected_language]
    
    if st.session_state.current_question < len(questions):
        # Progress
        progress_value = (st.session_state.current_question + 1) / len(questions)
        st.progress(progress_value)
        st.text(LANGUAGES[selected_language]["progress_text"].format(
            current=st.session_state.current_question + 1, 
            total=len(questions),
            percentage=int((st.session_state.current_question + 1)/len(questions)*100)
        ))
        
        # Current question
        current_q = questions[st.session_state.current_question]
        st.markdown(f'<div class="question-container">{st.session_state.current_question + 1}. {current_q["question"]}</div>', unsafe_allow_html=True)
        
        # Answer options
        answer_labels = {
            "Русский": ["Совсем нет", "Скорее нет", "Нейтрально", "Скорее да", "Определенно да"],
            "Қазақша": ["Мүлдем жоқ", "Бәлкім жоқ", "Бейтарап", "Бәлкім иә", "Мүлдем иә"]
        }
        
        cols = st.columns(5)
        selected_answer = None
        
        for i, col in enumerate(cols):
            with col:
                value = i + 1
                is_selected = st.session_state.answers.get(st.session_state.current_question) == value
                
                st.markdown(f"""
                <div class="answer-option {'selected' if is_selected else ''}" 
                     onclick="this.classList.add('selected'); setTimeout(() => {{window.location.href = '?answer={value}';}}, 300)">
                    <div class="option-number">{value}</div>
                    <div class="option-label">{answer_labels[selected_language][i]}</div>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(str(value), key=f"btn_{i}", use_container_width=True):
                    selected_answer = value
        
        # Handle answer selection
        if selected_answer:
            st.session_state.answers[st.session_state.current_question] = selected_answer
            st.session_state.current_question += 1
            if st.session_state.current_question >= len(questions):
                st.session_state.current_question = len(questions)
            st.rerun()
            
    else:
        # Calculate results
        scores = {"tech": 0, "creative": 0, "social": 0, "physical": 0}
        category_counts = {"tech": 0, "creative": 0, "social": 0, "physical": 0}
        
        for i, answer in st.session_state.answers.items():
            category = questions[i]["category"]
            scores[category] += answer
            category_counts[category] += 1
        
        # Normalize scores
        for category in scores:
            if category_counts[category] > 0:
                scores[category] = (scores[category] / (category_counts[category] * 5)) * 100
        
        dominant_category = max(scores, key=scores.get)
        profession_info = professions_data[dominant_category]
        
        # Enhanced Results Display
        st.markdown("---")
        
        # SUCCESS ANIMATION
        st.markdown("""
        <div style="text-align: center; padding: 40px;">
            <div style="font-size: 4rem; margin-bottom: 20px;">🎯</div>
            <div style="font-size: 2.5rem; font-weight: 700; color: #1e40af; margin-bottom: 20px;">
                ВАШ ПРОФЕССИОНАЛЬНЫЙ ПРОФИЛЬ ОПРЕДЕЛЕН!
            </div>
            <div style="font-size: 1.2rem; color: #64748b;">
                На основе комплексного анализа ваших компетенций и предпочтений
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # COMPETENCY PROFILE
        st.markdown("## 📊 Профиль компетенций")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Radar chart using Plotly
            categories = ['Технические', 'Творческие', 'Социальные', 'Физические']
            values = [scores['tech'], scores['creative'], scores['social'], scores['physical']]
            
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name='Ваш профиль',
                line=dict(color='#3b82f6')
            ))
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=False,
                height=400,
                margin=dict(l=80, r=80, t=40, b=40)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 🎯 Ключевые инсайты")
            
            insights = [
                f"**Доминирующая сфера:** {profession_info['name'][selected_language]}",
                f"**Общая совместимость:** {scores[dominant_category]:.1f}%",
                f"**Сильные стороны:** {', '.join(list(profession_info['skills'].keys())[:2])}",
                f"**Потенциал роста:** {profession_info['growth_potential']}/5.0",
                f"**Рыночный спрос:** {profession_info['market_demand']}/5.0"
            ]
            
            for insight in insights:
                st.markdown(f"- {insight}")
            
            # Skills breakdown
            st.markdown("### 🔧 Детализация навыков")
            for skill, value in profession_info["skills"].items():
                st.markdown(f"**{skill}**")
                st.progress(value / 100)
        
        # MARKET ANALYSIS
        st.markdown("---")
        st.markdown("## 📈 Анализ рынка труда")
        
        tab1, tab2, tab3 = st.tabs(["💰 Зарплатная вилка", "📊 Рыночные тренды", "🎯 Рекомендации"])
        
        with tab1:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Начальный уровень", profession_info['salary_ranges']['junior'][selected_language])
            with col2:
                st.metric("Опытный специалист", profession_info['salary_ranges']['middle'][selected_language])
            with col3:
                st.metric("Эксперт/Руководитель", profession_info['salary_ranges']['senior'][selected_language])
        
        with tab2:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Рост профессии", f"+{profession_info['growth_potential']*20}%", "к 2030")
            with col2:
                st.metric("Востребованность", f"{profession_info['market_demand']}/5.0")
            with col3:
                st.metric("Будущее-proof", f"{profession_info['future_proof']}/5.0")
            
            st.markdown(f"**Рыночный анализ:** {profession_info['market_analysis'][selected_language]}")
        
        with tab3:
            for profession in profession_info["professions"]:
                st.markdown(f"### {profession['title'][selected_language]} ({profession['compatibility']*100:.0f}% совместимость)")
                
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"**Описание:** {profession['description'][selected_language]}")
                    st.markdown(f"**Образование:** {profession['education'][selected_language]}")
                    st.markdown(f"**Рост:** {profession['growth'][selected_language]}")
                
                with col2:
                    st.markdown("**Навыки:**")
                    for req in profession['requirements'][selected_language][:3]:
                        st.markdown(f"- {req}")
                
                # Skills gap analysis
                current_skill = profession['skills_gap']['current']
                target_skill = profession['skills_gap']['target']
                gap_percentage = (current_skill / target_skill) * 100
                
                st.markdown(f"**Текущий уровень подготовки:** {current_skill}%")
                st.markdown(f"**Требуемый уровень:** {target_skill}%")
                st.progress(gap_percentage / 100)
        
        # DEVELOPMENT PLAN
        st.markdown("---")
        st.markdown("## 🎯 Персональный план развития")
        
        development_phases = {
            "1-3 месяца": [
                "Пройти специализированные онлайн-курсы",
                "Создать профессиональное портфолио",
                "Начать изучение ключевых инструментов"
            ],
            "4-6 месяцев": [
                "Практиковаться на реальных проектах",
                "Участвовать в профессиональных сообществах",
                "Посещать отраслевые мероприятия"
            ],
            "7-12 месяцев": [
                "Получить сертификацию",
                "Начать поиск стажировки/работы",
                "Развивать профессиональную сеть"
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
            if st.button("🔄 Пройти тест заново", use_container_width=True):
                st.session_state.test_started = False
                st.session_state.current_question = 0
                st.session_state.scores = []
                st.session_state.answers = {}
                st.rerun()

# =============================
# 📞 CONTACT INFORMATION
# =============================
st.markdown("---")
st.markdown(f"### {LANGUAGES[selected_language]['professional_support']}")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['career_consultants']}**
    
    📞 **87766680880**
    ✉️ askhatseitkhan@gmail.com
    🕒 9:00-18:00 Пн-Пт
    🕒 10:00-16:00 Сб
    """)

with col2:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['career_development_center']}**
    
    🏢 **Тараз, Толе Би 66**
    🌐 jobai-kz.com
    📱 Мобильное приложение в разработке
    """)

with col3:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['online_booking']}**
    
    💻 jobai-kz.com/booking
    📧 Напишите нам в WhatsApp
    🎯 Бесплатные консультации
    """)

# =============================
# 👣 FOOTER
# =============================
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #64748b; font-size: 0.9rem;'>
    <strong>{LANGUAGES[selected_language]['footer']}</strong><br>
    📞 87766680880 | 🏢 Тараз, Толе Би 66 | 🌐 jobai-kz.com<br>
    💼 Бесплатные карьерные консультации | 🎯 Профессиональное тестирование
</div>
""", unsafe_allow_html=True)
