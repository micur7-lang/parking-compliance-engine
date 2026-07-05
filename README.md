# One-Way Parking Decision Support System

An automated, deterministic rule-based compliance engine written in Python that evaluates real-time spatio-temporal variables to determine legal street parking eligibility.

## Project Architectural Overview
This system simulates an intelligent edge-computing municipal validation system designed to mitigate parking violations. By programmatically parsing intersecting real-world data points—including temporal constraints, permit status, multi-day intervals, and single-direction street vector orientations—the system minimizes user error through a logical evaluation matrix.

### High-Impact R&D Architectural Patterns Featured:
* **Separation of Concerns (SoC):** Time parsing, operational constraints, and edge-case exceptions are extracted into modular, testable pure functions.
* **Deterministic Logic Matrix:** Replaced flat, highly duplicated multi-nested loops with an immutable verification pipeline.
* **Defensive Input Sanitization:** Safely tokenizes user parameters while lowering string case profiles to prevent type-mismatch vulnerabilities.

## Tech Stack & Technical Domain
* **Language:** Python 3.10+
* **Structural Paradigms:** Functional decomposition, dry principles, edge-case masking.
* **Domains Addressed:** Rule-based expert systems, civic engineering simulation.

## Structural Layout
```text
parking-compliance-engine/
│
├── src/
│   ├── main.py          <-- Main logic script
│   └── test_parking.py   <-- Automated test suite
│
├── .gitignore           <-- Excludes compilation and system cache files
└── README.md            <-- Professional system documentation
```

## Installation and Execution
1. Clone the clean code repository:
   ```bash
   git clone https://github.com/micur7-lang/parking-compliance-engine.git
   ```
2. Step inside the application scope:
   ```bash
   cd parking-compliance-engine
   ```
3. Boot up the validation engine via CLI:
   ```bash
   python3 src/main.py
   ```

## Future Engineering Roadmap
* **Asynchronous API Upgrades:** Interface with public transit GIS layers to fetch live geometric orientations based on coordinate lookups.
* **Test Case Assertions:** Implement a robust standard Python `unittest` mock layer to programmatically feed boundary cases to the parser.

## Automated Testing
The engine includes an automated unit test suite utilizing Python's built-in `unittest` framework to guarantee logic matrix integrity.

To execute the verification test suite, run:
```bash
python3 -m unittest discover -s src
```