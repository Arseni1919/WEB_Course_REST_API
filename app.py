from flask import Flask, redirect, url_for, request
from flask import render_template
from flask import session
from flask import jsonify

app = Flask(__name__)

# ------------------------------------------------- #
# --------------- URL PARAMETERS ------------------ #
# ------------------------------------------------- #
@app.route('/profile', defaults={'user_id': -1})
@app.route('/profile/<int:user_id>')
def profile_func(user_id):
    # DB
    if user_id == -1:
        return render_template('profile.html', user_exists=False)

    query = "SELECT * FROM users WHERE id='%s';" % user_id
    query_result = interact_db(query=query, query_type='fetch')
    response = {}
    if len(query_result) != 0:
        response = query_result[0]

    response = jsonify(response)
    return response

    # return render_template('profile.html', user_id=user_id, user_exists=user_exists, category=category)


@app.route('/profiles')
def profiles_func():
    user_id, category = 10, 'username'
    # ...
    return redirect(url_for('profile_func', user_id=user_id, category=category))

#     if user_id == -1:
#         return render_template('profile.html', fill_form=True)
#     else:
#         query = "SELECT * FROM users WHERE id='%s';" % user_id
#         query_result = interact_db(query=query, query_type='fetch')
#         if len(query_result) == 0:
#             return render_template('404.html'), 404
#             # return jsonify({
#             #                 'success': 'False',
#             #                 "data": []
#             #             })
#         else:
#             # return render_template('profile.html', user_id=user_id, query_result=query_result)
#             return jsonify({
#                 'success': 'True',
#                 'data': query_result[0],
#             })






# @app.route('/profile/<int:user_id>')
# def profile_func(user_id):
#     return f'user ID: {user_id}'
# ------------------------------------------------- #
# @app.route('/profile/<int:user_id>')
# def profile_func(user_id):
#     return render_template('profile.html', user_id=user_id)
# ------------------------------------------------- #
# @app.route('/profile', defaults={'user_id': 15})
# @app.route('/profile/<int:user_id>')
# def profile_func(user_id):
#     return render_template('profile.html', user_id=user_id)
# ------------------------------------------------- #
# @app.route('/profile', defaults={'user_id': 777, 'email': 'example@email.com'})
# @app.route('/profile/<int:user_id>/<email>')
# def profile_func(user_id, email):
#     return render_template('profile.html', user_id=user_id, email=email)
# ------------------------------------------------- #
# @app.route('/profile', defaults={'user_id': -1}, methods=["GET", "POST"])
# @app.route('/profile/<int:user_id>')
# def profile_func(user_id):
#     if user_id == -1:
#         return render_template('profile.html', fill_form=True)
#     else:
#         query = "SELECT * FROM users WHERE id='%s';" % user_id
#         query_result = interact_db(query=query, query_type='fetch')
#         if len(query_result) == 0:
#             return render_template('404.html'), 404
#             # return jsonify({
#             #                 'success': 'False',
#             #                 "data": []
#             #             })
#         else:
#             # return render_template('profile.html', user_id=user_id, query_result=query_result)
#             return jsonify({
#                 'success': 'True',
#                 'data': query_result[0],
#             })
#
#
# @app.route('/get_user_info', methods=['POST'])
# def get_user_info():
#     user_id = request.form['user_id']
#     return redirect(url_for('profile_func', user_id=user_id))
# ------------------------------------------------- #
# ------------------------------------------------- #


# ------------------------------------------------- #
# -------------- MULTIPLE ROUTES ------------------ #
# ------------------------------------------------- #
@app.route('/index')
@app.route('/main')
@app.route('/home')
@app.route('/')
def index():
    # return render_template('index.html') #, name='Ariel')
    # return render_template('index.html', name=name)
    # DB
    # curr_user = ''
    return render_template('index.html',
                           hobbies=['Prog', 'Paint', "IEM", "Swim", "Sleep"],
                           degree=('B.Sc', 'M.Sc'))

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
