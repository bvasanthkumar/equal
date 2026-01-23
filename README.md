## :warning: Please read these instructions carefully and entirely first
* Clone this repository to your local machine.
* Use your IDE of choice to complete the assignment.
* When you have completed the assignment, you need to  push your code to this repository and [mark the assignment as completed by clicking here](https://app.snapcode.review/submission_links/0ed9e063-9d87-4cf7-aae8-cc71d94cdcac).
* Once you mark it as completed, your access to this repository will be revoked. Please make sure that you have completed the assignment and pushed all code from your local machine to this repository before you click the link.

## Operability Take-Home Exercise

Welcome to the start of our recruitment process for Operability Engineers. It was great to speak to you regarding an opportunity to join the Equal Experts network!

Please write code to deliver a solution to the problems outlined below.

We appreciate that your time is valuable and do not expect this exercise to **take more than 90 minutes**. If you think this exercise will take longer than that, I **strongly** encourage you to please get in touch to ask any clarifying questions.

### Submission guidelines
**Do**
- Provide a README file in text or markdown format that documents a concise way to set up and run the provided solution.
- Take the time to read any applicable API or service docs, it may save you significant effort.
- Make your solution simple and clear. We aren't looking for overly complex ways to solve the problem since in our experience, simple and clear solutions to problems are generally the most maintainable and extensible solutions.

**Don't**

Expect the reviewer to dedicate a machine to review the test by:

- Installing software globally that may conflict with system software
- Requiring changes to system-wide configurations
- Providing overly complex solutions that need to spin up a ton of unneeded supporting dependencies. We aspire to keep our dev experiences as simple as possible (but no simpler)!
- Include identifying information in your submission. We are endeavouring to make our review process anonymous to reduce bias.

### Exercise
If you have any questions on the below exercise, please do get in touch and we’ll answer as soon as possible.

#### Build an API, test it, and package it into a container
- Build a simple HTTP web server API in any general-purpose programming language[^1] that interacts with the GitHub API and responds to requests on `/<USER>` with a list of the user’s publicly available Gists[^2].
- Create an automated test to validate that your web server API works. An example user to use as test data is `octocat`.
- Package the web server API into a docker container that listens for requests on port `8080`. You do not need to publish the resulting container image in any container registry, but we are expecting the Dockerfile in the submission.
- The solution may optionally provide other functionality (e.g. pagination, caching) but the above **must** be implemented.

Best of luck,  
Equal Experts
__________________________________________
[^1]: For example Go, Python or Ruby but not Bash or Powershell.  
[^2]: https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28

# GitHub Gist API (Solution)

#### Project Overview

A simple HTTP API that fetches and returns a list of a GitHub user’s **publicly available Gists**.
Built using **FastAPI**, tested with **Pytest**, and packaged using a **secure, minimal Docker container** that runs on port **8080**.

---

## API Endpoints

### Get user’s publicly available Gists

```
GET /<username>
```

### Example Request

```
GET /octocat
```

### Sample Response

```json
{
  "user": "octocat",
  "public_gists": [
    {
      "id": "6cad326836d38bd3a7ae",
      "description": "Hello world!",
      "url": "https://gist.github.com/octocat/6cad326836d38bd3a7ae",
      "files": [
        "hello_world.rb"
      ]
    },
    {
      "id": "0831f3fbd83ac4d46451",
      "description": "",
      "url": "https://gist.github.com/octocat/0831f3fbd83ac4d46451",
      "files": [
        "git-author-rewrite.sh"
      ]
    },
    {
      "id": "1305321",
      "description": null,
      "url": "https://gist.github.com/octocat/1305321",
      "files": [
        "test.cs"
      ]
    }
  ]
}
```

### Health check

```
GET /health
```


### Sample Response

```json
{"status":"ok"}
```

---

## Setup & Run (Local)

### Prerequisite

```bash
python 3.13
Docker
```

---

## Run Using Docker

### Build Image

```bash
docker build -t gist-api .
```

### Run Container

```bash
docker run -p 8080:8080 gist-api
```

### Call API

```bash
curl http://localhost:8080/octocat
```

---

## Run Automated Tests

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate    # Windows
```

### 2. Install Dependencies

```bash
pip3 install -r requirements-dev.txt
```

### 3. Run tests

```bash
pytest
```