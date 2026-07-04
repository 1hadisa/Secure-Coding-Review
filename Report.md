# Objective

The objective of this project is to perform a secure code review on a simple Python login application using the Bandit static analysis tool. The review identifies security vulnerabilities, explains their potential impact, and provides recommendations to improve the application's security.

# Tool Used
**Bandit**
Bandit is a static security analysis tool designed for Python applications. It scans Python source code for common security issues and reports vulnerabilities along with their severity, confidence level, and remediation guidance.

## Assumptions

The reviewed application is a simplified demonstration. Hardcoded credentials were intentionally used to keep the code concise and focus the security review on common vulnerabilities identified by the Bandit static analysis tool.
In production environments, authentication should rely on securely stored, hashed passwords, proper user management, and secure authentication mechanisms rather than hardcoded credentials.

# Scan Summary
| Severity | Number of Issues |
|-----------|-----------------:|
| High | 1 |
| Medium | 1 |
| Low | 2 |
| **Total** | **4** |

Total lines of code scanned: **17**

---

# Findings

## 1. Hardcoded Password

**Bandit ID:** B105

**Severity:** Low

**Location:** `vulnerable_app.py` Line 10

### Description

The application contains a hardcoded password (`admin123`) directly in the source code.
Hardcoded credentials can be exposed if the source code is shared or compromised, allowing unauthorized users to access the application.

### Recommendation
- Store credentials securely outside the source code.
- Use environment variables or a secure configuration file.
- Store passwords as hashed values rather than plain text.
## 2. Use of eval()

**Bandit ID:** B307

**Severity:** Medium

**Location:** `vulnerable_app.py` Line 14

### Description

The application evaluates user input using Python's `eval()` function.
Since `eval()` executes arbitrary Python code, an attacker could execute malicious commands by entering specially crafted input.

### Recommendation
- Avoid using `eval()` on user input.
- Validate input before processing it.
- Use safer alternatives such as `ast.literal_eval()` when appropriate.
## 3. Command Injection

**Bandit ID:** B605

**Severity:** High

**Location:** `vulnerable_app.py` Line 17

### Description

The application executes user-supplied input using `os.system()`.

This may allow an attacker to execute arbitrary operating system commands, potentially compromising the entire system.

### Recommendation

- Avoid executing user input directly.
- If system commands are required, use `subprocess.run()` with validated arguments.
- Restrict executable commands whenever possible.
## 4. Weak Random Number Generator

**Bandit ID:** B311

**Severity:** Low

**Location:** `vulnerable_app.py` Line 19

### Description

The application generates session tokens using Python's `random` module.

The `random` module is not intended for cryptographic or security-sensitive operations and its output may be predictable.

### Recommendation

- Use Python's `secrets` module for generating session identifiers or security tokens.
- Avoid using `random` for authentication or security purposes.

---

# Remediation

A secure version of the application (`secure_app.py`) was developed to address the identified issues.

The following improvements were implemented:

- Removed the use of `eval()`.
- Removed the use of `os.system()`.
- Replaced `random.randint()` with `secrets.token_hex()`.
- Added a maximum login attempt limit.
- Added basic input validation.
- Improved overall code security and reliability.
# Conclusion
The Bandit security scan successfully identified four security vulnerabilities in the vulnerable login application.
The identified issues included hardcoded credentials, unsafe code execution using `eval()`, command injection through `os.system()`, and the use of an insecure random number generator.

After reviewing the findings, a secure version of the application was implemented following secure coding best practices. This demonstrates how static analysis tools such as Bandit can assist developers in identifying and mitigating common security vulnerabilities during software development.
