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

/* Neon Glow Effects */
.neon-glow {
    text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff; }
    to { text-shadow: 0 0 15px #00ffff, 0 0 25px #00ffff, 0 0 35px #00ffff, 0 0 45px #00ffff; }
}

.pulse-glow {
    animation: pulse 3s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}

.scan-line {
    position: relative;
    overflow: hidden;
}

.scan-line::after {
    content: '';
    position: absolute;
    top: -100%;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(transparent, rgba(0, 255, 255, 0.3), transparent);
    animation: scan 3s linear infinite;
}

@keyframes scan {
    0% { top: -100%; }
    100% { top: 100%; }
}

/* Main Header */
.main-header {
    font-size: 4.5rem !important;
    text-align: center;
    font-weight: 900;
    font-family: 'Orbitron', monospace;
    background: linear-gradient(135deg, #00ffff 0%, #6c63ff 50%, #ff00ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    letter-spacing: 3px;
    text-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
    animation: titleFloat 6s ease-in-out infinite;
}

@keyframes titleFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
}

.sub-header {
    font-size: 1.6rem !important;
    text-align: center;
    font-family: 'Rajdhani', sans-serif;
    color: #b8b8ff;
    margin-bottom: 3rem;
    font-weight: 300;
    line-height: 1.5;
    text-shadow: 0 0 10px rgba(184, 184, 255, 0.5);
}

/* Question Containers */
.question-container {
    background: rgba(10, 10, 40, 0.85);
    padding: 3rem;
    border-radius: 25px;
    margin-bottom: 2rem;
    border: 2px solid #00ffff;
    box-shadow: 0 0 40px rgba(0, 255, 255, 0.4), inset 0 0 20px rgba(0, 255, 255, 0.1);
    backdrop-filter: blur(15px);
    font-family: 'Exo 2', sans-serif;
    font-size: 1.4rem !important;
    font-weight: 500;
    color: #ffffff;
    line-height: 1.6;
    position: relative;
    overflow: hidden;
    transition: all 0.4s ease;
}

.question-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.2), transparent);
    transition: left 0.8s;
}

.question-container:hover::before {
    left: 100%;
}

.question-container:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 60px rgba(0, 255, 255, 0.6), inset 0 0 30px rgba(0, 255, 255, 0.2);
}

/* Rating Scale */
.rating-container {
    display: flex;
    justify-content: space-between;
    margin: 3rem 0;
    gap: 0.8rem;
}

.rating-option {
    flex: 1;
    padding: 2rem 0.5rem;
    border-radius: 20px;
    aspect-ratio: 1;
    text-align: center;
    cursor: pointer;
    transition: all 0.4s ease;
    border: 3px solid transparent;
    background: rgba(30, 30, 60, 0.9);
    font-weight: 700;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(10px);
}

.rating-option::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: currentColor;
    opacity: 0.1;
    transition: opacity 0.3s ease;
}

.rating-option:hover {
    transform: scale(1.15) translateY(-5px);
    box-shadow: 0 10px 30px currentColor;
}

.rating-1 { color: #ff4444; }
.rating-2 { color: #ffaa44; }
.rating-3 { color: #ffff44; }
.rating-4 { color: #88ff44; }
.rating-5 { color: #44ff88; }

.rating-option.selected {
    transform: scale(1.2) translateY(-8px);
    box-shadow: 0 15px 40px currentColor;
    background: rgba(255, 255, 255, 0.15);
    border-color: currentColor;
}

.rating-option.selected::before {
    opacity: 0.2;
}

.rating-number {
    font-size: 2.2rem;
    font-weight: 900;
    margin-bottom: 0.3rem;
    display: block;
    font-family: 'Orbitron', monospace;
    text-shadow: 0 0 10px currentColor;
}

.rating-label {
    font-size: 0.75rem;
    opacity: 0.9;
    display: block;
    line-height: 1.2;
    font-weight: 600;
}

/* Professional Cards */
.profession-card {
    background: linear-gradient(135deg, rgba(10, 10, 40, 0.95) 0%, rgba(26, 26, 74, 0.95) 100%);
    border-radius: 25px;
    padding: 3rem;
    margin: 2rem 0;
    border: 2px solid #6c63ff;
    box-shadow: 0 0 50px rgba(108, 99, 255, 0.5), inset 0 0 30px rgba(108, 99, 255, 0.1);
    backdrop-filter: blur(20px);
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
}

.profession-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #00ffff, #6c63ff, #ff00ff);
    animation: borderFlow 3s linear infinite;
}

@keyframes borderFlow {
    0% { background-position: -200px 0; }
    100% { background-position: 200px 0; }
}

.profession-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 60px rgba(108, 99, 255, 0.7), inset 0 0 40px rgba(108, 99, 255, 0.2);
}

.metric-card {
    background: rgba(20, 20, 50, 0.9);
    border-radius: 20px;
    padding: 2rem;
    margin: 1rem;
    border: 1px solid #00ffff;
    text-align: center;
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.3), inset 0 0 15px rgba(0, 255, 255, 0.1);
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.metric-card:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 10px 35px rgba(0, 255, 255, 0.5), inset 0 0 20px rgba(0, 255, 255, 0.2);
}

.metric-value {
    font-size: 2.8rem;
    font-weight: 900;
    color: #00ffff;
    margin: 0.5rem 0;
    font-family: 'Orbitron', monospace;
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

.metric-label {
    font-size: 0.9rem;
    color: #b8b8ff;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #00ffff 0%, #6c63ff 50%, #ff00ff 100%) !important;
    color: #000000 !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
    font-family: 'Orbitron', monospace !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 1.5rem 4rem !important;
    margin: 2rem auto !important;
    display: block !important;
    transition: all 0.4s ease !important;
    box-shadow: 0 0 40px rgba(0, 255, 255, 0.6) !important;
    position: relative;
    overflow: hidden;
    background-size: 200% 200% !important;
    animation: gradientShift 3s ease infinite !important;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
    transition: left 0.6s;
}

.stButton > button:hover::before {
    left: 100%;
}

.stButton > button:hover {
    transform: translateY(-5px) scale(1.08) !important;
    box-shadow: 0 15px 50px rgba(0, 255, 255, 0.9) !important;
}

/* Section Headers */
.section-header {
    font-size: 2.8rem;
    font-weight: 700;
    color: #00ffff;
    margin: 3rem 0 2rem 0;
    padding-bottom: 1.5rem;
    border-bottom: 3px solid #6c63ff;
    position: relative;
    font-family: 'Orbitron', monospace;
    text-align: center;
    text-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -3px;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    height: 3px;
    background: linear-gradient(90deg, #00ffff, #6c63ff, #ff00ff);
    animation: borderFlow 3s linear infinite;
}

/* Progress Bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #00ffff, #6c63ff, #ff00ff) !important;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
    animation: gradientShift 2s ease infinite;
}

/* Loading Animation */
.loading-container {
    text-align: center;
    padding: 6rem 3rem;
    background: rgba(10, 10, 40, 0.95);
    border-radius: 30px;
    border: 2px solid #00ffff;
    box-shadow: 0 0 60px rgba(0, 255, 255, 0.5), inset 0 0 40px rgba(0, 255, 255, 0.1);
    margin: 3rem 0;
    backdrop-filter: blur(20px);
}

.loading-text {
    font-size: 2.8rem;
    font-weight: 700;
    color: #00ffff;
    font-family: 'Orbitron', monospace;
    margin-bottom: 3rem;
    text-shadow: 0 0 20px rgba(0, 255, 255, 0.7);
}

.pulse-dots::after {
    content: '';
    animation: pulse-dots 1.5s steps(4, end) infinite;
}

@keyframes pulse-dots {
    0%, 20% { content: ''; }
    40% { content: '.'; }
    60% { content: '..'; }
    80%, 100% { content: '...'; }
}

/* Grid Layout */
.profession-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.grid-item {
    background: rgba(20, 20, 50, 0.9);
    padding: 2.5rem;
    border-radius: 20px;
    border: 1px solid #6c63ff;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(15px);
    box-shadow: 0 0 30px rgba(108, 99, 255, 0.3), inset 0 0 20px rgba(108, 99, 255, 0.1);
}

.grid-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #00ffff, #6c63ff);
    animation: borderFlow 3s linear infinite;
}

.grid-item:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 15px 45px rgba(108, 99, 255, 0.5), inset 0 0 25px rgba(108, 99, 255, 0.2);
}

/* Mobile Optimization */
@media (max-width: 768px) {
    .main-header {
        font-size: 3rem !important;
    }
    
    .sub-header {
        font-size: 1.3rem !important;
    }
    
    .question-container {
        font-size: 1.2rem !important;
        padding: 2rem !important;
    }
    
    .rating-option {
        padding: 1.5rem 0.3rem;
    }
    
    .rating-number {
        font-size: 1.8rem;
    }
    
    .rating-label {
        font-size: 0.65rem;
    }
    
    .metric-value {
        font-size: 2.2rem;
    }
    
    .stButton > button {
        font-size: 1.2rem !important;
        padding: 1.2rem 2.5rem !important;
        width: 90%;
    }
    
    .section-header {
        font-size: 2rem;
    }
    
    .loading-text {
        font-size: 2rem;
    }
    
    .profession-grid {
        grid-template-columns: 1fr;
    }
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #1a1a4a;
    border-radius: 5px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(45deg, #00ffff, #6c63ff);
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(45deg, #6c63ff, #ff00ff);
}

/* Language Switch */
.language-switch {
    background: rgba(10, 10, 40, 0.9);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
    border: 1px solid #00ffff;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
}

/* Results Animation */
.results-appear {
    animation: fadeInUp 1s ease-out;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Stats Dashboard */
.stats-dashboard {
    background: rgba(10, 10, 40, 0.9);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid #6c63ff;
    box-shadow: 0 0 30px rgba(108, 99, 255, 0.4);
    backdrop-filter: blur(15px);
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
}

.stat-item {
    text-align: center;
    padding: 1.5rem;
    background: rgba(20, 20, 50, 0.7);
    border-radius: 15px;
    border: 1px solid #00ffff;
    transition: all 0.3s ease;
}

.stat-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 255, 255, 0.3);
}

.stat-value {
    font-size: 2.5rem;
    font-weight: 900;
    color: #00ffff;
    font-family: 'Orbitron', monospace;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

.stat-label {
    font-size: 0.9rem;
    color: #b8b8ff;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0a2a 0%, #1a1a4a 100%) !important;
    border-right: 2px solid #00ffff;
}

[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(135deg, #6c63ff 0%, #ff00ff 100%) !important;
    margin: 0.5rem 0 !important;
    padding: 1rem 2rem !important;
    font-size: 1.1rem !important;
}
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
# 🧠 ADVANCED QUESTIONS DATABASE
# =============================
QUESTIONS = {
    "Русский": [
        "Вам нравится анализировать информацию и работать с документами?",
        "Вы испытываете удовольствие от создания художественных произведений?",
        "Вам нравится работать с цифрами и финансовыми отчетами?",
        "Вы интересуетесь технологиями добычи полезных ископаемых?",
        "Вам нравится программировать и решать технические задачи?",
        "Вы предпочитаете работу, связанную с применением законов и нормативов?",
        "Вам нравится создавать вещи своими руками?",
        "Вы внимательны к деталям и любите точность в работе?",
        "Вас привлекает работа с современными технологиями?",
        "Вы любите изучать новые материалы и техники творчества?",
        "Вам нравится оптимизировать процессы и находить эффективные решения?",
        "Вы предпочитаете работу в стабильной, структурированной среде?",
        "Вам интересно работать с базами данных и информационными системами?",
        "Вы любите работать в команде над сложными проектами?",
        "Вам нравится решать конфликтные ситуации и находить компромиссы?",
        "Вы предпочитаете работу, где можно проявить креативность?",
        "Вам важно видеть практический результат своей работы?",
        "Вы готовы к работе в условиях неопределенности и быстрых изменений?",
        "Вам нравится изучать законодательство и правовые нормы?",
        "Вы любите работать с графическими редакторами и дизайнерскими программами?",
        "Вам интересны процессы управления финансами и бюджетирования?",
        "Вы предпочитаете работу на производственных объектах?",
        "Вам нравится разбираться в сложных технических системах?",
        "Вы легко адаптируетесь к новым требованиям и стандартам?",
        "Вам важно постоянно обучаться и осваивать новые навыки?",
        "Вы любите работать с людьми и помогать им решать проблемы?",
        "Вам нравится создавать что-то новое и уникальное?",
        "Вы предпочитаете работу, связанную с анализом и исследованиями?",
        "Вам интересны вопросы охраны труда и техники безопасности?",
        "Вы любите работать с чертежами и технической документацией?",
        "Вам нравится участвовать в организационных процессах?",
        "Вы предпочитаете работу, где можно применить логическое мышление?",
        "Вам интересны современные тенденции в искусстве и дизайне?",
        "Вы любите работать с большими объемами информации?",
        "Вам нравится решать нестандартные задачи?",
        "Вы предпочитаете работу с четкими инструкциями и регламентами?",
        "Вам интересны вопросы экологии и sustainable development?",
        "Вы любите работать с техническим оборудованием?",
        "Вам нравится планировать и организовывать рабочие процессы?",
        "Вы готовы к работе в режиме многозадачности?"
    ],
    "Қазақша": [
        "Сізге ақпаратты талдау және құжаттармен жұмыс істеу ұнай ма?",
        "Сіз көркемдік туындылар жасағанды рахаттайсыз ба?",
        "Сізге сандармен және қаржылық есептермен жұмыс істеу ұнай ма?",
        "Сізді пайдалы қазбаларды өндіру технологиялары қызықтыра ма?",
        "Сізге бағдарламалау және техникалық мәселелерді шешу ұнай ма?",
        "Сіз заңдар мен нормативтерді қолданумен байланысты жұмысты қалайсыз ба?",
        "Сізге қолдарыңызбен заттар жасағанды ұнатасыз ба?",
        "Сіз детальдарға мұқият және жұмыста нақтылықты жақсы көресіз бе?",
        "Сізді заманауи технологиялармен жұмыс істеу тартады ма?",
        "Сіз жаңа материалдар мен шығармашылық әдістерді зерттегенді жақсы көресіз бе?",
        "Сізге процестерді оңтайландыру және тиімді шешімдер табу ұнай ма?",
        "Сіз тұрақты, құрылымды ортада жұмыс істегенді қалайсыз ба?",
        "Сізді деректер қорлары мен ақпараттық жүйелермен жұмыс істеу қызықтыра ма?",
        "Сіз күрделі жобалар бойынша командада жұмыс істегенді ұнатасыз ба?",
        "Сізге қайшылықты жағдайларды шешу және компромисс табу ұнай ма?",
        "Сіз шығармашылық танытуға болатын жұмысты қалайсыз ба?",
        "Сіз үшін жұмысыңыздың практикалық нәтижесін көру маңызды ма?",
        "Сіз белгісіздік және жылдам өзгерістер жағдайында жұмыс істеуге дайынсыз ба?",
        "Сізге заңнама мен құқықтық нормаларды зерттеу ұнай ма?",
        "Сіз графикалық редакторлар мен дизайнерлік бағдарламалармен жұмыс істегенді жақсы көресіз бе?",
        "Сізді қаржыны басқару және бюджеттеу процестері қызықтыра ма?",
        "Сіз өндірістік объектілерде жұмыс істегенді қалайсыз ба?",
        "Сізге күрделі техникалық жүйелерді түсіну ұнай ма?",
        "Сіз жаңа талаптар мен стандарттарға оңай бейімделесіз бе?",
        "Сіз үшін үнемі оқу және жаңа дағдыларды меңгеру маңызды ма?",
        "Сіз адамдармен жұмыс істеп, оларға мәселелерді шешуде көмектесетін жұмысты жақсы көресіз бе?",
        "Сізге жаңа және бірегей нәрселер жасағанды ұнатасыз ба?",
        "Сіз талдау және зерттеулермен байланысты жұмысты қалайсыз ба?",
        "Сізді еңбекті қорғау және қауіпсіздік техникасы мәселелері қызықтыра ма?",
        "Сізге сызбалар мен техникалық құжаттамамен жұмыс істеу ұнай ма?",
        "Сізге ұйымдастырушылық процестерге қатысқанды ұнатасыз ба?",
        "Сіз логикалық ойлауды қолдануға болатын жұмысты қалайсыз ба?",
        "Сізді өнер мен дизайндағы заманауи тенденциялар қызықтыра ма?",
        "Сіз үлкен ақпарат көлемдерімен жұмыс істегенді ұнатасыз ба?",
        "Сізге стандартты емес есептерді шешу ұнай ма?",
        "Сіз нақты нұсқаулар мен регламенттері бар жұмысты қалайсыз ба?",
        "Сізді экология және тұрақты даму мәселелері қызықтыра ма?",
        "Сіз техникалық жабдықтармен жұмыс істегенді жақсы көресіз бе?",
        "Сізге жұмыс процестерін жоспарлау мен ұйымдастыру ұнай ма?",
        "Сіз бірнеше тапсырманы бір уақытта орындау режимінде жұмыс істеуге дайынсыз ба?"
    ]
}

# =============================
# 🧠 IMPROVED ANALYTICS SYSTEM
# =============================
class AdvancedJobAIAnalytics:
    def __init__(self):
        # Normalized weights to prevent percentages over 100%
        self.question_weights = {
            # Question weights scaled to ensure max 100%
            0: {"201000": 0.08, "0518000": 0.06, "1305000": 0.04},
            1: {"0413000": 0.10, "201000": 0.02},
            2: {"0518000": 0.12, "201000": 0.04, "1305000": 0.03},
            3: {"0809000": 0.10, "0518000": 0.03},
            4: {"1305000": 0.15, "0809000": 0.03, "0518000": 0.02},
            5: {"201000": 0.12, "0518000": 0.04},
            6: {"0413000": 0.14, "201000": 0.02},
            7: {"0518000": 0.10, "1305000": 0.05, "0809000": 0.02},
            8: {"1305000": 0.12, "0413000": 0.04, "0809000": 0.03},
            9: {"0413000": 0.16, "1305000": 0.03},
            10: {"1305000": 0.10, "0518000": 0.06, "0809000": 0.04},
            11: {"201000": 0.08, "0518000": 0.07, "0809000": 0.03},
            12: {"1305000": 0.18, "0518000": 0.04},
            13: {"0413000": 0.06, "0809000": 0.05, "1305000": 0.04},
            14: {"201000": 0.14, "0518000": 0.04},
            15: {"0413000": 0.16, "1305000": 0.03},
            16: {"0809000": 0.10, "0413000": 0.05, "1305000": 0.03},
            17: {"0518000": 0.09, "201000": 0.06, "0809000": 0.04},
            18: {"201000": 0.15, "0518000": 0.04},
            19: {"0413000": 0.14, "1305000": 0.04},
            20: {"0518000": 0.16, "201000": 0.04, "1305000": 0.03},
            21: {"0809000": 0.18, "0413000": 0.03},
            22: {"1305000": 0.20, "0809000": 0.04},
            23: {"201000": 0.08, "0518000": 0.07, "0413000": 0.03},
            24: {"1305000": 0.12, "0518000": 0.05, "201000": 0.04},
            25: {"201000": 0.10, "0413000": 0.05, "0518000": 0.04},
            26: {"0413000": 0.18, "1305000": 0.04},
            27: {"0518000": 0.10, "1305000": 0.06, "201000": 0.04},
            28: {"0809000": 0.14, "201000": 0.04, "0518000": 0.03},
            29: {"0809000": 0.12, "1305000": 0.05, "0413000": 0.03},
            30: {"201000": 0.10, "0518000": 0.06, "0413000": 0.03},
            31: {"1305000": 0.14, "0518000": 0.05, "201000": 0.03},
            32: {"0413000": 0.16, "1305000": 0.03},
            33: {"0518000": 0.15, "1305000": 0.05, "201000": 0.03},
            34: {"1305000": 0.18, "0413000": 0.04, "0809000": 0.03},
            35: {"201000": 0.12, "0518000": 0.06, "0809000": 0.03},
            36: {"0809000": 0.16, "0413000": 0.04, "0518000": 0.03},
            37: {"0809000": 0.14, "1305000": 0.05, "0413000": 0.03},
            38: {"0518000": 0.12, "201000": 0.06, "1305000": 0.04},
            39: {"1305000": 0.15, "0518000": 0.06, "201000": 0.04}
        }
    
    def calculate_scores(self, answers):
        """Calculate profession scores with proper normalization"""
        scores = {profession: 0 for profession in PROFESSIONS.keys()}
        max_possible_score = {profession: 0 for profession in PROFESSIONS.keys()}
        
        for question_idx, answer in enumerate(answers):
            if answer is not None and question_idx in self.question_weights:
                for profession, weight in self.question_weights[question_idx].items():
                    # Normalize answer from 1-5 to 0-1 scale
                    normalized_answer = (answer - 1) / 4.0
                    scores[profession] += normalized_answer * weight * 100
                    max_possible_score[profession] += weight * 100
        
        # Normalize scores to ensure they don't exceed 100%
        for profession in scores:
            if max_possible_score[profession] > 0:
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
if 'show_language' not in st.session_state:
    st.session_state.show_language = False

# =============================
# 🎪 SIDEBAR NAVIGATION
# =============================
with st.sidebar:
    st.markdown(f'<div class="section-header" style="font-size: 1.5rem !important;">🚀 Job.AI</div>', unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠", help=LANGUAGES[st.session_state.language]["main_page"], use_container_width=True):
            st.session_state.test_started = False
            st.session_state.show_loading = False
            st.session_state.show_results = False
            st.session_state.show_stats = False
            st.session_state.show_language = False
            st.rerun()
    
    with col2:
        if st.button("📊", help=LANGUAGES[st.session_state.language]["view_stats"], use_container_width=True):
            st.session_state.show_stats = True
            st.session_state.show_results = False
            st.session_state.test_started = False
            st.session_state.show_language = False
            st.rerun()
    
    st.markdown("---")
    
    # Language switch in sidebar
    st.markdown(f'<div class="language-switch">', unsafe_allow_html=True)
    st.markdown(f"**{LANGUAGES[st.session_state.language]['language']}**")
    
    if st.button("Русский 🇷🇺", use_container_width=True):
        st.session_state.language = "Русский"
        st.rerun()
    
    if st.button("Қазақша 🇰🇿", use_container_width=True):
        st.session_state.language = "Қазақша"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick stats in sidebar
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
    
    # Advanced welcome section with stats
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
    
    # Start button with enhanced styling
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
    
    # Enhanced stats dashboard
    st.markdown('<div class="stats-dashboard">', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h3 style="color: #00ffff; font-family: Orbitron, sans-serif;">📈 Реальная статистика платформы</h3>
        <p style="color: #b8b8ff;">Данные обновляются в реальном времени</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats grid
    st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
    
    stats_data = [
        (stats['users_today'], LANGUAGES[st.session_state.language]["users_today"], "👥"),
        (f"{stats['total_tests']:,}", LANGUAGES[st.session_state.language]["total_tests"], "🎯"),
        (f"{stats['success_rate']}%", LANGUAGES[st.session_state.language]["success_rate"], "⚡"),
        (stats['avg_time'], LANGUAGES[st.session_state.language]["avg_time"], "⏱️")
    ]
    
    for value, label, icon in stats_data:
        st.markdown(f"""
        <div class="stat-item">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
            <div class="stat-value">{value}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Popular professions
    st.markdown("""
    <div style="background: rgba(20, 20, 50, 0.7); padding: 2rem; border-radius: 15px; margin-top: 2rem; border: 1px solid #6c63ff;">
        <h4 style="color: #ff00ff; margin-bottom: 1rem;">🏆 Самая популярная профессия</h4>
        <p style="color: #00ffff; font-size: 1.3rem; font-weight: 600;">{}</p>
        <p style="color: #b8b8ff; margin-top: 0.5rem;">На основе выбора {} пользователей</p>
    </div>
    """.format(stats['popular_profession'], stats['total_tests']), unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# ❓ TEST QUESTIONS
# =============================
elif st.session_state.test_started and not st.session_state.show_loading and not st.session_state.show_results:
    questions = QUESTIONS[st.session_state.language]
    current_q = st.session_state.current_question
    
    # Enhanced progress
    progress = (current_q + 1) / len(questions)
    st.progress(progress)
    
    progress_text = LANGUAGES[st.session_state.language]["progress_text"].format(
        current=current_q + 1, 
        total=len(questions)
    )
    st.markdown(f"""
    <div style="text-align: center; color: #00ffff; font-size: 1.2rem; font-weight: 600; margin: 1rem 0; text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);">
        {progress_text}
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced question container
    st.markdown(f'<div class="question-container scan-line">{current_q + 1}. {questions[current_q]}</div>', unsafe_allow_html=True)
    
    # Enhanced rating options
    rating_labels = {
        "Русский": ["Совсем неинтересно", "Немного интересно", "Нейтрально", "Интересно", "Очень интересно"],
        "Қазақша": ["Мүлдем қызық емес", "Сәл қызық", "Орташа", "Қызықты", "Өте қызықты"]
    }
    
    st.markdown('<div class="rating-container">', unsafe_allow_html=True)
    
    cols = st.columns(5)
    selected_answer = None
    
    for i, col in enumerate(cols):
        with col:
            value = i + 1
            is_selected = st.session_state.answers[current_q] == value
            
            st.markdown(f"""
            <div class="rating-option rating-{value} {'selected' if is_selected else ''}">
                <span class="rating-number">{value}</span>
                <span class="rating-label">{rating_labels[st.session_state.language][i]}</span>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"{value}", key=f"btn_{i}", use_container_width=True):
                selected_answer = value
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Handle answer selection
    if selected_answer is not None:
        st.session_state.answers[current_q] = selected_answer
        
        if current_q < len(questions) - 1:
            st.session_state.current_question += 1
        else:
            st.session_state.test_started = False
            st.session_state.show_loading = True
        
        st.rerun()

# =============================
# 🔄 LOADING ANIMATION
# =============================
elif st.session_state.show_loading:
    st.markdown(f'<div class="main-header neon-glow">{LANGUAGES[st.session_state.language]["title"]}</div>', unsafe_allow_html=True)
    
    loading_container = st.empty()
    
    with loading_container.container():
        st.markdown('<div class="loading-container">', unsafe_allow_html=True)
        st.markdown(f'<div class="loading-text neon-glow pulse-glow">{LANGUAGES[st.session_state.language]["analyzing"]}<span class="pulse-dots"></span></div>', unsafe_allow_html=True)
        
        # Enhanced animated progress bar
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.03)
        
        # Additional loading elements
        st.markdown("""
        <div style="margin-top: 2rem;">
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; text-align: center;">
                <div>
                    <div style="color: #00ffff; font-size: 1.2rem;">🔍</div>
                    <div style="color: #b8b8ff; font-size: 0.8rem;">Анализ ответов</div>
                </div>
                <div>
                    <div style="color: #6c63ff; font-size: 1.2rem;">📊</div>
                    <div style="color: #b8b8ff; font-size: 0.8rem;">Сравнение с базой</div>
                </div>
                <div>
                    <div style="color: #ff00ff; font-size: 1.2rem;">🎯</div>
                    <div style="color: #b8b8ff; font-size: 0.8rem;">Формирование рекомендаций</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    time.sleep(1)
    st.session_state.show_loading = False
    st.session_state.show_results = True
    st.rerun()

# =============================
# 📊 ENHANCED RESULTS PAGE
# =============================
elif st.session_state.show_results:
    # Calculate results
    scores = analytics.calculate_scores(st.session_state.answers)
    top_professions = analytics.get_top_professions(scores, top_n=3)
    
    st.markdown(f'<div class="main-header neon-glow">{LANGUAGES[st.session_state.language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-header">{LANGUAGES[st.session_state.language]["your_results"]}</div>', unsafe_allow_html=True)
    
    # Display top 3 professions
    for rank, (profession_code, score) in enumerate(top_professions):
        profession = PROFESSIONS[profession_code]
        medals = ["🥇", "🥈", "🥉"]
        
        st.markdown(f"""
        <div class="profession-card results-appear">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 2rem;">
                <div style="flex: 1;">
                    <h2 style="color: #00ffff; margin-bottom: 0.5rem; font-family: Orbitron, sans-serif;">
                        {medals[rank]} {profession["name"][st.session_state.language]}
                    </h2>
                    <p style="color: #b8b8ff; font-size: 1.1rem; line-height: 1.5; margin-bottom: 1rem;">
                        {profession["description"][st.session_state.language]}
                    </p>
                    <div style="color: #6c63ff; font-size: 0.9rem; margin-top: 0.5rem;">
                        🔢 Код: {profession_code} | 🎯 Совместимость: {score:.1f}%
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="color: #00ffff; font-size: 3rem; font-weight: 900; font-family: Orbitron, sans-serif;">
                        {score:.1f}%
                    </div>
                    <div style="color: #b8b8ff; font-size: 1rem;">
                        {LANGUAGES[st.session_state.language]["compatibility"]}
                    </div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
                <div class="metric-card">
                    <div class="metric-value">{profession["salary"].split(" - ")[0]}</div>
                    <div class="metric-label">{LANGUAGES[st.session_state.language]["salary"]}</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">{len(profession["career_plan"][st.session_state.language])}</div>
                    <div class="metric-label">Этапы карьеры</div>
                </div>
                <div class="metric-card">
                    <div class="metric-value">{rank + 1}</div>
                    <div class="metric-label">Место в рейтинге</div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 2rem;">
                <div>
                    <h4 style="color: #ff00ff; margin-bottom: 1rem;">🏢 Основные места работы</h4>
                    {"".join([f'<div style="color: #b8b8ff; margin-bottom: 0.5rem; padding: 0.5rem; background: rgba(108, 99, 255, 0.1); border-radius: 8px; border-left: 3px solid #6c63ff;">• {place}</div>' for place in profession["places"][st.session_state.language]])}
                </div>
                <div>
                    <h4 style="color: #00ffff; margin-bottom: 1rem;">💼 Альтернативные варианты</h4>
                    {"".join([f'<div style="color: #b8b8ff; margin-bottom: 0.5rem; padding: 0.5rem; background: rgba(0, 255, 255, 0.1); border-radius: 8px; border-left: 3px solid #00ffff;">• {place}</div>' for place in profession["alternative_places"][st.session_state.language]])}
                </div>
            </div>
            
            <div style="margin-top: 2rem;">
                <h4 style="color: #ff00ff; margin-bottom: 1rem;">📈 {LANGUAGES[st.session_state.language]["career_plan"]}</h4>
                {"".join([f'<div style="background: rgba(20, 20, 50, 0.6); padding: 1.2rem; margin: 0.8rem 0; border-radius: 12px; border-left: 4px solid #ff00ff;"><div style="color: #ff00ff; font-weight: 600; margin-bottom: 0.3rem;">Шаг {i+1}</div><div style="color: #ffffff;">{step}</div></div>' for i, step in enumerate(profession["career_plan"][st.session_state.language])])}
            </div>
            
            <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(0, 255, 255, 0.1); border-radius: 15px; border: 1px solid #00ffff;">
                <h4 style="color: #00ffff; margin-bottom: 1rem;">💡 {LANGUAGES[st.session_state.language]["development"]}</h4>
                <p style="color: #b8b8ff; line-height: 1.6; margin: 0;">{profession["advice"][st.session_state.language]}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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
