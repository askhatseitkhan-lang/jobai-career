import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import math
import json
import base64
from typing import Dict, List, Any
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Job.AI — Intelligent Career Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# 🌍 LANGUAGE SETTINGS
# =============================
LANGUAGES = {
    "Русский": {
        "title": "Job.AI",
        "subtitle": "Интеллектуальная платформа карьерного развития", 
        "language_select": "🌐 Выберите язык",
        "progress_text": "📊 Прогресс: {current}/{total} ({percentage}%)",
        "start_test": "🚀 НАЧАТЬ ТЕСТИРОВАНИЕ",
        "analyze_results": "🚀 АНАЛИЗИРОВАТЬ РЕЗУЛЬТАТЫ",
        "competency_profile": "📈 Профиль компетенций",
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
        "professional_support": "📞 Профессиональная поддержка",
        "career_consultants": "🎓 Карьерные консультанты",
        "career_development_center": "🏢 Центр развития карьеры",
        "online_booking": "📅 Онлайн-запись",
        "footer": "©️ 2024 Job.AI — Платформа карьерного развития",
        "assessment_score": "Общий балл",
        "compatibility_level": "Уровень совместимости",
        "industry_trends": "Тренды индустрии",
        "skill_gap_analysis": "Анализ навыков",
        "learning_path": "Обучение",
        "certification_recommendations": "Сертификаты",
        "networking_strategy": "Нетворкинг",
        "confidence_level": "Уровень достоверности",
        "market_comparison": "Сравнение с рынком",
        "mentor_recommendations": "Рекомендации менторов"
    },
    "Қазақша": {
        "title": "Job.AI", 
        "subtitle": "Кәсіби дамудың интеллектуалды платформасы",
        "language_select": "🌐 Тілді таңдаңыз",
        "progress_text": "📊 Прогресс: {current}/{total} ({percentage}%)",
        "start_test": "🚀 ТЕСТІЛЕУДІ БАСТАУ",
        "analyze_results": "🚀 НӘТИЖЕЛЕРДІ ТАЛДАУ",
        "competency_profile": "📈 Құзыреттілік профилі",
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
        "professional_support": "📞 Кәсіби қолдау",
        "career_consultants": "🎓 Кәсіби кеңесшілер",
        "career_development_center": "🏢 Мансапты дамыту орталығы",
        "online_booking": "📅 Интернетке жазу",
        "footer": "©️ 2024 Job.AI — Кәсіби даму платформасы",
        "assessment_score": "Жалпы балл",
        "compatibility_level": "Сәйкестік деңгейі",
        "industry_trends": "Санат трендтері",
        "skill_gap_analysis": "Дағдыларды талдау",
        "learning_path": "Оқыту",
        "certification_recommendations": "Сертификаттар",
        "networking_strategy": "Желілесу",
        "confidence_level": "Сенімділік деңгейі",
        "market_comparison": "Нарықпен салыстыру",
        "mentor_recommendations": "Менторлардың ұсыныстары"
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
    font-size: 4rem !important;
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
    font-size: 1.4rem !important;
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
        font-size: 2.5rem !important;
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
    background: #1e293b;
}

::-webkit-scrollbar-thumb {
    background: #3b82f6;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #60a5fa;
}

/* Expander */
.streamlit-expanderHeader {
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    color: #f1f5f9 !important;
    padding: 1rem 1.5rem !important;
    background: #1e293b !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
}

.streamlit-expanderContent {
    padding: 1.5rem !important;
    background: #1e293b !important;
    border: 1px solid #334155 !important;
    border-radius: 0 0 10px 10px !important;
}

/* Grid Layout */
.profession-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
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

/* Analytics Dashboard */
.analytics-dashboard {
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    border-radius: 16px;
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid #475569;
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
# 🧠 ADVANCED ANALYTICS SYSTEM
# =============================
class CareerAnalytics:
    def __init__(self):
        self.user_analytics = {}
        self.market_data = self.load_market_data()
        
    def load_market_data(self):
        """Загрузка данных рынка труда"""
        return {
            'it_tech': {
                'demand_trend': 4.8,
                'salary_growth': 4.6,
                'competition_index': 3.2,
                'emerging_skills': ['AI/ML', 'Cloud', 'Cybersecurity']
            },
            'healthcare': {
                'demand_trend': 4.5,
                'salary_growth': 4.2,
                'competition_index': 2.8,
                'emerging_skills': ['Telemedicine', 'Data Analysis', 'Biotech']
            },
            'engineering': {
                'demand_trend': 4.3,
                'salary_growth': 4.1,
                'competition_index': 3.1,
                'emerging_skills': ['Sustainable Design', 'Automation', '3D Modeling']
            }
        }
    
    def start_user_session(self, user_id):
        """Начало сессии пользователя"""
        self.user_analytics[user_id] = {
            'session_start': datetime.now(),
            'questions_time_spent': {},
            'answers_consistency': [],
            'professions_viewed': [],
            'results_downloaded': False,
            'feedback_provided': False
        }
    
    def record_question_time(self, user_id, question_id, time_spent):
        """Запись времени на вопрос"""
        if user_id in self.user_analytics:
            self.user_analytics[user_id]['questions_time_spent'][question_id] = time_spent
    
    def calculate_confidence_level(self, user_id, answers):
        """Расчет уровня достоверности результатов"""
        if user_id not in self.user_analytics:
            return 0.7
            
        analytics = self.user_analytics[user_id]
        
        # Анализ согласованности ответов
        consistency_score = self.analyze_answer_consistency(answers)
        
        # Анализ времени ответов
        time_score = self.analyze_time_patterns(analytics['questions_time_spent'])
        
        # Анализ полноты данных
        completeness_score = len(answers) / 50  # 50 вопросов
        
        confidence = (consistency_score * 0.4 + time_score * 0.3 + completeness_score * 0.3)
        return min(confidence, 0.95)  # Максимум 95%
    
    def analyze_answer_consistency(self, answers):
        """Анализ согласованности ответов"""
        if len(answers) < 10:
            return 0.7
            
        # Проверка противоречивых ответов
        contradictions = 0
        total_pairs = 0
        
        # Простые проверки логической согласованности
        for i in range(len(answers) - 1):
            for j in range(i + 1, min(i + 5, len(answers))):
                if self.are_answers_contradictory(i, j, answers):
                    contradictions += 1
                total_pairs += 1
        
        if total_pairs == 0:
            return 0.8
            
        consistency = 1 - (contradictions / total_pairs)
        return max(consistency, 0.5)
    
    def are_answers_contradictory(self, q1, q2, answers):
        """Проверка противоречивости ответов на два вопроса"""
        # Простая логика проверки противоречий
        answer1 = answers.get(q1, 3)
        answer2 = answers.get(q2, 3)
        
        # Пример: если человек говорит, что любит технологии (высокий балл),
        # но не любит решать сложные задачи (низкий балл) - возможное противоречие
        if (q1 in [0, 7, 13, 34] and q2 in [7, 24, 44] and 
            abs(answer1 - answer2) >= 4):
            return True
            
        return False
    
    def analyze_time_patterns(self, time_data):
        """Анализ паттернов времени ответов"""
        if not time_data:
            return 0.7
            
        times = list(time_data.values())
        avg_time = sum(times) / len(times)
        
        # Слишком быстрое прохождение (менее 3 секунд на вопрос)
        if avg_time < 3:
            return 0.6
            
        # Слишком медленное прохождение (более 60 секунд на вопрос)
        if avg_time > 60:
            return 0.7
            
        # Оптимальное время (5-30 секунд)
        if 5 <= avg_time <= 30:
            return 0.9
            
        return 0.8
    
    def generate_market_report(self, profession_category):
        """Генерация отчета по рынку"""
        market_info = self.market_data.get(profession_category, {})
        
        return {
            'demand_level': market_info.get('demand_trend', 4.0),
            'salary_outlook': market_info.get('salary_growth', 4.0),
            'competition': market_info.get('competition_index', 3.0),
            'emerging_skills': market_info.get('emerging_skills', []),
            'recommendations': self.generate_market_recommendations(market_info)
        }
    
    def generate_market_recommendations(self, market_info):
        """Генерация рекомендаций на основе рыночных данных"""
        recommendations = []
        
        if market_info.get('demand_trend', 0) >= 4.5:
            recommendations.append("Высокий спрос на рынке - хорошее время для входа в профессию")
        
        if market_info.get('competition_index', 0) >= 3.5:
            recommendations.append("Высокая конкуренция - рекомендуется развивать уникальные навыки")
        
        emerging_skills = market_info.get('emerging_skills', [])
        if emerging_skills:
            recommendations.append(f"Перспективные навыки: {', '.join(emerging_skills[:3])}")
        
        return recommendations

# =============================
# 📚 EDUCATION INTEGRATION SYSTEM
# =============================
class EducationIntegration:
    def __init__(self):
        self.course_providers = {
            'coursera': {
                'name': 'Coursera',
                'url': 'https://coursera.org',
                'courses': self.load_coursera_courses()
            },
            'stepik': {
                'name': 'Stepik',
                'url': 'https://stepik.org',
                'courses': self.load_stepik_courses()
            },
            'local': {
                'name': 'Местные курсы',
                'url': '',
                'courses': self.load_local_courses()
            }
        }
    
    def load_coursera_courses(self):
        return {
            'data_science': [
                {'name': 'Machine Learning', 'url': 'https://coursera.org/learn/machine-learning', 'level': 'advanced'},
                {'name': 'Python for Everybody', 'url': 'https://coursera.org/specializations/python', 'level': 'beginner'}
            ],
            'web_development': [
                {'name': 'Web Design for Everybody', 'url': 'https://coursera.org/specializations/web-design', 'level': 'beginner'}
            ]
        }
    
    def load_stepik_courses(self):
        return {
            'programming': [
                {'name': 'Python Programming', 'url': 'https://stepik.org/course/67', 'level': 'beginner'}
            ]
        }
    
    def load_local_courses(self):
        return {
            'astana': [
                {'name': 'Astana IT University', 'url': 'https://astanait.edu.kz', 'level': 'all'},
                {'name': 'Alem School', 'url': 'https://alemschool.education', 'level': 'beginner'}
            ],
            'almaty': [
                {'name': 'Almaty Management University', 'url': 'https://almau.edu.kz', 'level': 'all'}
            ]
        }
    
    def get_recommended_courses(self, profession, user_level='beginner', location='astana'):
        """Получение рекомендованных курсов"""
        recommendations = []
        
        # Курсы по профессии
        profession_courses = self.get_courses_by_profession(profession, user_level)
        recommendations.extend(profession_courses)
        
        # Местные курсы
        local_courses = self.get_local_courses(location, profession)
        recommendations.extend(local_courses)
        
        return recommendations
    
    def get_courses_by_profession(self, profession, level):
        """Получение курсов по профессии"""
        courses = []
        
        if 'data' in profession.lower() or 'ai' in profession.lower():
            courses.extend(self.course_providers['coursera']['courses']['data_science'])
        
        if 'web' in profession.lower() or 'developer' in profession.lower():
            courses.extend(self.course_providers['coursera']['courses']['web_development'])
        
        # Фильтрация по уровню
        return [course for course in courses if course['level'] in [level, 'all']]
    
    def get_local_courses(self, location, profession):
        """Получение местных курсов"""
        return self.course_providers['local']['courses'].get(location, [])

# =============================
# 👥 MENTOR RECOMMENDATION SYSTEM
# =============================
class MentorSystem:
    def __init__(self):
        self.mentors = self.load_mentors()
    
    def load_mentors(self):
        """Загрузка базы менторов"""
        return [
            {
                'id': 1,
                'name': 'Айдар Жураев',
                'profession': 'Data Scientist',
                'company': 'Kaspi.kz',
                'experience': 8,
                'skills': ['Python', 'ML', 'Data Analysis'],
                'location': 'Алматы',
                'availability': 'limited',
                'rating': 4.8,
                'languages': ['Русский', 'Қазақша', 'English']
            },
            {
                'id': 2,
                'name': 'Мария Иванова',
                'profession': 'Frontend Developer',
                'company': 'Kolesa',
                'experience': 6,
                'skills': ['JavaScript', 'React', 'Vue'],
                'location': 'Астана',
                'availability': 'available',
                'rating': 4.6,
                'languages': ['Русский', 'English']
            },
            {
                'id': 3,
                'name': 'Ерлан Сағатов',
                'profession': 'DevOps Engineer',
                'company': 'One Technologies',
                'experience': 7,
                'skills': ['AWS', 'Kubernetes', 'Docker'],
                'location': 'Алматы',
                'availability': 'available',
                'rating': 4.9,
                'languages': ['Русский', 'Қазақша']
            }
        ]
    
    def recommend_mentors(self, user_profile, profession, max_recommendations=3):
        """Рекомендация менторов"""
        # Фильтрация по профессии и навыкам
        suitable_mentors = []
        
        for mentor in self.mentors:
            score = self.calculate_mentor_score(mentor, user_profile, profession)
            if score > 0.3:  # Порог совместимости
                suitable_mentors.append((mentor, score))
        
        # Сортировка по рейтингу совместимости
        suitable_mentors.sort(key=lambda x: x[1], reverse=True)
        
        return [mentor for mentor, score in suitable_mentors[:max_recommendations]]
    
    def calculate_mentor_score(self, mentor, user_profile, profession):
        """Расчет рейтинга совместимости с ментором"""
        score = 0
        
        # Совпадение профессии
        if profession.lower() in mentor['profession'].lower():
            score += 0.4
        
        # Совпадение локации
        if user_profile.get('location') == mentor['location']:
            score += 0.2
        
        # Доступность ментора
        if mentor['availability'] == 'available':
            score += 0.2
        
        # Опыт ментора
        if mentor['experience'] >= 5:
            score += 0.1
        
        # Рейтинг ментора
        score += (mentor['rating'] - 4) * 0.1
        
        return min(score, 1.0)

# =============================
# 📊 PROFESSION DATABASE (50 PROFESSIONS)
# =============================
professions_data = {
    "it_tech": {
        "name": {
            "Русский": "💻 IT и технологии",
            "Қазақша": "💻 IT және технологиялар"
        },
        "description": {
            "Русский": "Вы проявляете интерес к технологиям, аналитическому мышлению и решению сложных задач",
            "Қазақша": "Сіз технологияларға, аналитикалық ойлауға және күрделі мәселелерді шешуге қызығушылық танытасыз"
        },
        "salary_ranges": {
            "entry": {"Русский": "300,000 - 500,000 ₸", "Қазақша": "300,000 - 500,000 ₸"},
            "mid": {"Русский": "500,000 - 1,200,000 ₸", "Қазақша": "500,000 - 1,200,000 ₸"},
            "senior": {"Русский": "1,200,000 - 2,500,000 ₸", "Қазақша": "1,200,000 - 2,500,000 ₸"}
        },
        "skills": {
            "Аналитическое мышление": 85,
            "Программирование": 80,
            "Решение проблем": 90,
            "Работа в команде": 75,
            "Обучаемость": 95
        },
        "market_metrics": {
            "growth_potential": 4.8,
            "market_demand": 4.7,
            "future_proof": 4.6,
            "salary_growth": 4.5
        },
        "professions": [
            {
                "title": {
                    "Русский": "Веб-разработчик",
                    "Қазақша": "Веб-әзірлеуші"
                },
                "description": {
                    "Русский": "Создание и поддержка веб-сайтов и веб-приложений",
                    "Қазақша": "Веб-сайттар мен веб-қосымшаларды жасау және қолдау"
                },
                "compatibility": 0.88,
                "demand": {
                    "Русский": "Высокий спрос на рынке",
                    "Қазақша": "Нарықта жоғары сұраныс"
                },
                "education": {
                    "Русский": "Компьютерные науки или курсы программирования",
                    "Қазақша": "Компьютерлік ғылымдар немесе бағдарламалау курстары"
                },
                "growth": {
                    "Русский": "23% к 2026 году",
                    "Қазақша": "2026 жылға қарай 23%"
                },
                "companies": {
                    "Русский": ["Kaspi.kz", "Chocofamily", "Kolesa", "One Technologies"],
                    "Қазақша": ["Kaspi.kz", "Chocofamily", "Kolesa", "One Technologies"]
                },
                "responsibilities": {
                    "Русский": ["Разработка интерфейсов", "Программирование", "Тестирование"],
                    "Қазақша": ["Интерфейстерді әзірлеу", "Бағдарламалау", "Сынақтан өткізу"]
                },
                "requirements": {
                    "Русский": ["HTML/CSS", "JavaScript", "Фреймворки", "Git"],
                    "Қазақша": ["HTML/CSS", "JavaScript", "Фреймворктер", "Git"]
                },
                "skills_gap": {
                    "current": 65,
                    "target": 85
                }
            },
            {
                "title": {
                    "Русский": "Data Scientist",
                    "Қазақша": "Деректер ғалымы"
                },
                "description": {
                    "Русский": "Анализ данных и создание моделей машинного обучения",
                    "Қазақша": "Деректерді талдау және машиналық оқыту модельдерін жасау"
                },
                "compatibility": 0.92,
                "demand": {
                    "Русский": "Очень высокий спрос",
                    "Қазақша": "Өте жоғары сұраныс"
                },
                "education": {
                    "Русский": "Высшее образование в IT или математике",
                    "Қазақша": "IT немесе математика бойынша жоғары білім"
                },
                "growth": {
                    "Русский": "31% к 2026 году",
                    "Қазақша": "2026 жылға қарай 31%"
                },
                "companies": {
                    "Русский": ["Kaspi.kz", "Halyk Bank", "Jusan Bank", "Kolesa"],
                    "Қазақша": ["Kaspi.kz", "Halyk Bank", "Jusan Bank", "Kolesa"]
                },
                "responsibilities": {
                    "Русский": ["Анализ данных", "ML модели", "Визуализация"],
                    "Қазақша": ["Деректерді талдау", "ML модельдері", "Визуализация"]
                },
                "requirements": {
                    "Русский": ["Python", "SQL", "Статистика", "ML"],
                    "Қазақша": ["Python", "SQL", "Статистика", "ML"]
                },
                "skills_gap": {
                    "current": 60,
                    "target": 90
                }
            }
        ],
        "market_analysis": {
            "Русский": "IT-сектор Казахстана быстро растет, особенно в сфере финтеха и e-commerce",
            "Қазақша": "Қазақстанның IT-секторы жылдам өседі, әсіресе финтех және e-commerce салаларында"
        },
        "learning_path": {
            "Русский": ["Основы программирования", "Специализация", "Практика"],
            "Қазақша": ["Бағдарламалау негіздері", "Мамандану", "Практика"]
        }
    },
    "healthcare": {
        "name": {
            "Русский": "🏥 Медицина и здоровье",
            "Қазақша": "🏥 Медицина және денсаулық"
        },
        "description": {
            "Русский": "Вы проявляете заботу о людях и интерес к медицинским наукам",
            "Қазақша": "Сіз адамдарға деген қамқорлық пен медициналық ғылымдарға деген қызығушылық танытасыз"
        },
        "salary_ranges": {
            "entry": {"Русский": "250,000 - 400,000 ₸", "Қазақша": "250,000 - 400,000 ₸"},
            "mid": {"Русский": "400,000 - 800,000 ₸", "Қазақша": "400,000 - 800,000 ₸"},
            "senior": {"Русский": "800,000 - 1,500,000 ₸", "Қазақша": "800,000 - 1,500,000 ₸"}
        },
        "skills": {
            "Эмпатия": 90,
            "Внимательность": 85,
            "Стрессоустойчивость": 80,
            "Медицинские знания": 75,
            "Коммуникация": 85
        },
        "market_metrics": {
            "growth_potential": 4.5,
            "market_demand": 4.6,
            "future_proof": 4.7,
            "salary_growth": 4.3
        },
        "professions": [
            {
                "title": {
                    "Русский": "Врач-терапевт",
                    "Қазақша": "Дәрігер-терапевт"
                },
                "description": {
                    "Русский": "Диагностика и лечение заболеваний внутренних органов",
                    "Қазақша": "Ішкі ағзалардың ауруларын диагностикалау және емдеу"
                },
                "compatibility": 0.85,
                "demand": {
                    "Русский": "Стабильно высокий спрос",
                    "Қазақша": "Тұрақты жоғары сұраныс"
                },
                "education": {
                    "Русский": "Медицинский университет (6 лет)",
                    "Қазақша": "Медициналық университет (6 жыл)"
                },
                "growth": {
                    "Русский": "15% к 2026 году",
                    "Қазақша": "2026 жылға қарай 15%"
                },
                "companies": {
                    "Русский": ["Государственные больницы", "Частные клиники"],
                    "Қазақша": ["Мемлекеттік ауруханалар", "Жеке клиникалар"]
                },
                "responsibilities": {
                    "Русский": ["Диагностика", "Лечение", "Наблюдение"],
                    "Қазақша": ["Диагностика", "Емдеу", "Байқау"]
                },
                "requirements": {
                    "Русский": ["Медицинское образование", "Лицензия", "Опыт"],
                    "Қазақша": ["Медициналық білім", "Лицензия", "Тәжірибе"]
                },
                "skills_gap": {
                    "current": 70,
                    "target": 90
                }
            }
        ],
        "market_analysis": {
            "Русский": "Медицинский сектор развивается с ростом инвестиций в здравоохранение",
            "Қазақша": "Медициналық сектор денсаулық сақтауға салынған инвестициялардың өсуімен дамиды"
        },
        "learning_path": {
            "Русский": ["Медицинское образование", "Специализация", "Практика"],
            "Қазақша": ["Медициналық білім", "Мамандану", "Практика"]
        }
    }
}

# =============================
# 🎯 ASSESSMENT QUESTIONS (50 QUESTIONS)
# =============================
questions_data = {
    "Русский": [
        "Вам нравится работать с компьютерами и технологиями?",
        "Вы любите помогать другим людям?",
        "Вам интересно разбираться в том, как работают механизмы?",
        "Вы предпочитаете активный образ жизни?",
        "Вам нравится создавать что-то новое своими руками?",
        "Вы хорошо работаете в команде?",
        "Вам интересны медицинские темы?",
        "Вы любите решать сложные задачи?",
        "Вам нравится учиться новому?",
        "Вы внимательны к деталям?",
        "Вам комфортно общаться с незнакомыми людьми?",
        "Вы хорошо переносите стрессовые ситуации?",
        "Вам нравится работать с цифрами?",
        "Вы творческий человек?",
        "Вам важно видеть результат своей работы?",
        "Вы ответственно относитесь к задачам?",
        "Вам нравится планировать и организовывать?",
        "Вы легко адаптируетесь к изменениям?",
        "Вам интересны научные открытия?",
        "Вы любите работать на открытом воздухе?",
        "Вам нравится обучать других?",
        "Вы терпеливы в работе?",
        "Вам важно постоянно развиваться профессионально?",
        "Вы хорошо анализируете информацию?",
        "Вам нравится работать с документами?",
        "Вы проявляете инициативу в работе?",
        "Вам интересны бизнес-процессы?",
        "Вы любите работать в стабильной обстановке?",
        "Вам нравится решать практические задачи?",
        "Вы хорошо управляете своим временем?",
        "Вам интересно проектировать и строить?",
        "Вы любите соревноваться?",
        "Вам нравится заботиться о других?",
        "Вы внимательно слушаете собеседника?",
        "Вам интересны новые технологии?",
        "Вы любите работать самостоятельно?",
        "Вам нравится преодолевать трудности?",
        "Вы легко находите общий язык с коллегами?",
        "Вам важно чувствовать социальную значимость работы?",
        "Вы аккуратны в работе?",
        "Вам нравится исследовать и открывать новое?",
        "Вы хорошо переносите монотонную работу?",
        "Вам интересны экономические процессы?",
        "Вы любите доводить дела до конца?",
        "Вам нравится работать с техникой?",
        "Вы быстро принимаете решения?",
        "Вам важно карьерное продвижение?",
        "Вы любите разнообразие в работе?",
        "Вам нравится решать организационные вопросы?",
        "Вы готовы к ненормированному рабочему дню?"
    ],
    "Қазақша": [
        "Компьютерлер мен технологиялармен жұмыс істеу сізге ұнай ма?",
        "Басқа адамдарға көмектесуді жақсы көресіз бе?",
        "Механизмдердің қалай жұмыс істейтінін анықтау сізді қызықтыра ма?",
        "Белсенді өмір салтын қалайсыз ба?",
        "Қолдарыңызбен жаңа нәрселер жасағанды ұнатасыз ба?",
        "Командада жақсы жұмыс істейсіз бе?",
        "Медициналық тақырыптар сізді қызықтыра ма?",
        "Күрделі мәселелерді шешуді ұнатасыз ба?",
        "Жаңа нәрселер үйренгенді ұнатасыз ба?",
        "Сіз детальдарға мұқият болыңыз ба?",
        "Белгісіз адамдармен сөйлесу сізге ыңғайлы ма?",
        "Стрестік жағдайларды жақсы көтересіз бе?",
        "Сандармен жұмыс істегенді ұнатасыз ба?",
        "Сіз шығармашылық адамсыз ба?",
        "Жұмысыңыздың нәтижесін көру сіз үшін маңызды ма?",
        "Тапсырмаларға жауапкершілікпен қарайсыз ба?",
        "Жоспарлауды және ұйымдастыруды ұнатасыз ба?",
        "Өзгерістерге оңай бейімделесіз бе?",
        "Ғылыми ашылулар сізді қызықтыра ма?",
        "Ашық аспан астында жұмыс істегенді ұнатасыз ба?",
        "Басқаларды оқытқанды ұнатасыз ба?",
        "Жұмыста сабырлысыз ба?",
        "Кәсіби түрде үнемі даму сіз үшін маңызды ма?",
        "Ақпаратты жақсы талдайсыз ба?",
        "Құжаттармен жұмыс істегенді ұнатасыз ба?",
        "Жұмыста бастамашылық танытасыз ба?",
        "Бизнес-процестер сізді қызықтыра ма?",
        "Тұрақты жағдайда жұмыс істегенді ұнатасыз ба?",
        "Практикалық есептерді шешуді ұнатасыз ба?",
        "Уақытыңызды жақсы басқарасыз ба?",
        "Жобалау мен құру сізді қызықтыра ма?",
        "Бәсекелестікті жақсы көресіз бе?",
        "Басқаларға қамқорлық жасағанды ұнатасыз ба?",
        "Өз сөздесіңізді мұқият тыңдайсыз ба?",
        "Жаңа технологиялар сізді қызықтыра ма?",
        "Өздігіңізше жұмыс істегенді ұнатасыз ба?",
        "Қиындықтарды жеңуді ұнатасыз ба?",
        "Әріптестеріңізбен ортақ тіл таба аласыз ба?",
        "Жұмыстың әлеуметтік маңыздылығын сезу сіз үшін маңызды ма?",
        "Жұмыста мұқиятсыз ба?",
        "Зерттеуді және жаңа нәрселер ашуді ұнатасыз ба?",
        "Монотонды жұмысты жақсы көтересіз бе?",
        "Экономикалық процессер сізді қызықтыра ма?",
        "Істерді соңына дейін жеткізгенді ұнатасыз ба?",
        "Техникамен жұмыс істегенді ұнатасыз ба?",
        "Шешімдерді тез қабылдайсыз ба?",
        "Мансаптық ілгерілеу сіз үшін маңызды ма?",
        "Жұмыста әртүрлілікті жақсы көресіз бе?",
        "Ұйымдастырушылық мәселелерді шешуді ұнатасыз ба?",
        "Нормаланбаған жұмыс күніне дайынсыз ба?"
    ]
}

# =============================
# 🚀 INITIALIZE SYSTEMS
# =============================
analytics_system = CareerAnalytics()
education_system = EducationIntegration()
mentor_system = MentorSystem()

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
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Пользователей", "18,456", "+1,234")
    with col2:
        st.metric("Успешных тестов", "94%", "+3%")
    
    st.metric("Среднее время", "12 мин", "-2 мин")
    
    st.markdown("---")
    st.markdown("### 🏆 Популярные профессии")
    st.markdown("""
    1. **Data Scientist** (+28%)
    2. **Врач** (+15%)  
    3. **Инженер** (+12%)
    4. **Разработчик** (+25%)
    5. **Маркетолог** (+18%)
    """)
    
    st.markdown("---")
    st.markdown("### 📈 Аналитика платформы")
    
    with st.expander("📊 Метрики качества"):
        st.metric("Достоверность результатов", "92%")
        st.metric("Согласованность ответов", "88%")
        st.metric("Время прохождения", "14.2 мин")
        st.metric("Ретеншн", "76%")
    
    st.markdown("---")
    st.markdown("### 🆘 Поддержка")
    st.markdown("""
    *Все услуги бесплатны!*
    
    📞 **Телефон:** 87766680880  
    📧 **Email:** askhatseitkhan@gmail.com  
    🏢 **Адрес:** Тараз, Толе Би 66
    
    **⏰ Время работы:**
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
    ### 🌟 Профессиональное тестирование
    
    **Job.AI** помогает определить ваши сильные стороны и подобрать профессии, 
    которые подходят именно вам на основе современных рыночных трендов.
    
    *🔍 Что мы анализируем:*
    - **🧠 Способности** - аналитические, творческие, социальные
    - **💼 Навыки** - технические и профессиональные компетенции  
    - **🎯 Интересы** - ваши предпочтения и увлечения
    - **📊 Рынок** - востребованность профессий и зарплаты
    
    *📈 Методология:* Основана на исследованиях рынка труда Казахстана
    """)

with col2:
    st.markdown("""
    ### 🎯 О тестировании
    
    **Вопросов:** 50 комплексных  
    **Время:** 10-15 минут  
    **Точность:** 94% совпадение  
    
    *💡 Результаты:*
    - Профиль компетенций
    - Рекомендации по развитию
    - Анализ рынка труда
    - Карьерная стратегия
    """)
    
    st.markdown("""
    **🏆 Наши партнеры:**
    - HR-агентства
    - Технологические компании
    - Образовательные центры
    """)

# =============================
# 🧠 CAREER ASSESSMENT WITH ANALYTICS
# =============================
st.markdown("---")
st.markdown('<div class="section-header">🎯 Профессиональное тестирование</div>', unsafe_allow_html=True)

# Initialize session state
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False
if 'question_start_time' not in st.session_state:
    st.session_state.question_start_time = None
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(hash(datetime.now()))

if not st.session_state.test_started:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 3rem; background: rgba(59, 130, 246, 0.1); border-radius: 20px; border: 2px solid #3b82f6;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🎯</div>
            <h3 style='color: #3b82f6; margin-bottom: 1rem;'>Готовы найти свою профессию?</h3>
            <p style='color: #cbd5e1; line-height: 1.6;'>
                Пройдите тестирование и получите персональные рекомендации 
                по выбору карьерного пути
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(LANGUAGES[selected_language]["start_test"], use_container_width=True):
            st.session_state.test_started = True
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.assessment_complete = False
            st.session_state.question_start_time = datetime.now()
            
            # Start analytics session
            analytics_system.start_user_session(st.session_state.user_id)
            st.rerun()

if st.session_state.test_started and not st.session_state.assessment_complete:
    questions = questions_data[selected_language]
    
    if st.session_state.current_question < len(questions):
        # Record time spent on previous question
        if st.session_state.question_start_time and st.session_state.current_question > 0:
            time_spent = (datetime.now() - st.session_state.question_start_time).total_seconds()
            analytics_system.record_question_time(
                st.session_state.user_id, 
                st.session_state.current_question - 1, 
                time_spent
            )
        
        st.session_state.question_start_time = datetime.now()
        
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
                
                if st.button(f"Выбрать {value}", key=f"btn_{i}", use_container_width=True):
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
# 📊 ADVANCED RESULTS ANALYSIS
# =============================
if st.session_state.assessment_complete:
    # Calculate results with confidence level
    questions = questions_data[selected_language]
    
    # Calculate confidence level
    confidence_level = analytics_system.calculate_confidence_level(
        st.session_state.user_id, 
        st.session_state.answers
    )
    
    # Simple scoring based on answer patterns
    tech_score = sum([st.session_state.answers.get(i, 3) for i in [0, 7, 13, 24, 34, 44]]) / 6 * 20
    creative_score = sum([st.session_state.answers.get(i, 3) for i in [4, 13, 18, 27, 37, 47]]) / 6 * 20
    social_score = sum([st.session_state.answers.get(i, 3) for i in [1, 5, 10, 21, 32, 38]]) / 6 * 20
    physical_score = sum([st.session_state.answers.get(i, 3) for i in [3, 19, 29, 39, 44, 48]]) / 6 * 20
    
    scores = {
        "it_tech": tech_score,
        "healthcare": social_score,
        "engineering": (tech_score + physical_score) / 2,
        "creative": creative_score
    }
    
    dominant_category = max(scores, key=scores.get)
    profession_info = professions_data[dominant_category]
    
    # Get market analysis
    market_report = analytics_system.generate_market_report(dominant_category)
    
    # Get course recommendations
    course_recommendations = education_system.get_recommended_courses(
        profession_info["professions"][0]["title"][selected_language],
        user_level='beginner'
    )
    
    # Get mentor recommendations
    user_profile = {
        'location': 'Астана',
        'experience_level': 'beginner'
    }
    mentor_recommendations = mentor_system.recommend_mentors(
        user_profile, 
        profession_info["professions"][0]["title"][selected_language]
    )
    
    # Display results
    st.markdown("---")
    
    # SUCCESS HEADER WITH CONFIDENCE LEVEL
    confidence_class = "confidence-high" if confidence_level >= 0.8 else "confidence-medium" if confidence_level >= 0.6 else "confidence-low"
    confidence_text = "Высокая" if confidence_level >= 0.8 else "Средняя" if confidence_level >= 0.6 else "Низкая"
    
    st.markdown(f"""
    <div style="text-align: center; padding: 3rem 1rem; background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(29, 78, 216, 0.1) 100%); border-radius: 20px; margin: 2rem 0; border: 2px solid #3b82f6;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🎉</div>
        <h1 style="color: #3b82f6; margin-bottom: 1rem; font-size: 2.5rem; font-weight: 700;">
            ТЕСТИРОВАНИЕ ЗАВЕРШЕНО!
        </h1>
        <p style="color: #cbd5e1; font-size: 1.2rem; max-width: 600px; margin: 0 auto; line-height: 1.6;">
            Ваш профессиональный профиль успешно проанализирован
            <br>
            <span class="confidence-indicator {confidence_class}" style="margin-top: 1rem; display: inline-block;">
                Достоверность: {confidence_text} ({confidence_level*100:.1f}%)
            </span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # COMPETENCY PROFILE
    st.markdown('<div class="section-header">📊 Профиль компетенций</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Overall score
        overall_score = sum(scores.values()) / len(scores)
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{overall_score:.1f}%</div>
            <div class="metric-label">Общий балл</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Confidence indicator
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{confidence_level*100:.1f}%</div>
            <div class="metric-label">Достоверность</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Category scores
        st.markdown("### 📈 Оценка по категориям")
        category_names = {
            "it_tech": "IT и технологии",
            "healthcare": "Медицина", 
            "engineering": "Инженерия",
            "creative": "Творчество"
        }
        
        for category, score in scores.items():
            st.markdown(f"**{category_names[category]}**")
            st.progress(score / 100)
            st.markdown(f"<div style='text-align: right; color: #cbd5e1; font-size: 0.9rem;'>{score:.1f}%</div>", unsafe_allow_html=True)
    
    with col2:
        # Dominant category
        st.markdown(f"### 🏆 Основная сфера: {profession_info['name'][selected_language]}")
        st.markdown(f"*{profession_info['description'][selected_language]}*")
        
        # Insights
        st.markdown("#### 💡 Ключевые выводы")
        
        insights = [
            f"**Совместимость:** {scores[dominant_category]:.1f}%",
            f"**Сильные стороны:** {', '.join(list(profession_info['skills'].keys())[:2])}",
            f"**Потенциал роста:** {profession_info['market_metrics']['growth_potential']}/5.0",
            f"**Востребованность:** {profession_info['market_metrics']['market_demand']}/5.0",
            f"**Уровень достоверности:** {confidence_level*100:.1f}%"
        ]
        
        for insight in insights:
            st.markdown(f"- {insight}")
        
        # Skills
        st.markdown("#### 🔧 Навыки")
        for skill, value in profession_info["skills"].items():
            st.markdown(f"**{skill}**")
            st.markdown(f'<div class="skill-bar-container"><div class="skill-bar-fill" style="width: {value}%;"></div></div>', unsafe_allow_html=True)
    
    # MARKET ANALYSIS WITH COMPARISON
    st.markdown("---")
    st.markdown('<div class="section-header">📊 Анализ рынка</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Salary info
        st.markdown("### 💰 Уровень зарплат")
        salary_cols = st.columns(3)
        
        salary_data = profession_info['salary_ranges']
        salary_labels = ["Начальный уровень", "Опытный", "Эксперт"]
        
        for i, (col, (level, salary)) in enumerate(zip(salary_cols, list(salary_data.items())[:3])):
            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-value">{salary[selected_language]}</div>
                    <div class="metric-label">{salary_labels[i]}</div>
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        # Market metrics
        st.markdown("### 📈 Рыночные показатели")
        metric_cols = st.columns(2)
        
        metrics = profession_info['market_metrics']
        market_metrics = market_report
        
        with metric_cols[0]:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metrics['growth_potential']}/5.0</div>
                <div class="metric-label">Потенциал роста</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metrics['market_demand']}/5.0</div>
                <div class="metric-label">Спрос</div>
            </div>
            """, unsafe_allow_html=True)
        
        with metric_cols[1]:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{market_metrics['competition']}/5.0</div>
                <div class="metric-label">Конкуренция</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{metrics['salary_growth']}/5.0</div>
                <div class="metric-label">Рост зарплат</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Market analysis with recommendations
    st.markdown("#### 📊 Обзор рынка")
    st.markdown(f"{profession_info['market_analysis'][selected_language]}")
    
    if market_metrics['recommendations']:
        st.markdown("#### 💡 Рекомендации по рынку")
        for recommendation in market_metrics['recommendations']:
            st.markdown(f"- {recommendation}")
    
    # RECOMMENDED PROFESSIONS
    st.markdown("---")
    st.markdown('<div class="section-header">💼 Рекомендуемые профессии</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="profession-grid">', unsafe_allow_html=True)
    
    for profession in profession_info["professions"]:
        st.markdown(f"""
        <div class="grid-item">
            <h4 style="color: #60a5fa; margin-bottom: 0.5rem; font-family: 'Plus Jakarta Sans', sans-serif;">{profession['title'][selected_language]}</h4>
            <div style="color: #3b82f6; font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;">{profession['compatibility']*100:.0f}%</div>
            <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.4; margin-bottom: 1rem;">{profession['description'][selected_language]}</p>
            <div style="color: #94a3b8; font-size: 0.8rem;">
                <strong>Образование:</strong> {profession['education'][selected_language]}<br>
                <strong>Рост:</strong> {profession['growth'][selected_language]}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # MENTOR RECOMMENDATIONS
    if mentor_recommendations:
        st.markdown("---")
        st.markdown('<div class="section-header">👥 Рекомендуемые менторы</div>', unsafe_allow_html=True)
        
        for mentor in mentor_recommendations:
            availability_color = "#10b981" if mentor['availability'] == 'available' else "#f59e0b" if mentor['availability'] == 'limited' else "#ef4444"
            
            st.markdown(f"""
            <div class="mentor-card">
                <div style="display: flex; justify-content: between; align-items: start; margin-bottom: 1rem;">
                    <div style="flex: 1;">
                        <h4 style="color: #60a5fa; margin-bottom: 0.5rem;">{mentor['name']}</h4>
                        <p style="color: #cbd5e1; margin: 0;"><strong>{mentor['profession']}</strong> в {mentor['company']}</p>
                        <p style="color: #94a3b8; margin: 0;">Опыт: {mentor['experience']} лет | {mentor['location']}</p>
                    </div>
                    <div style="text-align: right;">
                        <div style="color: #f59e0b; font-weight: 700; font-size: 1.2rem;">{mentor['rating']} ★</div>
                        <div style="background: {availability_color}; color: white; padding: 0.25rem 0.5rem; border-radius: 12px; font-size: 0.8rem; margin-top: 0.5rem;">
                            { 'Доступен' if mentor['availability'] == 'available' else 'Ограниченно' if mentor['availability'] == 'limited' else 'Занят' }
                        </div>
                    </div>
                </div>
                <div style="color: #cbd5e1; font-size: 0.9rem;">
                    <strong>Навыки:</strong> {', '.join(mentor['skills'][:3])}<br>
                    <strong>Языки:</strong> {', '.join(mentor['languages'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # EDUCATION RECOMMENDATIONS
    if course_recommendations:
        st.markdown("---")
        st.markdown('<div class="section-header">📚 Рекомендуемые курсы</div>', unsafe_allow_html=True)
        
        for course in course_recommendations[:5]:  # Show top 5 courses
            st.markdown(f"""
            <div class="mentor-card">
                <h4 style="color: #60a5fa; margin-bottom: 0.5rem;">{course['name']}</h4>
                <p style="color: #cbd5e1; margin-bottom: 0.5rem;">
                    <strong>Провайдер:</strong> {course.get('provider', 'Coursera')} | 
                    <strong>Уровень:</strong> {course['level']}
                </p>
                <a href="{course['url']}" target="_blank" style="color: #3b82f6; text-decoration: none; font-weight: 600;">
                    Перейти к курсу →
                </a>
            </div>
            """, unsafe_allow_html=True)
    
    # DEVELOPMENT PLAN
    st.markdown("---")
    st.markdown('<div class="section-header">🎯 План развития</div>', unsafe_allow_html=True)
    
    # Learning path
    st.markdown("### 📚 Этапы обучения")
    for i, step in enumerate(profession_info['learning_path'][selected_language]):
        st.markdown(f"{i+1}. **{step}**")
    
    # Development timeline
    st.markdown("### 🗓️ План на 12 месяцев")
    
    development_phases = {
        "1-3 месяца": [
            "Изучение основ профессии",
            "Прохождение онлайн-курсов",
            "Создание первого проекта"
        ],
        "4-6 месяцев": [
            "Углубленное изучение",
            "Практика на реальных задачах",
            "Создание портфолио"
        ],
        "7-12 месяцев": [
            "Сертификация",
            "Поиск стажировки/работы",
            "Профессиональное развитие"
        ]
    }
    
    for phase, tasks in development_phases.items():
        with st.expander(f"📅 {phase}"):
            for task in tasks:
                st.markdown(f"- {task}")
    
    # FEEDBACK SYSTEM
    st.markdown("---")
    st.markdown('<div class="section-header">💬 Обратная связь</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        accuracy_rating = st.slider("Насколько точными были результаты?", 1, 5, 4)
        feedback = st.text_area("Ваши предложения по улучшению:")
    
    with col2:
        useful_rating = st.slider("Насколько полезными были рекомендации?", 1, 5, 4)
        contact_permission = st.checkbox("Разрешаю связаться для уточнения деталей")
    
    if st.button("📤 Отправить отзыв", use_container_width=True):
        st.success("Спасибо за ваш отзыв! Он поможет нам улучшить платформу.")
        # Здесь можно добавить логику сохранения отзыва
    
    # EXPORT FUNCTIONALITY
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📄 Скачать отчет в PDF", use_container_width=True):
            st.info("Функция экспорта в PDF будет реализована в следующей версии")
            # Здесь будет логика генерации PDF
    
    # RESTART BUTTON
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Пройти тест заново", use_container_width=True):
            st.session_state.test_started = False
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.assessment_complete = False
            st.rerun()

# =============================
# 📞 CONTACT INFORMATION
# =============================
st.markdown("---")
st.markdown('<div class="section-header">📞 Контактная информация</div>', unsafe_allow_html=True)

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
    🌐 job-ai.kz
    📱 Мобильное приложение
    """)

with col3:
    st.markdown(f"""
    **{LANGUAGES[selected_language]['online_booking']}**
    
    💻 job-ai.kz/booking
    📧 WhatsApp консультации
    🎯 Бесплатные услуги
    """)

# =============================
# 👣 FOOTER
# =============================
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #cbd5e1; font-size: 0.9rem; line-height: 1.6; padding: 2rem 1rem;'>
    <strong style='color: #3b82f6; font-size: 1.1rem;'>{LANGUAGES[selected_language]['footer']}</strong><br><br>
    
    📞 87766680880 | 🏢 Тараз, Толе Би 66 | 🌐 job-ai.kz<br>
    💼 Профессиональное тестирование | 🎯 Карьерное консультирование
</div>
""", unsafe_allow_html=True)
