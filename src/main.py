from github import Github
import os

# Your GitHub username and personal access token for authentication
USERNAME = os.environ.get("USERNAME")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

# Repository details
REPO_OWNER = os.environ.get("REPO_OWNER")
REPO_NAME = os.environ.get("REPO_NAME")

def github_profile_maker(branch_name, file_path, commit_message, content):
    # create a Github instance using an access token
    g = Github(ACCESS_TOKEN)

    # get the repository object
    repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

    # get the master branch object
    master = repo.get_branch("master")

    # create a new branch from the master branch
    new_branch = repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=master.commit.sha)

    # create a new file with some content
    repo.create_file(file_path, commit_message, content=content, branch=new_branch.ref)

    # create a pull request from the new branch to the master branch
    pr = repo.create_pull(title=f"pull request {branch_name}", body="pull request body", head=new_branch.ref, base=master.name)

    # get the pull request object
    pr = repo.get_pull(pr.number)

    # create a review for the pull request
    review = pr.create_review(body="review body", event="COMMENT")

    # merge the pull request
    pr.merge(commit_title="merge commit title", commit_message="merge commit message")