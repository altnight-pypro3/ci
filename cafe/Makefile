# 10.5 django 節のサンプルアプリを動かすMakefile

default: prepare run
all: clean prepare run

run:
	cd apps && \
	  ~/venv/bin/python manage.py test && \
	  cd ..

prepare:
    # cafe ディレクトリは作られてるものとする
    # mkdir cafe
    # cd cafe

	~/venv/bin/pip install django==1.11.7

	# コマンド類は pypro2 また django 公式ドキュメントのチュートリアルにあわせている
	# ~/venv/bin/django-admin stratproject apps
	# cd apps
	#   ~/venv/bin/python manage.py startapp menu
	#   forms, models. tests, INSTALLED_APPS += ('menu') を追加
	#   ~/venv/bin/python manage.py makemigrations
	#   ~/venv/bin/python manage.py migrate
	# cd ..

clean:
	if [ -f ./cafe/db.sqlite3 ]; then rm ./cafe/db.sqlite3 ; fi
	find ./apps -name "__pycache__" | xargs rm -rf

.PHONY: default all run prepare clean
