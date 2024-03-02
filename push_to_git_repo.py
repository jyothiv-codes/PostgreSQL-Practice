import os
from git import Repo

def push_changes(repo_path, commit_message):
    repo = Repo(repo_path)

    # Add all changes
    repo.git.add(all=True)

    # Commit changes
    repo.index.commit(commit_message)

    # Push changes to remote
    origin = repo.remote(name='origin')
    origin.push()

if __name__ == "__main__":
    # Specify the path to the Git repository
    repo_path = 'https://github.com/jyothiv-codes/PostgreSQL-Practice.git'

    # Specify commit message
    commit_message = 'Automated commit'

    # Call function to push changes
    push_changes(repo_path, commit_message)
