from flask import Blueprint, render_template, request, redirect

from Processors.ProfileData import Wrapper
from app_config import session
from decorators.login_required import login_required
from models.CRUD import CRUD
from models.dataClass.profile import Profile


class ProfileController(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        self.wrapper = Wrapper()
        self.crud = CRUD()

        @self.route('/profile', methods=['POST', 'GET'])
        @login_required
        def profile():
            login = session['login']

            data = self.wrapper.get_profile_data(login)

            return render_template('profile.html', data=data)

        @self.route('/profile/change', methods=['POST', 'GET'])
        @login_required
        def change_profile():
            login = session['login']
            new_phone_num = request.form['phone']
            new_email = request.form['email']

            data = self.wrapper.get_profile_data(login)

            prof = self.crud.read(Profile, email=data[1].data)

            self.crud.update_object(Profile, prof[0].id, phone_num=new_phone_num, email=new_email)

            return redirect('/profile')
