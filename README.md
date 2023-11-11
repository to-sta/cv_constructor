![Alt text](docs/readme/Banner.png)

![](https://img.shields.io/badge/Python-informational?style=for-the-badge&logo=python&logoColor=white&color=black&labelColor=EEC800)
![](https://img.shields.io/badge/Django-informational?style=for-the-badge&logo=django&logoColor=white&color=black&labelColor=EEC800)
![](https://img.shields.io/badge/Svelte-informational?style=for-the-badge&logo=svelte&logoColor=white&color=black&labelColor=EEC800)
![](https://img.shields.io/badge/Tailwind_CSS-informational?style=for-the-badge&logo=tailwindcss&logoColor=white&color=black&labelColor=EEC800)
![](https://img.shields.io/badge/pre_commit-informational?style=for-the-badge&logo=pre-commit&logoColor=white&color=black&labelColor=EEC800)
![](https://img.shields.io/badge/prettier-informational?style=for-the-badge&logo=prettier&logoColor=white&color=black&labelColor=EEC800)
![](https://img.shields.io/badge/Figma-informational?style=for-the-badge&logo=figma&logoColor=white&color=black&labelColor=EEC800)
![](https://img.shields.io/badge/Docker-informational?style=for-the-badge&logo=docker&logoColor=white&color=black&labelColor=EEC800)
![](https://img.shields.io/badge/Ruff-informational?style=for-the-badge&logo=ruff&logoColor=white&color=black&labelColor=EEC800)

## CV Constructor

**CV Constructor** is a software that simplifies the process of creating a CV (Curriculum Vitae). With CV Constructor, users can input their information and choose from a variety of templates and colors to create their CV. The software is designed to be user-friendly and intuitive, making it easy for anyone to create a professional-looking CV in no time.


## Contributing

Contributions to CV Constructor are always welcome. Check the open issues or if you suggestions create an issue.

### Development Setup

1. Install git:

    For instructions see https://git-scm.com/.

2. To setup your development environment, first install [Docker](https://docs.docker.com/get-docker/) and [Docker-Compose](https://docs.docker.com/compose/).


2. Fork the project:

    Click the "fork" button on the top of this repository (repo) to create a copy of the project for you to work on. You will need a GitHub account. This will allow you to make a "Pull Request" (PR) to this repo later on.

3. Clone your fork to your local machine:

    ```bash
    git clone https://github.com/<your-username>/cv_constructor.git
    ```
    GitHub will provide both a SSH and HTTPS url for cloning.  You can use SSH if you have SSH keys setup.

4. Change the directory to enter the project folder:

    ```bash
    cd cv_constructor
    ```

5. Add the upstream repository:

    ```bash
    git remote add https://github.com/to-sta/cv_constructor.git
    ```

    >[!INFO]
    > With the command `git remote -v` you can check if it was successful. You should see two remote repos named **origin** and **upstream**.

6. Install Pre-commit:

    ```bash
    pre-commit install
    ```

    This will ensure during development that each of your commits is properly formatted against our linter and formatters.

7. Create a .env file and start your docker images with the following:

    ```bash
    cp .env.example .env
    docker-compose up
    # Or with new dependencies:
    # docker-compose up --build
    ```
8. Then you are able to visit the frontend and backend on:

    * frontend: http://localhost:8000
    * backend: http://localhost:5174

### Develop your contribution

1. Checkout your local repo's main branch and pull the latest changes from the upstream, into your local repo:

    ```bash
    git checkout main
    git pull
    ```

2. Create a seperate branch for your contribution:

    ```bash
    git branch <name-of-the-branch>
    git checkout <name-of-the-branch>
    ```

3. Write some code :smiley:


### Submit your Pull request

1. Update your fork on GitHub to reflect your local changes

    ```bash
    git push -u origin <branch name>
    ```

2. Make a pull request on GitHub :rocket:

    Please describe your contribution briefly.

    * What have you implemented / changed?
    * Did you test your changes?

    We ran automated tests on every PR, these include linting, formatting and logic test for the backend and frontend.

    You will likely be asked to edit or modify your PR in one way or another during this process. This is not an indictment of your work, but rather a strong signal that the community wants to merge your changes! Once approved, your changes may be merged!
