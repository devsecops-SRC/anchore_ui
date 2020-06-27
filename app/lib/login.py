# -*- coding: UTF-8 -*-

from functools import wraps
from flask import session, url_for, redirect
from app import log


def login_check(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            if session.has_key('login'):
                if session['login'] == 'login_success':
                    return f(*args, **kwargs)
                else:
                    return redirect(url_for('login'))

            else:

                return redirect(url_for('login'))
        except Exception, e:
            log.exception("error")
            return redirect(url_for('runtime_error'))

    return wrapper
