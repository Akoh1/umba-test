from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
# from app.models import User, Newuser
from . import home as home_blueprint
import os
from app import database
from itsdangerous import URLSafeTimedSerializer
from scripts.seed import Seed
import math


# @home_blueprint.route('/all/users', methods=['GET'])
# def all_users():
#     """
#     List all Users
#     """
#     all_users = User.query.all()
#     return render_template('home/home.html', users=all_users, title="Users")


@home_blueprint.route("/")
def home():
 
    return render_template('home.html')

@home_blueprint.route("/users")
def users():
    res = request.args
    limit = 25
    if res:
        print(f"Res: {res}")
        limit = int(res['pagination'])
        print(f'page: {limit}')

    users = Seed()
    all_users = users.select_all(limit=limit)
    # prev = page - 1
    # _next = page + 1

    num_of_pages = math.ceil(int(users.count_rows()) / 25) + 1
    print(f"num pages: {num_of_pages}")
  
    num_list = []
    for i in range(1, num_of_pages):
        
        num_list.append(i)

    length = int(len(num_list))
    # return f'Data: {all_users}'
    return render_template('users_page.html', users=all_users, num_pages=num_list, len=length)

@home_blueprint.route("/users/<int:page>")
def users_page(page):
    page = int(page)
    prev = page - 1
    _next = page + 1
    page_n = page -1
    print(f"page num: {page}")
    res = request.args
    limit = 25
    if res:
        print(f"Res: {res}")
        limit = int(res['pagination'])
        print(f'page: {limit}')

    users = Seed()
    all_users = users.select_all(page=page_n, limit=limit)
    

    num_of_pages = math.ceil(int(users.count_rows()) / 25) + 1
    print(f"num pages: {num_of_pages}")
  
    num_list = []
    for i in range(1, num_of_pages):
        num_list.append(i)

    length = int(len(num_list))
    print(f"Length in pages {length}")
    # return f'Data: {all_users}'
   
    return render_template('users.html', users=all_users, prev=prev, 
                           next=_next, num_pages=num_list, len=length,
                           page=page, pages=num_of_pages)


@home_blueprint.route('/users/profiles', methods =['GET'])
def get_users():
    users = Seed()
    all_users = users.select_all()
    res = request.args
    
    if res:
        print(f"Res: {res}")
        if 'page' in res:
            page = res['page']
        # if page:
            page = int(res['page'])
            print(f'page: {page}')
            all_users = users.select_all(page=page-1)
        if 'pagination' in res:
            limit = int(res['pagination'])
        # if limit:
            all_users = users.select_all(limit=limit)
        if 'order_by' in res:
            order_by = str(res['order_by'])
            all_users = users.order_by(value=order_by)
        if 'username' in res:
            print(f"Username: {res['username']}")
            username = str(res['username'])
            all_users = users.filter_username(username=username)
        if 'id' in res:
            uid = int(res['id'])
            all_users = users.filter_id(uid=uid)

    # converting the query objects
    # to list of jsons
    output = []
    for user in all_users:
        # appending the user data json
        # to the response list
        output.append({
            'id': user[0],
            'username' : user[1],
            'avatar_url' : user[2],
            'type': user[3],
            'url' : user[4],
            
        })
  
    return jsonify({'users': output})

