## 📊 Dataset Overview

This project uses a **Predictive Maintenance Dataset** containing **10,000 records** and **10 features**, representing sensor readings, machine characteristics, and failure labels for industrial equipment.

---

### **Dataset Structure**
| Column Name | Description | Data Type |
|-------------|-------------|-----------|
| **UDI** | Unique identifier for each record | Integer |
| **Product ID** | Unique ID of the product | String |
| **Type** | Product type (e.g., L, M, H) | Categorical |
| **Air temperature [K]** | Ambient air temperature in Kelvin | Float |
| **Process temperature [K]** | Temperature during the process in Kelvin | Float |
| **Rotational speed [rpm]** | Rotational speed of the machine in revolutions per minute | Integer |
| **Torque [Nm]** | Torque applied on the tool in Newton-meters | Float |
| **Tool wear [min]** | Tool wear measured in minutes | Integer |
| **Target** | Failure indicator (0 = No Failure, 1 = Failure) | Integer |
| **Failure Type** | Type of machine failure (e.g., No Failure, Heat Dissipation Failure, etc.) | Categorical |

---

### **Key Characteristics**
- **Total Records:** 10,000  
- **Missing Values:** None  
- **Feature Types:**  
  - Numerical: 7  
  - Categorical: 3  
- **Target Variable:** `Target` (Binary classification — Predict failure occurrence)

---

### **Statistical Summary**
| Feature | Mean | Std Dev | Min | Max |
|---------|------|---------|-----|-----|
| Air temperature [K] | 300.00 | 2.00 | 295.3 | 304.5 |
| Process temperature [K] | 310.01 | 1.48 | 305.7 | 313.8 |
| Rotational speed [rpm] | 1538.78 | 179.28 | 1168 | 2886 |
| Torque [Nm] | 39.99 | 9.97 | 3.8 | 76.6 |
| Tool wear [min] | 107.95 | 63.65 | 0 | 253 |
| Target (Failure Rate) | 3.39% | - | 0 | 1 |

---

### **Use Case**
This dataset is ideal for:
- **Predictive Maintenance** — Forecasting potential equipment failures.
- **Classification Modeling** — Identifying machines likely to fail.
- **Feature Importance Analysis** — Determining which machine parameters most influence failures.

---

> **Source:** The dataset is typically used in predictive maintenance research and industrial machine learning case studies.
