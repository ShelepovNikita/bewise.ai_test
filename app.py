"""Main file for Flask app."""
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

from validators import is_int, is_positive_int
from exceptions import InvalidNumber
from utils import get_questions_json, to_python_datetime


app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
db = SQLAlchemy(app)


class Question(db.Model):
    """Model for question response."""
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    quest_id = db.Column(db.Integer, unique=True)
    question = db.Column(db.String, unique=True, nullable=False)
    answer = db.Column(db.String, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, unique=False, nullable=False)

    def json(self):
        return {'quest_id': self.quest_id,
                'question': self.question,
                'answer': self.answer,
                'created_at': self.created_at}


db.create_all()


def get_object_questions(questions) -> list:
    """Create list with questions objects."""
    questions_obj_list = []
    for question in questions:
        new_question = Question(
                                quest_id=question.get('id'),
                                question=question.get('question'),
                                answer=question.get('answer'),
                                created_at=to_python_datetime(
                                    question.get('created_at')))
        questions_obj_list.append(new_question)
    return questions_obj_list


@app.route('/questions', methods=['POST'])
def get_questions():
    """Create questions in db and return last saved question."""
    try:
        last_question = Question.query.order_by(Question.id.desc()).first()
        num_of_questions = request.get_json().get('questions_num')
        if (not is_int(num_of_questions)
                or not is_positive_int(num_of_questions)):
            raise InvalidNumber('Invalid number')
        num_of_questions = int(num_of_questions)
        if num_of_questions == 0:
            raise InvalidNumber('Number must be > 0')
        while num_of_questions != 0:
            questions = get_questions_json(num_of_questions)
            questions_obj_list = get_object_questions(questions)
            for question_obj in questions_obj_list:
                try:
                    db.session.add(question_obj)
                    num_of_questions -= 1
                except Exception:
                    pass
                else:
                    continue
        db.session.commit()
        if last_question is None:
            return make_response()
        return make_response(jsonify(last_question.json()), 200)
    except Exception as error:
        return make_response(jsonify({'ERROR': f'{error}'}), 500)
