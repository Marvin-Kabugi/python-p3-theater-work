#!/usr/bin/env python3

from models import session, Role, Audition
import pdb;

if __name__ == '__main__':

    audition = session.query(Audition).first()
    audition2 = session.query(Audition).filter(Audition.id == 20).first()
    audition3 = session.query(Audition).filter(Audition.id == 19).first()
    print('_' * 50 + 'Audition' + '_' * 50)
    print(audition)
    print(audition.role)
    audition.call_back()
    audition3.call_back()
    audition2.call_back()
    print(audition)

    print('_' * 50 + 'Role' + '_' * 50)
    role = session.query(Role).first()
    role2 = session.query(Role).filter(Role.id == 22).first()
    print(role)
    print(role2)
    print(role.auditions)
    print(role.actors)
    print(role.locations)
    print(role.lead())
    print(role2.lead())
    print(role2.understudy())

    pdb.set_trace()
