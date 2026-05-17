# Task Tracker CLI

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Task Tracker CLI is for managing task with 'todo list' concept, CRUD (Create, Read, Update and Delete) concept are in project :D

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

first of all, you must be have git and python in your environment.
i assumse you use linux.

```sh
apt install git python3 -y
```

### Installing

A step by step to download the repo for use in your environment.
first of all, use git to clone

```sh
git clone https://github.com/LetnanGM/task-tracker-cli
```

then change directory to folder repo

```sh
cd task-tracker-cli
```

after all in above, run it and feel the script :D

```sh
python main.py --help
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

how to use the script?
here is the small docs about the command:

- add : create a new task, need `title` in subargument, example `python main.py add hell-yeah`
- update : change old info to new object, need `id` and `title`, example `python main.py update 1 i just wanna be yours`, number `1` is id subargument after `update` command, and `i just wanna be yours` is new name for task :D
- delete : like the name, remove your task forom list.
- mark-in-progress : change old status project to `progress`.
- mark-done : change old status project to `done`.
- list : showing all of task, need `status` subargument, `status` must be `todo`, `progress`, `done` or `all`, after that, list will be filter all of project with status :D

Happy Coding!
