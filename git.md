# Instructions for Working with GitHub

A good resource for learning how to leverage GitHub: [GitHub Learning Labs](https://lab.github.com/courses)  
VCS stands for Version Control System. Git is a VCS and GitHub is a collection of repositories that leverage git as a VCS.  
**IMPORTANT:** Make sure to follow the [Git](../master/git.md#Git) instructions to enable the functionality on your machine.

## GitHub
1. If you don't already have one, [create an account](https://help.github.com/en/articles/signing-up-for-a-new-github-account) on GitHub. Your GitHub page is an online portfolio of technical projects that contains version control and ease of collaboration. A GitHub is just as important as having a tailored LinkedIn profile or professional business cards.
2. [Fork the parent repo](https://help.github.com/en/articles/fork-a-repo) into your personal GitHub account. This will allow you to update the project with your work.
3. The parent repo can change based on feedback and new content. Read and understand how to [sync a repo](https://help.github.com/en/articles/syncing-a-fork) to ensure you have the current version of the project.

## Git
1. Download and install [git](https://git-scm.com/downloads).
2. Follow GitHub's instructions for [setting up git](https://help.github.com/en/articles/set-up-git).
3. Take some time to explore [Pro Git](https://git-scm.com/book/en/v2) or the [reference documents](https://git-scm.com/docs) to understand VCS and this platform. There are also four [tutorial videos](https://git-scm.com/videos) if that is your preferred method.
4. Open GitHub and press the green _Clone or Download_ button.
5. Copy the URL provided. It should be in this format: `https://github.com/<USERNAME>/100DaysPython.git`
6. If using PyCharm for the project, skip to that [section](../master/git.md#PyCharm).  
7. Follow GitHub's instructions for [forking a repo](https://help.github.com/en/articles/fork-a-repo).

## PyCharm
1. JetBrains provides [detailed procedures](https://www.jetbrains.com/help/pycharm/github.html) on how to interact with your GitHub account.
2. [Clone your forked repo](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub) from your GitHub page to import the project into the PyCharm IDE.
3. When you wish to commit changes to your GitHub repo, you can select the _green checkmark_ in the top right of the IDE, select _Commit_ from the _VCS_ menu, or press _Ctrl+K_ to bring up the commit dialog box.
4. Add a comment about the changes made and select the down arrow next to _Commit_ or press _Ctrl+Alt+K_ for **Commit and Push**. Commit will accept the changes, but Push is the process that updates the GitHub repo with changed files.

## Anaconda
1. The only way to interact with the VCS is through the _Anaconda Prompt_.
2. Run the command `conda install -c conda-forge git` in _Anaconda Prompt_ to ensure git is enabled on your Anaconda virtual environment. Then follow the same procedures as [Git](../master/git.md#Git). 

## VS Code
1. Follow the [documented procedures](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support) from Visual Studio.