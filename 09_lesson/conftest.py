# -*- coding: utf-8 -*-
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import DATABASE_URL


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.rollback()
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture
def sample_student():
    from models import Student
    return Student(name="Иван Петров", age=20, grade=4.5)
