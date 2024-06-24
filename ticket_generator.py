import random
from faker import Faker
from data import list_of_questions, python_words


class TicketGenerator:
    def __init__(self, num_tickets):
        self.num_tickets = num_tickets
        self.fake = Faker('ru_RU')
        self.ticket_numbers = []
        self.ticket_names = []
        self.questions = []
        self.additional_questions = []
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.num_tickets:
            ticket_number = self.generate_ticket_number()
            ticket_name = self.generate_ticket_name()
            question_list = self.generate_questions()
            additional_question = self.generate_additional_question()

            self.ticket_numbers.append(ticket_number)
            self.ticket_names.append(ticket_name)
            self.questions.append(question_list)
            self.additional_questions.append(additional_question)

            self.current_index += 1
            return ticket_number, ticket_name, question_list, additional_question
        else:
            raise StopIteration()

    def generate_ticket_number(self):
        number = self.fake.numerify(text='##')
        return f"{number}"

    def generate_ticket_name(self):
        return self.fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=list_of_questions)

    def generate_questions(self):
        questions = []
        num_questions = random.randint(3, 6)
        for _ in range(num_questions):
            num_words = random.randint(10, 15)
            question = self.fake.sentence(nb_words=num_words, variable_nb_words=True, ext_word_list=python_words)
            questions.append(question)
        return questions

    def generate_additional_question(self):
        return self.fake.sentence(nb_words=15, variable_nb_words=True)
