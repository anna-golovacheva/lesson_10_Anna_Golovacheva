import json
import random


class Question:
    def __init__(self, text_q, difficulty, text_a, is_question_asked=False, user_answer=None, question_points=0):
        self.text_q = text_q
        self.difficulty = difficulty
        self.text_a = text_a
        self.is_question_asked = is_question_asked
        self.user_answer = user_answer
        self.question_points = question_points

    def get_points(self) -> int:
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        self.question_points = int(self.difficulty) * 10
        return self.question_points

    def is_correct(self) -> bool:
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом, иначе False.
        """
        correct = False
        if self.user_answer == self.text_a:
            correct = True
        return correct

    def build_question(self) -> str:
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'Вопрос: {self.text_q}\nСложность  {self.difficulty}/5.'

    def build_positive_feedback(self) -> str:
        """Возвращает:
        Ответ верный, получено __ баллов
        """
        return f'Ответ верный, получено {self.question_points} баллов.'

    def build_negative_feedback(self) -> str:
        """Возвращает:
        Ответ неверный, верный ответ __
        """
        return f'Ответ неверный, верный ответ - {self.text_a}.'


def get_statistics(q_list: list) -> None:
    """Считает и выводит количество заданных вопросов и общее количество баллов.
    """
    answers, points = 0, 0
    for q in q_list:
        if q.is_question_asked:
            answers += 1
            points += q.question_points
    print(f'Вот и всё!\nОтвечено {answers} вопрос(-а/-ов) из {len(q_list)}\nНабрано баллов: {points}.')





def main():
    with open('q_dict.json', 'r') as questions_dict:
        q_dictionary = json.load(questions_dict)

    questions = []
    for q in q_dictionary:
        question = Question(q['q'], q['d'], q['a'])
        questions.append(question)

    random.shuffle(questions)
    for q in questions:
        print(q.build_question())
        q.user_answer = input('Ответ: ')
        if q.is_correct():
            q.get_points()
            print(q.build_positive_feedback())
        else:
            print(q.build_negative_feedback())
        q.is_question_asked = True

    get_statistics(questions)


if __name__ == '__main__':
    main()


