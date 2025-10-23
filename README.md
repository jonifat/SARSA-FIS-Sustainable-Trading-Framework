**SARSA-FIS Sustainable Trading Framework (EURUSD Case Study)**

This repository contains reproducible components of the SARSA-FIS Framework for Sustainable Forex Trading, developed as part of an ongoing doctoral research project on responsible AI and sustainable algorithmic trading. The framework integrates SARSA reinforcement learning with a Sugeno-type Fuzzy Inference System (FIS) to build an adaptive, interpretable, and ethically aligned trading agent for the EURUSD currency pair. The project advances responsible AI by embedding explainability, risk-awareness, and sustainability constraints into algorithmic trading design.

**Repository Contents**
SARSA-FIS-Sustainable-Trading-Framework/
│
├── data/
│   ├── EURUSD_M15_Data_History_Raw.csv
│   ├── EURUSD_Data_Historical_Treated.xlsx
│   └── README.md
│
├── model/
│   ├── Q_TABLE_SARSA_Training_Result.xlsx
│   └── README.md
│
├── results/
│   ├── ReportTester-213033105.xlsx
│   ├── testergraph.report.2025.05.14_Deposit_Load.xlsx
│   └── README.md
│
├── src/
│   └── sarsa_v.py
│
├── .gitignore
├── LICENSE
└── README.md

**Requirements**
- Python 3.10+
- Libraries: numpy, pandas, csv
- MetaTrader 5 (build 4755) for backtesting
- MATLAB R2023a (optional) for FIS modeling

**How to Reproduce**
1. Place raw or processed EURUSD data in the data/ folder.
2. Configure parameters in src/sarsa_v.py.
3. Run the SARSA training script: python src/sarsa_v.py
4. Check generated Q-table in the model/ folder.
5. Review results in the results/ folder.

**Core Components**
- SARSA Reinforcement Learning – Learns optimal trading policies via reward updates.
- Sugeno-type Fuzzy Inference System – Provides interpretability through rule-based decision logic.
- Sustainability Filters – Enforce drawdown control, volatility checks, and ethical risk management.

**License**
CC BY-NC-ND 4.0 (Attribution–NonCommercial–NoDerivatives)
You may share this work with proper citation for academic purposes.
Commercial use or derivative works are not allowed.

**This repository supports the paper:**
“A SARSA-FIS Framework for Sustainable Forex Trading: A EURUSD Case Study”
Under review in TELKOMNIKA.
