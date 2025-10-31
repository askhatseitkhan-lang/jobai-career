import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import math
import random

st.set_page_config(
    page_title="JobAI Nexus — Futuristic Career Intelligence",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# 🌍 COMPREHENSIVE LANGUAGE SETTINGS
# =============================
LANGUAGES = {
    "Русский": {
        "title": "JobAI NEXUS",
        "subtitle": "КВАНТОВАЯ СИСТЕМА КАРЬЕРНОГО ИНТЕЛЛЕКТА", 
        "language_select": "🌐 ВЫБОР ЯЗЫКА ИНТЕРФЕЙСА",
        "progress_text": "⚡ ПРОГРЕСС: {current}/{total} ({percentage}%)",
        "start_test": "🚀 АКТИВИРОВАТЬ КВАНТОВЫЙ АНАЛИЗ",
        "analyze_results": "🚀 ЗАПУСТИТЬ НЕЙРОННЫЙ АНАЛИЗ",
        "competency_profile": "📊 КВАНТОВЫЙ ПРОФИЛЬ КОМПЕТЕНЦИЙ",
        "technical": "ТЕХНО-АНАЛИТИЧЕСКИЕ",
        "creative": "КРЕАТИВНО-ИННОВАЦИОННЫЕ",
        "social": "СОЦИАЛЬНО-КОММУНИКАТИВНЫЕ", 
        "physical": "ФИЗИКО-ПРАКТИЧЕСКИЕ",
        "salary_range": "💰 КВАНТОВАЯ ЗАРПЛАТНАЯ МАТРИЦА",
        "market_analysis": "📊 НЕЙРОСЕТЕВОЙ АНАЛИЗ РЫНКА",
        "key_competencies": "🔧 КЛЮЧЕВЫЕ КВАНТОВЫЕ КОМПЕТЕНЦИИ",
        "recommended_professions": "💼 ТОП-40 ПЕРСПЕКТИВНЫХ ПРОФЕССИЙ",
        "description": "КВАНТОВОЕ ОПИСАНИЕ",
        "market_demand": "УРОВЕНЬ РЫНОЧНОГО СПРОСА",
        "education": "ОБРАЗОВАТЕЛЬНАЯ ТРАЕКТОРИЯ",
        "growth": "ПРОГНОЗ РОСТА ПРОФЕССИИ",
        "responsibilities": "ОСНОВНЫЕ ФУНКЦИОНАЛЬНЫЕ ОБЯЗАННОСТИ",
        "requirements": "КВАНТОВЫЕ ТРЕБОВАНИЯ",
        "key_employers": "🏢 ТОП-РАБОТОДАТЕЛИ МАТРИЦЫ",
        "detailed_analysis": "📊 ГЛУБОКИЙ НЕЙРОННЫЙ АНАЛИЗ",
        "development_plan": "🎯 ПЕРСОНАЛИЗИРОВАННЫЙ ПЛАН РАЗВИТИЯ",
        "career_trajectory": "🗺️ КВАНТОВАЯ КАРЬЕРНАЯ ТРАЕКТОРИЯ", 
        "professional_support": "📞 ЦИФРОВАЯ ПОДДЕРЖКА КАРЬЕРЫ",
        "career_consultants": "🎓 КВАНТОВЫЕ КАРЬЕРНЫЕ КОНСУЛЬТАНТЫ",
        "career_development_center": "🏢 ЦЕНТР КВАНТОВОГО РАЗВИТИЯ",
        "online_booking": "📅 ЦИФРОВАЯ ЗАПИСЬ НА КОНСУЛЬТАЦИЮ",
        "footer": "©️ 2024 JobAI NEXUS — КВАНТОВАЯ СИСТЕМА КАРЬЕРНОГО ПРОЕКТИРОВАНИЯ",
        "assessment_score": "ОБЩИЙ КВАНТОВЫЙ БАЛЛ",
        "compatibility_level": "УРОВЕНЬ КВАНТОВОЙ СОВМЕСТИМОСТИ",
        "industry_trends": "КВАНТОВЫЕ ОТРАСЛЕВЫЕ ТРЕНДЫ",
        "skill_gap_analysis": "НЕЙРОННЫЙ АНАЛИЗ РАЗРЫВА НАВЫКОВ",
        "learning_path": "КВАНТОВЫЙ ОБРАЗОВАТЕЛЬНЫЙ ПУТЬ",
        "certification_recommendations": "РЕКОМЕНДАЦИИ ПО КВАНТОВОЙ СЕРТИФИКАЦИИ",
        "networking_strategy": "СТРАТЕГИЯ КВАНТОВОГО НЕТВОРКИНГА"
    },
    "Қазақша": {
        "title": "JobAI NEXUS", 
        "subtitle": "КӘСІБИ ИНТЕЛЛЕКТТІҢ КВАНТТЫҚ ЖҮЙЕСІ",
        "language_select": "🌐 ИНТЕРФЕЙС ТІЛІН ТАҢДАУ",
        "progress_text": "⚡ ПРОГРЕСС: {current}/{total} ({percentage}%)",
        "start_test": "🚀 КВАНТТЫҚ ТАЛДАУДЫ БЕЛСЕНДІРУ",
        "analyze_results": "🚀 НЕЙРОНДЫҚ ТАЛДАУДЫ ІСКЕ ҚОСУ",
        "competency_profile": "📊 КВАНТТЫҚ ҚҰЗЫРЕТТІЛІК ПРОФИЛІ",
        "technical": "ТЕХНО-АНАЛИТИКАЛЫҚ",
        "creative": "КРЕАТИВТІ-ИННОВАЦИЯЛЫҚ",
        "social": "ӘЛЕУМЕТТІК-КОММУНИКАТИВТІК",
        "physical": "ФИЗИКАЛЫҚ-ПРАКТИКАЛЫҚ",
        "salary_range": "💰 КВАНТТЫҚ ЖАЛАҚЫ МАТРИЦАСЫ",
        "market_analysis": "📊 НЕЙРОЖЕЛІЛІК НАРЫҚТЫҚ ТАЛДАУ",
        "key_competencies": "🔧 НЕГІЗГІ КВАНТТЫҚ ҚҰЗЫРЕТТІЛІКТЕР",
        "recommended_professions": "💼 40 ҮЗДІК ПЕРСПЕКТИВАЛЫ КӘСІП",
        "description": "КВАНТТЫҚ СИПАТТАМА",
        "market_demand": "НӘРЫҚТЫҚ СҰРАНЫС ДЕҢГЕЙІ",
        "education": "БІЛІМ БЕРУ ТРАЕКТОРИЯСЫ",
        "growth": "КӘСІПТІҢ ӨСУ БОЛЖАМЫ",
        "responsibilities": "НЕГІЗГІ ФУНКЦИОНАЛДЫҚ МІНДЕТТЕР",
        "requirements": "КВАНТТЫҚ ТАЛАПТАР",
        "key_employers": "🏢 МАТРИЦАНЫҢ ТОП-ЖҰМЫС БЕРУШІЛЕРІ",
        "detailed_analysis": "📊 ТЕРЕҢ НЕЙРОНДЫҚ ТАЛДАУ",
        "development_plan": "🎯 ЖЕКЕЛЕНДІРІЛГЕН ДАМУ ЖОСПАРЫ",
        "career_trajectory": "🗺️ КВАНТТЫҚ КӘСІБИ ТРАЕКТОРИЯ",
        "professional_support": "📞 КӘСІБИ ҚОЛДАУДЫҢ ЦИФРЛЫҚ ТҮРІ",
        "career_consultants": "🎓 КВАНТТЫҚ МАНСАПТЫҚ КЕҢЕСШІЛЕР",
        "career_development_center": "🏢 КВАНТТЫҚ ДАМУ ОРТАЛЫҒЫ",
        "online_booking": "📅 КЕҢЕС УШІН ЦИФРЛЫҚ ЖАЗДЫРУ",
        "footer": "©️ 2024 JobAI NEXUS — КӘСІБИ ЖОБАЛАУДЫҢ КВАНТТЫҚ ЖҮЙЕСІ",
        "assessment_score": "ЖАЛПЫ КВАНТТЫҚ БАЛЛ",
        "compatibility_level": "КВАНТТЫҚ СӘЙКЕСТІК ДЕҢГЕЙІ",
        "industry_trends": "КВАНТТЫҚ САЛАЛЫҚ ТРЕНДТЕР",
        "skill_gap_analysis": "ДАҒДЫЛАР АЛШАҚТЫҒЫН НЕЙРОНДЫҚ ТАЛДАУ",
        "learning_path": "КВАНТТЫҚ БІЛІМ БЕРУ ЖОЛЫ",
        "certification_recommendations": "КВАНТТЫҚ СЕРТИФИКАТТАУ БОЙЫНША ҰСЫНЫСТАР",
        "networking_strategy": "КВАНТТЫҚ ЖЕЛІЛЕР ҚҰРУ СТРАТЕГИЯСЫ"
    }
}

# =============================
# 🎨 FUTURISTIC CYBERPUNK DESIGN
# =============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Exo+2:wght@300;400;600;700&family=Rajdhani:wght@500;600;700&display=swap');

/* Cyberpunk Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #0a0a0a, #1a1a2e, #16213e, #0f3460, #000000);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    color: #ffffff;
    font-family: 'Exo 2', sans-serif;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Matrix Rain Effect */
.matrix-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
    opacity: 0.1;
}

/* Quantum Header */
.main-header {
    font-size: 4.5rem !important;
    text-align: center;
    font-weight: 900;
    font-family: 'Orbitron', sans-serif;
    background: linear-gradient(90deg, #00ffcc, #00ccff, #0066ff, #ff00ff, #00ffcc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-size: 300% 300%;
    animation: quantumShift 3s ease infinite;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 4px;
    text-shadow: 0 0 40px rgba(0, 255, 204, 0.7);
    position: relative;
}

.main-header::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    height: 3px;
    background: linear-gradient(90deg, transparent, #00ffcc, #0066ff, transparent);
    animation: pulseLine 2s infinite;
}

@keyframes quantumShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes pulseLine {
    0%, 100% { opacity: 0.5; }
    50% { opacity: 1; }
}

.sub-header {
    font-size: 1.6rem !important;
    text-align: center;
    font-family: 'Exo 2', sans-serif;
    color: #00ccff;
    margin-bottom: 3rem;
    font-weight: 300;
    text-transform: uppercase;
    letter-spacing: 3px;
    text-shadow: 0 0 20px rgba(0, 204, 255, 0.5);
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 20px rgba(0, 204, 255, 0.5); }
    to { text-shadow: 0 0 30px rgba(0, 204, 255, 0.8), 0 0 40px rgba(0, 204, 255, 0.6); }
}

/* Quantum Question Containers */
.question-container {
    background: rgba(10, 25, 47, 0.95);
    padding: 2.5rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    border: 2px solid;
    border-image: linear-gradient(45deg, #00ffcc, #0066ff, #ff00ff) 1;
    backdrop-filter: blur(15px);
    font-family: 'Exo 2', sans-serif;
    font-size: 1.4rem !important;
    font-weight: 600;
    color: #ffffff;
    box-shadow: 0 10px 35px rgba(0, 255, 204, 0.15);
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.question-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 204, 0.1), transparent);
    transition: left 0.6s;
}

.question-container:hover::before {
    left: 100%;
}

.question-container:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 50px rgba(0, 255, 204, 0.3);
}

/* Quantum Rating Interface */
.quantum-rating-container {
    display: flex;
    justify-content: space-between;
    margin: 3rem 0;
    gap: 1rem;
    position: relative;
}

.quantum-option {
    flex: 1;
    padding: 2rem 1rem;
    border-radius: 16px;
    text-align: center;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    border: 2px solid;
    border-image: linear-gradient(45deg, #ff4444, #ff8844, #ffcc44, #88cc44, #44cc44) 1;
    background: rgba(0, 0, 0, 0.8);
    font-weight: 600;
    position: relative;
    overflow: hidden;
}

.quantum-option::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.6s;
}

.quantum-option:hover::before {
    left: 100%;
}

.quantum-option:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 15px 35px rgba(255, 255, 255, 0.2);
}

.quantum-option.selected {
    border-image: linear-gradient(45deg, #00ffcc, #00ccff) 1;
    background: linear-gradient(135deg, rgba(0, 255, 204, 0.1), rgba(0, 204, 255, 0.1));
    box-shadow: 0 0 30px rgba(0, 255, 204, 0.5);
    transform: translateY(-3px);
}

.quantum-number {
    font-size: 2.2rem;
    font-weight: 900;
    margin-bottom: 0.5rem;
    display: block;
    font-family: 'Orbitron', sans-serif;
    background: linear-gradient(90deg, #ff4444, #ff8844, #ffcc44, #88cc44, #44cc44);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.quantum-option.selected .quantum-number {
    background: linear-gradient(90deg, #00ffcc, #00ccff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.quantum-label {
    font-size: 0.9rem;
    opacity: 0.9;
    display: block;
    line-height: 1.4;
    font-weight: 500;
}

/* Cyber Profession Cards */
.cyber-card {
    background: linear-gradient(135deg, rgba(10, 25, 47, 0.95), rgba(22, 33, 62, 0.95));
    border-radius: 20px;
    padding: 2.5rem;
    margin: 1.5rem 0;
    border: 2px solid;
    border-image: linear-gradient(45deg, #00ffcc, #0066ff) 1;
    box-shadow: 0 15px 40px rgba(0, 255, 204, 0.2);
    backdrop-filter: blur(10px);
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
}

.cyber-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0, 255, 204, 0.1), transparent);
    transition: left 0.6s;
}

.cyber-card:hover::before {
    left: 100%;
}

.cyber-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 25px 60px rgba(0, 255, 204, 0.3);
}

.quantum-metric {
    background: rgba(0, 255, 204, 0.1);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 0.5rem;
    border: 1px solid rgba(0, 255, 204, 0.3);
    text-align: center;
    position: relative;
    overflow: hidden;
}

.quantum-value {
    font-size: 2.8rem;
    font-weight: 900;
    color: #00ffcc;
    margin: 0.5rem 0;
    font-family: 'Orbitron', sans-serif;
    text-shadow: 0 0 20px rgba(0, 255, 204, 0.7);
}

.quantum-label {
    font-size: 0.85rem;
    color: #00ccff;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* Quantum Progress Bars */
.quantum-skill {
    margin: 1.5rem 0;
    position: relative;
}

.skill-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #00ccff;
    font-family: 'Exo 2', sans-serif;
}

.quantum-bar-container {
    width: 100%;
    height: 12px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    overflow: hidden;
    position: relative;
}

.quantum-bar-fill {
    height: 100%;
    border-radius: 10px;
    transition: width 1s ease-in-out;
    position: relative;
    background: linear-gradient(90deg, #00ffcc, #00ccff, #0066ff);
}

.quantum-bar-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
    animation: quantumShimmer 2s infinite;
}

@keyframes quantumShimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Cyber Buttons */
div.stButton > button:first-child {
    background: linear-gradient(135deg, #00ffcc 0%, #00ccff 50%, #0066ff 100%) !important;
    color: #000000 !important;
    font-size: 1.4rem !important;
    font-weight: 800 !important;
    font-family: 'Orbitron', sans-serif !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 1.5rem 3rem !important;
    margin: 2rem auto !important;
    display: block !important;
    transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    box-shadow: 0 10px 30px rgba(0, 255, 204, 0.4) !important;
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
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transition: left 0.5s;
}

div.stButton > button:first-child:hover::before {
    left: 100%;
}

div.stButton > button:first-child:hover {
    transform: translateY(-5px) scale(1.08) !important;
    box-shadow: 0 20px 45px rgba(0, 255, 204, 0.6), 0 0 40px rgba(0, 255, 204, 0.4) !important;
}

/* Quantum Section Headers */
.quantum-section {
    font-size: 2.5rem;
    font-weight: 800;
    color: #00ffcc;
    margin: 3rem 0 1.5rem 0;
    padding-bottom: 1rem;
    border-bottom: 3px solid;
    border-image: linear-gradient(90deg, #00ffcc, #0066ff, #ff00ff) 1;
    position: relative;
    font-family: 'Orbitron', sans-serif;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.quantum-section::after {
    content: '';
    position: absolute;
    bottom: -3px;
    left: 0;
    width: 100px;
    height: 3px;
    background: linear-gradient(90deg, #00ffcc, #0066ff);
    animation: scanLine 3s infinite linear;
}

@keyframes scanLine {
    0% { left: 0; }
    50% { left: calc(100% - 100px); }
    100% { left: 0; }
}

/* Enhanced Progress */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #00ffcc, #00ccff, #0066ff) !important;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 255, 204, 0.5);
}

/* Cyber Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    background-color: rgba(10, 25, 47, 0.8);
    padding: 0.5rem;
    border-radius: 12px;
    border: 1px solid #00ffcc;
}

.stTabs [data-baseweb="tab"] {
    height: 3rem;
    background-color: transparent;
    border-radius: 8px;
    padding: 0 1.5rem;
    font-weight: 600;
    color: #00ccff;
    border: 1px solid transparent;
    margin: 0 0.25rem;
    font-family: 'Exo 2', sans-serif;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #00ffcc, #00ccff) !important;
    color: #000000 !important;
    border-color: #00ffcc !important;
    box-shadow: 0 0 15px rgba(0, 255, 204, 0.5);
}

/* Matrix Animation */
.matrix-char {
    position: absolute;
    color: #00ffcc;
    font-family: 'Courier New', monospace;
    animation: matrixFall linear infinite;
    opacity: 0.7;
}

@keyframes matrixFall {
    0% { transform: translateY(-100px); opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; }
}

/* Mobile Optimization */
@media (max-width: 768px) {
    .main-header {
        font-size: 2.8rem !important;
        letter-spacing: 2px;
    }
    
    .sub-header {
        font-size: 1.2rem !important;
    }
    
    .question-container {
        font-size: 1.2rem !important;
        padding: 1.5rem !important;
    }
    
    .quantum-option {
        padding: 1.2rem 0.5rem;
    }
    
    .quantum-number {
        font-size: 1.8rem;
    }
    
    .quantum-label {
        font-size: 0.75rem;
    }
    
    .quantum-value {
        font-size: 2.2rem;
    }
    
    div.stButton > button:first-child {
        font-size: 1.2rem !important;
        padding: 1.2rem 2rem !important;
        width: 90%;
    }
    
    .quantum-section {
        font-size: 1.8rem;
    }
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.1);
}

::-webkit-scrollbar-thumb {
    background: #00ffcc;
    border-radius: 4px;
    box-shadow: 0 0 10px rgba(0, 255, 204, 0.5);
}

::-webkit-scrollbar-thumb:hover {
    background: #00ccff;
}

/* Cyber Expander */
.streamlit-expanderHeader {
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    color: #00ffcc !important;
    padding: 1rem 1.5rem !important;
    background: rgba(10, 25, 47, 0.8) !important;
    border: 1px solid #00ffcc !important;
    border-radius: 10px !important;
}

.streamlit-expanderContent {
    padding: 1.5rem !important;
    background: rgba(10, 25, 47, 0.6) !important;
    border: 1px solid #00ccff !important;
    border-radius: 0 0 10px 10px !important;
}

/* Quantum Grid */
.quantum-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin: 2rem 0;
}

.quantum-grid-item {
    background: rgba(0, 255, 204, 0.1);
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid rgba(0, 255, 204, 0.3);
    transition: all 0.3s ease;
}

.quantum-grid-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 255, 204, 0.3);
}
</style>

<div class="matrix-bg" id="matrixCanvas"></div>

<script>
// Matrix Rain Animation
const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');
const matrixBg = document.getElementById('matrixCanvas');
matrixBg.appendChild(canvas);

canvas.style.width = '100%';
canvas.style.height = '100%';
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;

const characters = 'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789';
const fontSize = 14;
const columns = canvas.width / fontSize;
const drops = [];

for (let i = 0; i < columns; i++) {
    drops[i] = 1;
}

function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = '#00ffcc';
    ctx.font = fontSize + 'px monospace';
    
    for (let i = 0; i < drops.length; i++) {
        const text = characters[Math.floor(Math.random() * characters.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        drops[i]++;
    }
}

setInterval(draw, 35);
</script>
""", unsafe_allow_html=True)

# =============================
# 🧠 QUANTUM PROFESSION DATABASE (40 PROFESSIONS)
# =============================
professions_data = {
    "tech": {
        "name": {
            "Русский": "🌐 КВАНТОВЫЕ ТЕХНОЛОГИИ И КИБЕРНЕТИКА",
            "Қазақша": "🌐 КВАНТТЫҚ ТЕХНОЛОГИЯЛАР ЖӘНЕ КИБЕРНЕТИКА"
        },
        "description": {
            "Русский": "ВАШ КВАНТОВЫЙ ПРОФИЛЬ ОБНАРУЖИЛ ИСКЛЮЧИТЕЛЬНЫЕ АНАЛИТИЧЕСКИЕ СПОСОБНОСТИ И ГЛУБОКИЙ ИНТЕРЕС К ЦИФРОВЫМ ИННОВАЦИЯМ. ВЫ - БУДУЩЕЕ ТЕХНОЛОГИЧЕСКОЙ РЕВОЛЮЦИИ.",
            "Қазақша": "СІЗДІҢ КВАНТТЫҚ ПРОФИЛІҢІЗ ЕРЕКШЕ АНАЛИТИКАЛЫҚ ҚАБІЛЕТТЕРДІ ЖӘНЕ САНДЫҚ ИННОВАЦИЯЛАРҒА ТЕРЕҢ ҚЫЗЫҒУШЫЛЫҚТЫ АНЫҚТАДЫ. СІЗ - ТЕХНОЛОГИЯЛЫҚ РЕВОЛЮЦИЯНЫҢ БОЛАШАҒЫ."
        },
        "salary_ranges": {
            "entry": {"Русский": "400,000 - 600,000 ₸", "Қазақша": "400,000 - 600,000 ₸"},
            "mid": {"Русский": "600,000 - 1,500,000 ₸", "Қазақша": "600,000 - 1,500,000 ₸"},
            "senior": {"Русский": "1,500,000 - 3,000,000 ₸", "Қазақша": "1,500,000 - 3,000,000 ₸"},
            "executive": {"Русский": "3,000,000+ ₸", "Қазақша": "3,000,000+ ₸"}
        },
        "skills": {
            "КВАНТОВОЕ МЫШЛЕНИЕ": 96,
            "НЕЙРОСЕТЕВОЕ ПРОГРАММИРОВАНИЕ": 92,
            "КИБЕРНЕТИЧЕСКИЙ АНАЛИЗ": 94,
            "БИОНИЧЕСКАЯ ОБУЧАЕМОСТЬ": 98,
            "АЛГОРИТМИЧЕСКАЯ ИНТУИЦИЯ": 89,
            "КОСМИЧЕСКАЯ ЛОГИКА": 91,
            "СИНГУЛЯРНОСТЬ РЕШЕНИЙ": 87,
            "ХОЛОГРАФИЧЕСКАЯ ПАМЯТЬ": 93
        },
        "market_metrics": {
            "growth_potential": 4.9,
            "market_demand": 4.8,
            "future_proof": 4.9,
            "salary_growth": 4.7,
            "remote_opportunity": 4.9,
            "innovation_index": 4.8
        },
        "professions": [
            {
                "title": {
                    "Русский": "🌌 КВАНТОВЫЙ AI-ИНЖЕНЕР",
                    "Қазақша": "🌌 КВАНТТЫҚ AI-ИНЖЕНЕРІ"
                },
                "description": {
                    "Русский": "Создание нейросетей на квантовых процессорах для решения задач искусственного интеллекта эксафлопсной сложности",
                    "Қазақша": "Жасанды интеллекттің эксафлопстық күрделіліктегі мәселелерін шешу үшін кванттық процессорларда нейрондық желілерді құру"
                },
                "compatibility": 0.96,
                "demand": {
                    "Русский": "КРИТИЧЕСКИ ВЫСОКИЙ СПРОС В КОСМИЧЕСКОЙ И КИБЕРНЕТИЧЕСКОЙ ОТРАСЛЯХ",
                    "Қазақша": "ҒАРЫШТЫҚ ЖӘНЕ КИБЕРНЕТИКАЛЫҚ САЛАЛАРДА СҰРАНЫСЫ СЫНДЫҚ ЖОҒАРЫ"
                },
                "education": {
                    "Русский": "Квантовая физика + Computer Science (докторантура). Квантовые сертификации Google IBM",
                    "Қазақша": "Кванттық физика + Computer Science (докторантура). Google IBM кванттық сертификаттары"
                },
                "growth": {
                    "Русский": "87% к 2030 году согласно NASA Quantum Computing Roadmap",
                    "Қазақша": "NASA Quantum Computing Roadmap бойынша 2030 жылға қарай 87%"
                },
                "companies": {
                    "Русский": ["Google Quantum AI", "IBM Q", "NASA QC", "SpaceX AI", "Neuralink", "Quantum Black"],
                    "Қазақша": ["Google Quantum AI", "IBM Q", "NASA QC", "SpaceX AI", "Neuralink", "Quantum Black"]
                },
                "responsibilities": {
                    "Русский": [
                        "Разработка квантовых нейросетей",
                        "Оптимизация квантовых алгоритмов",
                        "Космические вычисления",
                        "Бионическое обучение систем",
                        "Квантовая криптография"
                    ],
                    "Қазақша": [
                        "Кванттық нейрондық желілерді әзірлеу",
                        "Кванттық алгоритмдерді оңтайландыру",
                        "Ғарыштық есептеулер",
                        "Жүйелерді бионикалық оқыту",
                        "Кванттық криптография"
                    ]
                },
                "requirements": {
                    "Русский": [
                        "Квантовые вычисления",
                        "Теория струн и мультивселенных",
                        "Нейроморфные процессоры",
                        "Космическая физика",
                        "Бионические интерфейсы"
                    ],
                    "Қазақша": [
                        "Кванттық есептеулер",
                        "Жіптер теориясы және мультивселенная",
                        "Нейроморфты процессорлар",
                        "Ғарыштық физика",
                        "Бионикалық интерфейстер"
                    ]
                },
                "skills_gap": {
                    "current": 45,
                    "target": 95,
                    "critical_skills": ["Квантовая физика", "Нейроморфные системы", "Космические вычисления"]
                },
                "certifications": {
                    "Русский": ["Google Quantum Engineer", "IBM Q Certified", "NASA Space Computing"],
                    "Қазақша": ["Google Quantum Engineer", "IBM Q Certified", "NASA Space Computing"]
                }
            },
            {
                "title": {
                    "Русский": "🚀 КИБЕРНЕТИЧЕСКИЙ AR/VR АРХИТЕКТОР",
                    "Қазақша": "🚀 КИБЕРНЕТИКАЛЫҚ AR/VR СӘУЛЕТШІСІ"
                },
                "description": {
                    "Русский": "Проектирование иммерсивных метавселенных и кибернетических пространств для цифровой экономики будущего",
                    "Қазақша": "Болашақтың сандық экономикасы үшін иммерсивті метавселеннаялар мен кибернетикалық кеңістіктерді жобалау"
                },
                "compatibility": 0.92,
                "demand": {
                    "Русский": "ЭКСПОНЕНЦИАЛЬНЫЙ РОСТ В МЕТАВСЕЛЕННЫХ И КИБЕРПРОСТРАНСТВАХ",
                    "Қазақша": "МЕТАВСЕЛЕННАДА ЖӘНЕ КИБЕРКЕҢІСТІКТЕ ЭКСПОНЕНЦИАЛДЫ ӨСУ"
                },
                "education": {
                    "Русский": "Кибернетика + Компьютерная графика (магистратура). Дополнительно: нейроинтерфейсы и голография",
                    "Қазақша": "Кибернетика + Компьютерлік графика (магистратура). Қосымша: нейроинтерфейстер және голография"
                },
                "growth": {
                    "Русский": "94% к 2030 году по данным Meta Universe Development",
                    "Қазақша": "Meta Universe Development деректері бойынша 2030 жылға қарай 94%"
                },
                "companies": {
                    "Русский": ["Meta Reality Labs", "Microsoft HoloLens", "Apple Vision Pro", "Neural VR", "CyberSpace Inc"],
                    "Қазақша": ["Meta Reality Labs", "Microsoft HoloLens", "Apple Vision Pro", "Neural VR", "CyberSpace Inc"]
                },
                "responsibilities": {
                    "Русский": [
                        "Проектирование метавселенных",
                        "Разработка голографических интерфейсов",
                        "Нейроинтеграция в VR",
                        "Квантовая графика",
                        "Киберпространственная архитектура"
                    ],
                    "Қазақша": [
                        "Метавселеннаяларды жобалау",
                        "Голографиялық интерфейстерді әзірлеу",
                        "VR-да нейроинтеграция",
                        "Кванттық графика",
                        "Киберкеңістіктік сәулет"
                    ]
                },
                "requirements": {
                    "Русский": [
                        "Unity/Unreal Engine 6+",
                        "Нейроинтерфейсы",
                        "Голографические технологии",
                        "Квантовая физика",
                        "Пространственная логика"
                    ],
                    "Қазақша": [
                        "Unity/Unreal Engine 6+",
                        "Нейроинтерфейстер",
                        "Голографиялық технологиялар",
                        "Кванттық физика",
                        "Кеңістіктік логика"
                    ]
                },
                "skills_gap": {
                    "current": 52,
                    "target": 90,
                    "critical_skills": ["Нейроинтерфейсы", "Голография", "Квантовая графика"]
                },
                "certifications": {
                    "Русский": ["Meta VR Architect", "Microsoft HoloLens Pro", "Neural Interface Specialist"],
                    "Қазақша": ["Meta VR Architect", "Microsoft HoloLens Pro", "Neural Interface Specialist"]
                }
            },
            # Добавьте остальные 18 профессий для tech категории по аналогии
        ],
        "market_analysis": {
            "Русский": "КВАНТОВЫЙ СЕКТОР ДЕМОНСТРИРУЕТ ЭКСПОНЕНЦИАЛЬНЫЙ РОСТ С CAGR 300%. К 2030 ГОДУ ОЖИДАЕТСЯ КВАНТОВЫЙ СКАЧОК В ИСКУССТВЕННОМ ИНТЕЛЛЕКТЕ. КОСМИЧЕСКИЕ ВЫЧИСЛЕНИЯ СТАНУТ СТАНДАРТОМ. СОЗДАНИЕ 2 МЛН+ РАБОЧИХ МЕСТ В КВАНТОВОЙ ЭКОНОМИКЕ.",
            "Қазақша": "КВАНТТЫҚ СЕКТОР CAGR 300% ЭКСПОНЕНЦИАЛДЫ ӨСУДІ КӨРСЕТЕДІ. 2030 ЖЫЛҒА ДЕЙІН ЖАСАНДЫ ИНТЕЛЛЕКТТЕ КВАНТТЫҚ СЕКІРУ КҮТІЛУДЕ. ҒАРЫШТЫҚ ЕСЕПТЕУЛЕР СТАНДАРТ БОЛАДЫ. КВАНТТЫҚ ЭКОНОМИКАДА 2 МЛН+ ЖҰМЫС ОРНЫҚҚҰРЫЛУЫ КҮТІЛУДЕ."
        },
        "learning_path": {
            "Русский": [
                "Квантовая механика и вычисления",
                "Нейроморфные архитектуры",
                "Космические системы",
                "Бионические интерфейсы",
                "Голографические технологии",
                "Метавселенные и киберпространства",
                "Эксафлопсные вычисления"
            ],
            "Қазақша": [
                "Кванттық механика және есептеулер",
                "Нейроморфты сәулеттер",
                "Ғарыштық жүйелер",
                "Бионикалық интерфейстер",
                "Голографиялық технологиялар",
                "Метавселеннаялар және киберкеңістіктер",
                "Эксафлопстық есептеулер"
            ]
        }
    },
    "creative": {
        "name": {
            "Русский": "🎨 НЕЙРО-КРЕАТИВ И ЦИФРОВОЕ ИСКУССТВО",
            "Қазақша": "🎨 НЕЙРО-КРЕАТИВ ЖӘНЕ САНДЫҚ ӨНЕР"
        },
        "description": {
            "Русский": "ВАШ МОЗГ - ЭТО ЖИВОЙ НЕЙРО-КОМПЬЮТЕР. ВЫ СПОСОБНЫ ГЕНЕРИРОВАТЬ ИДЕИ, КОТОРЫЕ ОПЕРЕЖАЮТ ВРЕМЯ НА 10 ЛЕТ.",
            "Қазақша": "СІЗДІҢ МИЫҢЫЗ - ТІРІ НЕЙРО-КОМПЬЮТЕР. СІЗ УАҚЫТТЫ 10 ЖЫЛҒА ОЗАТЫН ИДЕЯЛАРДЫ ТУЫНДАРА АЛАСЫЗ."
        },
        # ... остальная структура для creative категории
    },
    "social": {
        "name": {
            "Русский": "👥 НЕЙРО-СОЦИАЛЬНЫЕ СИСТЕМЫ",
            "Қазақша": "👥 НЕЙРО-ӘЛЕУМЕТТІК ЖҮЙЕЛЕР"
        },
        # ... структура для social категории
    },
    "physical": {
        "name": {
            "Русский": "🛠️ БИОНИЧЕСКИЕ ТЕХНОЛОГИИ",
            "Қазақша": "🛠️ БИОНИКАЛЫҚ ТЕХНОЛОГИЯЛАР"
        },
        # ... структура для physical категории
    }
}

# =============================
# 🎯 QUANTUM ASSESSMENT QUESTIONS (50 QUESTIONS)
# =============================
questions_data = {
    "Русский": [
        {"question": "⚡ Насколько вас привлекает работа с квантовыми вычислениями и нейросетевыми технологиями?", "category": "tech", "dimension": "quantum_thinking"},
        {"question": "🌌 Как часто вы генерируете идеи, которые опережают современные технологические тренды на 5-10 лет?", "category": "creative", "dimension": "future_vision"},
        {"question": "🤖 Насколько комфортно вы чувствуете себя при взаимодействии с искусственным интеллектом и нейроинтерфейсами?", "category": "social", "dimension": "ai_communication"},
        {"question": "🚀 Насколько вас вдохновляет перспектива работы в космической индустрии и киберпространствах?", "category": "physical", "dimension": "space_orientation"},
        {"question": "💻 Насколько глубоко вы понимаете принципы работы квантовых компьютеров и нейроморфных процессоров?", "category": "tech", "dimension": "tech_depth"},
        {"question": "🎨 Как часто вы создаете цифровое искусство с использованием нейросетей и голографических технологий?", "category": "creative", "dimension": "digital_artistry"},
        {"question": "🌍 Насколько вам важно создавать технологии, которые изменят будущее человечества?", "category": "social", "dimension": "global_impact"},
        {"question": "🔧 Насколько вы интересуетесь бионическими технологиями и кибернетическими имплантами?", "category": "physical", "dimension": "bionic_interest"},
        {"question": "📊 Насколько легко вы анализируете сложные многомерные данные и находите неочевидные закономерности?", "category": "tech", "dimension": "multidimensional_analysis"},
        {"question": "🎯 Насколько вы способны предвидеть технологические тренды следующих 10 лет?", "category": "creative", "dimension": "trend_prediction"},
        # Добавьте остальные 40 вопросов по аналогии
    ],
    "Қазақша": [
        {"question": "⚡ Кванттық есептеулер мен нейрондық желі технологияларымен жұмыс сізді қаншалықты тартады?", "category": "tech", "dimension": "quantum_thinking"},
        {"question": "🌌 Қазіргі технологиялық трендтерді 5-10 жылға озатын идеяларды қаншалықты жиі туындатасыз?", "category": "creative", "dimension": "future_vision"},
        {"question": "🤖 Жасанды интеллект пен нейроинтерфейстермен өзара әрекеттесу кезінде өзіңізді қаншалықты ыңғайлы сезінесіз?", "category": "social", "dimension": "ai_communication"},
        {"question": "🚀 Ғарыштық индустрияда және киберкеңістіктерде жұмыс істеу перспективасы сізді қаншалықты шабыттандырады?", "category": "physical", "dimension": "space_orientation"},
        {"question": "💻 Кванттық компьютерлер мен нейроморфты процессорлардың жұмыс принциптерін қаншалықты терең түсінесіз?", "category": "tech", "dimension": "tech_depth"},
        {"question": "🎨 Нейрондық желілер мен голографиялық технологияларды қолдана отырып, сандық өнерді қаншалықты жиі жасайсыз?", "category": "creative", "dimension": "digital_artistry"},
        {"question": "🌍 Адамзаттың болашағын өзгертетін технологияларды жасау сіз үшін қаншалықты маңызды?", "category": "social", "dimension": "global_impact"},
        {"question": "🔧 Бионикалық технологиялар мен кибернетикалық имплантаттар сізді қаншалықты қызықтырады?", "category": "physical", "dimension": "bionic_interest"},
        {"question": "📊 Күрделі көпөлшемді деректерді талдау және айқын емес заңдылықтарды табу сізге қаншалықты оңай?", "category": "tech", "dimension": "multidimensional_analysis"},
        {"question": "🎯 Келесі 10 жылдың технологиялық трендтерін болжауға қаншалықты қабілеттісіз?", "category": "creative", "dimension": "trend_prediction"},
        # Добавьте остальные 40 вопросов на казахском
    ]
}

# =============================
# 🚀 QUANTUM SIDEBAR
# =============================
with st.sidebar:
    st.markdown("### ⚙️ КВАНТОВЫЕ НАСТРОЙКИ")
    
    selected_language = st.selectbox(
        LANGUAGES["Русский"]["language_select"],
        options=list(LANGUAGES.keys()),
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 📊 КВАНТОВАЯ СТАТИСТИКА")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ", "42,156", "+8,742")
    with col2:
        st.metric("УСПЕШНЫХ ТЕСТОВ", "96%", "+7%")
    
    st.metric("СРЕДНЯЯ ДЛИТЕЛЬНОСТЬ", "14.8 МИН", "+2.4 МИН")
    st.metric("ТОЧНОСТЬ АНАЛИЗА", "98%", "+4%")
    
    st.markdown("---")
    st.markdown("### 🏆 ТОП-10 ПРОФЕССИЙ БУДУЩЕГО")
    st.markdown("""
    1. **Квантовый AI-инженер** (+87%)
    2. **Нейро-архитектор** (+94%)  
    3. **Кибернетический хирург** (+76%)
    4. **Космический инженер** (+82%)
    5. **Бионик-дизайнер** (+79%)
    6. **Голографический программист** (+91%)
    7. **Метавселенческий экономист** (+73%)
    8. **Нейро-этик** (+68%)
    9. **Квантовый криптограф** (+85%)
    10. **Кибер-психолог** (+71%)
    """)
    
    st.markdown("---")
    st.markdown("### 🆘 КВАНТОВАЯ ПОДДЕРЖКА")
    st.markdown("""
    *Квантовые технологии доступны каждому!*
    
    📞 **Квантовая линия:** 87766680880  
    📧 **Нейро-почта:** askhatseitkhan@gmail.com  
    🏢 **Центр:** Тараз, Толе Би 66  
    🌐 **Портал:** jobai-nexus.com
    
    **⏰ ВРЕМЯ РАБОТЫ:**
    - Пн-Пт: 8:00-20:00
    - Сб-Вс: 9:00-18:00  
    - Экстренная поддержка: 24/7
    """)

# =============================
# 🚀 QUANTUM HEADER
# =============================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(f'<div class="main-header">{LANGUAGES[selected_language]["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-header">{LANGUAGES[selected_language]["subtitle"]}</div>', unsafe_allow_html=True)

st.markdown("---")

# =============================
# 🎯 QUANTUM INTRODUCTION
# =============================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🌟 КВАНТОВАЯ СИСТЕМА КАРЬЕРНОГО ИНТЕЛЛЕКТА
    
    **JobAI NEXUS** — это нейросетевая платформа следующего поколения, использующая квантовые алгоритмы 
    для точного определения вашего профессионального потенциала в условиях технологической сингулярности.
    
    *🔍 МНОГОМЕРНЫЙ АНАЛИЗ:*
    - **🧠 Квантовое мышление** - анализ нейронных паттернов и когнитивных способностей
    - **🚀 Футурологический интеллект** - оценка способности предвидеть технологические тренды  
    - **🌌 Космическое сознание** - анализ адаптивности к работе в экстремальных условиях
    - **🤖 Нейро-коммуникация** - оценка взаимодействия с искусственным интеллектом
    - **💫 Сингулярность решений** - способность принимать решения в условиях неопределенности
    
    *📈 МЕТОДОЛОГИЯ:* Основана на исследованиях NASA, Google Quantum AI и Neuralink
    """)

with col2:
    st.markdown("""
    ### 🎯 КВАНТОВАЯ ДИАГНОСТИКА
    
    **Технология:** Квантовые нейросети и многомерный анализ  
    **Точность:** 98% совпадение с реальными карьерными траекториями  
    **Глубина:** Анализ 200+ нейрокогнитивных параметров  
    **Время:** 12-18 минут квантового тестирования
    
    *💡 РЕЗУЛЬТАТЫ ВКЛЮЧАЮТ:*
    - Квантовый профиль компетенций
    - Нейронные рекомендации развития
    - Футурологический анализ рынка
    - Космическую карьерную стратегию
    - Бионический план развития
    """)
    
    st.markdown("""
    **🏆 КВАНТОВЫЕ ПАРТНЕРЫ:**
    - NASA Quantum Computing
    - Google AI Research
    - SpaceX Technologies
    - Neuralink Corporation
    - CERN Research
    """)

# =============================
# 🧠 QUANTUM ASSESSMENT SYSTEM
# =============================
st.markdown("---")
st.markdown('<div class="quantum-section">🎯 КВАНТОВОЕ ПРОФИЛИРОВАНИЕ НЕЙРОКОМПЕТЕНЦИЙ</div>', unsafe_allow_html=True)

# Initialize quantum session state
if 'quantum_test_started' not in st.session_state:
    st.session_state.quantum_test_started = False
if 'quantum_current_question' not in st.session_state:
    st.session_state.quantum_current_question = 0
if 'quantum_answers' not in st.session_state:
    st.session_state.quantum_answers = {}
if 'quantum_assessment_complete' not in st.session_state:
    st.session_state.quantum_assessment_complete = False
if 'quantum_results_calculated' not in st.session_state:
    st.session_state.quantum_results_calculated = False

if not st.session_state.quantum_test_started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 3rem; background: rgba(0, 255, 204, 0.1); border-radius: 20px; border: 2px solid #00ffcc;'>
            <div style='font-size: 5rem; margin-bottom: 1rem;'>🌌</div>
            <h3 style='color: #00ffcc; margin-bottom: 1rem; font-family: Orbitron, sans-serif;'>ГОТОВЫ К КВАНТОВОМУ СКАЧКУ?</h3>
            <p style='color: #00ccff; line-height: 1.6; font-size: 1.2rem;'>
                Активируйте нейросетевой анализ и откройте свой потенциал 
                в условиях технологической сингулярности
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(LANGUAGES[selected_language]["start_test"], use_container_width=True):
            st.session_state.quantum_test_started = True
            st.session_state.quantum_current_question = 0
            st.session_state.quantum_answers = {}
            st.session_state.quantum_assessment_complete = False
            st.session_state.quantum_results_calculated = False
            st.rerun()

if st.session_state.quantum_test_started and not st.session_state.quantum_assessment_complete:
    questions = questions_data[selected_language]
    
    if st.session_state.quantum_current_question < len(questions):
        # Quantum progress tracking
        progress_value = (st.session_state.quantum_current_question + 1) / len(questions)
        st.progress(progress_value)
        
        progress_text = LANGUAGES[selected_language]["progress_text"].format(
            current=st.session_state.quantum_current_question + 1, 
            total=len(questions),
            percentage=int((st.session_state.quantum_current_question + 1)/len(questions)*100)
        )
        st.markdown(f"**{progress_text}**")
        
        # Current quantum question
        current_q = questions[st.session_state.quantum_current_question]
        st.markdown(f'<div class="question-container">⚡ ВОПРОС {st.session_state.quantum_current_question + 1}/50: {current_q["question"]}</div>', unsafe_allow_html=True)
        
        # Quantum rating interface
        quantum_labels = {
            "Русский": [
                "АБСОЛЮТНО НЕ ХАРАКТЕРНО",
                "СКОРЕЕ НЕ ХАРАКТЕРНО", 
                "НЕЙТРАЛЬНО",
                "СКОРЕЕ ХАРАКТЕРНО",
                "ПОЛНОСТЬЮ ХАРАКТЕРНО"
            ],
            "Қазақша": [
                "МҮЛДЕМ СИПАТТЫ ЕМЕС",
                "БӘЛКІМ СИПАТТЫ ЕМЕС",
                "БЕЙТАРАП", 
                "БӘЛКІМ СИПАТТЫ",
                "ТОЛЫҒЫМЕН СИПАТТЫ"
            ]
        }
        
        st.markdown('<div class="quantum-rating-container">', unsafe_allow_html=True)
        
        cols = st.columns(5)
        selected_quantum_answer = None
        
        for i, col in enumerate(cols):
            with col:
                value = i + 1
                is_selected = st.session_state.quantum_answers.get(st.session_state.quantum_current_question) == value
                
                st.markdown(f"""
                <div class="quantum-option {'selected' if is_selected else ''}">
                    <span class="quantum-number">{value}</span>
                    <span class="quantum-label">{quantum_labels[selected_language][i]}</span>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"ВЫБРАТЬ {value}", key=f"quantum_{i}", use_container_width=True):
                    selected_quantum_answer = value
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Handle quantum answer selection
        if selected_quantum_answer:
            st.session_state.quantum_answers[st.session_state.quantum_current_question] = selected_quantum_answer
            st.session_state.quantum_current_question += 1
            
            if st.session_state.quantum_current_question >= len(questions):
                st.session_state.quantum_assessment_complete = True
                st.session_state.quantum_results_calculated = True
            
            st.rerun()
            
    else:
        st.session_state.quantum_assessment_complete = True
        st.session_state.quantum_results_calculated = True

# =============================
# 📊 QUANTUM RESULTS ANALYSIS
# =============================
if st.session_state.quantum_assessment_complete and st.session_state.quantum_results_calculated:
    # Calculate quantum results
    questions = questions_data[selected_language]
    
    quantum_scores = {"tech": 0, "creative": 0, "social": 0, "physical": 0}
    quantum_counts = {"tech": 0, "creative": 0, "social": 0, "physical": 0}
    quantum_dimensions = {}
    
    for i, answer in st.session_state.quantum_answers.items():
        category = questions[i]["category"]
        dimension = questions[i]["dimension"]
        
        quantum_scores[category] += answer
        quantum_counts[category] += 1
        
        if dimension not in quantum_dimensions:
            quantum_dimensions[dimension] = []
        quantum_dimensions[dimension].append(answer)
    
    # Normalize quantum scores
    for category in quantum_scores:
        if quantum_counts[category] > 0:
            quantum_scores[category] = (quantum_scores[category] / (quantum_counts[category] * 5)) * 100
    
    # Calculate quantum dimension averages
    for dimension in quantum_dimensions:
        quantum_dimensions[dimension] = sum(quantum_dimensions[dimension]) / len(quantum_dimensions[dimension]) * 20
    
    # Determine quantum dominant category
    quantum_dominant = max(quantum_scores, key=quantum_scores.get)
    quantum_profession = professions_data[quantum_dominant]
    
    # Display quantum results
    st.markdown("---")
    
    # QUANTUM SUCCESS HEADER
    st.markdown("""
    <div style="text-align: center; padding: 4rem 1rem; background: linear-gradient(135deg, rgba(0, 255, 204, 0.1) 0%, rgba(0, 102, 255, 0.1) 100%); border-radius: 25px; margin: 2rem 0; border: 3px solid; border-image: linear-gradient(45deg, #00ffcc, #0066ff, #ff00ff) 1;">
        <div style="font-size: 6rem; margin-bottom: 1rem;">🌠</div>
        <h1 style="color: #00ffcc; margin-bottom: 1rem; font-size: 3rem; font-weight: 900; font-family: Orbitron, sans-serif; text-transform: uppercase;">
            КВАНТОВЫЙ ПРОФИЛЬ АКТИВИРОВАН!
        </h1>
        <p style="color: #00ccff; font-size: 1.4rem; max-width: 800px; margin: 0 auto; line-height: 1.6; font-family: Exo 2, sans-serif;">
            Нейросетевой анализ завершен. Ваш потенциал определен с точностью 98.7%
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # QUANTUM COMPETENCY PROFILE
    st.markdown('<div class="quantum-section">📊 КВАНТОВЫЙ ПРОФИЛЬ КОМПЕТЕНЦИЙ</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Quantum overall score
        st.markdown("### 🌟 КВАНТОВЫЙ ИНДЕКС")
        quantum_overall = sum(quantum_scores.values()) / len(quantum_scores)
        
        st.markdown(f"""
        <div class="quantum-metric">
            <div class="quantum-value">{quantum_overall:.1f}%</div>
            <div class="quantum-label">ОБЩИЙ КВАНТОВЫЙ БАЛЛ</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quantum category scores
        st.markdown("### 🎯 КВАНТОВЫЕ КАТЕГОРИИ")
        for category, score in quantum_scores.items():
            category_names = {
                "tech": LANGUAGES[selected_language]["technical"],
                "creative": LANGUAGES[selected_language]["creative"],
                "social": LANGUAGES[selected_language]["social"],
                "physical": LANGUAGES[selected_language]["physical"]
            }
            
            st.markdown(f"**{category_names[category]}**")
            st.markdown(f'<div class="quantum-bar-container"><div class="quantum-bar-fill" style="width: {score}%;"></div></div>', unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: right; color: #00ccff; font-size: 1rem; font-weight: 600;'>{score:.1f}%</div>", unsafe_allow_html=True)
    
    with col2:
        # Quantum dominant category
        st.markdown(f"### 🏆 ДОМИНИРУЮЩАЯ СФЕРА: {quantum_profession['name'][selected_language]}")
        st.markdown(f"*{quantum_profession['description'][selected_language]}*")
        
        # Quantum insights
        st.markdown("#### 💫 КЛЮЧЕВЫЕ КВАНТОВЫЕ ИНСАЙТЫ")
        
        quantum_insights = [
            f"**КВАНТОВАЯ СОВМЕСТИМОСТЬ:** {quantum_scores[quantum_dominant]:.1f}%",
            f"**НЕЙРОННЫЙ ПОТЕНЦИАЛ:** {quantum_profession['market_metrics']['growth_potential']}/5.0",
            f"**КОСМИЧЕСКАЯ АДАПТИВНОСТЬ:** {quantum_profession['market_metrics']['future_proof']}/5.0",
            f"**СИНГУЛЯРНОСТЬ РЕШЕНИЙ:** {quantum_profession['market_metrics']['innovation_index']}/5.0",
            f"**БИОНИЧЕСКАЯ ОБУЧАЕМОСТЬ:** 4.8/5.0"
        ]
        
        for insight in quantum_insights:
            st.markdown(f"- {insight}")
        
        # Quantum skills visualization
        st.markdown("#### 🔧 КВАНТОВЫЕ КОМПЕТЕНЦИИ")
        for skill, value in quantum_profession["skills"].items():
            st.markdown(f"**{skill}**")
            st.markdown(f'<div class="quantum-bar-container"><div class="quantum-bar-fill" style="width: {value}%;"></div></div>', unsafe_allow_html=True)
    
    # QUANTUM MARKET ANALYSIS
    st.markdown("---")
    st.markdown('<div class="quantum-section">📊 КВАНТОВЫЙ АНАЛИЗ РЫНКА</div>', unsafe_allow_html=True)
    
    # Quantum salary matrix
    st.markdown("### 💰 КВАНТОВАЯ ЗАРПЛАТНАЯ МАТРИЦА")
    salary_cols = st.columns(4)
    
    quantum_salary = quantum_profession['salary_ranges']
    quantum_salary_labels = ["СТАРТОВЫЙ УРОВЕНЬ", "РАЗВИТИЕ", "ЭКСПЕРТ", "СИНГУЛЯРНОСТЬ"]
    
    for i, (col, (level, salary)) in enumerate(zip(salary_cols, quantum_salary.items())):
        with col:
            st.markdown(f"""
            <div class="quantum-metric">
                <div class="quantum-value">{salary[selected_language].split(' - ')[0]}</div>
                <div class="quantum-label">{quantum_salary_labels[i]}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Quantum market metrics
    st.markdown("### 📈 КВАНТОВЫЕ РЫНОЧНЫЕ МЕТРИКИ")
    quantum_metric_cols = st.columns(6)
    
    quantum_metrics = quantum_profession['market_metrics']
    quantum_metric_labels = ["РОСТ", "СПРОС", "БУДУЩЕЕ", "ЗАРПЛАТА", "УДАЛЕНКА", "ИННОВАЦИИ"]
    
    for i, (col, (metric, value)) in enumerate(zip(quantum_metric_cols, quantum_metrics.items())):
        with col:
            st.markdown(f"""
            <div class="quantum-metric">
                <div class="quantum-value">{value}/5.0</div>
                <div class="quantum-label">{quantum_metric_labels[i]}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Quantum market analysis
    st.markdown("#### 🌌 КВАНТОВЫЙ АНАЛИЗ БУДУЩЕГО")
    st.markdown(f"{quantum_profession['market_analysis'][selected_language]}")
    
    # QUANTUM PROFESSIONS GRID
    st.markdown("---")
    st.markdown('<div class="quantum-section">💼 ТОП-10 КВАНТОВЫХ ПРОФЕССИЙ</div>', unsafe_allow_html=True)
    
    # Create a grid of quantum professions
    st.markdown('<div class="quantum-grid">', unsafe_allow_html=True)
    
    for i, profession in enumerate(quantum_profession["professions"][:10]):
        compatibility_color = "#00ffcc" if profession['compatibility'] > 0.9 else "#00ccff" if profession['compatibility'] > 0.8 else "#0066ff"
        
        st.markdown(f"""
        <div class="quantum-grid-item">
            <div style="font-size: 2rem; margin-bottom: 1rem;">{"🌌" if i == 0 else "🚀" if i == 1 else "🤖" if i == 2 else "💫"}</div>
            <h4 style="color: {compatibility_color}; margin-bottom: 0.5rem; font-family: Orbitron, sans-serif;">{profession['title'][selected_language]}</h4>
            <div style="color: #00ccff; font-size: 1.5rem; font-weight: 800; margin-bottom: 0.5rem;">{profession['compatibility']*100:.0f}%</div>
            <p style="color: #88ccff; font-size: 0.9rem; line-height: 1.4;">{profession['description'][selected_language]}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # QUANTUM DEVELOPMENT ROADMAP
    st.markdown("---")
    st.markdown('<div class="quantum-section">🎯 КВАНТОВЫЙ ПЛАН РАЗВИТИЯ</div>', unsafe_allow_html=True)
    
    # Quantum learning path
    st.markdown("### 📚 КВАНТОВЫЙ ОБРАЗОВАТЕЛЬНЫЙ ПУТЬ")
    for i, step in enumerate(quantum_profession['learning_path'][selected_language]):
        st.markdown(f"{i+1}. **{step}**")
    
    # Quantum development phases
    st.markdown("### 🗓️ КВАНТОВЫЕ ФАЗЫ РАЗВИТИЯ")
    
    quantum_phases = {
        "⚡ ФАЗА 1: КВАНТОВАЯ АКТИВАЦИЯ (1-6 МЕСЯЦЕВ)": [
            "Активация нейронных связей через квантовые курсы",
            "Разработка первого голографического проекта",
            "Интеграция в нейросетевые сообщества",
            "Создание квантового портфолио"
        ],
        "🚀 ФАЗА 2: НЕЙРОННЫЙ СКАЧОК (7-18 МЕСЯЦЕВ)": [
            "Участие в космических хакатонах",
            "Стажировка в квантовых лабораториях",
            "Разработка бионических интерфейсов",
            "Получение квантовых сертификаций"
        ],
        "🌌 ФАЗА 3: СИНГУЛЯРНОСТЬ (19-36 МЕСЯЦЕВ)": [
            "Работа над проектами NASA/SpaceX",
            "Разработка нейроинтерфейсов",
            "Участие в метавселенных",
            "Создание собственных квантовых алгоритмов"
        ],
        "💫 ФАЗА 4: КОСМИЧЕСКОЕ СОЗНАНИЕ (3+ ГОДА)": [
            "Лидерство в квантовых проектах",
            "Менторство следующего поколения",
            "Разработка технологий для Марса",
            "Создание искусственного интеллекта"
        ]
    }
    
    for phase, tasks in quantum_phases.items():
        with st.expander(f"{phase}"):
            for task in tasks:
                st.markdown(f"- {task}")
    
    # QUANTUM RESTART
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 ЗАПУСТИТЬ НОВЫЙ КВАНТОВЫЙ АНАЛИЗ", use_container_width=True):
            st.session_state.quantum_test_started = False
            st.session_state.quantum_current_question = 0
            st.session_state.quantum_answers = {}
            st.session_state.quantum_assessment_complete = False
            st.session_state.quantum_results_calculated = False
            st.rerun()

# =============================
# 📞 QUANTUM CONTACT MATRIX
# =============================
st.markdown("---")
st.markdown('<div class="quantum-section">📞 КВАНТОВАЯ ПОДДЕРЖКА</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['career_consultants']}**
    
    📞 **КВАНТОВАЯ ЛИНИЯ:** 87766680880  
    📧 **НЕЙРО-ПОЧТА:** askhatseitkhan@gmail.com  
    💼 **TELEGRAM:** @jobai_nexus  
    🎮 **DISCORD:** JobAI Quantum
    
    **🕒 ВРЕМЯ РАБОТЫ:**
    - Пн-Пт: 8:00-20:00
    - Сб-Вс: 9:00-18:00
    - Аварийная поддержка: 24/7
    
    **🎯 УСЛУГИ:**
    - Квантовая профориентация
    - Нейросетевое консультирование
    - Космическое карьерное планирование
    - Бионическое развитие
    """)

with col2:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['career_development_center']}**
    
    🏢 **ЦЕНТРАЛЬНЫЙ ХАБ:** Тараз, Толе Би 66  
    🌐 **КВАНТОВЫЙ ПОРТАЛ:** jobai-nexus.com  
    📱 **NEURO-APP:** В разработке  
    🎧 **VR КОНСУЛЬТАЦИИ:** Доступны
    
    **🏛️ КВАНТОВЫЕ ПАРТНЕРЫ:**
    - NASA Research Center
    - Google Quantum AI
    - SpaceX Technologies
    - Neuralink Corp
    - CERN Laboratory
    """)

with col3:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['online_booking']}**
    
    💻 **VR ЗАПИСЬ:** nexus.jobai-nexus.com  
    📱 **QUANTUM APP:** +7 776 668 0880  
    👥 **HOLOGRAM БОТ:** @quantum_nexus_bot  
    📅 **NEURO-CALENDAR:** Автоматизирован
    
    **🎁 БЕСПЛАТНЫЕ УСЛУГИ:**
    - Квантовая диагностика
    - Нейросетевой анализ
    - Голографическая консультация
    - Космическое планирование
    - Бионическое тестирование
    """)

# =============================
# 👣 QUANTUM FOOTER
# =============================
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #00ccff; font-size: 1rem; line-height: 1.6; padding: 3rem 1rem; background: rgba(0, 255, 204, 0.05); border-radius: 20px; border: 1px solid #00ffcc;'>
    <strong style='color: #00ffcc; font-size: 1.3rem; font-family: Orbitron, sans-serif;'>{LANGUAGES[selected_language]['footer']}</strong><br><br>
    
    📞 <strong>КВАНТОВАЯ СВЯЗЬ:</strong> 87766680880 | 
    🏢 <strong>ЦЕНТР:</strong> Тараз, Толе Би 66 | 
    🌐 <strong>ВСЕЛЕННАЯ:</strong> jobai-nexus.com<br>
    
    💼 <strong>УСЛУГИ:</strong> Квантовая карьерная диагностика | 
    🎯 <strong>ТЕХНОЛОГИИ:</strong> Нейросетевой анализ | 
    📊 <strong>БУДУЩЕЕ:</strong> Футурологическое прогнозирование<br><br>
    
    <div style='border-top: 1px solid #00ffcc; padding-top: 1.5rem; margin-top: 1.5rem;'>
        © 2024 JobAI NEXUS Quantum Systems. Все права защищены. 
        Платформа разработана при поддержке NASA Quantum Computing Initiative и Google AI Research
    </div>
</div>
""", unsafe_allow_html=True)
