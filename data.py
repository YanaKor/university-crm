from enum import Enum
# list_of_questions = ['использовать', 'Sanity', 'STLC', 'анализ', 'приоритетного', 'Smoke', 'тестировать', 'стандарты',
#                      'тестирование', 'Testing', 'End', 'регрессионное', 'Exploratory', 'White', 'UI', 'Box', 'рисков',
#                      'Matrix', 'Failure', 'план', 'валидацией', 'предельных', 'этапы', 'интеграционного', 'виды',
#                      'Error', 'основе', 'классов', 'Exit', 'разница', 'Black', 'Entry', 'кейсами', 'приоритетом',
#                      'серьезностью', 'динамическое', 'безопасности', 'Confirmation', 'тестовая', 'типы', 'репорта',
#                      'тест', 'Bug', 'Grey', 'поля', 'Performance', 'Criteria', 'техники', 'ценность', 'Traceability',
#                      'элементы', 'чеклистом', 'значени', 'пестицида', 'верификацией', 'документация', 'Regression',
#                      'серьезного', 'парадокс', 'испытание', 'фазы', 'поддерживать', 'эквивалентности', 'баг',
#                      'Configuration', 'кейса', 'уровни', 'Fault', 'заполнения']
#
# python_words = ["Python", "программирование", "код", "функция", "класс", "объект", "переменная", "список", "словарь",
#                 "кортеж", "множество", "if", "else", "while", "for", "def", "return", "import", "print"]
#
#
# teachers_degree = ["Профессор", "Доцент", "Старший преподаватель"]

list_of_questions = ['use', 'Sanity', 'STLC', 'analysis', 'priority', 'Smoke', 'test', 'standards',
                     'testing', 'Testing', 'End', 'regression', 'Exploratory', 'White', 'UI', 'Box', 'risks',
                     'Matrix', 'Failure', 'plan', 'validation', 'boundary', 'stages', 'integration', 'types',
                     'Error', 'basis', 'classes', 'Exit', 'difference', 'Black', 'Entry', 'test cases', 'priority',
                     'severity', 'dynamic', 'security', 'Confirmation', 'test', 'types', 'report',
                     'test', 'Bug', 'Grey', 'fields', 'Performance', 'Criteria', 'techniques', 'value', 'Traceability',
                     'elements', 'checklist', 'significance', 'pesticide', 'verification', 'documentation', 'Regression',
                     'serious', 'paradox', 'test', 'phases', 'maintain', 'equivalence', 'bug',
                     'Configuration', 'case', 'levels', 'Fault', 'filling']

python_words = ["Python", "programming", "code", "function", "class", "object", "variable", "list", "dictionary",
                "tuple", "set", "if", "else", "while", "for", "def", "return", "import", "print"]

teachers_degree = ["Professor", "Associate Professor", "Senior Lecturer"]

class Constants(Enum):
    NUM_OF_QUESTIONS_START = 3
    NUM_OF_QUESTIONS_STOP = 6
    NUM_OF_WORDS_START = 12
    NUM_OF_WORDS_STOP = 20
