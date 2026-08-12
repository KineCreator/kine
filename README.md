# Kine

[![PyPI version](https://badge.fury.io/py/kine-engine.svg)](https://badge.fury.io/py/kine-engine)
[![Python Version](https://img.shields.io/pypi/pyversions/kine-engine.svg)](https://pypi.org/project/kine-engine/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Kine** is a minimal and fast Python animation engine designed for creating mathematical videos with canonical LaTeX typography (Computer Modern) directly rendered to MP4 files.

---

## Key Features

- **Canonical LaTeX Typography:** Automatic rendering of mathematical formulas using the Computer Modern font, proper variable italics, and academic operators ($\sin$, $\cos$, $\cdot$).
- **High Performance:** Optimized frame rendering powered by Matplotlib, OpenCV, and NumPy.
- **Direct MP4 Export:** Compiles ready-to-use video files without requiring complex external rendering dependencies.
- **Command-Line Interface:** Quick animation compilation directly from the terminal.
- **Dynamic Variables:** Smooth animation of parameter value transitions with automatic formula re-evaluation (`shift_delta`).

---

## Installation

Install the package via `pip`:

```bash
pip install kine-engine