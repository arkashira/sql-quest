# breakeven.md

## Unit Economics & Break-even Analysis for SQL Quest

### Cost per Active User
1. **Compute Costs**: 
   - Average cost per user per month: $5
   - Estimated monthly compute cost per user (cloud services): $5

2. **Storage Costs**: 
   - Average storage requirement per user: 10 GB
   - Cost per GB per month: $0.02
   - Estimated monthly storage cost per user: $0.20

3. **Bandwidth Costs**: 
   - Average data transfer per user: 50 GB
   - Cost per GB of data transfer: $0.01
   - Estimated monthly bandwidth cost per user: $0.50

**Total Cost per Active User**:  
Compute + Storage + Bandwidth = $5 + $0.20 + $0.50 = **$5.70**

### Pricing Tiers
| Tier        | Price ($/mo) | Features                                               |
|-------------|---------------|--------------------------------------------------------|
| Basic       | $15           | 1 User, 10 GB Storage, Basic Query Automation         |
| Professional | $30          | 5 Users, 50 GB Storage, Advanced Query Automation, Analytics Dashboard |
| Enterprise   | $60          | 20 Users, 200 GB Storage, Custom Integrations, Priority Support |

### Customer Acquisition Cost (CAC) Range
- Estimated CAC: $100 - $200 per user
  - This includes marketing, sales, and onboarding costs.

### Lifetime Value (LTV) Estimate
- Average user lifespan: 24 months
- Average revenue per user (ARPU) for Basic Tier: $15
- LTV = ARPU * Average User Lifespan = $15 * 24 = **$360**

### Break-even Users Count
- Fixed Costs (monthly): $5,000
- Contribution Margin per User (ARPU - Cost per Active User):
  - Basic Tier: $15 - $5.70 = $9.30
  - Professional Tier: $30 - $5.70 = $24.30
  - Enterprise Tier: $60 - $5.70 = $54.30

**Break-even Users Count**:
- Basic Tier: $5,000 / $9.30 ≈ **537 users**
- Professional Tier: $5,000 / $24.30 ≈ **206 users**
- Enterprise Tier: $5,000 / $54.30 ≈ **92 users**

### Path to $10K MRR
To achieve $10,000 in Monthly Recurring Revenue (MRR), we can analyze the required users for each tier:

1. **Basic Tier**:
   - $10,000 / $15 = **667 users**

2. **Professional Tier**:
   - $10,000 / $30 = **334 users**

3. **Enterprise Tier**:
   - $10,000 / $60 = **167 users**

### Summary
- **Total Cost per Active User**: $5.70
- **Pricing Tiers**: Basic ($15), Professional ($30), Enterprise ($60)
- **CAC Range**: $100 - $200
- **LTV Estimate**: $360
- **Break-even Users Count**: Basic (537), Professional (206), Enterprise (92)
- **Path to $10K MRR**: Basic (667 users), Professional (334 users), Enterprise (167 users)