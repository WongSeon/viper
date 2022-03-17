from utils import log
from utils import template
from utils import http_response
from utils import redirect
from utils import get_db_connection


def route_index(request):
    conn = get_db_connection()
    if request.method == 'POST':
        form = request.form()
        name = form["name"]
        body = form["body"]
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            # flash(error)
            pass
        else:
            sql = '''
                INSERT INTO message (name, body)
                VALUES (?, ?)
            '''
            conn.execute(sql, (name, body))
            conn.commit()
            conn.close()
            # flash('Your message have been sent to the world!')
            return redirect('/')
    sql = '''
        SELECT *
        FROM message
        ORDER BY created DESC
    '''
    messages = conn.execute(sql).fetchall()
    conn.close()
    body = template('index.html', messages=messages)
    return http_response(body)


route_dict = {
    '/': route_index,
}


"""
def route_login(request):
    headers = {
        'Content-Type': 'text/html',
    }
    if request.method == 'POST':
        form = request.form()
        u = form["name"]
        if u.validate_login():
            user = User.query.first()
            # creat session
            session_id = random_key()
            session[session_id] = user.id
            headers['Set-Cookie'] = 'user={}'.format(session_id)
            return redirect('/', headers)
    body = template('login.html')
    header = response_with_headers(headers)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def new(request):
    uid = current_user(request)
    user = User.find(uid)
    body = template('new.html')
    return http_response(body)


def login_required(route_function):
    def func(request):
        uid = current_user(request)
        if uid == -1:
            return redirect('/login')
        else:
            return route_function(request)
    return func


route_dict = {
    '/': index,
    '/admin/new': login_required(new),
}

"""
