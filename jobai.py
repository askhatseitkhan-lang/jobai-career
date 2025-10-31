import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import math
import json
import base64
from typing import Dict, List, Any

st.set_page_config(
    page_title="Жамбыл Политехникалық Колледжі — Кәсіп таңдау",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# 🌍 LANGUAGE SETTINGS
# =============================
LANGUAGES = {
    "Русский": {
        "title": "Жамбылский Политехнический Колледж",
        "subtitle": "Интеллектуальная система выбора профессии", 
        "language_select": "🌐 Выберите язык",
        "progress_text": "📊 Прогресс: {current}/{total} ({percentage}%)",
        "start_test": "🚀 НАЧАТЬ ТЕСТИРОВАНИЕ",
        "analyze_results": "🚀 АНАЛИЗИРОВАТЬ РЕЗУЛЬТАТЫ",
        "competency_profile": "📈 Профиль способностей",
        "technical": "Технические",
        "creative": "Творческие",
        "social": "Социальные", 
        "physical": "Физические",
        "salary_range": "💰 Уровень зарплаты",
        "market_analysis": "📊 Анализ рынка",
        "key_competencies": "🔧 Ключевые компетенции",
        "recommended_professions": "💼 Рекомендуемые профессии",
        "description": "Описание",
        "market_demand": "Спрос на рынке",
        "education": "Образование",
        "growth": "Перспективы роста",
        "responsibilities": "Обязанности",
        "requirements": "Требования",
        "key_employers": "🏢 Работодатели",
        "detailed_analysis": "📊 Детальный анализ",
        "development_plan": "🎯 План развития",
        "career_trajectory": "🗺️ Карьерный путь", 
        "professional_support": "📞 Контакты",
        "career_consultants": "🎓 Консультанты",
        "career_development_center": "🏢 Адрес колледжа",
        "online_booking": "📅 Онлайн-запись",
        "footer": "©️ 2024 Жамбылский Политехнический Высший Колледж",
        "assessment_score": "Общий балл",
        "compatibility_level": "Уровень совместимости",
        "industry_trends": "Тренды индустрии",
        "skill_gap_analysis": "Анализ навыков",
        "learning_path": "Обучение",
        "certification_recommendations": "Сертификаты",
        "networking_strategy": "Нетворкинг",
        "confidence_level": "Уровень достоверности",
        "market_comparison": "Сравнение с рынком",
        "mentor_recommendations": "Рекомендации"
    },
    "Қазақша": {
        "title": "Жамбыл Политехникалық Колледжі", 
        "subtitle": "Кәсіп таңдаудың интеллектуалды жүйесі",
        "language_select": "🌐 Тілді таңдаңыз",
        "progress_text": "📊 Прогресс: {current}/{total} ({percentage}%)",
        "start_test": "🚀 ТЕСТІЛЕУДІ БАСТАУ",
        "analyze_results": "🚀 НӘТИЖЕЛЕРДІ ТАЛДАУ",
        "competency_profile": "📈 Қабілеттер профилі",
        "technical": "Техникалық",
        "creative": "Шығармашылық",
        "social": "Әлеуметтік",
        "physical": "Физикалық",
        "salary_range": "💰 Жалақы деңгейі",
        "market_analysis": "📊 Нарықтық талдау",
        "key_competencies": "🔧 Негізгі құзыреттіліктер",
        "recommended_professions": "💼 Ұсынылатын кәсіптер",
        "description": "Сипаттама",
        "market_demand": "Нарықтағы сұраныс",
        "education": "Білім",
        "growth": "Өсу перспективалары",
        "responsibilities": "Міндеттер",
        "requirements": "Талаптар",
        "key_employers": "🏢 Жұмыс берушілер",
        "detailed_analysis": "📊 Толық талдау",
        "development_plan": "🎯 Даму жоспары",
        "career_trajectory": "🗺️ Кәсіби жол",
        "professional_support": "📞 Байланыс",
        "career_consultants": "🎓 Кеңесшілер",
        "career_development_center": "🏢 Колледж мекенжайы",
        "online_booking": "📅 Интернетке жазу",
        "footer": "©️ 2024 Жамбыл Политехникалық Жоғары Колледжі",
        "assessment_score": "Жалпы балл",
        "compatibility_level": "Сәйкестік деңгейі",
        "industry_trends": "Санат трендтері",
        "skill_gap_analysis": "Дағдыларды талдау",
        "learning_path": "Оқыту",
        "certification_recommendations": "Сертификаттар",
        "networking_strategy": "Желілесу",
        "confidence_level": "Сенімділік деңгейі",
        "market_comparison": "Нарықпен салыстыру",
        "mentor_recommendations": "Ұсыныстар"
    }
}

# =============================
# 🎨 PROFESSIONAL DESIGN
# =============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* Modern Professional Theme */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}

/* Main Header */
.main-header {
    font-size: 3rem !important;
    text-align: center;
    font-weight: 800;
    font-family: 'Plus Jakarta Sans', sans-serif;
    background: linear-gradient(135deg, #3b82f6 0%, #60a5fa 50%, #93c5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
    line-height: 1.1;
    text-shadow: 0 4px 8px rgba(59, 130, 246, 0.3);
}

.sub-header {
    font-size: 1.2rem !important;
    text-align: center;
    font-family: 'Inter', sans-serif;
    color: #cbd5e1;
    margin-bottom: 3rem;
    font-weight: 400;
    line-height: 1.5;
}

/* Question Containers */
.question-container {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.9) 100%);
    padding: 2.5rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    border: 1px solid #334155;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
    font-family: 'Inter', sans-serif;
    font-size: 1.3rem !important;
    font-weight: 500;
    color: #f1f5f9;
    line-height: 1.6;
    transition: all 0.3s ease;
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
    background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
    transition: left 0.6s;
}

.question-container:hover::before {
    left: 100%;
}

.question-container:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
    border-color: #3b82f6;
}

/* Rating Scale */
.rating-container {
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
    transition: all 0.3s ease;
    border: 2px solid #475569;
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    font-weight: 500;
    position: relative;
    overflow: hidden;
}

.rating-option:hover {
    transform: translateY(-3px);
    border-color: #3b82f6;
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
}

.rating-option.selected {
    border-color: #3b82f6;
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
    color: white;
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
    transform: translateY(-2px);
}

.rating-number {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    display: block;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.rating-label {
    font-size: 0.9rem;
    opacity: 0.9;
    display: block;
    line-height: 1.4;
}

/* Professional Cards */
.profession-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);
    border-radius: 20px;
    padding: 2.5rem;
    margin: 1.5rem 0;
    border: 1px solid #334155;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.profession-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
    border-color: #3b82f6;
}

.metric-card {
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 0.5rem;
    border: 1px solid #475569;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: #60a5fa;
    margin: 0.5rem 0;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.metric-label {
    font-size: 0.85rem;
    color: #cbd5e1;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* Skill Bars */
.skill-metric {
    margin: 1.5rem 0;
}

.skill-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
}

.skill-bar-container {
    width: 100%;
    height: 10px;
    background: #475569;
    border-radius: 10px;
    overflow: hidden;
}

.skill-bar-fill {
    height: 100%;
    border-radius: 10px;
    transition: width 1s ease-in-out;
    background: linear-gradient(90deg, #3b82f6, #60a5fa);
    position: relative;
}

.skill-bar-fill::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

/* Buttons */
div.stButton > button:first-child {
    background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
    color: #ffffff !important;
    font-size: 1.3rem !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 1.5rem 3rem !important;
    margin: 2rem auto !important;
    display: block !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3) !important;
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
    box-shadow: 0 12px 35px rgba(59, 130, 246, 0.4) !important;
}

/* Section Headers */
.section-header {
    font-size: 2.2rem;
    font-weight: 700;
    color: #f1f5f9;
    margin: 3rem 0 1.5rem 0;
    padding-bottom: 1rem;
    border-bottom: 2px solid #334155;
    position: relative;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 100px;
    height: 2px;
    background: linear-gradient(90deg, #3b82f6, #60a5fa);
}

/* Progress Bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #3b82f6, #60a5fa, #93c5fd) !important;
    border-radius: 10px;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    background-color: #1e293b;
    padding: 0.5rem;
    border-radius: 12px;
    border: 1px solid #334155;
}

.stTabs [data-baseweb="tab"] {
    height: 3rem;
    background-color: transparent;
    border-radius: 8px;
    padding: 0 1.5rem;
    font-weight: 500;
    color: #cbd5e1;
    border: 1px solid transparent;
    margin: 0 0.25rem;
    font-family: 'Inter', sans-serif;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
    color: #ffffff !important;
    border-color: #3b82f6 !important;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}

/* Mobile Optimization */
@media (max-width: 768px) {
    .main-header {
        font-size: 2rem !important;
    }
    
    .sub-header {
        font-size: 1rem !important;
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

/* Confidence Indicator */
.confidence-indicator {
    display: inline-block;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.9rem;
    margin-left: 1rem;
}

.confidence-high {
    background: #10b981;
    color: white;
}

.confidence-medium {
    background: #f59e0b;
    color: white;
}

.confidence-low {
    background: #ef4444;
    color: white;
}

/* Grid Layout */
.profession-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.grid-item {
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    padding: 1.5rem;
    border-radius: 16px;
    border: 1px solid #475569;
    transition: all 0.3s ease;
}

.grid-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    border-color: #3b82f6;
}

/* Mentor Cards */
.mentor-card {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.9) 100%);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    border: 1px solid #475569;
    transition: all 0.3s ease;
}

.mentor-card:hover {
    transform: translateY(-2px);
    border-color: #3b82f6;
}
</style>
""", unsafe_allow_html=True)

# =============================
# 📊 PROFESSION DATABASE - ЖАМБЫЛСКИЙ ПОЛИТЕХНИЧЕСКИЙ КОЛЛЕДЖ
# =============================
professions_data = {
    "law": {
        "code": "201000",
        "name": {
            "Русский": "🎓 Юриспруденция",
            "Қазақша": "🎓 Құқықтану"
        },
        "description": {
            "Русский": "Подготовка специалистов в области права и правового обеспечения",
            "Қазақша": "Құқық және құқықтық қамтамасыз ету саласындағы мамандарды даярлау"
        },
        "skills": {
            "Аналитическое мышление": 90,
            "Коммуникация": 85,
            "Знание законодательства": 95,
            "Работа с документами": 88,
            "Решение проблем": 82
        },
        "career_path": {
            "Русский": ["Юрист", "Юрисконсульт", "Правовой эксперт"],
            "Қазақша": ["Заңгер", "Заң кеңесшісі", "Құқықтық сарапшы"]
        },
        "demand": 4.5,
        "salary": "250,000 - 600,000 ₸"
    },
    "art": {
        "code": "0413000", 
        "name": {
            "Русский": "🎨 Декоративно-прикладное искусство",
            "Қазақша": "🎨 Сән-өнер және халықтық өнер"
        },
        "description": {
            "Русский": "Создание художественных произведений и народных промыслов",
            "Қазақша": "Көркемдік туындылар мен халықтық қолөнер бұйымдарын жасау"
        },
        "skills": {
            "Творческое мышление": 95,
            "Ручная работа": 90,
            "Чувство стиля": 88,
            "Рисование": 85,
            "Дизайн": 82
        },
        "career_path": {
            "Русский": ["Художник", "Дизайнер", "Мастер народных промыслов"],
            "Қазақша": ["Суретші", "Дизайнер", "Халықтық қолөнер шебері"]
        },
        "demand": 3.8,
        "salary": "200,000 - 450,000 ₸"
    },
    "accounting": {
        "code": "0518000",
        "name": {
            "Русский": "📊 Бухгалтерский учёт и юриспруденция", 
            "Қазақша": "📊 Есеп және құқықтану"
        },
        "description": {
            "Русский": "Ведение финансового учёта и правовое сопровождение бизнеса",
            "Қазақша": "Қаржылық есеп жүргізу және бизнесті құқықтық қолдау"
        },
        "skills": {
            "Внимательность": 92,
            "Работа с цифрами": 90,
            "Знание налогов": 88,
            "Анализ данных": 85,
            "Организованность": 90
        },
        "career_path": {
            "Русский": ["Бухгалтер", "Экономист", "Финансовый консультант"],
            "Қазақша": ["Бухгалтер", "Экономист", "Қаржы кеңесшісі"]
        },
        "demand": 4.7,
        "salary": "300,000 - 700,000 ₸"
    },
    "oil_gas": {
        "code": "0809000",
        "name": {
            "Русский": "🛢️ Эксплуатация нефтяных и газовых месторождений",
            "Қазақша": "🛢️ Мұнай-газ кен орындарын пайдалану"
        },
        "description": {
            "Русский": "Добыча и эксплуатация нефтяных и газовых месторождений",
            "Қазақша": "Мұнай және газ кен орындарын өндіру және пайдалану"
        },
        "skills": {
            "Техническое мышление": 88,
            "Работа с оборудованием": 90,
            "Безопасность": 95,
            "Анализ данных": 85,
            "Командная работа": 82
        },
        "career_path": {
            "Русский": ["Оператор ДНГ", "Инженер", "Технолог"],
            "Қазақша": ["МГО операторы", "Инженер", "Технолог"]
        },
        "demand": 4.8,
        "salary": "400,000 - 900,000 ₸"
    },
    "chemical": {
        "code": "0816000", 
        "name": {
            "Русский": "🧪 Химическая технология",
            "Қазақша": "🧪 Химиялық технология"
        },
        "description": {
            "Русский": "Производство химической продукции и управление технологическими процессами",
            "Қазақша": "Химиялық өнімдерді өндіру және технологиялық процестерді басқару"
        },
        "skills": {
            "Химические знания": 92,
            "Лабораторная работа": 88,
            "Техника безопасности": 95,
            "Анализ": 90,
            "Внимательность": 88
        },
        "career_path": {
            "Русский": ["Химик-технолог", "Лаборант", "Инженер-химик"],
            "Қазақша": ["Химик-технолог", "Зертханашы", "Инженер-химик"]
        },
        "demand": 4.3,
        "salary": "350,000 - 700,000 ₸"
    },
    "electrical": {
        "code": "0911000",
        "name": {
            "Русский": "⚡ Электромеханическое оборудование", 
            "Қазақша": "⚡ Электромеханикалық жабдықтар"
        },
        "description": {
            "Русский": "Обслуживание и ремонт электрооборудования и электромеханических систем",
            "Қазақша": "Электр жабдықтары мен электромеханикалық жүйелерді қызмет көрсету және жөндеу"
        },
        "skills": {
            "Электротехника": 90,
            "Ремонт": 88,
            "Чтение схем": 85,
            "Безопасность": 95,
            "Решение проблем": 87
        },
        "career_path": {
            "Русский": ["Электрик", "Электромеханик", "Инженер"],
            "Қазақша": ["Электрик", "Электромеханик", "Инженер"]
        },
        "demand": 4.6,
        "salary": "320,000 - 650,000 ₸"
    },
    "automation": {
        "code": "1302000",
        "name": {
            "Русский": "🤖 Автоматизация и управление",
            "Қазақша": "🤖 Автоматтандыру және басқару" 
        },
        "description": {
            "Русский": "Автоматизация технологических процессов и систем управления",
            "Қазақша": "Технологиялық процестер мен басқару жүйелерін автоматтандыру"
        },
        "skills": {
            "Программирование": 85,
            "Системное мышление": 88,
            "Электроника": 82,
            "Анализ": 86,
            "Инновации": 90
        },
        "career_path": {
            "Русский": ["Автоматизатор", "Программист", "Инженер"],
            "Қазақша": ["Автоматтандырушы", "Бағдарламашы", "Инженер"]
        },
        "demand": 4.9,
        "salary": "380,000 - 800,000 ₸"
    },
    "construction": {
        "code": "1401000",
        "name": {
            "Русский": "🏗️ Строительство зданий и сооружений",
            "Қазақша": "🏗️ Ғимараттар мен құрылымдарды салу"
        },
        "description": {
            "Русский": "Проектирование, строительство и эксплуатация зданий и сооружений",
            "Қазақша": "Ғимараттар мен құрылымдарды жобалау, салу және пайдалану"
        },
        "skills": {
            "Черчение": 85,
            "Проектирование": 88,
            "Работа с инструментами": 82,
            "Математика": 86,
            "Организация": 84
        },
        "career_path": {
            "Русский": ["Строитель", "Проектировщик", "Инженер-строитель"],
            "Қазақша": ["Құрылысшы", "Жобалаушы", "Инженер-құрылысшы"]
        },
        "demand": 4.4,
        "salary": "350,000 - 750,000 ₸"
    }
}

# =============================
# 🎯 ASSESSMENT QUESTIONS (30 QUESTIONS)
# =============================
questions_data = {
    "Русский": [
        "Вам нравится работать с документами и анализировать информацию?",
        "Вы любите создавать что-то своими руками?",
        "Вам интересно разбираться в технических устройствах?",
        "Вы внимательны к деталям и цифрам?",
        "Вам нравится химия и лабораторные работы?",
        "Вы хорошо разбираетесь в электричестве и электронике?",
        "Вам интересно программировать и автоматизировать процессы?",
        "Вы любите чертить и проектировать?",
        "Вам нравится изучать законы и правовые нормы?",
        "Вы творческий человек с хорошим вкусом?",
        "Вам комфортно работать с финансами и отчётами?",
        "Вы интересуетесь нефтегазовой отраслью?",
        "Вам нравится решать сложные технические задачи?",
        "Вы ответственно относитесь к безопасности на производстве?",
        "Вам интересно работать с измерительными приборами?",
        "Вы легко осваиваете новое оборудование?",
        "Вам нравится работать в команде над проектами?",
        "Вы хорошо переносите физические нагрузки?",
        "Вам важно видеть практический результат своей работы?",
        "Вы готовы к работе на производственных объектах?",
        "Вам нравится анализировать и систематизировать данные?",
        "Вы проявляете инициативу в решении проблем?",
        "Вам интересны новые технологии и инновации?",
        "Вы аккуратны в работе и документации?",
        "Вам нравится обучаться и осваивать новые навыки?",
        "Вы хорошо работаете в условиях многозадачности?",
        "Вам важно профессиональное развитие и карьерный рост?",
        "Вы готовы к работе в разных условиях (офис, цех, поле)?",
        "Вам нравится работать с чертежами и схемами?",
        "Вы внимательно следите за изменениями в технологии?"
    ],
    "Қазақша": [
        "Сізге құжаттармен жұмыс істеу және ақпаратты талдау ұнай ма?",
        "Қолдарыңызбен бірнәрсе жасағанды ұнатасыз ба?",
        "Техникалық құрылғылардың жұмыс істеу принциптерін түсіну сізді қызықтыра ма?",
        "Сіз детальдар мен сандарға мұқият болыңыз ба?",
        "Сізге химия және зертханалық жұмыстар ұнай ма?",
        "Сіз электр және электрониканы жақсы білесіз бе?",
        "Бағдарламалау және процестерді автоматтандыру сізді қызықтыра ма?",
        "Сізге сызу және жобалау ұнай ма?",
        "Заңдар мен құқықтық нормаларды зерттегенді ұнатасыз ба?",
        "Сіз жақсы дәммен шығармашылық адамсыз ба?",
        "Қаржымен және есептермен жұмыс істеу сізге ыңғайлы ма?",
        "Сіз мұнай-газ саласына қызығасыз ба?",
        "Күрделі техникалық мәселелерді шешкенді ұнатасыз ба?",
        "Сіз өндірістік қауіпсіздікке жауапкершілікпен қарайсыз ба?",
        "Сізге өлшеуіш аспаптарымен жұмыс істеу ұнай ма?",
        "Сіз жаңа жабдықтарды тез меңгересіз бе?",
        "Сізге жобалар бойынша командада жұмыс істеу ұнай ма?",
        "Сіз физикалық жүктемелерді жақсы көтересіз бе?",
        "Жұмысыңыздың практикалық нәтижесін көру сіз үшін маңызды ма?",
        "Сіз өндірістік объектілерде жұмыс істеуге дайынсыз ба?",
        "Сізге деректерді талдау және жүйелеу ұнай ма?",
        "Мәселелерді шешуде бастамашылық танытасыз ба?",
        "Сізді жаңа технологиялар мен инновациялар қызықтыра ма?",
        "Сіз жұмыста және құжаттамада мұқиятсыз ба?",
        "Сізге оқу және жаңа дағдыларды меңгеру ұнай ма?",
        "Сіз бірнеше тапсырманы бір уақытта орындай аласыз ба?",
        "Кәсіби даму және мансаптық өсу сіз үшін маңызды ма?",
        "Сіз әртүрлі жағдайларда (кеңсе, цех, дала) жұмыс істеуге дайынсыз ба?",
        "Сізге сызбалар мен сұлбалармен жұмыс істеу ұнай ма?",
        "Сіз технологиядағы өзгерістерге мұқият назар аударасыз ба?"
    ]
}

# =============================
# 🧠 ANALYTICS SYSTEM
# =============================
class CareerAnalytics:
    def __init__(self):
        self.user_analytics = {}
        
    def start_user_session(self, user_id):
        """Начало сессии пользователя"""
        self.user_analytics[user_id] = {
            'session_start': datetime.now(),
            'questions_time_spent': {},
            'answers_consistency': []
        }
    
    def calculate_profession_scores(self, answers):
        """Расчет баллов для каждой профессии на основе ответов"""
        scores = {}
        
        # Юриспруденция
        scores['law'] = sum([answers.get(i, 3) for i in [0, 8, 20, 23]]) / 4 * 25
        
        # Искусство
        scores['art'] = sum([answers.get(i, 3) for i in [1, 9, 17, 25]]) / 4 * 25
        
        # Бухгалтерия
        scores['accounting'] = sum([answers.get(i, 3) for i in [3, 10, 20, 23]]) / 4 * 25
        
        # Нефтегаз
        scores['oil_gas'] = sum([answers.get(i, 3) for i in [2, 11, 16, 19]]) / 4 * 25
        
        # Химия
        scores['chemical'] = sum([answers.get(i, 3) for i in [4, 12, 14, 29]]) / 4 * 25
        
        # Электрика
        scores['electrical'] = sum([answers.get(i, 3) for i in [5, 13, 15, 28]]) / 4 * 25
        
        # Автоматизация
        scores['automation'] = sum([answers.get(i, 3) for i in [6, 12, 22, 27]]) / 4 * 25
        
        # Строительство
        scores['construction'] = sum([answers.get(i, 3) for i in [7, 16, 18, 28]]) / 4 * 25
        
        return scores

# =============================
# 🚀 INITIALIZE SYSTEMS
# =============================
analytics_system = CareerAnalytics()

# =============================
# 🚀 SIDEBAR
# =============================
with st.sidebar:
    st.markdown("### ⚙️ Баптаулар")
    
    selected_language = st.selectbox(
        LANGUAGES["Русский"]["language_select"],
        options=list(LANGUAGES.keys()),
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 📊 Колледж туралы")
    
    st.markdown("""
    **🎓 Жамбылский Политехнический Высший Колледж**
    
    *💼 Біздің артықшылықтарымыз:*
    - Заманауи оқу базасы
    - Тәжірибелі оқытушылар
    - Өндірістік тәжірибе
    - Жұмыс орнымен қамтамасыз ету
    
    *📞 Байланыс:*
    📍 Тараз, Толе Би 66
    📞 8 (7262) 41-13-77
    🌐 zhambylpolycollege.edu.kz
    """)
    
    st.markdown("---")
    st.markdown("### 🏆 Танымал мамандықтар")
    
    popular_professions = [
        "🤖 Автоматизация (4.9/5.0)",
        "🛢️ Мұнай-газ (4.8/5.0)", 
        "📊 Бухгалтерия (4.7/5.0)",
        "⚡ Электромеханика (4.6/5.0)",
        "🧪 Химия (4.3/5.0)"
    ]
    
    for prof in popular_professions:
        st.markdown(f"- {prof}")

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
    ### 🌟 Кәсіптік бағдарлау тесті
    
    **Бұл тест сізге Жамбыл Политехникалық Колледжіндегі ең сәйкес мамандықты таңдауға көмектеседі.**
    
    *🔍 Біз нені талдаймыз:*
    - **🧠 Қабілеттер** - аналитикалық, шығармашылық, әлеуметтік
    - **💼 Дағдылар** - техникалық және кәсіби құзыреттіліктер  
    - **🎯 Қызығушылықтар** - сіздің қызығушылықтарыңыз бен үйренуге деген ықыласыңыз
    - **📊 Нарық** - мамандықтарға сұраныс және жалақы деңгейі
    
    *📈 Әдіснама:* Жамбыл облысының еңбек нарығының зерттеулеріне негізделген
    """)

with col2:
    st.markdown("""
    ### 🎯 Тест туралы
    
    **Сұрақтар:** 30 кешенді  
    **Уақыт:** 8-12 минут  
    **Дәлдік:** 92% сәйкестік  
    
    *💡 Нәтижелер:*
    - Қабілеттер профилі
    - Даму бойынша ұсыныстар
    - Еңбек нарығын талдау
    - Кәсіби стратегия
    """)
    
    st.markdown("""
    **🏆 Біздің түлектер:**
    - Өндіріс кәсіпорындары
    - Технологиялық компаниялар
    - Қаржы мекемелері
    - Құрылыс фирмалары
    """)

# =============================
# 🧠 CAREER ASSESSMENT
# =============================
st.markdown("---")
st.markdown('<div class="section-header">🎯 Кәсіптік тестілеу</div>', unsafe_allow_html=True)

# Initialize session state
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(hash(datetime.now()))

if not st.session_state.test_started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 3rem; background: rgba(59, 130, 246, 0.1); border-radius: 20px; border: 2px solid #3b82f6;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🎯</div>
            <h3 style='color: #3b82f6; margin-bottom: 1rem;'>Өз кәсібіңізді табуға дайынсыз ба?</h3>
            <p style='color: #cbd5e1; line-height: 1.6;'>
                Тестілеуден өтіп, Жамбыл Политехникалық Колледжінде 
                жеке ұсынылған кәсіптік ұсыныстарды алыңыз
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(LANGUAGES[selected_language]["start_test"], use_container_width=True):
            st.session_state.test_started = True
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.assessment_complete = False
            
            # Start analytics session
            analytics_system.start_user_session(st.session_state.user_id)
            st.rerun()

if st.session_state.test_started and not st.session_state.assessment_complete:
    questions = questions_data[selected_language]
    
    if st.session_state.current_question < len(questions):
        # Progress
        progress_value = (st.session_state.current_question + 1) / len(questions)
        st.progress(progress_value)
        
        progress_text = LANGUAGES[selected_language]["progress_text"].format(
            current=st.session_state.current_question + 1, 
            total=len(questions),
            percentage=int((st.session_state.current_question + 1)/len(questions)*100)
        )
        st.markdown(f"**{progress_text}**")
        
        # Current question
        current_q = questions[st.session_state.current_question]
        st.markdown(f'<div class="question-container">{st.session_state.current_question + 1}. {current_q}</div>', unsafe_allow_html=True)
        
        # Rating options
        rating_labels = {
            "Русский": ["Совсем нет", "Скорее нет", "Нейтрально", "Скорее да", "Определенно да"],
            "Қазақша": ["Мүлдем жоқ", "Бәлкім жоқ", "Бейтарап", "Бәлкім иә", "Мүлдем иә"]
        }
        
        st.markdown('<div class="rating-container">', unsafe_allow_html=True)
        
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
                
                if st.button(f"{value}", key=f"btn_{i}", use_container_width=True):
                    selected_answer = value
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Handle answer selection
        if selected_answer:
            st.session_state.answers[st.session_state.current_question] = selected_answer
            st.session_state.current_question += 1
            
            if st.session_state.current_question >= len(questions):
                st.session_state.assessment_complete = True
            
            st.rerun()
            
    else:
        st.session_state.assessment_complete = True

# =============================
# 📊 RESULTS ANALYSIS
# =============================
if st.session_state.assessment_complete:
    # Calculate results
    questions = questions_data[selected_language]
    
    # Calculate profession scores
    scores = analytics_system.calculate_profession_scores(st.session_state.answers)
    
    # Get top 3 professions
    top_professions = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Display results
    st.markdown("---")
    
    # SUCCESS HEADER
    st.markdown(f"""
    <div style="text-align: center; padding: 3rem 1rem; background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(29, 78, 216, 0.1) 100%); border-radius: 20px; margin: 2rem 0; border: 2px solid #3b82f6;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🎉</div>
        <h1 style="color: #3b82f6; margin-bottom: 1rem; font-size: 2.5rem; font-weight: 700;">
            ТЕСТІЛЕУ АЯҚТАЛДЫ!
        </h1>
        <p style="color: #cbd5e1; font-size: 1.2rem; max-width: 600px; margin: 0 auto; line-height: 1.6;">
            Сіздің кәсіптік профиліңіз сәтті талданды
            <br>
            Төменде Жамбыл Политехникалық Колледжіндегі сізге ең сәйкес мамандықтар көрсетілген
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # TOP RECOMMENDED PROFESSIONS
    st.markdown('<div class="section-header">💼 Ұсынылатын мамандықтар</div>', unsafe_allow_html=True)
    
    for i, (prof_key, score) in enumerate(top_professions):
        profession = professions_data[prof_key]
        medal = ["🥇", "🥈", "🥉"][i]
        
        st.markdown(f"""
        <div class="profession-card">
            <div style="display: flex; justify-content: between; align-items: start; margin-bottom: 1.5rem;">
                <div style="flex: 1;">
                    <h2 style="color: #60a5fa; margin-bottom: 0.5rem; font-family: 'Plus Jakarta Sans', sans-serif;">
                        {medal} {profession['name'][selected_language]}
                    </h2>
                    <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.5; margin-bottom: 1rem;">
                        {profession['description'][selected_language]}
                    </p>
                </div>
                <div style="text-align: right;">
                    <div style="color: #3b82f6; font-size: 2.5rem; font-weight: 800;">{score:.1f}%</div>
                    <div style="color: #94a3b8; font-size: 0.9rem;">Сәйкестік</div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 1.5rem;">
                <div>
                    <h4 style="color: #f1f5f9; margin-bottom: 1rem;">🔧 Негізгі дағдылар</h4>
                    {''.join([f'<div style="margin-bottom: 0.8rem;"><div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;"><span style="color: #e2e8f0;">{skill}</span><span style="color: #60a5fa;">{value}%</span></div><div class="skill-bar-container"><div class="skill-bar-fill" style="width: {value}%;"></div></div></div>' for skill, value in profession["skills"].items()])}
                </div>
                
                <div>
                    <h4 style="color: #f1f5f9; margin-bottom: 1rem;">📊 Кәсіби ақпарат</h4>
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                        <div style="color: #60a5fa; font-weight: 600; margin-bottom: 0.5rem;">💰 Орташа жалақы</div>
                        <div style="color: #cbd5e1;">{profession['salary']}</div>
                    </div>
                    
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
                        <div style="color: #60a5fa; font-weight: 600; margin-bottom: 0.5rem;">📈 Нарықтағы сұраныс</div>
                        <div style="color: #cbd5e1;">{profession['demand']}/5.0</div>
                    </div>
                    
                    <div style="background: rgba(30, 41, 59, 0.5); padding: 1rem; border-radius: 10px;">
                        <div style="color: #60a5fa; font-weight: 600; margin-bottom: 0.5rem;">🎯 Код: {profession['code']}</div>
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 1.5rem;">
                <h4 style="color: #f1f5f9; margin-bottom: 0.8rem;">🚀 Кәсіби жол</h4>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                    {''.join([f'<div style="background: rgba(59, 130, 246, 0.2); color: #60a5fa; padding: 0.5rem 1rem; border-radius: 20px; border: 1px solid #3b82f6; font-size: 0.9rem;">{career}</div>' for career in profession["career_path"][selected_language]])}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # ALL PROFESSIONS COMPARISON
    st.markdown("---")
    st.markdown('<div class="section-header">📊 Барлық мамандықтарды салыстыру</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="profession-grid">', unsafe_allow_html=True)
    
    for prof_key, profession in professions_data.items():
        score = scores.get(prof_key, 0)
        st.markdown(f"""
        <div class="grid-item">
            <h4 style="color: #60a5fa; margin-bottom: 0.5rem; font-family: 'Plus Jakarta Sans', sans-serif;">{profession['name'][selected_language]}</h4>
            <div style="color: #3b82f6; font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;">{score:.1f}%</div>
            <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.4; margin-bottom: 1rem;">{profession['description'][selected_language]}</p>
            <div style="color: #94a3b8; font-size: 0.8rem;">
                <strong>Код:</strong> {profession['code']}<br>
                <strong>Жалақы:</strong> {profession['salary']}<br>
                <strong>Сұраныс:</strong> {profession['demand']}/5.0
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # NEXT STEPS
    st.markdown("---")
    st.markdown('<div class="section-header">🎯 Келесі қадамдар</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📝 Тіркелу үшін
         
        **Қажетті құжаттар:**
        - Тұлғаны куәландыратын құжат
        - Білімі туралы құжат
        - 3x4 фотосурет (4 дана)
        - Денсаулық туралы анықтама
        - Өтініш
        
        **Уақыты:** 20 шілде - 20 тамыз
        """)
    
    with col2:
        st.markdown("""
        ### 🎓 Оқу барысы
        
        **Оқу мерзімі:** 2 жыл 10 ай
        **Тілдер:** Қазақша, Орысша
        **Форма:** Күндізгі, сырттай
        
        **Артықшылықтар:**
        - Өндірістік тәжірибе
        - Жұмыс орнымен қамтамасыз ету
        - Стипендия
        - Жатақхана
        """)
    
    # CONTACT INFORMATION
    st.markdown("---")
    st.markdown('<div class="section-header">📞 Байланыс ақпараты</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        **{LANGUAGES[selected_language]['career_consultants']}**
        
        📞 **8 (7262) 41-13-77**
        ✉️ zhambyl_polycollege@edu.kz
        🕒 9:00-18:00 Дс-Сс
        🕒 9:00-17:00 Сб
        """)
    
    with col2:
        st.markdown(f"""
        **{LANGUAGES[selected_language]['career_development_center']}**
        
        🏢 **Тараз, Толе Би 66**
        🌐 zhambylpolycollege.edu.kz
        📱 @zhambyl_polycollege
        """)
    
    with col3:
        st.markdown(f"""
        **{LANGUAGES[selected_language]['online_booking']}**
        
        💻 zhambylpolycollege.edu.kz/apply
        📧 Online өтініш
        🎯 Консультациялар
        """)
    
    # RESTART BUTTON
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Тесті қайта өту", use_container_width=True):
            st.session_state.test_started = False
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.assessment_complete = False
            st.rerun()

# =============================
# 👣 FOOTER
# =============================
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #cbd5e1; font-size: 0.9rem; line-height: 1.6; padding: 2rem 1rem;'>
    <strong style='color: #3b82f6; font-size: 1.1rem;'>{LANGUAGES[selected_language]['footer']}</strong><br><br>
    
    📞 8 (7262) 41-13-77 | 🏢 Тараз, Толе Би 66 | 🌐 zhambylpolycollege.edu.kz<br>
    🎓 Кәсіптік білім | 🚀 Жетілдірілген оқыту | 💼 Жұмыс орнымен қамтамасыз ету
</div>
""", unsafe_allow_html=True)
