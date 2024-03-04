#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder"""
from time import strftime
from invoke import task

@task
def do_pack(c):
    """Function to compress files"""
    file = strftime("%Y%m%d%H%M%S")
    try:
        c.run("mkdir -p versions")
        c.run(f"tar -czvf versions/web_static_{file}.tgz web_static/")

        print(f"versions/web_static_{file}.tgz")

    except Exception as e:
        return None
