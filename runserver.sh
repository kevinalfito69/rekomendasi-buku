#!/bin/sh
echo -e "\e[34;1mStarting Program...\[0m"
gnome-terminal --tab --title="Tailwind CSS"  -- bash -c 'npm run tailwind'
gnome-terminal --tab --title="Django Server"  -- bash -c 'python manage.py runserver'
gnome-terminal --tab --title="Django Live Reload" -- bash -c 'python manage.py livereload'