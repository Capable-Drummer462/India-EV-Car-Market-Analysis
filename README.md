India EV Market Analysis (2019–2025)

A comprehensive data analysis project exploring the growth of India's electric vehicle passenger car market — covering brand competition, model performance, price-range positioning,state-wise adoption, and the impact of government policy.

## Project Summary

India's EV market has gone from near-zero in 2019 to a meaningful share of total passenger car sales by 2025. This project investigates **who is selling, what they're selling, where it's being bought, and what's driving it** — using real sales data, model specifications, geographic data, and policy information, in fact, the point of starting my analysis from 2019 was because of Tata, the EV giant in indian market today, their TigorEV was launched in 2019 which acted as a stepping stone for the EV market.

Key questions that are answered;
- How fast has India's EV market grown, and what drove the inflection points?
- Which brands and models are dominating — and is Tata's lead under threat?
- Does affordability (price) or range anxiety matter more for adoption?
- Which states are leading EV uptake, and which ones lag behind?
- How closely does government policy spending correlate with sales growth?


## Project Structure

```
india_ev_analysis/
│
├── data/
│   ├── ev_sales.csv          # Annual model-level sales (2019–2025)
│   ├── ev_models.csv         # Model specs: price, battery, segment
│   ├── state_sales.csv       # State-wise EV registrations (2024)
│   └── policy.csv            # Government policy timeline & budgets
│
├── India_EV_Market_Analysis.ipynb   # Main analysis notebook (10 sections)
├── dashboard.py                      # Interactive Streamlit dashboard
├── requirements.txt                  # Python dependencies
└── README.md                         # This file
```

## Datasets

| File | Rows | Description |
|------|------|-------------|
| `ev_sales.csv` | 66 | Year, brand, model, segment, units sold (2019–2025) |
| `ev_models.csv` | 24 | Brand, model, launch year, price (₹L), battery (kWh) |
| `state_sales.csv` | 10 | Top 10 states by EV registrations (2024 snapshot) |
| `policy.csv` | 7 | Policy name, year, budget (₹ Crore), target segment |

**Data Sources:**
- Sales data compiled from VAHAN Dashboard (vahan.parivahan.gov.in) and SIAM Annual Reports
- Model specifications from official brand websites and CarWale
- State-wise data from VAHAN portal (2024 annual snapshot)
- Policy data from Ministry of Heavy Industries press releases (PIB.gov.in)

---

## Analysis Sections

| Section | What it covers |
|---------|----------------|
| 1. Setup & Data Loading | Imports, cleaning, merging, null checks |
| 2. Exploratory Data Analysis | Shape, dtypes, summary stats, missing values |
| 3. Market Growth | YoY sales, growth rates, totals by year |
| 4. Brand Market Share | Stacked area chart, donut chart, trend lines |
| 5. Model Analysis | Top 10 models, segment breakdown over time |
| 6. Price vs Range | Bubble chart, price segment bucketing |
| 7. State Adoption | Bar chart, pie chart, geographic concentration |
| 8. Policy Impact | Dual-axis overlay: policy budget vs sales |
| 9. 2025 Deep Dive | 2024 vs 2025 brand comparison |
| 10. Key Findings | Printed summary of all major insights |

---

## Key Findings

1. **Market size:** ~3.17 lakh EV passenger cars sold across 2019–2025 in the tracked segments; 2025 is the highest single year
2. **Tata dominance:** Tata Motors holds ~56% of all EV sales — built on affordable models (Nexon, Tiago, Punch)
3. **Affordability drives volume:** 60%+ of sales come from models priced under ₹20L; budget EVs under ₹12L opened entirely new buyer segments
4. **2022 was the inflection year:** ~400% YoY growth driven by FAME II subsidies + Nexon EV scaling
5. **2025 competition heats up:** Mahindra's BE6 became the fastest-selling EV in India; MG Windsor surpassed MG's own ZS EV within a year
6. **Geographic concentration:** Maharashtra, Karnataka, and Kerala account for ~48% of all sales; Tier-2 cities are the next growth frontier
7. **Policy → sales lag:** Major sales spikes follow government policy announcements by ~18–24 months; FAME II (2019) → 2022 boom

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Jupyter Notebook
```bash
jupyter notebook India_EV_Market_Analysis.ipynb
```
Run all cells top to bottom. Charts will render inline and also save to the `data/` folder as `.png` files.

### 3. Launch the Streamlit Dashboard
```bash
streamlit run dashboard.py
```
Opens at `http://localhost:8501` — interactive filters for year range and brand selection across 5 analysis tabs.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| pandas | Data loading, cleaning, aggregation |
| matplotlib | All charts and figures |
| seaborn | Statistical visualizations |
| numpy | Numerical operations |
| Streamlit | Interactive web dashboard |
| Jupyter | Notebook-based EDA and narrative |

## Requirements

Check out `requirements.txt`:
```
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
seaborn>=0.12
streamlit>=1.30
jupyter>=1.0
notebook>=7.0
```

## Author

**Gopal Vashistha**  
Data Analysis Project | Python · pandas · Streamlit  
Data collected and verified: 2025
