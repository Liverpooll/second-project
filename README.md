# second-project

[설계도]
https://docs.google.com/spreadsheets/d/1sPgWZGo3QXdOFqY_rTgXjaErAeDtvpf8jPUbEuEjork/edit#gid=0

1. 각 앱별로 __pycache__, migrations 폴더 모두 지우기
2. sqlLite3 삭제

DB 재생성
1. python manage.py makemgirations accounts
2. python manage.py migrate accounts
3. python manage.py makemgirations blog
4. python manage.py migrate blog
5. python manage.py migrate

requirements.txt 업데이트했으니까 꼭 다시 업데이트 해주기
pip install -r requirements.txt
