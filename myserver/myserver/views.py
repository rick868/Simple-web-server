import sqlite3
import json
from django.http import JsonResponse
from django.conf import settings
import os

def get_users(request):
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, age FROM users")
    rows = cursor.fetchall()
    conn.close()

    users = []
    for row in rows:
        user = {
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'age': row[3]
        }
        users.append(user)
    return JsonResponse(users, safe=False)
