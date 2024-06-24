from ticket_generator import TicketGenerator


class Tickets:

    def __init__(self, num_tickets):
        self.ticket_generator = TicketGenerator(num_tickets)
        self.tickets = []

    def generate_tickets(self):
        for ticket in self.ticket_generator:
            ticket_number, ticket_name, question_list, additional_question = ticket
            exam_ticket = {
                "ticket_number": ticket_number,
                "ticket_name": ticket_name,
                "questions": question_list,
                "additional_question": additional_question
            }
            self.tickets.append(exam_ticket)

    def print_tickets(self):
        for ticket in self.tickets:
            print(f"Билет номер: {ticket['ticket_number']}")
            print(f"Название билета: {ticket['ticket_name']}")
            print("Вопросы:")
            for question in ticket['questions']:
                print(f"- {question}")
            print(f"Дополнительные вопросы: {ticket['additional_question']}")
            print()


if __name__ == '__main__':
    exam_tickets = Tickets(5)
    exam_tickets.generate_tickets()
    exam_tickets.print_tickets()

