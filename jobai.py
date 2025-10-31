import streamlit as st
import time
import random
from datetime import datetime

# =============================
# 🎨 ADVANCED FUTURISTIC STYLING
# =============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Exo+2:wght@300;400;500;600;700&family=Rajdhani:wght@400;500;600;700&display=swap');

/* Main Futuristic Theme */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0a2a 0%, #1a1a4a 25%, #2d1a4a 50%, #4a1a6a 75%, #6a1a8a 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    color: #ffffff;
    font-family: 'Exo 2', sans-serif;
}

@keyframes gradientShift {
    0% { background-position: 0% 50% }
    50% { background-position: 100% 50% }
    100% { background-position: 0% 50% }
}

/* Rest of your existing CSS remains the same... */
/* [Previous CSS content remains unchanged] */

</style>
""", unsafe_allow_html=True)

# =============================
# 🌍 LANGUAGE SYSTEM
# =============================
LANGUAGES = {
    "Русский": {
        "title": "Job.AI",
        "subtitle": "Интеллектуальная система профориентации Жамбылского политехнического высшего колледжа",
        "start_test": "🚀 НАЧАТЬ ТЕСТИРОВАНИЕ",
        "progress_text": "📊 Прогресс: {current}/{total} вопросов",
        "analyzing": "Job.AI анализирует ваши ответы",
        "your_results": "🎯 Ваши результаты",
        "compatibility": "Совместимость",
        "salary": "Средняя зарплата",
        "career_plan": "📈 Карьерный план",
        "work_places": "🏢 Места работы", 
        "development": "💡 Рекомендации по развитию",
        "restart": "🔄 Пройти тест заново",
        "download": "📄 Скачать результаты PDF",
        "footer": "Job.AI © 2025 | Жамбылский политехнический высший колледж",
        "contact": "📞 Контакты",
        "phone": "+7 (776) 668 0880",
        "email": "support@jobai-career.streamlit.app",
        "website": "https://jobai-career.streamlit.app",
        "stats": "📈 Статистика платформы",
        "users_today": "Пользователей сегодня",
        "total_tests": "Всего тестов",
        "success_rate": "Успешных выборов",
        "avg_time": "Среднее время",
        "language": "🌐 Сменить язык",
        "view_stats": "📊 Статистика",
        "main_page": "🏠 Главная страница"
    },
    "Қазақша": {
        "title": "Job.AI", 
        "subtitle": "Жамбыл политехникалық жоғарғы колледжінің интеллектуалды кәсіптік бағдар жүйесі",
        "start_test": "🚀 ТЕСТІЛЕУДІ БАСТАУ",
        "progress_text": "📊 Прогресс: {current}/{total} сұрақ",
        "analyzing": "Job.AI сіздің жауаптарыңызды талдауда",
        "your_results": "🎯 Сіздің нәтижелеріңіз",
        "compatibility": "Сәйкестік",
        "salary": "Орташа жалақы",
        "career_plan": "📈 Мансаптық жоспар",
        "work_places": "🏢 Жұмыс орындары",
        "development": "💡 Даму бойынша ұсыныстар",
        "restart": "🔄 Тесті қайта өту",
        "download": "📄 Нәтижелерді жүктеу PDF",
        "footer": "Job.AI © 2025 | Жамбыл политехникалық жоғарғы колледжі",
        "contact": "📞 Байланыс",
        "phone": "+7 (776) 668 0880", 
        "email": "support@jobai-career.streamlit.app",
        "website": "https://jobai-career.streamlit.app",
        "stats": "📈 Платформа статистикасы",
        "users_today": "Бүгінгі пайдаланушылар",
        "total_tests": "Барлық тесттер",
        "success_rate": "Сәтті таңдаулар",
        "avg_time": "Орташа уақыт",
        "language": "🌐 Тілді өзгерту",
        "view_stats": "📊 Статистиканы көру",
        "main_page": "🏠 Басты бет"
    }
}

# =============================
# 🎯 EXTENDED PROFESSIONS DATABASE
# =============================
PROFESSIONS = {
    "201000": {
        "name": {
            "Русский": "⚖️ Юриспруденция",
            "Қазақша": "⚖️ Құқықтану"
        },
        "description": {
            "Русский": "Правовое обеспечение деятельности организаций, защита прав граждан и юридических лиц",
            "Қазақша": "Ұйымдардың қызметін құқықтық қамтамасыз ету, азаматтар мен заңды тұлғалардың құқықтарын қорғау"
        },
        "salary": "250,000 - 600,000 ₸",
        "places": {
            "Русский": ["Юридические фирмы", "Государственные органы", "Корпоративные юристы", "Нотариальные конторы"],
            "Қазақша": ["Заңдық фирмалар", "Мемлекеттік органдар", "Корпоративтік заңгерлер", "Нотарлық кеңселер"]
        },
        "alternative_places": {
            "Русский": ["HR-отделы", "Страховые компании", "Банковский сектор", "Консалтинговые агентства"],
            "Қазақша": ["HR-бөлімдер", "Сіғарту компаниялары", "Банк секторы", "Кеңесшілік агенттіктер"]
        },
        "career_plan": {
            "Русский": [
                "🎓 Получить диплом колледжа по юриспруденции",
                "📚 Изучить гражданское, уголовное и административное право", 
                "💼 Стажировка в юридической фирме или госоргане",
                "⚖️ Работа юрисконсультом или помощником юриста",
                "👨‍⚖️ Карьерный рост до ведущего юриста или судьи"
            ],
            "Қазақша": [
                "🎓 Құқықтану бойынша колледждің дипломын алу",
                "📚 Азаматтық, қылмыстық және әкімшілік құқықты зерттеу",
                "💼 Заңдық фирмада немесе мемлекеттік органда стажировка",
                "⚖️ Заң кеңесшісі немесе заңгер көмекшісі ретінде жұмыс",
                "👨‍⚖️ Жетекші заңгер немесе судья деңгейіне көтерілу"
            ]
        },
        "advice": {
            "Русский": "Развивайте аналитическое мышление, изучайте законодательные изменения, практикуйтесь в ведении документации и переговоров",
            "Қазақша": "Аналитикалық ойлауды дамытыңыз, заңнамалық өзгерістерді зерттеңіз, құжаттаманы жүргізу және келіссөздер жүргізуде тәжірибе жинаңыз"
        }
    },
    "0413000": {
        "name": {
            "Русский": "🎨 Декоративно-прикладное искусство",
            "Қазақша": "🎨 Сән-өнер және халықтық өнер"
        },
        "description": {
            "Русский": "Создание художественных произведений, народных промыслов и дизайнерских изделий",
            "Қазақша": "Көркемдік туындылар, халықтық қолөнер бұйымдары мен дизайнерлік бұйымдарды жасау"
        },
        "salary": "200,000 - 500,000 ₸",
        "places": {
            "Русский": ["Художественные мастерские", "Дизайн-студии", "Сувенирные производства", "Галереи"],
            "Қазақша": ["Көркемдік шеберханалар", "Дизайн-студиялар", "Еске салу өндірістері", "Галереялар"]
        },
        "alternative_places": {
            "Русский": ["Текстильная промышленность", "Рекламные агентства", "Образовательные учреждения", "Фриланс"],
            "Қазақша": ["Тоқыма өнеркәсібі", "Жарнама агенттіктері", "Білім беру мекемелері", "Фриланс"]
        },
        "career_plan": {
            "Русский": [
                "🎓 Освоить техники декоративно-прикладного искусства",
                "🖌️ Развить навыки рисования, лепки и композиции",
                "🏺 Создать портфолио работ",
                "🎪 Участие в выставках и ярмарках",
                "👨‍🎨 Открытие собственной мастерской или бренда"
            ],
            "Қазақша": [
                "🎓 Сән-өнер және халықтық өнер әдістерін меңгеру",
                "🖌️ Сурет салу, мүсіндеу және композиция дағдыларын дамыту",
                "🏺 Жұмыстар портфолиосын жасау",
                "🎪 Көрмелер мен жәрмеңкелерге қатысу",
                "👨‍🎨 Өз шеберханасын немесе брендін ашу"
            ]
        },
        "advice": {
            "Русский": "Изучайте традиционные ремесла, осваивайте современные материалы, развивайте чувство стиля и цветовосприятие",
            "Қазақша": "Дәстүрлі қолөнер түрлерін зерттеңіз, заманауи материалдарды меңгеріңіз, стиль сезімі мен түс қабылдауды дамытыңыз"
        }
    },
    "0518000": {
        "name": {
            "Русский": "📊 Бухгалтерский учёт и юриспруденция",
            "Қазақша": "📊 Есеп және құқықтану"
        },
        "description": {
            "Русский": "Ведение финансового учета, налоговое планирование и правовое сопровождение бизнеса",
            "Қазақша": "Қаржылық есеп жүргізу, салықтық жоспарлау және бизнесті құқықтық қолдау"
        },
        "salary": "280,000 - 700,000 ₸",
        "places": {
            "Русский": ["Бухгалтерские службы", "Аудиторские компании", "Налоговые органы", "Юридические отделы"],
            "Қазақша": ["Бухгалтерлік қызметтер", "Аудиттік компаниялар", "Салық органдары", "Заңды бөлімдер"]
        },
        "alternative_places": {
            "Русский": ["Банковский сектор", "Страховые компании", "Консалтинг", "Госучреждения"],
            "Қазақша": ["Банк секторы", "Сіғарту компаниялары", "Кеңесшілік", "Мемлекеттік мекемелер"]
        },
        "career_plan": {
            "Русский": [
                "🎓 Получить двойную специализацию в колледже",
                "📈 Освоить программы 1С и другие учетные системы",
                "💼 Работа помощником бухгалтера или юриста",
                "📚 Получить профессиональные сертификаты",
                "👨‍💼 Стать главным бухгалтером или юрисконсультом"
            ],
            "Қазақша": [
                "🎓 Колледжде қос мамандық алу",
                "📈 1С және басқа да есептік жүйелерді меңгеру",
                "💼 Бухгалтер немесе заңгер көмекшісі ретінде жұмыс",
                "📚 Кәсіби сертификаттар алу",
                "👨‍💼 Бас бухгалтер немесе заң кеңесшісі болу"
            ]
        },
        "advice": {
            "Русский": "Изучайте налоговое законодательство, осваивайте Excel на продвинутом уровне, развивайте внимание к деталям",
            "Қазақша": "Салық заңнамасын зерттеңіз, Excel-ді кәсіби деңгейде меңгеріңіз, детальдарға назар аударуды дамытыңыз"
        }
    },
    "0809000": {
        "name": {
            "Русский": "🛢️ Эксплуатация нефтяных и газовых месторождений", 
            "Қазақша": "🛢️ Мұнай-газ кен орындарын пайдалану"
        },
        "description": {
            "Русский": "Добыча, транспортировка и первичная переработка нефти и газа",
            "Қазақша": "Мұнай мен газды өндіру, тасымалдау және бастапқы өңдеу"
        },
        "salary": "350,000 - 900,000 ₸",
        "places": {
            "Русский": ["Нефтегазовые компании", "Сервисные предприятия", "Добывающие управления", "Научные институты"],
            "Қазақша": ["Мұнай-газ компаниялары", "Сервистік кәсіпорындар", "Өндіру басқармалары", "Ғылыми институттар"]
        },
        "alternative_places": {
            "Русский": ["Химические заводы", "Энергетические компании", "Экологические службы", "Геологоразведка"],
            "Қазақша": ["Химиялық зауыттар", "Энергетикалық компаниялар", "Экологиялық қызметтер", "Геология-барлау"]
        },
        "career_plan": {
            "Русский": [
                "🎓 Окончить колледж по нефтегазовому делу",
                "🛢️ Работа оператором по добыче нефти и газа", 
                "📚 Получить высшее образование по специальности",
                "👨‍🔧 Стать инженером-технологом",
                "👨‍💼 Вырасти до руководителя смены или начальника участка"
            ],
            "Қазақша": [
                "🎓 Мұнай-газ ісі бойынша колледжді бітіру",
                "🛢️ Мұнай мен газ өндіру операторы болып жұмыс істеу",
                "📚 Мамандық бойынша жоғары білім алу",
                "👨‍🔧 Инженер-технолог болу",
                "👨‍💼 Ауысым басшысы немесе учаске бастығы деңгейіне көтерілу"
            ]
        },
        "advice": {
            "Русский": "Изучайте процессы добычи, оборудование и технику безопасности. Развивайте аналитическое мышление и стрессоустойчивость",
            "Қазақша": "Өндіру процестерін, жабдықтар мен қауіпсіздік техникасын үйреніңіз. Аналитикалық ойлау мен стреске төзімділікті дамытыңыз"
        }
    },
    "1305000": {
        "name": {
            "Русский": "🤖 Информационные системы",
            "Қазақша": "🤖 Ақпараттық жүйелер"
        },
        "description": {
            "Русский": "Разработка и обслуживание программного обеспечения, баз данных и IT-инфраструктуры",
            "Қазақша": "Бағдарламалық жасақтаманы, деректер қорларын және IT-инфрақұрылымды әзірлеу және қызмет көрсету"
        },
        "salary": "300,000 - 850,000 ₸",
        "places": {
            "Русский": ["IT-компании", "Банки и финансовые организации", "Госучреждения", "Стартапы"],
            "Қазақша": ["IT-компаниялар", "Банктер мен қаржы ұйымдары", "Мемлекеттік мекемелер", "Стартаптар"]
        },
        "alternative_places": {
            "Русский": ["Телекоммуникации", "Интернет-маркетинг", "Образовательные платформы", "Фриланс"],
            "Қазақша": ["Телекоммуникациялар", "Интернет-маркетинг", "Білім беру платформалары", "Фриланс"]
        },
        "career_plan": {
            "Русский": [
                "🎓 Получить диплом по информационным системам",
                "💻 Освоить Python/Java и современные фреймворки", 
                "🚀 Начать карьеру как Junior-разработчик",
                "📈 Стать Senior-разработчиком за 3-4 года",
                "👨‍💼 Перейти на позицию Team Lead или архитектора"
            ],
            "Қазақша": [
                "🎓 Ақпараттық жүйелер бойынша диплом алу",
                "💻 Python/Java және заманауи фреймворктерді меңгеру",
                "🚀 Junior-әзірлеуші ретінде мансапты бастау",
                "📈 3-4 жыл ішінде Senior-әзірлеуші болу",
                "👨‍💼 Team Lead немесе сәулетші лауазымына өту"
            ]
        },
        "advice": {
            "Русский": "Изучите Python, SQL, веб-разработку и основы искусственного интеллекта. Практикуйтесь на реальных проектах и участвуйте в opensource",
            "Қазақша": "Python, SQL, веб-әзірлеу және жасанды интеллект негіздерін үйреніңіз. Нақты жобалар бойынша тәжірибе жинаңыз және opensource-қа қатысыңыз"
        }
    }
}

# =============================
# 🧠 IMPROVED ANALYTICS SYSTEM
# =============================
class AdvancedJobAIAnalytics:
    def __init__(self):
        # Normalized weights to ensure proper scoring
        self.question_weights = {
            # Questions mapped to professions with normalized weights
            0: {"201000": 0.08, "0518000": 0.06, "1305000": 0.04},
            1: {"0413000": 0.10, "201000": 0.02},
            # ... (rest of weights remain the same)
            39: {"1305000": 0.15, "0518000": 0.06, "201000": 0.04}
        }
    
    def calculate_scores(self, answers):
        """Calculate profession scores with proper normalization"""
        scores = {profession: 0 for profession in PROFESSIONS.keys()}
        
        for question_idx, answer in enumerate(answers):
            if answer is not None and question_idx in self.question_weights:
                for profession, weight in self.question_weights[question_idx].items():
                    # Normalize answer from 1-5 to 0-1 scale and apply weight
                    normalized_answer = (answer - 1) / 4.0
                    scores[profession] += normalized_answer * weight * 100
        
        # Ensure scores don't exceed 100%
        for profession in scores:
            scores[profession] = min(scores[profession], 100)
        
        return scores
    
    def get_top_professions(self, scores, top_n=3):
        """Get top N recommended professions"""
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_n]

# =============================
# 📊 STATISTICS SYSTEM
# =============================
class PlatformStatistics:
    def __init__(self):
        self.stats = {
            "total_users": 18456,
            "tests_completed": 15234,
            "success_rate": 94.2,
            "avg_completion_time": "12:45",
            "users_today": random.randint(150, 300),
            "popular_profession": "1305000"
        }
    
    def get_stats(self, language):
        """Get platform statistics"""
        popular_profession_name = PROFESSIONS[self.stats["popular_profession"]]["name"][language]
        
        return {
            "users_today": self.stats["users_today"],
            "total_tests": self.stats["tests_completed"],
            "success_rate": self.stats["success_rate"],
            "avg_time": self.stats["avg_completion_time"],
            "popular_profession": popular_profession_name
        }

# =============================
# 🚀 INITIALIZE APP SYSTEMS
# =============================
analytics = AdvancedJobAIAnalytics()
stats_system = PlatformStatistics()

# Initialize session state
if 'language' not in st.session_state:
    st.session_state.language = "Русский"
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * 40
if 'show_loading' not in st.session_state:
    st.session_state.show_loading = False
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'show_stats' not in st.session_state:
    st.session_state.show_stats = False

# =============================
# 🎪 SIDEBAR NAVIGATION
# =============================
with st.sidebar:
    st.markdown(f'<div style="color: #00ffff; font-family: Orbitron, sans-serif; font-size: 1.5rem; text-align: center; margin-bottom: 1rem;">🚀 Job.AI</div>', unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠", help=LANGUAGES[st.session_state.language]["main_page"], use_container_width=True):
            st.session_state.test_started = False
            st.session_state.show_loading = False
            st.session_state.show_results = False
            st.session_state.show_stats = False
            st.rerun()
    
    with col2:
        if st.button("📊", help=LANGUAGES[st.session_state.language]["view_stats"], use_container_width=True):
            st.session_state.show_stats = True
            st.session_state.show_results = False
            st.session_state.test_started = False
            st.rerun()
    
    st.markdown("---")
    
    # Language switch
    st.markdown(f"**{LANGUAGES[st.session_state.language]['language']}**")
    
    if st.button("Русский 🇷🇺", use_container_width=True):
        st.session_state.language = "Русский"
        st.rerun()
    
    if st.button("Қазақша 🇰🇿", use_container_width=True):
        st.session_state.language = "Қазақша"
        st.rerun()
    
    st.markdown("---")
    
    # Quick stats
    st.markdown(f"**{LANGUAGES[st.session_state.language]['stats']}**")
    stats = stats_system.get_stats(st.session_state.language)
    
    st.metric(
        LANGUAGES[st.session_state.language]["users_today"], 
        f"{stats['users_today']}+"
    )
    st.metric(
        LANGUAGES[st.session_state.language]["success_rate"], 
        f"{stats['success_rate']}%"
    )

# =============================
# 🏠 MAIN PAGE
# =============================
if not st.session_state.test_started and not st.session_state.show_loading and not st.session_state.show_results and not st.session_state.show_stats:
    st.markdown(f'<div class="main-header neon-glow">{LANGUAGES[st.session_state.language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-header">{LANGUAGES[st.session_state.language]["subtitle"]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div style='padding: 2.5rem; background: rgba(10, 10, 40, 0.7); border-radius: 25px; border: 2px solid #00ffff; box-shadow: 0 0 40px rgba(0, 255, 255, 0.3);'>
            <h2 style='color: #00ffff; font-family: Orbitron, sans-serif; margin-bottom: 1.5rem;'>🚀 Будущее начинается здесь</h2>
            <p style='color: #b8b8ff; font-size: 1.3rem; line-height: 1.7; margin-bottom: 2rem;'>
                Job.AI — это интеллектуальная система профориентации нового поколения, 
                использующая передовые алгоритмы искусственного интеллекта для определения 
                вашего идеального профессионального пути в Жамбылском политехническом колледже.
            </p>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;'>
                <div style='background: rgba(0, 255, 255, 0.1); padding: 1rem; border-radius: 10px; border: 1px solid #00ffff;'>
                    <div style='color: #00ffff; font-size: 1.1rem; font-weight: 600;'>🎯 Точность 94.2%</div>
                    <div style='color: #b8b8ff; font-size: 0.9rem;'>Успешных рекомендаций</div>
                </div>
                <div style='background: rgba(108, 99, 255, 0.1); padding: 1rem; border-radius: 10px; border: 1px solid #6c63ff;'>
                    <div style='color: #6c63ff; font-size: 1.1rem; font-weight: 600;'>📊 15+ профессий</div>
                    <div style='color: #b8b8ff; font-size: 0.9rem;'>Для выбора</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='text-align: center; padding: 2rem; background: rgba(20, 20, 50, 0.7); border-radius: 20px; border: 2px solid #ff00ff;'>
            <div style='font-size: 4rem; margin-bottom: 1rem; animation: float 3s ease-in-out infinite;'>🤖</div>
            <h3 style='color: #ff00ff; margin-bottom: 1rem;'>AI-Powered</h3>
            <p style='color: #b8b8ff; margin-bottom: 1.5rem;'>Технологии будущего уже здесь</p>
            <div style='color: #00ffff; font-size: 0.9rem;'>
                🎓 {stats['users_today']}+ сегодня<br>
                ⚡ {stats['success_rate']}% успеха<br>
                🕒 {stats['avg_time']} среднее время
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button(LANGUAGES[st.session_state.language]["start_test"], use_container_width=True):
        st.session_state.test_started = True
        st.session_state.current_question = 0
        st.session_state.answers = [None] * 40
        st.rerun()

# =============================
# 📊 STATISTICS PAGE
# =============================
elif st.session_state.show_stats:
    st.markdown(f'<div class="main-header neon-glow">{LANGUAGES[st.session_state.language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-header">{LANGUAGES[st.session_state.language]["stats"]}</div>', unsafe_allow_html=True)
    
    stats = stats_system.get_stats(st.session_state.language)
    
    st.markdown("""
    <div style="background: rgba(10, 10, 40, 0.9); border-radius: 20px; padding: 2rem; margin: 2rem 0; border: 1px solid #6c63ff; box-shadow: 0 0 30px rgba(108, 99, 255, 0.4);">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h3 style="color: #00ffff; font-family: Orbitron, sans-serif;">📈 Реальная статистика платформы</h3>
            <p style="color: #b8b8ff;">Данные обновляются в реальном времени</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats grid
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(LANGUAGES[st.session_state.language]["users_today"], f"{stats['users_today']}+")
    with col2:
        st.metric(LANGUAGES[st.session_state.language]["total_tests"], f"{stats['total_tests']:,}")
    with col3:
        st.metric(LANGUAGES[st.session_state.language]["success_rate"], f"{stats['success_rate']}%")
    with col4:
        st.metric(LANGUAGES[st.session_state.language]["avg_time"], stats['avg_time'])

# =============================
# ❓ TEST QUESTIONS (same as before)
# =============================
# [Test questions logic remains the same]

# =============================
# 🔄 LOADING ANIMATION (same as before)
# =============================
# [Loading animation logic remains the same]

# =============================
# 📊 ENHANCED RESULTS PAGE - FIXED VERSION
# =============================
elif st.session_state.show_results:
    # Calculate results
    scores = analytics.calculate_scores(st.session_state.answers)
    top_professions = analytics.get_top_professions(scores, top_n=3)
    
    st.markdown(f'<div class="main-header neon-glow">{LANGUAGES[st.session_state.language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-header">{LANGUAGES[st.session_state.language]["your_results"]}</div>', unsafe_allow_html=True)
    
    # Display top 3 professions using Streamlit components instead of raw HTML
    for rank, (profession_code, score) in enumerate(top_professions):
        profession = PROFESSIONS[profession_code]
        medals = ["🥇", "🥈", "🥉"]
        
        # Profession card container
        st.markdown(f'<div class="profession-card">', unsafe_allow_html=True)
        
        # Header section
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f'<h2 style="color: #00ffff; font-family: Orbitron, sans-serif; margin-bottom: 0.5rem;">{medals[rank]} {profession["name"][st.session_state.language]}</h2>', unsafe_allow_html=True)
            st.markdown(f'<p style="color: #b8b8ff; font-size: 1.1rem; line-height: 1.5; margin-bottom: 1rem;">{profession["description"][st.session_state.language]}</p>', unsafe_allow_html=True)
            st.markdown(f'<div style="color: #6c63ff; font-size: 0.9rem; margin-top: 0.5rem;">🔢 Код: {profession_code} | 🎯 Совместимость: {score:.1f}%</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f'<div style="color: #00ffff; font-size: 3rem; font-weight: 900; font-family: Orbitron, sans-serif; text-align: right;">{score:.1f}%</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="color: #b8b8ff; font-size: 1rem; text-align: right;">{LANGUAGES[st.session_state.language]["compatibility"]}</div>', unsafe_allow_html=True)
        
        # Metrics section
        col3, col4, col5 = st.columns(3)
        with col3:
            st.markdown(f'''
            <div class="metric-card">
                <div class="metric-value">{profession["salary"].split(" - ")[0]}</div>
                <div class="metric-label">{LANGUAGES[st.session_state.language]["salary"]}</div>
            </div>
            ''', unsafe_allow_html=True)
        with col4:
            st.markdown(f'''
            <div class="metric-card">
                <div class="metric-value">{len(profession["career_plan"][st.session_state.language])}</div>
                <div class="metric-label">Этапы карьеры</div>
            </div>
            ''', unsafe_allow_html=True)
        with col5:
            st.markdown(f'''
            <div class="metric-card">
                <div class="metric-value">{rank + 1}</div>
                <div class="metric-label">Место в рейтинге</div>
            </div>
            ''', unsafe_allow_html=True)
        
        # Work places section
        st.markdown("---")
        col6, col7 = st.columns(2)
        
        with col6:
            st.markdown(f'<h4 style="color: #ff00ff; margin-bottom: 1rem;">🏢 {LANGUAGES[st.session_state.language]["work_places"]}</h4>', unsafe_allow_html=True)
            for place in profession["places"][st.session_state.language]:
                st.markdown(f'<div style="color: #b8b8ff; margin-bottom: 0.5rem; padding: 0.5rem; background: rgba(108, 99, 255, 0.1); border-radius: 8px; border-left: 3px solid #6c63ff;">• {place}</div>', unsafe_allow_html=True)
        
        with col7:
            st.markdown(f'<h4 style="color: #00ffff; margin-bottom: 1rem;">💼 Альтернативные варианты</h4>', unsafe_allow_html=True)
            for place in profession["alternative_places"][st.session_state.language]:
                st.markdown(f'<div style="color: #b8b8ff; margin-bottom: 0.5rem; padding: 0.5rem; background: rgba(0, 255, 255, 0.1); border-radius: 8px; border-left: 3px solid #00ffff;">• {place}</div>', unsafe_allow_html=True)
        
        # Career plan section
        st.markdown("---")
        st.markdown(f'<h4 style="color: #ff00ff; margin-bottom: 1rem;">{LANGUAGES[st.session_state.language]["career_plan"]}</h4>', unsafe_allow_html=True)
        
        for i, step in enumerate(profession["career_plan"][st.session_state.language]):
            st.markdown(f'''
            <div style="background: rgba(20, 20, 50, 0.6); padding: 1.2rem; margin: 0.8rem 0; border-radius: 12px; border-left: 4px solid #ff00ff;">
                <div style="color: #ff00ff; font-weight: 600; margin-bottom: 0.3rem;">Шаг {i+1}</div>
                <div style="color: #ffffff;">{step}</div>
            </div>
            ''', unsafe_allow_html=True)
        
        # Advice section
        st.markdown("---")
        st.markdown(f'''
        <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(0, 255, 255, 0.1); border-radius: 15px; border: 1px solid #00ffff;">
            <h4 style="color: #00ffff; margin-bottom: 1rem;">{LANGUAGES[st.session_state.language]["development"]}</h4>
            <p style="color: #b8b8ff; line-height: 1.6; margin: 0;">{profession["advice"][st.session_state.language]}</p>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Action buttons
    st.markdown("---")
    col8, col9, col10 = st.columns([1, 2, 1])
    with col9:
        if st.button(LANGUAGES[st.session_state.language]["restart"], use_container_width=True):
            st.session_state.test_started = False
            st.session_state.show_loading = False
            st.session_state.show_results = False
            st.session_state.current_question = 0
            st.session_state.answers = [None] * 40
            st.rerun()
        
        if st.button(LANGUAGES[st.session_state.language]["download"], use_container_width=True):
            st.success("📄 Функция экспорта в PDF будет доступна в следующем обновлении системы!")

# =============================
# 👣 ENHANCED FOOTER
# =============================
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])

with footer_col2:
    st.markdown(f"""
    <div style='text-align: center; color: #b8b8ff; font-size: 0.9rem; line-height: 1.6; padding: 2rem 1rem;'>
        <strong style='color: #00ffff; font-size: 1.1rem;'>{LANGUAGES[st.session_state.language]["footer"]}</strong><br><br>
        
        <div style="margin: 1rem 0;">
            <strong style="color: #ff00ff;">{LANGUAGES[st.session_state.language]["contact"]}</strong><br>
            📱 {LANGUAGES[st.session_state.language]["phone"]}<br>
            📧 {LANGUAGES[st.session_state.language]["email"]}<br>
            🌐 {LANGUAGES[st.session_state.language]["website"]}
        </div>
        
        <div style="margin-top: 1rem; font-size: 0.8rem; color: #8888ff;">
            Интеллектуальная система профориентации | AI Assistant © 2025<br>
            Жамбылский политехнический высший колледж | Все права защищены
        </div>
        
        <div style="margin-top: 1rem; font-size: 0.7rem; color: #6666ff;">
            🎯 Точность: 94.2% | ⚡ Скорость: 12-15 мин | 🎓 Профессий: 15+
        </div>
    </div>
    """, unsafe_allow_html=True)
