# Secure Coding Review
This project was completed as part of the CodeAlpha Cyber Security Internship.

## Project Objective
Review the security of a simple Python login application using the Bandit static analysis tool, identify security vulnerabilities, and implement a secure version of the application.

## Note
This project was intentionally designed as a small demonstration for a secure coding review. To keep the focus on identifying and remediating common security vulnerabilities, the application uses hardcoded login credentials.
In a real-world application, credentials should never be hardcoded. Instead, user credentials should be securely stored using hashed passwords in a database or managed through secure authentication systems.

## Project Files
- `vulnerable_app.py` – Intentionally vulnerable login application.
- `secure_app.py` – Remediated version following secure coding practices.
- `report.md` – Detailed security review and remediation report.
- `requirements.txt` – Project dependencies.

## Tool Used
- Bandit

## Running the Project
Run the vulnerable application:

```bash
python vulnerable_app.py
```

Run the secure application:

```bash
python secure_app.py
```

Run Bandit:

```bash
bandit vulnerable_app.py
```

## Results
Bandit identified four security issues:
- Hardcoded password
- Unsafe use of `eval()`
- Command injection via `os.system()`
- Weak random number generator

These issues were addressed in `secure_app.py`.

## Documentation
For the complete security review, see report.md.