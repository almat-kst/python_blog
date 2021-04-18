class PostController:
    __post_repo = None

    def __init__(self, post_repo):
        self.__post_repo = post_repo

    def select_post(self, id):
        return self.__post_repo.select_post(id)

    def create_post(self, post):
        return self.__post_repo.create_post(post)

    def update_post(self, post):
        return self.__post_repo.update_post(post)

    def select_all_post(self):
        return self.__post_repo.select_all_post()

    def delete_post(self, id):
        return self.__post_repo.delete_post(id)