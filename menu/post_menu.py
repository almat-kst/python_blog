from menu import BaseMenu
from utils import *
from models import Context, Post
from models.repositories.post_repository import PostRepository
from models.controllers.post_controller import PostController
from models.controllers.user_controller import UserController

class PostMenu(BaseMenu):
    __header = '-' * 10 + 'My Post ' + '-' * 10
    __options = ('[1] - Update post\n[2] - Create post\n[3] - Delete post\n[4] - Exit')
    __next_menus = {}

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()
        self.__next_menus = {
            '1': self.update_post,
            '2': self.create_post,
            '3': self.delete_post, 
            '4': lambda *_: raise_exception(ExitFromMenuException)
        }


    def update_post(self):
        #input_id_func = get_id_func()
        input_title_func = get_title_input()
        input_description_func = get_description_func()

        # def get_id():
        #     return input_id_func('Enter id: ')

        def get_title():
            return input_title_func('Enter new title: ')
        
        def get_description():
            return input_description_func('Enter new description: ')

        #id_title = self.input_secure_wrap(get_id)
        post_title = self.input_secure_wrap(get_title)
        post_description = self.input_secure_wrap(get_description)

        user_id = self.__user_controller.select_user_id(self.__context.user.username)

        update = Post(user_id = user_id, title = post_title, description = post_description)

        if user_id:
            self.__post_controller.update_post(update)
            print('Update post was successfully')
        else:
            print('Update failed')


    def create_post(self):
        input_title_func = get_title_input()
        input_description_func = get_description_func()

        def get_title():
            return input_title_func('Enter title: ')
        
        def get_description():
            return input_description_func('Enter description: ')

        title = self.input_secure_wrap(get_title)
        description = self.input_secure_wrap(get_description)

        user_id = self.__user_controller.select_user_id(self.__context.user.username)
        new_post = Post(user_id = user_id, title= title, description = description)

        if user_id:
            self.__post_controller.create_post(new_post) 
            print(f'Post with title - *{title}* successfully created!')
            return
        else:
            print('Post failed!')


    def delete_post(self):
        input_id_func = get_option_input()

        def get_id():
            return input_id_func('Enter id: ')
    
        delete_id = self.input_secure_wrap(get_id)

        delete = self.__post_controller.delete_post(int(delete_id))
        print('Post was deleted!')


    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.__header)
            #print(self.__context.profile)
            print(self.__options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                next_menu = self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return







