# liatrio-app
A simple Flask app for the Liatrio interview project.

## Running Locally
1. Clone the repo
`git clone https://github.com/mcbanderson/liatrio-app.git`

2. Install dependencies
`pip install -r app/requirements.txt`

3. Run the app
`python app/app.py`

4. Navigate to http://localhost:5000 in your browser

## Running Locally via Docker
1. Clone the repo
`git clone https://github.com/mcbanderson/liatrio-app.git`

2. Build the image
`docker build --tag liatrio-app .`

3. Run the container
`docker run -d -p 80:5000 liatrio-app`

4. Navigate to http://localhost in your browser

## Development
### Conventional Commits
This project uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages. This allows for automated versioning and changelog generation. The following commit types are used:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries such as documentation generation
- `ci`: Changes to CI configuration files and scripts
- `build`: Changes that affect the build system or external dependencies (example scopes: pip, docker, npm)

### Versioning
This project uses [Semantic Versioning](https://semver.org/) for versioning. The version is automatically incremented based on the commit type via [semantic-release](https://github.com/semantic-release/semantic-release).
