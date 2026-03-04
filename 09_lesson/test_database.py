# -*- coding: utf-8 -*-
from models import Student


class TestStudentCRUD:

    def test_create_student(self, db_session):
        new_student = Student(name="Тестовый Студент", age=22, grade=3.8)
        db_session.add(new_student)
        db_session.commit()
        saved_student = db_session.query(Student).filter_by(
            name="Тестовый Студент"
        ).first()
        assert saved_student is not None
        assert saved_student.age == 22
        assert saved_student.grade == 3.8
        print(f" Студент создан: {saved_student}")

    def test_update_student(self, db_session):
        student = Student(name="Старое Имя", age=20, grade=4.0)
        db_session.add(student)
        db_session.commit()
        student_id = student.id
        student_to_update = db_session.get(Student, student_id)
        student_to_update.name = "Новое Имя"
        student_to_update.grade = 4.8
        db_session.commit()
        updated = db_session.get(Student, student_id)
        assert updated.name == "Новое Имя"
        assert updated.grade == 4.8
        print(f" Студент обновлён: {updated}")

    def test_delete_student(self, db_session):
        student = Student(name="Удаляемый Студент", age=19, grade=3.5)
        db_session.add(student)
        db_session.commit()
        student_id = student.id
        assert db_session.get(Student, student_id) is not None
        student_to_delete = db_session.get(Student, student_id)
        db_session.delete(student_to_delete)
        db_session.commit()
        assert db_session.get(Student, student_id) is None
        print(" Студент удалён")
