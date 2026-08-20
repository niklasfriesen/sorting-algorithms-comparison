# Learnings
This was my first project using Git and GitHub.
Here are my notes on what I learned, my difficulties and what I would do differently next time


## Git & GitHub basics
- **pull, branch, switch, add, commit, push**
- **Branches instead of comitting straigt to `main`.** I worked in feature branches and merged them via pull requests.
- **Pull requests as checkpoint.** Even when working solo, opening a PR forced me to review my own changes and helped me find mistakes.
- **Commit/PR messages should describe the changes.** Looking back at the history, the short commit- and the standard PR-messages are the hardest ones to understand.


## Project structure
- Splitting `src/` from `tests/` made the structure clear.
- `pyproject.toml` vs. `requirements.txt`: I initially added both without realizing they overlap.
- `.gitignore` matters from commit #1, to not pollute the repository.

## Testing
- `pytest` with `@pytest.mark.parametrize` let me run the same test cases for all sorting algorithms without duplicating the test code.

## Algorithms
- Implementing all six from scratch made the complexity differences clear - you can see it in the benchmark chart, not just imagine it.

## What I'd do differently next time
- Set up CI from the start so tests run automatically on every push/PR, instead of running `pytest` every time.
- Make a plan - I just started head first and had to fix them with multiple annoying PRs
- Use `pyproject.toml` from the beginning instead of adding `requirements.txt`.
