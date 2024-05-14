import git

def push_to_github(repo_path, file_path):
    repo = git.Repo(repo_path)
    repo.git.add(file_path)
    repo.index.commit("Add encrypted .env file")
    origin = repo.remote(name="origin")
    origin.push()