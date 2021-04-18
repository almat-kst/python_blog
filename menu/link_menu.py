from menu import BaseMenu
from utils import *
from models import Context
from models.repositories.post_repository import PostRepository
from models.controllers.post_controller import PostController
from db import DBService


class LinkMenu(BaseMenu):
    __header = '-' * 10 + 'All Link ' + '-' * 10
    __options = ('[1] - Exit')
    __next_menus = {
        '1':'ok'
    }

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()
        self.__next_menus = {
            '1': lambda *_: raise_exception(ExitFromMenuException)
        }

    def show(self):
        db = DBService()
        post_repo = PostRepository(db)
        print(self.__header)
        input_func = get_option_input()
    

        def get_input():
            selected_option = input_func('Enter option: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.__header)
            post_repo.select_all_post()
            print(self.__options)

            selected_option = self.input_secure_wrap(get_input)

            try:
                next_menu = self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return


