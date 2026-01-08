import matplotlib.pyplot as plt

# ============================================================
# USER PARAMETERS
# ============================================================

years = 10
months = years * 12

# Targets
lisa_target = 25000  # Deposit must come from LISA
isa_fees_target = 2000  # Fees paid from Cash ISA

# Starting balances (Jan 2026)
lisa_balance = 0.0
isa_balance = 0.0

# Monthly contributions
regular_lisa_monthly = 333
isa_monthly = 67

# Remaining LISA allowance this financial year (Jan–Mar 2025)
remaining_lisa_allowance = 1665
catchup_months = 3
lisa_catchup_monthly = remaining_lisa_allowance / catchup_months

# Interest rates (AER)
lisa_aer = 0.028
isa_aer = 0.0275

bonus_rate = 0.25

# Convert AER → monthly
lisa_r = (1 + lisa_aer) ** (1 / 12) - 1
isa_r = (1 + isa_aer) ** (1 / 12) - 1

# ============================================================
# STATE & TRACKING
# ============================================================

pending_lisa_bonus = 0.0

time_years = []
lisa_history = []
isa_history = []
total_history = []

target_month = None

# ============================================================
# SIMULATION
# ============================================================

for month in range(1, months + 1):

    # --- Apply bonus from last month ---
    lisa_balance += pending_lisa_bonus
    pending_lisa_bonus = 0.0

    # --- Contributions ---
    if month <= catchup_months:
        lisa_contribution = lisa_catchup_monthly
    else:
        lisa_contribution = regular_lisa_monthly

    isa_contribution = isa_monthly

    lisa_balance += lisa_contribution
    isa_balance += isa_contribution

    # Generate bonus (paid next month)
    pending_lisa_bonus = lisa_contribution * bonus_rate

    # --- Interest ---
    lisa_balance *= 1 + lisa_r
    isa_balance *= 1 + isa_r

    total = lisa_balance + isa_balance

    # --- Check if deposit + fees are ready ---
    if (
        target_month is None
        and lisa_balance >= lisa_target
        and isa_balance >= isa_fees_target
    ):
        target_month = month

    # --- Store history ---
    time_years.append(month / 12)
    lisa_history.append(lisa_balance)
    isa_history.append(isa_balance)
    total_history.append(total)

# ============================================================
# REPORT RESULTS
# ============================================================

print("--------------------------------------------------")
if target_month is not None:
    years_to_target = target_month // 12
    months_to_target = target_month % 12
    print(
        f"Deposit & fees ready after "
        f"{years_to_target} years and {months_to_target} months.\n"
        f"  LISA ≥ £{lisa_target:,.0f}\n"
        f"  Cash ISA ≥ £{isa_fees_target:,.0f}"
    )
else:
    print("Deposit + fees not reached within projection period.")
print("--------------------------------------------------")

# ============================================================
# PLOT
# ============================================================

plt.figure()
plt.plot(time_years, lisa_history, label="LISA")
plt.plot(time_years, isa_history, label="Cash ISA")
plt.plot(time_years, total_history, label="Total Savings")

# Target lines
plt.axhline(lisa_target, linestyle=":", linewidth=2, label="LISA deposit target (£25k)")

plt.axhline(isa_fees_target, linestyle="--", linewidth=2, label="ISA fees target (£2k)")

plt.xlabel("Years from Jan 2025")
plt.ylabel("Balance (£)")
plt.title("House Purchase Savings Projection")
plt.legend()
plt.grid(True)
plt.show()
