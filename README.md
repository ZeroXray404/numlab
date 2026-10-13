# numlab

**A Python laboratory for scientific computing, mathematical modeling, simulations, and data visualization.**

Numlab is a personal learning and experimentation environment built with Python, JupyterLab, and modern scientific computing libraries.

The purpose of this repository is to explore mathematical concepts, physical phenomena, statistical methods, and computational problems through practical experiments, numerical calculations, and visualizations.

## Features

- Numerical and symbolic mathematical computations
- Scientific modeling and simulations
- Static and interactive data visualizations
- Statistical analysis and regression
- Interactive Jupyter notebooks
- Reproducible Python environments using uv

## Technologies & Libraries

### Scientific Computing

| Library | Import | Description | Documentation |
|---|---|---|---|
| NumPy | `import numpy as np` | Numerical computing, arrays, and matrix operations. | [Docs](https://numpy.org/doc/stable/) |
| SciPy | `import scipy` | Scientific algorithms, optimization, integration, and numerical methods. | [Docs](https://docs.scipy.org/doc/scipy/) |
| SymPy | `import sympy as sp` | Symbolic mathematics, algebra, derivatives, and integrals. | [Docs](https://docs.sympy.org/latest/) |
| Pandas | `import pandas as pd` | Data manipulation and analysis using DataFrames. | [Docs](https://pandas.pydata.org/docs/) |

### Data Visualization

| Library | Import | Description | Documentation |
|---|---|---|---|
| Matplotlib | `import matplotlib.pyplot as plt` | Static plots, charts, and scientific visualizations. | [Docs](https://matplotlib.org/stable/) |
| Plotnine | `from plotnine import ggplot, aes` | Statistical visualization using Grammar of Graphics. | [Docs](https://plotnine.org/) |
| Plotly | `import plotly.express as px` | Interactive charts and 3D visualizations. | [Docs](https://plotly.com/python/) |
| ipywidgets | `import ipywidgets as widgets` | Interactive sliders, buttons, and notebook controls. | [Docs](https://ipywidgets.readthedocs.io/) |

### Jupyter Environment

| Tool | Description | Documentation |
|---|---|---|
| JupyterLab | Interactive development environment for notebooks, code, and data. | [Docs](https://jupyterlab.readthedocs.io/) |
| ipykernel | Python execution kernel for Jupyter notebooks. | [Docs](https://ipykernel.readthedocs.io/) |
| uv | Python package and environment management. | [Docs](https://docs.astral.sh/uv/) |

### Development Tools

| Tool | Description | Documentation |
|---|---|---|
| Ruff | Fast Python linter and code formatter. | [Docs](https://docs.astral.sh/ruff/) |
| nbdime | Diffing and merging Jupyter notebooks. | [Docs](https://nbdime.readthedocs.io/) |
| Jupytext | Convert and synchronize notebooks with text-based Python files. | [Docs](https://jupytext.readthedocs.io/) |

Development tools are managed through the `dev` dependency group.

## Getting Started

### Prerequisites

- Git
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Installation

Clone the repository:

```bash
git clone https://github.com/ZeroXray404/numlab.git
cd numlab
```

Install and synchronize the Python environment:

```bash
uv sync
```

This installs the project dependencies, including the default development dependency group, according to `uv.lock`.

### Launch JupyterLab

```bash
uv run jupyter lab
```

JupyterLab will normally open in your default web browser.

Create a new notebook or open an existing `.ipynb` file to begin experimenting.

## Usage

### Example: Visualizing a Mathematical Function

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = x**2 - 4*x + 3

plt.plot(x, y, label="f(x) = x² - 4x + 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Quadratic Function")
plt.legend()
plt.grid(True)
plt.show()
```

### Managing Dependencies

Add a new library:

```bash
uv add package_name
```

Add a development tool:

```bash
uv add --dev package_name
```

Update the project environment:

```bash
uv sync
```

Inspect installed dependencies:

```bash
uv tree
```

## Project Structure

The repository is organized by subject to keep experiments and notebooks easy to navigate.

```text
numlab/
├── notebooks/
│   ├── experiments/
│   ├── finance/
│   ├── mathematics/
│   ├── physics/
│   └── statistics/
├── data/
├── src/
├── pyproject.toml
├── README.md
└── uv.lock
```

The structure may evolve as new experiments and projects are introduced.

## Project Goals

- Strengthen practical knowledge of Python and scientific computing.
- Explore mathematical and physical models through computation.
- Apply numerical methods to real-world problems.
- Develop skills in statistics and data visualization.
- Document experiments and findings in reproducible notebooks.

## License

This repository currently has no open-source license. All rights are reserved unless otherwise stated.