from db import DBService
from models import Post
from models import *
from models.repositories.user_repository import UserRepository
from models.controllers.post_controller import PostController

class PostRepository:
    __db = None
    
    def __init__(self, db: DBService):
        self.__db = db


    def create_post(self, post: Post):
        try:
            with self.__db.connection.cursor() as cursor:
                query = "INSERT INTO post (user_id, title, description) VALUES (user_id,'{title}','{description}') "
                #query = "INSERT INTO post (user_id, title, description) VALUES (__user_controller.select_user_id,'{title}','{description}') "
                query = query.format(
                    user_id = post.user_id,
                    title = post.title,
                    description = post.description 
                )

                self.__db.execute(query)
            return True
        except Exception as ex:
            print(ex)
            return False

    def delete_post(self, id):
        try:
            with self.__db.connection.cursor() as cursor:
                query = "DELETE FROM post WHERE id = %d " % id

                self.__db.execute(query)
            return True
        except Exception as ex:
            print(ex)
            return False


    def select_post(self, id):
        try:
            query = "SELECT * FROM post WHERE id = %d " % id
            self.__db.execute(query)

            if self.__db.cursor.rowcount == 1:
                return Post.from_dict(self.__db.cursor.fetchone())
            else:
                return None

        except Exception as ex:
            print(ex)

#####
    def select_all_post(self):
        try:
            query = "SELECT `user_id`, `title`, `description` from post"
            self.__db.execute(query)

            if self.__db.cursor.rowcount >= 1:
                for i in self.__db.cursor.fetchall():
                    print(f'*id: {i["user_id"]}')
                    print(f'*title: {i["title"]}')
                    print(f'*description: {i["description"]}\n')
        except Exception as ex:
            print(ex)

###
    def update_post(self, post: Post):
        try:
            query = "UPDATE post SET `user_id` = user_id, `title` = '{title}', `description` = '{description}' WHERE `user_id` = user_id "
            query = query.format(
                user_id =  post.user_id,
                title = post.title,
                description = post.description
            )
            self.__db.execute(query)
        except Exception as ex:
            print(ex)