from flask import url_for, request
from webapp import create_app


app = create_app()


def print_urls_for_views():
    with app.test_request_context():
        print('URL for index view:               ', url_for('index'))
        print('URL for webapp view:               ', url_for('webapp'))
        print('URL for show_user_profile view:   ', url_for('show_user_profile', username='esheeran'))
        print('URL for show_post view:           ', url_for('show_post', post_id=6))
        print('URL for show_subpath view:        ', url_for('show_subpath', subpath='abc/def'))


def print_request_info():
    with app.test_request_context('webapp?name=Ed', method='GET'):
        print('Request path:                     ', request.path)
        print('Request HTTP method:              ', request.method)
        print('Request query parameter for name: ', request.args.get('name'))


print_urls_for_views()
print_request_info()