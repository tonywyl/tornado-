from sqlalchemy import *

from sqlalchemy.orm import *

#Settings to connect to mysql database

database_setting={
    'database_type':'mysql',
    'connector':'pymysql',
    'user_name':'root',
    'password':'admin',
    'host_name':'192.168.44.143',
    'database_name':'testsql',
    'charset':'utf8',
    'echo':'True'


}

class User(object):
    def __init__(self,user_name,user_age,user_sex,user_score,user_subject):

        self.user_name=user_name
        self.user_age=user_age
        self.user_sex=user_sex
        self.user_score=user_score
        self.user_subject=user_subject


class UserManagerORM():
    def __init__(self):

        self.engine=create_engine(
            database_setting['database_type']+'+'+
            database_setting['connector']+'://'+
            database_setting['user_name']+':'+
            database_setting['password']+'@'+
            database_setting['host_name']+'/'+
            database_setting['database_name']



        )

        self.metadata=MetaData(self.engine)
        #
        self.user_table=Table('user',self.metadata,autoload=True)
        mapper(User,self.user_table)
        self.Session=sessionmaker()
        self.Session.configure(bind=self.engine)
        self.session=self.Session()

    def CreateNewUser(self,user_info):
        new_user=User(
            user_info['user_name'],
            user_info['user_age'],
            user_info['user_sex'],
            user_info['user_score'],
            user_info['user_subject']
        )



        self.session.add(new_user)
        self.session.commit()
        
    def GetUserByName(self,user_name):
        return self.session.query(User).filter_by(
            user_name=user_name
        ).all()[0]


    def GetAllUser(self):
        return self.session.query(User)


    def UpdateUserInfoByName(self,user_info):
        user_name=user_info['user_name']
        user_info_without_name={'user_age':user_info['user_age'],
                                'user_sex':user_info['user_sex'],
                                'user_score':user_info['user_score'],
                                'user_subject':user_info['user_subject']
                                }

        self.session.query(User).filter_by(user_name=user_name).update(
            user_info_without_name
        )
        self.session.commit()

    def DeleteUserByName(self,user_name):
        user_need_to_delete=self.session.query(User).filter_by(user_name=user_name).all()[0]

        self.session.delete(user_need_to_delete)
        self.session.commit()












