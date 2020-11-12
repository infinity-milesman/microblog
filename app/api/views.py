from flask import Blueprint, render_template

api = Blueprint('api',__name__,url_prefix='/api/v1',
                template_folder='templates',
                static_folder='static'
                )

@api.route('/simple_api')
def simple_api():
    return render_template('new_index.html')