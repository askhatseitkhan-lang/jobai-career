import streamlit as st
import time
import random
from datetime import datetime

# =============================
# 🎨 FUTURISTIC STYLING
# =============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Exo+2:wght@300;400;500;600;700&display=swap');

/* Main Futuristic Theme */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0a2a 0%, #1a1a4a 30%, #2d1a4a 70%, #4a1a6a 100%);
    color: #ffffff;
    font-family: 'Exo 2', sans-serif;
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
    background: linear-gradient(transparent, rgba(0, 255, 255, 0.4), transparent);
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
    letter-spacing: 2px;
    text-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
}

.sub-header {
    font-size: 1.6rem !important;
    text-align: center;
    font-family: 'Exo 2', sans-serif;
    color: #b8b8ff;
    margin-bottom: 3rem;
    font-weight: 300;
    line-height: 1.5;
}

/* Question Containers */
.question-container {
    background: rgba(10, 10, 40, 0.8);
    padding: 3rem;
    border-radius: 25px;
    margin-bottom: 2rem;
    border: 2px solid #00ffff;
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    font-family: 'Exo 2', sans-serif;
    font-size: 1.4rem !important;
    font-weight: 500;
    color: #ffffff;
    line-height: 1.6;
    position: relative;
    overflow: hidden;
}

.question-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 255, 0.1), transparent);
    transition: left 0.6s;
}

.question-container:hover::before {
    left: 100%;
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
    border-radius: 50%;
    aspect-ratio: 1;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 3px solid transparent;
    background: rgba(30, 30, 60, 0.8);
    font-weight: 700;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.rating-option:hover {
    transform: scale(1.1);
    box-shadow: 0 0 20px currentColor;
}

.rating-1 { color: #ff4444; border-color: #ff4444; }
.rating-2 { color: #ffaa44; border-color: #ffaa44; }
.rating-3 { color: #ffff44; border-color: #ffff44; }
.rating-4 { color: #88ff44; border-color: #88ff44; }
.rating-5 { color: #44ff88; border-color: #44ff88; }

.rating-option.selected {
    transform: scale(1.15);
    box-shadow: 0 0 30px currentColor;
    background: rgba(255, 255, 255, 0.1);
}

.rating-number {
    font-size: 2rem;
    font-weight: 900;
    margin-bottom: 0.3rem;
    display: block;
    font-family: 'Orbitron', monospace;
}

.rating-label {
    font-size: 0.7rem;
    opacity: 0.9;
    display: block;
    line-height: 1.2;
}

/* Professional Cards */
.profession-card {
    background: linear-gradient(135deg, rgba(10, 10, 40, 0.9) 0%, rgba(26, 26, 74, 0.9) 100%);
    border-radius: 25px;
    padding: 3rem;
    margin: 2rem 0;
    border: 2px solid #6c63ff;
    box-shadow: 0 0 40px rgba(108, 99, 255, 0.4);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
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
}

.profession-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 50px rgba(108, 99, 255, 0.6);
}

.metric-card {
    background: rgba(20, 20, 50, 0.8);
    border-radius: 20px;
    padding: 2rem;
    margin: 1rem;
    border: 1px solid #00ffff;
    text-align: center;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.4);
}

.metric-value {
    font-size: 2.8rem;
    font-weight: 900;
    color: #00ffff;
    margin: 0.5rem 0;
    font-family: 'Orbitron', monospace;
}

.metric-label {
    font-size: 0.9rem;
    color: #b8b8ff;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #00ffff 0%, #6c63ff 100%) !important;
    color: #000000 !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
    font-family: 'Orbitron', monospace !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 1.5rem 4rem !important;
    margin: 2rem auto !important;
    display: block !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.5) !important;
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
    transition: left 0.5s;
}

.stButton > button:hover::before {
    left: 100%;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.05) !important;
    box-shadow: 0 0 40px rgba(0, 255, 255, 0.8) !important;
}

/* Section Headers */
.section-header {
    font-size: 2.5rem;
    font-weight: 700;
    color: #00ffff;
    margin: 3rem 0 2rem 0;
    padding-bottom: 1rem;
    border-bottom: 3px solid #6c63ff;
    position: relative;
    font-family: 'Orbitron', monospace;
    text-align: center;
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
}

/* Progress Bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #00ffff, #6c63ff, #ff00ff) !important;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

/* Loading Animation */
.loading-container {
    text-align: center;
    padding: 5rem 2rem;
    background: rgba(10, 10, 40, 0.9);
    border-radius: 25px;
    border: 2px solid #00ffff;
    box-shadow: 0 0 50px rgba(0, 255, 255, 0.3);
    margin: 3rem 0;
}

.loading-text {
    font-size: 2.5rem;
    font-weight: 700;
    color: #00ffff;
    font-family: 'Orbitron', monospace;
    margin-bottom: 2rem;
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
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.grid-item {
    background: rgba(20, 20, 50, 0.8);
    padding: 2rem;
    border-radius: 20px;
    border: 1px solid #6c63ff;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.grid-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #00ffff, #6c63ff);
}

.grid-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(108, 99, 255, 0.3);
}

/* Mobile Optimization */
@media (max-width: 768px) {
    .main-header {
        font-size: 2.8rem !important;
    }
    
    .sub-header {
        font-size: 1.2rem !important;
    }
    
    .question-container {
        font-size: 1.2rem !important;
        padding: 2rem !important;
    }
    
    .rating-option {
        padding: 1.5rem 0.3rem;
    }
    
    .rating-number {
        font-size: 1.5rem;
    }
    
    .rating-label {
        font-size: 0.6rem;
    }
    
    .metric-value {
        font-size: 2rem;
    }
    
    .stButton > button {
        font-size: 1.2rem !important;
        padding: 1.2rem 2.5rem !important;
        width: 90%;
    }
    
    .section-header {
        font-size: 1.8rem;
    }
    
    .loading-text {
        font-size: 1.8rem;
    }
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #1a1a4a;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(#00ffff, #6c63ff);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(#6c63ff, #ff00ff);
}

/* Language Switch */
.language-switch {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
}

/* Results Animation */
.results-appear {
    animation: fadeInUp 0.8s ease-out;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

# =============================
# 🌍 LANGUAGE SYSTEM
# =============================
LANGUAGES = {
    "Русский": {
        "title": "Job.AI",
        "subtitle": "Профориентационный тест Жамбылского политехнического высшего колледжа",
        "start_test": "🚀 НАЧАТЬ ТЕСТИРОВАНИЕ",
        "progress_text": "📊 Прогресс: {current}/{total} вопросов",
        "analyzing": "Job.AI анализирует ваши ответы",
        "your_results": "🎯 Ваши результаты",
        "compatibility": "Совместимость",
        "salary": "Средняя зарплата",
        "career_plan": "Карьерный план",
        "work_places": "Места работы", 
        "development": "Рекомендации по развитию",
        "restart": "🔄 Пройти тест заново",
        "download": "📄 Скачать результаты PDF",
        "footer": "Job.AI © 2025 | Жамбылский политехнический высший колледж",
        "contact": "📞 Контакты",
        "phone": "+7 (776) 668 0880",
        "email": "support@jobai-career.streamlit.app",
        "website": "https://jobai-career.streamlit.app"
    },
    "Қазақша": {
        "title": "Job.AI", 
        "subtitle": "Жамбыл политехникалық жоғарғы колледжінің кәсіптік бағдар тесті",
        "start_test": "🚀 ТЕСТІЛЕУДІ БАСТАУ",
        "progress_text": "📊 Прогресс: {current}/{total} сұрақ",
        "analyzing": "Job.AI сіздің жауаптарыңызды талдауда",
        "your_results": "🎯 Сіздің нәтижелеріңіз",
        "compatibility": "Сәйкестік",
        "salary": "Орташа жалақы",
        "career_plan": "Мансаптық жоспар",
        "work_places": "Жұмыс орындары",
        "development": "Даму бойынша ұсыныстар",
        "restart": "🔄 Тесті қайта өту",
        "download": "📄 Нәтижелерді жүктеу PDF",
        "footer": "Job.AI © 2025 | Жамбыл политехникалық жоғарғы колледжі",
        "contact": "📞 Байланыс",
        "phone": "+7 (776) 668 0880", 
        "email": "support@jobai-career.streamlit.app",
        "website": "https://jobai-career.streamlit.app"
    }
}

# =============================
# 🎯 PROFESSIONS DATABASE
# =============================
PROFESSIONS = {
    "1305000": {
        "name": {
            "Русский": "🤖 Информационные системы",
            "Қазақша": "🤖 Ақпараттық жүйелер"
        },
        "description": {
            "Русский": "Разработка и обслуживание программного обеспечения, баз данных и IT-инфраструктуры",
            "Қазақша": "Бағдарламалық жасақтаманы, деректер қорларын және IT-инфрақұрылымды әзірлеу және қызмет көрсету"
        },
        "salary": "350,000 - 900,000 ₸",
        "places": {
            "Русский": "IT-компании, банки, госучреждения, стартапы",
            "Қазақша": "IT-компаниялар, банктер, мемлекеттік мекемелер, стартаптар"
        },
        "career_plan": {
            "Русский": [
                "🎓 Получить диплом колледжа",
                "💻 Освоить Python/Java и фреймворки", 
                "🚀 Начать как Junior-разработчик",
                "📈 Стать Senior-разработчиком за 3-4 года",
                "👨‍💼 Перейти на позицию Team Lead"
            ],
            "Қазақша": [
                "🎓 Колледждің дипломын алу",
                "💻 Python/Java және фреймворктерді меңгеру",
                "🚀 Junior-әзірлеуші ретінде бастау",
                "📈 3-4 жыл ішінде Senior-әзірлеуші болу",
                "👨‍💼 Team Lead лауазымына өту"
            ]
        },
        "advice": {
            "Русский": "Изучите Python, SQL, веб-разработку и искусственный интеллект. Практикуйтесь на реальных проектах.",
            "Қазақша": "Python, SQL, веб-әзірлеу және жасанды интеллекті үйреніңіз. Нақты жобалар бойынша тәжірибе жинаңыз."
        }
    },
    "0809000": {
        "name": {
            "Русский": "🛢️ Нефтегазовое дело", 
            "Қазақша": "🛢️ Мұнай-газ ісі"
        },
        "description": {
            "Русский": "Добыча, переработка и транспортировка нефти и газа",
            "Қазақша": "Мұнай мен газды өндіру, өңдеу және тасымалдау"
        },
        "salary": "400,000 - 1,200,000 ₸",
        "places": {
            "Русский": "Нефтегазовые компании, сервисные компании, НИИ",
            "Қазақша": "Мұнай-газ компаниялары, сервистік компаниялар, ғылыми-зерттеу институттары"
        },
        "career_plan": {
            "Русский": [
                "🎓 Окончить колледж по специальности",
                "🛢️ Устроиться оператором ДНГ",
                "📚 Получить высшее образование",
                "👨‍🔧 Стать инженером-технологом", 
                "👨‍💼 Вырасти до руководителя смены"
            ],
            "Қазақша": [
                "🎓 Мамандық бойынша колледжді бітіру",
                "🛢️ МГО операторы болып жұмысқа орналасу",
                "📚 Жоғары білім алу",
                "👨‍🔧 Инженер-технолог болу",
                "👨‍💼 Ауысым басшысы деңгейіне көтерілу"
            ]
        },
        "advice": {
            "Русский": "Изучите процессы добычи, оборудование и технику безопасности. Развивайте аналитическое мышление.",
            "Қазақша": "Өндіру процестерін, жабдықтар мен қауіпсіздік техникасын үйреніңіз. Аналитикалық ойлау дағдыларын дамытыңыз."
        }
    },
    "1401000": {
        "name": {
            "Русский": "🏗️ Строительство",
            "Қазақша": "🏗️ Құрылыс"
        },
        "description": {
            "Русский": "Проектирование, строительство и эксплуатация зданий и сооружений",
            "Қазақша": "Ғимараттар мен құрылымдарды жобалау, салу және пайдалану"
        },
        "salary": "300,000 - 800,000 ₸", 
        "places": {
            "Русский": "Строительные компании, проектные институты, госзаказчики",
            "Қазақша": "Құрылыс компаниялары, жобалау институттары, мемлекеттік тапсырыс берушілер"
        },
        "career_plan": {
            "Русский": [
                "🎓 Получить строительное образование",
                "📐 Работать техником-строителем",
                "🏢 Освоить проектирование и смету",
                "👨‍🔧 Стать прорабом на объекте",
                "👨‍💼 Вырасти до главного инженера"
            ],
            "Қазақша": [
                "🎓 Құрылыс білімі алу",
                "📐 Техник-құрылысшы болып жұмыс істеу",
                "🏢 Жобалау мен сметаны меңгеру",
                "👨‍🔧 Объектте прораб болу",
                "👨‍💼 Бас инженер деңгейіне көтерілу"
            ]
        },
        "advice": {
            "Русский": "Освойте AutoCAD, сметное дело и строительные нормы. Развивайте пространственное мышление.",
            "Қазақша": "AutoCAD, смета ісі мен құрылыс нормаларын меңгеріңіз. Кеңістіктік ойлау дағдыларын дамытыңыз."
        }
    },
    "0911000": {
        "name": {
            "Русский": "⚡ Электротехника",
            "Қазақша": "⚡ Электротехника" 
        },
        "description": {
            "Русский": "Монтаж, наладка и обслуживание электрооборудования",
            "Қазақша": "Электр жабдықтарын орнату, реттеу және қызмет көрсету"
        },
        "salary": "320,000 - 750,000 ₸",
        "places": {
            "Русский": "Энергетические компании, заводы, сервисные центры",
            "Қазақша": "Энергетикалық компаниялар, зауыттар, сервистік орталықтар"
        },
        "career_plan": {
            "Русский": [
                "🎓 Окончить электротехнический колледж",
                "🔌 Работать электромонтажником",
                "📚 Получить высшее образование",
                "👨‍🔧 Стать инженером-электриком",
                "👨‍💼 Вырасти до главного энергетика"
            ],
            "Қазақша": [
                "🎓 Электротехникалық колледжді бітіру",
                "🔌 Электрмонтер болып жұмыс істеу",
                "📚 Жоғары білім алу", 
                "👨‍🔧 Инженер-электрик болу",
                "👨‍💼 Бас энергетик деңгейіне көтерілу"
            ]
        },
        "advice": {
            "Русский": "Изучите электротехнику, схемы и правила безопасности. Практикуйтесь в чтении чертежей.",
            "Қазақша": "Электротехниканы, сұлбалар мен қауіпсіздік ережелерін үйреніңіз. Сызбаларды оқуда тәжірибе жинаңыз."
        }
    },
    "1302000": {
        "name": {
            "Русский": "🤖 Автоматизация",
            "Қазақша": "🤖 Автоматтандыру"
        },
        "description": {
            "Русский": "Автоматизация технологических процессов и производств",
            "Қазақша": "Технологиялық процестер мен өндірістерді автоматтандыру"
        },
        "salary": "380,000 - 950,000 ₸",
        "places": {
            "Русский": "Промышленные предприятия, IT-компании, КИПиА",
            "Қазақша": "Өнеркәсіптік кәсіпорындар, IT-компаниялар, ӨКЖ"
        },
        "career_plan": {
            "Русский": [
                "🎓 Получить образование по автоматизации", 
                "🔧 Работать техником КИПиА",
                "📚 Освоить PLC-программирование",
                "👨‍🔧 Стать инженером-автоматизатором",
                "👨‍💼 Вырасти до руководителя проекта"
            ],
            "Қазақша": [
                "🎓 Автоматтандыру бойынша білім алу",
                "🔧 ӨКЖ технігі болып жұмыс істеу",
                "📚 PLC-бағдарламалауды меңгеру",
                "👨‍🔧 Инженер-автоматтандырушы болу",
                "👨‍💼 Жоба басшысы деңгейіне көтерілу"
            ]
        },
        "advice": {
            "Русский": "Изучите ПЛК-программирование, SCADA-системы и промышленные сети. Развивайте системное мышление.",
            "Қазақша": "PLC-бағдарламалау, SCADA-жүйелер мен өнеркәсіптік желілерді үйреніңіз. Жүйелік ойлау дағдыларын дамытыңыз."
        }
    }
}

# =============================
# 🧠 QUESTIONS DATABASE (40 QUESTIONS)
# =============================
QUESTIONS = {
    "Русский": [
        "Вам нравится работать с компьютерами и новыми технологиями?",
        "Вы любите разбираться в том, как работают механизмы?",
        "Вам интересно программировать и создавать программное обеспечение?",
        "Вы предпочитаете работать с цифрами и расчетами?",
        "Вам нравится решать сложные технические задачи?",
        "Вы любите работать руками и собирать конструкции?",
        "Вам интересны электрические схемы и электроника?",
        "Вы предпочитаете анализировать данные и находить закономерности?",
        "Вам нравится проектировать и создавать новые системы?",
        "Вы любите работать с чертежами и технической документацией?",
        "Вам интересны промышленные процессы и производство?",
        "Вы предпочитаете работу, связанную с техникой и оборудованием?",
        "Вам нравится находить нестандартные решения проблем?",
        "Вы любите изучать новые технологии и инновации?",
        "Вам интересно работать с базами данных и информацией?",
        "Вы предпочитаете системный подход к решению задач?",
        "Вам нравится работать в команде над сложными проектами?",
        "Вы любите доводить начатое дело до конца?",
        "Вам интересно оптимизировать и улучшать процессы?",
        "Вы предпочитаете работу, где нужна точность и внимательность?",
        "Вам нравится обучаться новым навыкам и технологиям?",
        "Вы любите работать с измерительными приборами?",
        "Вам интересны автоматизированные системы управления?",
        "Вы предпочитаете работу, связанную с проектированием?",
        "Вам нравится анализировать и улучшать существующие системы?",
        "Вы любите работать с техническими спецификациями?",
        "Вам интересны монтажные и пусконаладочные работы?",
        "Вы предпочитаете работу, где можно применить творческий подход?",
        "Вам нравится решать практические инженерные задачи?",
        "Вы любите работать с современным оборудованием?",
        "Вам интересны вопросы энергетики и электроснабжения?",
        "Вы предпочитаете работу, связанную с контролем качества?",
        "Вам нравится участвовать в создании новых продуктов?",
        "Вы любите работать в условиях многозадачности?",
        "Вам интересны вопросы технической безопасности?",
        "Вы предпочитаете работу, где нужны аналитические способности?",
        "Вам нравится изучать иностранные языки для работы с техникой?",
        "Вы любите работать с программными комплексами?",
        "Вам интересны исследования и разработки?",
        "Вы предпочитаете работу, где можно постоянно развиваться?"
    ],
    "Қазақша": [
        "Сізге компьютерлермен және жаңа технологиялармен жұмыс істеу ұнай ма?",
        "Механизмдердің қалай жұмыс істейтінін анықтағанды ұнатасыз ба?",
        "Бағдарламалау және бағдарламалық жасақтама жасағанды қызықтырасыз ба?",
        "Сандармен және есептеулермен жұмыс істегенді қалайсыз ба?",
        "Күрделі техникалық мәселелерді шешкенді ұнатасыз ба?",
        "Қолдарыңызбен жұмыс істеп, конструкциялар жинағанды жақсы көресіз бе?",
        "Электр сұлбалары мен электроника сізді қызықтыра ма?",
        "Деректерді талдап, заңдылықтарды тапқанды ұнатасыз ба?",
        "Жаңа жүйелерді жобалау мен жасағанды ұнатасыз ба?",
        "Сызбалармен және техникалық құжаттамамен жұмыс істегенді жақсы көресіз бе?",
        "Өнеркәсіптік процестер мен өндіріс сізді қызықтыра ма?",
        "Техника мен жабдықпен байланысты жұмысты қалайсыз ба?",
        "Мәселелерге стандартты емес шешімдер тапқанды ұнатасыз ба?",
        "Жаңа технологиялар мен инновацияларды зерттегенді ұнатасыз ба?",
        "Деректер қорларымен және ақпаратпен жұмыс істеу сізді қызықтыра ма?",
        "Мәселелерді шешуде жүйелік тәсілді қалайсыз ба?",
        "Күрделі жобалар бойынша командада жұмыс істегенді ұнатасыз ба?",
        "Бастаған істі соңына дейін жеткізгенді жақсы көресіз бе?",
        "Процестерді оңтайландыру мен жақсартқанды қызықтырасыз ба?",
        "Нақтылық пен мұқияттық қажет жұмысты қалайсыз ба?",
        "Жаңа дағдылар мен технологияларды үйренгенді ұнатасыз ба?",
        "Өлшеуіш аспаптарымен жұмыс істегенді ұнатасыз ба?",
        "Автоматтандырылған басқару жүйелері сізді қызықтыра ма?",
        "Жобалаумен байланысты жұмысты қалайсыз ба?",
        "Қолданыстағы жүйелерді талдау мен жақсартқанды ұнатасыз ба?",
        "Техникалық сипаттамалармен жұмыс істегенді жақсы көресіз бе?",
        "Монтаждау және іске қосу жұмыстары сізді қызықтыра ма?",
        "Шығармашылық тәсілді қолдануға болатын жұмысты қалайсыз ба?",
        "Практикалық инженерлік есептерді шешкенді ұнатасыз ба?",
        "Заманауи жабдықтармен жұмыс істегенді ұнатасыз ба?",
        "Энергетика мен электрмен жабдықтау мәселелері сізді қызықтыра ма?",
        "Сапаны бақылаумен байланысты жұмысты қалайсыз ба?",
        "Жаңа өнімдерді жасауға қатысқанды ұнатасыз ба?",
        "Бірнеше тапсырманы бір уақытта орындайтын жұмысты жақсы көресіз бе?",
        "Техникалық қауіпсіздік мәселелері сізді қызықтыра ма?",
        "Аналитикалық қабілеттер қажет жұмысты қалайсыз ба?",
        "Техникамен жұмыс істеу үшін шет тілдерін үйренгенді ұнатасыз ба?",
        "Бағдарламалық кешендермен жұмыс істегенді ұнатасыз ба?",
        "Зерттеулер мен әзірлемелер сізді қызықтыра ма?",
        "Үнемі дами алатын жұмысты қалайсыз ба?"
    ]
}

# =============================
# 🧠 ANALYTICS SYSTEM
# =============================
class JobAIAnalytics:
    def __init__(self):
        self.question_weights = {
            # Вопросы взвешены по профессиям: 1305000-IT, 0809000-Нефтегаз, 1401000-Строительство, 0911000-Электротехника, 1302000-Автоматизация
            0: {"1305000": 0.9, "1302000": 0.7, "0911000": 0.3},
            1: {"0809000": 0.8, "1401000": 0.6, "0911000": 0.7},
            2: {"1305000": 1.0, "1302000": 0.8},
            3: {"1305000": 0.7, "0809000": 0.6, "1401000": 0.5},
            4: {"1302000": 0.9, "0911000": 0.8, "0809000": 0.6},
            5: {"1401000": 0.9, "0911000": 0.7},
            6: {"0911000": 1.0, "1302000": 0.7},
            7: {"1305000": 0.8, "1302000": 0.9, "0809000": 0.5},
            8: {"1302000": 0.9, "1401000": 0.7, "1305000": 0.6},
            9: {"1401000": 0.8, "0911000": 0.7, "1302000": 0.6},
            10: {"0809000": 0.9, "1302000": 0.7, "1401000": 0.5},
            11: {"0911000": 0.9, "0809000": 0.7, "1401000": 0.6},
            12: {"1305000": 0.8, "1302000": 0.9, "0911000": 0.6},
            13: {"1305000": 0.9, "1302000": 0.8, "0911000": 0.5},
            14: {"1305000": 1.0, "1302000": 0.7},
            15: {"1302000": 0.9, "1305000": 0.7, "0809000": 0.5},
            16: {"1401000": 0.7, "0809000": 0.6, "1302000": 0.5},
            17: {"0809000": 0.8, "1401000": 0.7, "0911000": 0.6},
            18: {"1302000": 0.9, "1305000": 0.7, "0809000": 0.6},
            19: {"0911000": 0.8, "1302000": 0.7, "1401000": 0.6},
            20: {"1305000": 0.8, "1302000": 0.7, "0911000": 0.6},
            21: {"0911000": 0.9, "1302000": 0.7, "0809000": 0.5},
            22: {"1302000": 1.0, "0911000": 0.7, "1305000": 0.5},
            23: {"1401000": 0.9, "1302000": 0.7, "0911000": 0.6},
            24: {"1302000": 0.9, "1305000": 0.7, "0809000": 0.5},
            25: {"1401000": 0.8, "0911000": 0.7, "1302000": 0.6},
            26: {"0911000": 0.9, "1401000": 0.7, "0809000": 0.5},
            27: {"1305000": 0.7, "1401000": 0.6, "1302000": 0.5},
            28: {"1302000": 0.9, "1401000": 0.7, "0911000": 0.6},
            29: {"0911000": 0.8, "1302000": 0.7, "0809000": 0.6},
            30: {"0911000": 1.0, "0809000": 0.5},
            31: {"0809000": 0.7, "1401000": 0.6, "0911000": 0.5},
            32: {"1305000": 0.8, "1302000": 0.7, "1401000": 0.5},
            33: {"1305000": 0.7, "1302000": 0.6, "0809000": 0.5},
            34: {"0911000": 0.9, "0809000": 0.8, "1401000": 0.7},
            35: {"1305000": 0.8, "1302000": 0.7, "0809000": 0.5},
            36: {"1305000": 0.7, "1302000": 0.6, "0911000": 0.5},
            37: {"1305000": 0.9, "1302000": 0.7},
            38: {"1305000": 0.8, "1302000": 0.7, "0809000": 0.5},
            39: {"1305000": 0.8, "1302000": 0.7, "0911000": 0.6}
        }
    
    def calculate_scores(self, answers):
        """Calculate profession scores based on answers"""
        scores = {profession: 0 for profession in PROFESSIONS.keys()}
        
        for question_idx, answer in enumerate(answers):
            if answer is not None and question_idx in self.question_weights:
                for profession, weight in self.question_weights[question_idx].items():
                    # Normalize answer from 1-5 to 0-1 scale and apply weight
                    normalized_answer = (answer - 1) / 4.0
                    scores[profession] += normalized_answer * weight * 25  # Scale up
        
        return scores
    
    def get_top_profession(self, scores):
        """Get the top recommended profession"""
        return max(scores.items(), key=lambda x: x[1])

# =============================
# 🚀 INITIALIZE APP
# =============================
analytics = JobAIAnalytics()

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

# =============================
# 🌍 LANGUAGE SWITCHER
# =============================
col1, col2, col3 = st.columns([3, 2, 1])
with col3:
    lang_option = st.selectbox(
        "🌐",
        options=list(LANGUAGES.keys()),
        index=list(LANGUAGES.keys()).index(st.session_state.language),
        key="lang_switch"
    )
    if lang_option != st.session_state.language:
        st.session_state.language = lang_option
        st.rerun()

# =============================
# 🏠 MAIN PAGE
# =============================
if not st.session_state.test_started and not st.session_state.show_loading and not st.session_state.show_results:
    st.markdown(f'<div class="main-header neon-glow">{LANGUAGES[st.session_state.language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-header">{LANGUAGES[st.session_state.language]["subtitle"]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Welcome section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style='padding: 2rem; background: rgba(10, 10, 40, 0.6); border-radius: 20px; border: 2px solid #6c63ff;'>
            <h2 style='color: #00ffff; font-family: Orbitron, sans-serif;'>🚀 Будущее начинается здесь</h2>
            <p style='color: #b8b8ff; font-size: 1.2rem; line-height: 1.6;'>
                Job.AI — это интеллектуальная система профориентации, которая использует 
                передовые алгоритмы искусственного интеллекта для определения вашего 
                идеального профессионального пути в Жамбылском политехническом колледже.
            </p>
            <p style='color: #b8b8ff; font-size: 1.1rem;'>
                📊 <strong>40 вопросов</strong> для глубокого анализа<br>
                🎯 <strong>Точные рекомендации</strong> по профессиям<br>
                💼 <strong>Карьерный план</strong> и развитие<br>
                ⚡ <strong>Мгновенные результаты</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
            <div style='font-size: 5rem; margin-bottom: 1rem;'>🤖</div>
            <h3 style='color: #ff00ff;'>AI-Powered</h3>
            <p style='color: #b8b8ff;'>Технологии будущего уже здесь</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Start button
    if st.button(LANGUAGES[st.session_state.language]["start_test"], use_container_width=True):
        st.session_state.test_started = True
        st.session_state.current_question = 0
        st.session_state.answers = [None] * 40
        st.rerun()

# =============================
# ❓ TEST QUESTIONS
# =============================
elif st.session_state.test_started and not st.session_state.show_loading and not st.session_state.show_results:
    questions = QUESTIONS[st.session_state.language]
    current_q = st.session_state.current_question
    
    # Progress
    progress = (current_q + 1) / len(questions)
    st.progress(progress)
    st.markdown(f"**{LANGUAGES[st.session_state.language]['progress_text'].format(current=current_q + 1, total=len(questions))}**")
    
    # Question
    st.markdown(f'<div class="question-container scan-line">{current_q + 1}. {questions[current_q]}</div>', unsafe_allow_html=True)
    
    # Rating options
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
        st.markdown(f'<div class="loading-text neon-glow">{LANGUAGES[st.session_state.language]["analyzing"]}<span class="pulse-dots"></span></div>', unsafe_allow_html=True)
        
        # Animated progress bar
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.05)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    time.sleep(1)
    st.session_state.show_loading = False
    st.session_state.show_results = True
    st.rerun()

# =============================
# 📊 RESULTS PAGE
# =============================
elif st.session_state.show_results:
    # Calculate results
    scores = analytics.calculate_scores(st.session_state.answers)
    top_profession_code, top_score = analytics.get_top_profession(scores)
    top_profession = PROFESSIONS[top_profession_code]
    
    st.markdown(f'<div class="main-header neon-glow">{LANGUAGES[st.session_state.language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-header">{LANGUAGES[st.session_state.language]["your_results"]}</div>', unsafe_allow_html=True)
    
    # Top profession card
    st.markdown(f"""
    <div class="profession-card results-appear">
        <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 2rem;">
            <div style="flex: 1;">
                <h2 style="color: #00ffff; margin-bottom: 0.5rem; font-family: Orbitron, sans-serif;">
                    {top_profession["name"][st.session_state.language]}
                </h2>
                <p style="color: #b8b8ff; font-size: 1.1rem; line-height: 1.5;">
                    {top_profession["description"][st.session_state.language]}
                </p>
                <div style="color: #6c63ff; font-size: 0.9rem; margin-top: 0.5rem;">
                    🔢 Код: {top_profession_code}
                </div>
            </div>
            <div style="text-align: right;">
                <div style="color: #00ffff; font-size: 3rem; font-weight: 900; font-family: Orbitron, sans-serif;">
                    {top_score:.0f}%
                </div>
                <div style="color: #b8b8ff; font-size: 1rem;">
                    {LANGUAGES[st.session_state.language]["compatibility"]}
                </div>
            </div>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
            <div class="metric-card">
                <div class="metric-value">{top_profession["salary"].split(" - ")[0]}</div>
                <div class="metric-label">{LANGUAGES[st.session_state.language]["salary"]}</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{len(top_profession["career_plan"][st.session_state.language])}</div>
                <div class="metric-label">Этапы карьеры</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">5/5</div>
                <div class="metric-label">Перспективность</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Career plan
    st.markdown(f'<div class="section-header">📋 {LANGUAGES[st.session_state.language]["career_plan"]}</div>', unsafe_allow_html=True)
    
    career_col1, career_col2 = st.columns([2, 1])
    
    with career_col1:
        for i, step in enumerate(top_profession["career_plan"][st.session_state.language]):
            st.markdown(f"""
            <div style="background: rgba(20, 20, 50, 0.6); padding: 1.5rem; margin: 1rem 0; border-radius: 15px; border-left: 4px solid #00ffff;">
                <div style="color: #00ffff; font-weight: 700; margin-bottom: 0.5rem;">Шаг {i+1}</div>
                <div style="color: #ffffff;">{step}</div>
            </div>
            """, unsafe_allow_html=True)
    
    with career_col2:
        st.markdown(f"""
        <div style="background: rgba(20, 20, 50, 0.8); padding: 2rem; border-radius: 15px; border: 1px solid #6c63ff;">
            <h4 style="color: #ff00ff; margin-bottom: 1rem;">🚀 {LANGUAGES[st.session_state.language]["development"]}</h4>
            <p style="color: #b8b8ff; line-height: 1.5;">{top_profession["advice"][st.session_state.language]}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Work places
    st.markdown(f'<div class="section-header">🏢 {LANGUAGES[st.session_state.language]["work_places"]}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: rgba(20, 20, 50, 0.6); padding: 2rem; border-radius: 15px; border: 1px solid #00ffff;">
        <p style="color: #ffffff; font-size: 1.2rem; text-align: center;">
            {top_profession["places"][st.session_state.language]}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # All professions comparison
    st.markdown(f'<div class="section-header">📊 Сравнение всех профессий</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="profession-grid">', unsafe_allow_html=True)
    
    for profession_code, profession in PROFESSIONS.items():
        score = scores.get(profession_code, 0)
        st.markdown(f"""
        <div class="grid-item">
            <h4 style="color: #00ffff; margin-bottom: 0.5rem; font-family: Exo 2, sans-serif;">
                {profession["name"][st.session_state.language]}
            </h4>
            <div style="color: #6c63ff; font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5rem;">
                {score:.0f}%
            </div>
            <p style="color: #b8b8ff; font-size: 0.9rem; line-height: 1.4; margin-bottom: 1rem;">
                {profession["description"][st.session_state.language]}
            </p>
            <div style="color: #8888ff; font-size: 0.8rem;">
                <strong>Зарплата:</strong> {profession["salary"]}<br>
                <strong>Код:</strong> {profession_code}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Action buttons
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
            st.info("Функция экспорта в PDF будет доступна в следующем обновлении!")

# =============================
# 👣 FOOTER
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
            Профориентационная система | AI Assistant © 2025<br>
            Жамбылский политехнический высший колледж
        </div>
    </div>
    """, unsafe_allow_html=True)
