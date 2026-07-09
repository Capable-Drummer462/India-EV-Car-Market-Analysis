(Kindly read this readme file for the analysis, hypothesis and conclusion)

India EV Market Analysis (2019–2025)

A comprehensive data analysis project exploring the growth of India's electric vehicle passenger car market — covering brand competition, model performance, price-range positioning,state-wise adoption, and the impact of government policy.

### Key questions that are answered;
- How fast has India's EV market grown, and what drove the inflection points?
- Which brands and models are dominating — and is Tata's lead under threat?
- Does affordability or range anxiety matter more for adoption?
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
- Model specifications from official brand websites CarWale, EvoIndia and TeamBHP
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
## My Findings

Lets start with the reason why I started my analysis from 2019, it was the year when Tata Motors launched TigorEv, which acted as a stepping stone in the EV market of India, prior to this Mahindra had electric cars, a tribute to Rewa which was launched in 2001, Mahindra had 2 cars in their portfolio, e2o, which was launched in 2013, and e-verito in 2016, both of these cars were not much heard about or known in the market and their sales reflected that, also since the brands are many and units are less of luxury cars, I put them in the other category and we wont count them as brand and model list however we definitely would check their trends, lets dive into our analysis year-wise

2019 

Total Sales - 1554
Brands - 3, Models - 4

Tata tigor EV launched, Mahindra had 2 cars in portfolio, Hyundai Launched Kona electric as a premium CBU unit, which did decent in numbers

2020

Total Sales - 4003 (YoY growth- 157%)
Brands - 4, Models - 5

NexonEv launched, Tata influenced the market growth, MG entered Ev market with their ZS EV, Mahindra was dying, their sales were just 9 in whole year. with Mahindra out Tata established their monopoly with 2 solid products, MG as a main competitor.

2021

Total Sales - 14690 (YoY growth- 267%)
Brands - 3, Models - 4

NexonEv became a huge name in indian public for the go-to Electric family car, and people were buying it, Governmentt officials also used these heavily to promote both indegeniousity and clean fuel alternative, Tata's market share was 78.4% this year. Luxury car market was also expanding, so much to the fact that their total sales outnumbered the sales of Hyundai's Kona, which is kindof big.

2022

Total Sales - 48262 (YoY growth- 229%)
Brands - 4, Models - 5

NexonEv sold 30,000 units, TigorEv was popular in commercial fleet market, it was widely popular in being used as taxi in BluSmart. Tata's Market Share was 85%. BYD enters the game, with their e6 MUV it was reasonably priced earlier in 2021 it was just restricted to B2B but in 2022 opened to the private buyers and market, Luxury Car Market was also booming, sales increased by 5 folds compared to last year.

2023

Total Sales - 89549 (YoY Growth- 85%)
Brands - 6, Models - 11

Tata Launched TiagoEv, which became a success and highest selling in its launch year, a compact secondary city car, but the Tata's Market share remained somewhat stagnant, 74.1%, although it still had the strong hold, the reason? MG + Mahindra, MG added CometEV in their portfolio which was a hit. Mahindra was back from the dead, they launched XUV400, the electric version of XUV300, 
By now everyone was observing the Indian Market boom and everybody wanted a piece, so they came in active mode, Hyundai phased out Kona Electric and brought in their premium IONIQ5, Citreon also joined with their ec3 but it wasnt as good as expected, Mahindra was going good for its start plus to mention the fact they kindof started the trend before it became mainstream, BYD adds anohte car in their lineup.

2024

Total Sales - 105109 (YoY Growth- 17.4%)
Brands - 6, Models - 13

A bad year for EVs, although total sales market crossed 100k milestone, YoY was just 17.4%.
In attempt to capture the market again, Tata added 2 another cars in their lineup, PunchEv and CurvvEv, Punch did good but curvv lagged behind, Tata still had the top 3 most selling cars of the year, Punch Tiago Nexon, but it started losing its market share, i.e., 67.9%, MG became serious too, they launched WindsorEv, which was going well for its launch year itself, WindsorEv became a good alternate of Nexon in passenger market, also in commercial fleets. Mahindra saw a steady increase, Luxury cars sales fell drastically from before, Vinfast enters indian market.

2025

Total Sales - 162511 (YoY Growth- 54.6%)
Brands - 8, Models - 21

Considerable industry revival, from last years fiasco, YoY was 54.6%.
Tata launched a solid product like HarrierEv but it couldnt do much as it was on an upper price bracket, Tata's market share fell drastically, even with the strong sales, ie., 42% the reason? Mahindra. Mahindra revamped their entire operation, from just focusing on EV market as seconday they decided to go mainstream, launched 2 products, BE6 and XEV9E, and these 2 products proved to be a blockbuster for indian market, tech packed and many first in segment features with the up-market finishes with solid performance motors and decent batteries, it was a buzzing sensation with a good on-point price tag, recorded a large number of pre-bookings and BE6 became #1 selling in country within its year of launch, that smashed tata's monopoly, MG windsor was going strong with #2 in sales ranking, to establish a class MG also launched their first sports segment car, cyberster in market overseeing their steady expansion, Luxury Market which was crashing remained stable over the time period, Kia enters the market with ClavisEv MUV.

# States;
(Note - The units sold numbers are approximate cumulative registrations for only 4 wheelers EV sales recorded in mid 2024, the rankings and hypothesis are absolutely correct)

1. Maharashtra - 78000

Maharashtra seems to lead the list because of 2 key cities, Mumbai and Pune, due to the urban ev friendly infrastructure and a progressive population.

2. Karnataka - 52000

The pattern is similar here, the attractive government subsidies and key cities like Mangalore, an industrial hub and Bengaluru, which is commonly called silicon valley of india, is the IT hub of nation, the population comparitvely is better paid than rest of country and has the urban layout which makes sense to adopt an electric vehicle..

3. Kerala - 48000

Kerala is an automobile obsessed state, it is highly popular for its car culture in the country, plus the government policies promoting sustainable growth combined with exorbitant fuel prices and a natural interest to newer tech may be the reason for high EV sales.

4. Delhi - 39000

The National Capital Territory of Delhi is suffering from a major air pollution crisis, that resulted in strict measures over curbing the pollution from vehicles by the government that includes popular policies like GRAP, 10 year old diesel vehicle ban, odd even rule and Diesel-free buses in the city, plus its a political hub that resulted in major government fleets to include electric cars to promote idea of green growth, and major subsidies provided to the customers again to curb pollution.

5. Tamil Nadu - 34000

This state is popular for being called Detroit of India, major automakers factories are situated here, and the 100% waiver on road tax by government on electric vehicles since 2020 reflects in the sales here.

6. Uttar Pradesh - 28000

The surprising contender in the list, Uttar Pradesh has high cars sales because of 2 districts, Noida (Gautam Buddh Nagar) and Ghaziabad, these 2 cities of UP are a part of broader Delhi spectrum, i.e., Delhi NCR, the proximity to delhi and the factor that many people commute noida to delhi (and vice versa) for work on daily basis because Noida is a key corporate hub, plus the direct subsidies by the government.

7. Gujarat - 25000

This state is popular for its industries and a major port hub that specialises in the petroleum and its refinery, which in turn grows more awareness about the volatily of global changes that influence oil prices and how the state leads in residential solar capacity that helps in charging the vehicle, plus road tax being reduced to just 1%.  

8. Rajasthan - 19000

The sales of EV here highly comprises of 2 cities where within-city commuting becomes very affordable, Jaipur and Jodhpur, plus the subsidies are directly linked to the Income Tax benefits while financing an EV for upto 1.5 lakhs

# Policy impact and Summary;

The foundation pillar was established in 2013, by FAME - I (Faster Adoption and Manufacturing of Hybrid and Electric Vehicles) to promote clean mobility, but FAME - II in 2019, which heavily emphasised on mass adoption of EVs as an alternate to ICEs, although the effects lagged 2 years, the peaks of Indian markets was influenced by these 2 policies, PLI ACC Batteries (Production Linked Incentive Advanced Chemistry Cell) and PLI Automobiles, these 2 policies were a masterstroke by indian Government and a boon for indeginous manufacturers like Tata and Mahindra, basically they were brought to reduce import duties and boost local EV supply chains and manufacturing batteries here in India, this let Tata and Mahindra keep their products prices very competitve and affordable for indian consumers with types of features they had. PM E-drive scheme launched in 2024 is also alloted a big budget like PLIs to emphasise next big bottleneck, i.e., charging the vehicle. 

# My Hypothesis

In the next few years; 

Mahindra would work tirelessly to capture the Tata's spot Vacuum, although tata lost the absolute monopoly but it would continue to provide a good neck-and-neck competition to Mahindra because Tata has an upper hand over a broad portfolio of segments of the EV cars, where mahindra manufactures bigger SUVs, Tata has a good foundation in entry level EVs, where Mahindra would attract premium seeking buyers, Tata is for base practicality and all rounder-ness.

MG would ramp up their production as well, their windsor ev has been a top performer in our last recorded data, they would broaden their portfolio as well like they did with adding cyberster for premium clients.

Hyundai and Kia, being in top 10 automakers in india overall, might build EV cars on their ICE models, expected to build domestically for few years rather than designing whole new chassis and framework if the trends from my datasets hold true.

One factor that is from the Govt policy section is that there are talks to blend ethanol in petrol for Oil dependency reasons and the blend percentage would increase over time, ethanol blending in existing vehicles heavily influences the mileage of cars by dropping them, keeping this in mind, consumers might see EV cars as a reliable alternate, atleast in tier 1 cities over the ICE cars. 

Luxury car models faced a setback in our dataset from 2023 to 2024, but then from 2024 to 2025 they jumped 2x because of new brands and models added in lineup, with that trend the luxury cars sales will continue to increase in near future.

To Summarize the hypothesis, the future of EV market looks good, from a monopoly the market has developed into a diverse one with healthy competition that ultimately benefits the consumers.

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
Data Analysis Project | Python pandas Streamlit  
Data collected and verified: 2025
