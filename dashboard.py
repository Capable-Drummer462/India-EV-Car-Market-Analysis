import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="India EV Market Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Styling ───────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #F8F9FA; }
    .metric-card {
        background: white; border-radius: 10px; padding: 16px 20px;
        border: 1px solid #E8ECF0; margin-bottom: 8px;
    }
    .metric-val { font-size: 28px; font-weight: 700; color: #185FA5; }
    .metric-label { font-size: 13px; color: #666; margin-bottom: 4px; }
    .metric-delta { font-size: 12px; color: #1D9E75; font-weight: 500; }
    .section-header {
        font-size: 20px; font-weight: 700; color: #1A1A2E;
        border-left: 4px solid #185FA5; padding-left: 10px;
        margin: 24px 0 16px 0;
    }
    .insight-box {
        background: #EBF4FF; border-radius: 8px; padding: 12px 16px;
        border-left: 3px solid #185FA5; font-size: 13px; color: #333;
        margin-top: 12px;
    }
</style>
""", unsafe_allow_html=True)

PALETTE = ['#185FA5', '#1D9E75', '#D85A30', '#BA7517', '#7F77DD', '#C44569', '#2C3E50', '#8E44AD']

plt.rcParams.update({
    'figure.facecolor': 'white', 'axes.facecolor': 'white',
    'axes.grid': True, 'grid.alpha': 0.25,
    'axes.spines.top': False, 'axes.spines.right': False,
    'font.family': 'DejaVu Sans',
})

# ── Data loading ──────────────────────────────────────────────
@st.cache_data
def load_data():
    sales = pd.read_csv('data/ev_sales.csv')
    models = pd.read_csv('data/ev_models.csv')
    states = pd.read_csv('data/state_sales.csv')
    policy = pd.read_csv('data/policy.csv')

    sales.columns = sales.columns.str.strip()
    sales['Car_Brand'] = sales['Car_Brand'].str.strip()
    sales['Model'] = sales['Model'].str.strip()
    sales['Segment'] = sales['Segment'].str.strip().str.title().replace('-', 'Other')

    models.columns = models.columns.str.strip()
    models['Car_Brand'] = models['Car_Brand'].str.strip()
    models['Model'] = models['Model'].str.strip().replace('ClavisEV', 'ClavisEv')
    models.rename(columns={
        'price (Lakhs) (on road)': 'Price_Lakh',
        'battery (kWh)': 'Battery_kWh',
        'launch_year': 'Launch_Year'
    }, inplace=True)

    states['Units_Sold'] = states['Units_Sold'].astype(str).str.replace(',', '').astype(int)
    policy.columns = policy.columns.str.strip()
    policy.rename(columns={'Budget (in crore)': 'Budget_Crore'}, inplace=True)

    return sales, models, states, policy

sales, models, states, policy = load_data()

# ── Sidebar ───────────────────────────────────────────────────
st.sidebar.title("India EV Analysis")
st.sidebar.markdown("---")

years = sorted(sales['Year'].unique())
selected_years = st.sidebar.slider("Year Range", int(min(years)), int(max(years)),
                                    (int(min(years)), int(max(years))))

all_brands = sorted([b for b in sales['Car_Brand'].unique() if b != 'Others'])
selected_brands = st.sidebar.multiselect("Filter Brands", all_brands, default=all_brands)

st.sidebar.markdown("---")
st.sidebar.markdown("**Data Sources**")
st.sidebar.caption("VAHAN Dashboard, SIAM, ET Auto, EvoIndia, TeamBHP, Brand Websites, Ministry of Heavy Industries")
st.sidebar.markdown("---")
st.sidebar.caption("Built with Python  pandas  matplotlib  Streamlit")

# ── Filter data ────────────────────────────────────────────────
filtered = sales[
    (sales['Year'] >= selected_years[0]) &
    (sales['Year'] <= selected_years[1]) &
    (sales['Car_Brand'].isin(selected_brands + ['Others']))
]

# ── Header ─────────────────────────────────────────────────────
st.title("India Electric Vehicle Market Analysis")
st.markdown("**Passenger cars · 2019–2025 · All Major Car Brands**")
st.markdown("---")

# ── KPI Metrics ────────────────────────────────────────────────
col1, col2, col3, col4, col5 = st.columns(5)
total = filtered['Units_Sold'].sum()
tata = filtered[filtered['Car_Brand'] == 'Tata']['Units_Sold'].sum()
brands_n = filtered['Car_Brand'].nunique()
models_n = filtered['Model'].nunique()

latest_year = filtered['Year'].max()
prev_year = latest_year - 1
latest_sales = filtered[filtered['Year'] == latest_year]['Units_Sold'].sum()
prev_sales = filtered[filtered['Year'] == prev_year]['Units_Sold'].sum()
yoy = ((latest_sales / prev_sales) - 1) * 100 if prev_sales > 0 else 0

with col1:
    st.metric("Total Units Sold", f"{total:,}", help="All years selected")
with col2:
    st.metric("Tata Motors Share", f"{tata/total*100:.1f}%", help="% of filtered sales")
with col3:
    st.metric(f"{latest_year} Sales", f"{latest_sales:,}", f"{yoy:+.1f}% vs {prev_year}")
with col4:
    st.metric("Brands Tracked", str(brands_n))
with col5:
    st.metric("Models Tracked", str(models_n))

st.markdown("---")

# ── Tab layout ─────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Market Growth", "Brand Analysis", "Model Deep Dive",
    "State Adoption", "Policy Impact"
])

# ═══════════════════════════════════════
# TAB 1: MARKET GROWTH
# ═══════════════════════════════════════
with tab1:
    st.markdown('<div class="section-header">Year-over-Year EV Market Growth</div>', unsafe_allow_html=True)

    yearly = filtered.groupby('Year')['Units_Sold'].sum().reset_index()
    yearly['YoY_%'] = yearly['Units_Sold'].pct_change() * 100

    col_a, col_b = st.columns(2)

    with col_a:
        fig, ax = plt.subplots(figsize=(7, 4))
        bars = ax.bar(yearly['Year'], yearly['Units_Sold'], color=PALETTE[0], alpha=0.85, width=0.6)
        for bar, val in zip(bars, yearly['Units_Sold']):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 800,
                    f'{val:,}', ha='center', fontsize=8, fontweight='bold')
        ax.set_title('Total EV Sales Per Year', fontweight='bold')
        ax.set_xlabel('Year')
        ax.set_ylabel('Units Sold')
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
        st.pyplot(fig)
        plt.close()

    with col_b:
        fig, ax = plt.subplots(figsize=(7, 4))
        yoy_data = yearly.dropna(subset=['YoY_%'])
        colors = [PALETTE[1] if v >= 0 else '#E74C3C' for v in yoy_data['YoY_%']]
        bars = ax.bar(yoy_data['Year'], yoy_data['YoY_%'], color=colors, alpha=0.85, width=0.6)
        for bar, val in zip(bars, yoy_data['YoY_%']):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{val:.0f}%', ha='center', fontsize=8, fontweight='bold')
        ax.axhline(0, color='gray', linewidth=0.8)
        ax.set_title('Year-over-Year Growth Rate', fontweight='bold')
        ax.set_xlabel('Year')
        ax.set_ylabel('Growth (%)')
        st.pyplot(fig)
        plt.close()

    st.markdown('<div class="insight-box"> <strong>Key Insight:</strong> The market exploded in 2022 (~400% growth), driven by Tata\'s Nexon EV reaching mass scale and FAME II subsidies kicking in. 2025 shows a new acceleration as Mahindra enters the premium segment aggressively.</div>', unsafe_allow_html=True)

    # Cumulative growth
    st.markdown('<div class="section-header">Cumulative Sales Trajectory</div>', unsafe_allow_html=True)
    yearly['Cumulative'] = yearly['Units_Sold'].cumsum()
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.fill_between(yearly['Year'], yearly['Cumulative'], alpha=0.2, color=PALETTE[0])
    ax.plot(yearly['Year'], yearly['Cumulative'], marker='o', color=PALETTE[0], linewidth=2.5)
    for _, row in yearly.iterrows():
        ax.annotate(f"{int(row['Cumulative']):,}", (row['Year'], row['Cumulative']),
                    textcoords='offset points', xytext=(0, 8), ha='center', fontsize=8)
    ax.set_title('Cumulative EV Sales (Running Total)', fontweight='bold')
    ax.set_ylabel('Cumulative Units')
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)
    plt.close()

# ═══════════════════════════════════════
# TAB 2: BRAND ANALYSIS
# ═══════════════════════════════════════
with tab2:
    st.markdown('<div class="section-header">Brand Market Share</div>', unsafe_allow_html=True)

    brand_year = filtered.groupby(['Year', 'Car_Brand'])['Units_Sold'].sum().reset_index()
    brand_total = filtered.groupby('Car_Brand')['Units_Sold'].sum().sort_values(ascending=False).reset_index()

    col_a, col_b = st.columns([3, 2])

    with col_a:
        fig, ax = plt.subplots(figsize=(8, 5))
        pivot = brand_year.pivot_table(index='Year', columns='Car_Brand', values='Units_Sold', fill_value=0)
        pivot_pct = pivot.div(pivot.sum(axis=1), axis=0) * 100
        pivot_pct.plot(kind='area', stacked=True, ax=ax, alpha=0.8,
                       color=PALETTE[:len(pivot_pct.columns)])
        ax.set_title('Brand Market Share Over Time (%)', fontweight='bold')
        ax.set_ylabel('Market Share (%)')
        ax.set_ylim(0, 100)
        ax.legend(fontsize=8, loc='upper left')
        st.pyplot(fig)
        plt.close()

    with col_b:
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(brand_total['Units_Sold'], labels=brand_total['Car_Brand'],
               autopct='%1.1f%%', startangle=140,
               colors=PALETTE[:len(brand_total)],
               wedgeprops=dict(width=0.55), pctdistance=0.82)
        ax.set_title('Overall Brand Share', fontweight='bold')
        st.pyplot(fig)
        plt.close()

    st.markdown('<div class="section-header">Brand Sales Trends</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 5))
    top_brands = brand_total['Car_Brand'].head(6).tolist()
    for i, brand in enumerate(top_brands):
        data = brand_year[brand_year['Car_Brand'] == brand]
        ax.plot(data['Year'], data['Units_Sold'], marker='o', linewidth=2.5,
                markersize=6, label=brand, color=PALETTE[i])
        last = data.iloc[-1]
        ax.annotate(f"{int(last['Units_Sold']):,}", xy=(last['Year'], last['Units_Sold']),
                    xytext=(5, 0), textcoords='offset points', fontsize=8, color=PALETTE[i])
    ax.set_title('Brand-wise Sales Trend', fontweight='bold')
    ax.set_ylabel('Units Sold')
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    ax.legend()
    st.pyplot(fig)
    plt.close()

    # Brand table
    st.markdown('<div class="section-header">Brand Summary Table</div>', unsafe_allow_html=True)
    brand_summary = brand_total.copy()
    brand_summary['Share_%'] = (brand_summary['Units_Sold'] / brand_summary['Units_Sold'].sum() * 100).round(1)
    brand_summary.columns = ['Brand', 'Total Units Sold', 'Market Share (%)']
    st.dataframe(brand_summary.set_index('Brand'), use_container_width=True)

# ═══════════════════════════════════════
# TAB 3: MODEL DEEP DIVE
# ═══════════════════════════════════════
with tab3:
    st.markdown('<div class="section-header">Top Models by Total Sales</div>', unsafe_allow_html=True)

    model_total = filtered.groupby(['Car_Brand', 'Model'])['Units_Sold'].sum().reset_index()
    model_total['Model_Label'] = model_total['Car_Brand'] + ' ' + model_total['Model']
    top10 = model_total.sort_values('Units_Sold', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    brand_color_map = {b: PALETTE[i] for i, b in enumerate(top10['Car_Brand'].unique())}
    colors = [brand_color_map[b] for b in top10['Car_Brand']]
    bars = ax.barh(top10['Model_Label'][::-1], top10['Units_Sold'][::-1], color=colors[::-1], alpha=0.87)
    for bar, val in zip(bars, top10['Units_Sold'][::-1]):
        ax.text(bar.get_width() + 200, bar.get_y() + bar.get_height()/2,
                f'{val:,}', va='center', fontsize=9, fontweight='bold')
    ax.set_title('Top 10 EV Models by Total Sales', fontweight='bold')
    ax.set_xlabel('Total Units Sold')
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)
    plt.close()

    st.markdown('<div class="section-header">Price vs Battery Capacity</div>', unsafe_allow_html=True)
    st.caption("Bubble size represents total units sold. Models without spec data excluded.")

    model_sales = sales.groupby(['Car_Brand', 'Model'])['Units_Sold'].sum().reset_index()
    specs_clean = models[models['Car_Brand'] != 'Others'].copy()
    spec_sales = pd.merge(specs_clean, model_sales, on=['Car_Brand', 'Model'], how='left')
    spec_sales['Units_Sold'] = spec_sales['Units_Sold'].fillna(100)

    brand_colors = {b: PALETTE[i] for i, b in enumerate(spec_sales['Car_Brand'].unique())}

    fig, ax = plt.subplots(figsize=(12, 6))
    for brand, group in spec_sales.groupby('Car_Brand'):
        color = brand_colors.get(brand, '#999')
        ax.scatter(group['Price_Lakh'], group['Battery_kWh'],
                   s=group['Units_Sold'] / 15, color=color, alpha=0.75,
                   label=brand, edgecolors='white', linewidths=0.8)
        for _, row in group.iterrows():
            ax.annotate(row['Model'], (row['Price_Lakh'], row['Battery_kWh']),
                        textcoords='offset points', xytext=(5, 4), fontsize=7.5, color='#333')
    ax.axvspan(0, 20, alpha=0.04, color='green')
    ax.axvline(20, color='green', linestyle='--', alpha=0.3, linewidth=1.2)
    ax.set_title('Price vs Battery Capacity (bubble = sales volume)', fontweight='bold')
    ax.set_xlabel('Price (₹ Lakh, on-road)')
    ax.set_ylabel('Battery Capacity (kWh)')
    ax.legend(fontsize=9, loc='upper left')
    st.pyplot(fig)
    plt.close()

    st.markdown('<div class="insight-box"> Models under ₹20L (green) account for the majority of sales volume, the larger bubbles cluster in the affordable-to-mid segment, confirming that <strong>price sensitivity drives EV adoption</strong> in India more than battery size.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">Full Model Specifications</div>', unsafe_allow_html=True)
    display_models = models[models['Car_Brand'] != 'Others'][['Car_Brand', 'Model', 'Segment', 'Launch_Year', 'Price_Lakh', 'Battery_kWh']].copy()
    display_models.columns = ['Brand', 'Model', 'Segment', 'Launch Year', 'Price (₹L)', 'Battery (kWh)']
    st.dataframe(display_models.sort_values(['Brand', 'Price (₹L)']).set_index('Brand'), use_container_width=True)

# ═══════════════════════════════════════
# TAB 4: STATE ADOPTION
# ═══════════════════════════════════════
with tab4:
    st.markdown('<div class="section-header">State-wise EV Registrations (2024)</div>', unsafe_allow_html=True)

    states_sorted = states.sort_values('Units_Sold', ascending=True)
    states_sorted['Share_%'] = (states_sorted['Units_Sold'] / states_sorted['Units_Sold'].sum() * 100).round(1)

    col_a, col_b = st.columns([3, 2])

    with col_a:
        fig, ax = plt.subplots(figsize=(8, 5))
        color_grad = plt.cm.Blues(np.linspace(0.35, 0.85, len(states_sorted)))
        bars = ax.barh(states_sorted['State'], states_sorted['Units_Sold'], color=color_grad, alpha=0.9)
        for bar, row in zip(bars, states_sorted.itertuples()):
            ax.text(bar.get_width() + 300, bar.get_y() + bar.get_height()/2,
                    f'{row.Units_Sold:,}  ({row._3}%)', va='center', fontsize=9)
        ax.set_title('EV Registrations by State', fontweight='bold')
        ax.set_xlabel('Units Sold')
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
        st.pyplot(fig)
        plt.close()

    with col_b:
        st.dataframe(
            states.sort_values('Units_Sold', ascending=False)
                  .assign(**{'Share (%)': lambda d: (d['Units_Sold'] / d['Units_Sold'].sum() * 100).round(1)})
                  .set_index('State'),
            use_container_width=True
        )
        st.markdown('<div class="insight-box"> Maharashtra + Karnataka + Kerala account for <strong> around 48%</strong> of all EV sales. Tier-2 cities represent a massive untapped growth.</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════
# TAB 5: POLICY IMPACT
# ═══════════════════════════════════════
with tab5:
    st.markdown('<div class="section-header">Government Policy vs Sales Growth</div>', unsafe_allow_html=True)

    yearly_all = sales.groupby('Year')['Units_Sold'].sum().reset_index()

    fig, ax1 = plt.subplots(figsize=(13, 6))
    ax1.bar(yearly_all['Year'], yearly_all['Units_Sold'], color=PALETTE[0], alpha=0.5, label='EV Units Sold', width=0.5)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Units Sold', color=PALETTE[0])
    ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    ax1.tick_params(axis='y', labelcolor=PALETTE[0])

    ax2 = ax1.twinx()
    ax2.plot(policy['Year'], policy['Budget_Crore'], 'o--', color=PALETTE[2],
             linewidth=2.5, markersize=9, label='Policy Budget (₹ Cr)')
    ax2.set_ylabel('Policy Budget (₹ Crore)', color=PALETTE[2])
    ax2.tick_params(axis='y', labelcolor=PALETTE[2])
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

    for _, row in policy.iterrows():
        ax1.axvline(x=row['Year'], color='gray', linestyle=':', alpha=0.35, linewidth=1)
        y_vals = yearly_all[yearly_all['Year'] == row['Year']]['Units_Sold'].values
        y = y_vals[0] if len(y_vals) > 0 else 3000
        ax1.text(row['Year'], y + 2000, row['Policy Name'].replace(' ', '\n'),
                 ha='center', fontsize=6.5, color='#444',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.75))

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    ax1.set_title('Government Policy Spend vs EV Market Growth', fontsize=13, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.markdown('<div class="section-header">Policy Timeline</div>', unsafe_allow_html=True)
    st.dataframe(policy.set_index('Year'), use_container_width=True)

    st.markdown('<div class="insight-box">  <strong>FAME II (₹11,500 Cr, 2019)</strong> was the single biggest catalyst — but effects lagged ~2 years. The PLI schemes for batteries (₹18,100 Cr) and automobiles (₹25,938 Cr) are structural investments expected to drive cost reduction through 2026–28. PM E-Drive (2024) focuses on charging infrastructure — the next key bottleneck.</div>', unsafe_allow_html=True)
