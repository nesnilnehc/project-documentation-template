# Release Quality Gate

Test System Refactoring Specification

---

## 1. Purpose

This document defines how the project test system must be structured to act as a **Release Quality Gate** rather than a developer-level test script.

The goal is to ensure that every build produces a **clear, auditable release decision**:

- Can this version be released?
- If not, which quality layer blocks it?

---

## 2. Quality Layer Model

The test system must be organized into the following three layers:

```text
L1 – Unit Tests (Backend + Frontend)  
L2 – Service Integration Tests  
L3 – End-to-End System Tests  
```

Each layer is a **release gate**.

A higher layer must not run if a lower layer fails.

---

## 3. Layer Definitions

### L1 – Unit Tests

Validates individual code components.

Includes:

- Backend unit tests (e.g. pytest)
- Frontend unit tests (e.g. Jest, Vitest)

Purpose:
> Is the code logically correct?

---

### L2 – Service Integration Tests

Validates real service-to-service behavior.

Must use **real dependencies**:

- API → Database
- API → Cache
- API → Message Queue
- Cross-service calls

Mocks are not allowed at this layer.

Purpose:
> Do real services work together?

---

### L3 – End-to-End System Tests

Validates real user workflows.

Must include:

- Login
- Core business actions
- Data creation and queries
- UI → API → DB → response

Purpose:
> Can a real user complete real work?

---

## 4. Gate vs Signal

The test system must output two distinct sections.

### 4.1 Quality Gates (Release Blocking)

These determine if a release is allowed:

```text
L1 Unit Tests  
L2 Integration Tests  
L3 End-to-End Tests  
```

If any gate fails, the release is blocked.

---

### 4.2 Quality Signals (Non-Blocking)

These provide risk and code health information but must not block releases:

```text
Code Coverage  
Test Count  
Failure Trend  
Flaky Rate  
```

Coverage is a **code quality signal**, not a release decision.

---

## 5. Failure Diagnostics

Failures must be reported at dependency level.

Not allowed:

```text
L2 Integration Tests: FAILED
```

Required:

```text
L2 Integration Tests:
  AuthService → Redis: FAIL (timeout)
  OrderService → DB: PASS
  ReportService → MQ: PASS
```

This makes failures actionable without log digging.

---

## 6. Release Decision

Every test run must produce a final decision.

### Example — Blocked

```text
FINAL DECISION: RELEASE BLOCKED
BLOCKED BY: L2 Backend Integration
REASON: AuthService → Redis timeout
```

### Example — Approved

```text
FINAL DECISION: RELEASE APPROVED
```

This decision must be suitable for CI/CD automation.

---

## 7. Output Structure (Standard)

Every test run must generate a report in this structure:

```text
Release Candidate: <build-id>

Quality Gates
────────────────────
L1 Unit Tests          PASS
L2 Integration Tests   FAIL
L3 End-to-End Tests    NOT RUN

Quality Signals
────────────────────
Backend Coverage      78%
Frontend Coverage     62%
Total Tests           1342
Flaky Tests           3

Decision
────────────────────
FINAL DECISION: RELEASE BLOCKED
BLOCKED BY: L2 Integration
REASON: AuthService → Redis timeout
```

---

## 8. Design Principle

This system is designed so that:

- Gates decide **if** a version can be released.
- Signals decide **how risky** the version is.

They must never be mixed.
