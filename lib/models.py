from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine('sqlite:///moringa_theater.db')
Session = sessionmaker(bind=engine)
session = Session()

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer(), primary_key=True)
    character_name = Column(Integer())
    auditions = relationship('Audition', backref='role')

    def __init__ (self, character_name):
        self.character_name = character_name
        self.order_hired = []

    @hybrid_property
    def actors(cls):
        return [audition.actor for audition in cls.auditions]
    
    @hybrid_property
    def locations(cls):
        return [audition.location for audition in cls.auditions]


    def lead(self):
        order_hired = [audition for audition in self.auditions if audition.hired == 1]
        if len(order_hired) == 0:
            return 'no actor has been hired for this role.'
        else:
            return order_hired[0].actor
        
    def understudy(self):
        order_hired = [audition for audition in self.auditions if audition.hired == 1]
        if len(order_hired) == 0 or len(order_hired) == 1:
            return 'no actor has been hired for understudy for this role.'
        else:
            return order_hired[1].actor

    def __repr__(self):
        return f'{self.character_name}'

class Audition(Base):
    __tablename__ = 'auditions'
    
    id = Column(Integer(), primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Integer())
    role_id = Column(Integer(), ForeignKey('roles.id', ondelete='CASCADE'))

    def call_back(self):
        self.hired = 1
        session.commit()

    def __repr__(self):
        return f'id: {self.id}, name: {self.actor}, ' + \
            f'location: {self.location}, hired: {self.hired}'
    
