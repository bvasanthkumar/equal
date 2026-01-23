from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

GITHUB_API = "https://api.github.com/users"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/{username}")
def get_gists(username: str):
    url = f"{GITHUB_API}/{username}/gists"

    response = requests.get(url)

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="GitHub API error")

    gists = response.json()
    result = []
    for gist in gists:
        result.append({
            "id": gist["id"],
            "description": gist["description"],
            "url": gist["html_url"],
            "files": list(gist["files"].keys())
        })

    return {
        "user": username,
        "public_gists": result
    }