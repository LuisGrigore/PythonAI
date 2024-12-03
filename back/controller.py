from app import app


class UserController:

    @staticmethod
    @app.route('/model', methods=['GET'])
    def get_user_posts():
        return "aaaaa"
