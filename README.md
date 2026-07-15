# 📈 Annual CMS Onboarding Trends: January Medical Waste Audit Optimization ## 

📋 **Executive Summary:** This project analyzes the July 2026 Centers for Medicare & Medicaid Services (CMS) dataset containing **57,197 medical equipment supplier records**. The analysis reveals a massive **annual onboarding peak in January (20k+ suppliers)**, identifying a critical window for targeted waste audits and supply chain risk mitigation. 

<img width="567" height="353" alt="Image" src="https://github.com/user-attachments/assets/2ded0a72-fdd5-4305-9d20-4c075d5107c2" />

🔗 **View Interactive Tableau Dashboard:** 
https://public.tableau.com/authoring/AnnualOnboardingTrendsJanuaryPeakPerformance/Sheet1#1

 📁 **View Python Data Pipeline**
(PASTE_YOUR_GITHUB_CODE_LINK_HERE)

⚠️ **The Business Challenge:** Healthcare networks nationwide face severe financial and operational strain from **wasted medical equipment and inventory stockouts**. Hospital administrators benefit from data driven insights into the **equipment supplier peaks that cause:**
* **Higher risks of accidental inventory waste and expiration.** 
* **Severe processing and compliance delays.** 

🛠️ **Data Pipeline & Methodology:** To solve this, I built a data pipeline to ingest, clean, and visualize the CMS registry: 
* **Data Wrangling:** **Cleaned 57,197 raw records** using `Python`, `Pandas`, and `NumPy` to handle missing values and standardize supplier profiles. 
* **Feature Engineering:** Converted irregular string timestamps into standardized `datetime` formats to isolate seasonal trends. 
* **Data Visualization:** Built an interactive trend dashboard in `Tableau Public` to track month-over-month onboarding volumes for stakeholder presentations. 

📊 **Key Insights & Analytics:**

<img width="567" height="353" alt="Image" src="https://github.com/user-attachments/assets/2ded0a72-fdd5-4305-9d20-4c075d5107c2" />

* **January Peak:** Onboarding spikes dramatically in January with **over 20,000 new suppliers**—double any other month. 
* **Secondary Influxes:** March serves as the second-highest month (10,000+), followed by a minor peak in July (5,000+). 
* **Seasonality Pattern:** The first month of Q1 and Q3 drive the highest administrative and inventory risk. 

💡 **Business Impact & Recommendations:** 
* **Operational Optimization:** Armed with this data, hospital management can transition from reactive scheduling to a **predictive staffing model**, heavily scaling inventory teams in January. 
* **Targeted Waste Audits:** Directing compliance audits specifically to the January onboarding cohort minimizes processing bottlenecks and prevents early-stage inventory waste. 
* **Risk Mitigation:** Aligning supply chain guardrails with known CMS release cycles reduces equipment shortages and optimizes holding costs. 

📁 **Technical Appendix** 
* **Data Sources:** Centers for Medicare & Medicaid Services (CMS) July 2026 Supplier Directory
 https://data.cms.gov/provider-data/dataset/ct36-nrcq
* **Tech Stack:** Python 3.x, Pandas, NumPy, Tableau Public 

