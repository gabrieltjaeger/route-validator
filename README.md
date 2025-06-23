# Route Validation Service

A Python project for validating routes between states in a country, using Brazil as an example.  
The service checks if a given route (sequence of state abbreviations) is valid, i.e., each state in the route is a neighbor of the next.

## Features

- **State and Country modeling**
- **Route parsing and validation**
- **Service and use-case layers**
- **Comprehensive unit tests with pytest**

---

## Requirements

- Python **3.13** (recommended to use a virtual environment)
- See `requirements.txt` for dependencies

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/gabrieltjaeger/route-validator.git
cd route-validator
```

### 2. Create a virtual environment

It’s recommended to use a `.venv` folder for your virtual environment:

```bash
python3.13 -m venv .venv
```

### 3. Activate the virtual environment

- **Linux/macOS:**
  ```bash
  source .venv/bin/activate
  ```
- **Windows:**
  ```cmd
  .venv\Scripts\activate
  ```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main script to validate a sample route:

```bash
python main.py
```

Input example:

```bash
MG,GO,DF,GO,TO
```

Output example:

```bash
True
```

---

## Testing

This project uses **pytest** for unit testing.

To run all tests:

```bash
pytest test/test.py
```

---

## Example

You can validate a route by editing the `route` variable in `main.py`:

```python
route = "MG,GO,DF,GO,TO"
```

Or use the classes in your own scripts for custom validation.
