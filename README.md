# DCE-KG: Disease-Centric Evidence-Based Knowledge Graph

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**DCE-KG** automatically builds a biomedical knowledge graph from PubMed Central articles using NLP and stores it in Neo4j. It provides evidence scoring and provenance for every relationship.

## Quick Start

1. Clone the repository.
2. Create virtual environment: `python -m venv venv` and activate.
3. Install: `pip install -r requirements.txt`
4. Install SciSpacy model: `pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz`
5. Start Neo4j (localhost:7474, user neo4j, password password)
6. Run `python main.py` or execute notebooks sequentially.
7. Open `dcekg_viz.html` for interactive graph.

## Repository Structure
