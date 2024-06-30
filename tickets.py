class Tickets:

    def __init__(self, ticket_number, ticket_name, question_list, additional_question):
        self.ticket_number = ticket_number
        self.ticket_name = ticket_name
        self.questions = question_list
        self.additional_question = additional_question

    def __str__(self):
        ticket_info = f"Ticket Number: {self.ticket_number}\n"
        ticket_info += f"Ticket Name: {self.ticket_name}\n"
        ticket_info += "Questions:\n"
        for question in self.questions:
            ticket_info += f"- {question}\n"
        ticket_info += f"Additional Question: {self.additional_question}\n\n"
        return ticket_info
