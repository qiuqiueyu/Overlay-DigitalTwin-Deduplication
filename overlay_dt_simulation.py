import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Academic plotting standard configuration
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# ==========================================
# 1. Parameter Definition & Data Generation
# ==========================================
N_range = np.arange(10, 101, 10)  # Physical scale: N = 10 to 100 Leaf switches
T_samples = [50, 150, 300]        # Tenant scale samples

# Relative weight coefficients from the mathematical model
C_leaf = 10
C_tun = 5
C_instance = 2
C_obj = 1
C_link = 0.5

plot_data = []
np.random.seed(42)  # For perfect reproducibility

for T in T_samples:
    for N in N_range:
        # --- Underlay 1:1 Full Physical Model (Mu) ---
        S_leaf_total = N * C_leaf
        S_tunnel_total = (N * (N - 1) / 2) * C_tun  # O(N^2) item
        
        # Simulating ANYCAST gateway multi-replication across scattered Leaf switches
        S_instance_total = 0
        for _ in range(T):
            b_i = np.random.randint(2, 7)  # 2 to 6 BDs per tenant
            scattered_leaf_count = max(1, int(N * 0.35))  # VM scattered over 35% of network
            S_instance_total += scattered_leaf_count * (1 + b_i) * C_instance
            
        S_u = S_leaf_total + S_tunnel_total + S_instance_total
        
        # --- Proposed Overlay Deduplicated Logical Model (Mo) ---
        S_logic_total = 0
        for _ in range(T):
            b_i = np.random.randint(2, 7)
            S_logic_total += (1 + b_i) * C_obj  # Fully decoupled from N
        S_logic_link = T * 4 * C_link
        S_o = S_logic_total + S_logic_link
        
        CR = S_u / S_o
        plot_data.append({'T': T, 'N': N, 'S_u': S_u, 'S_o': S_o, 'CR': CR})

df = pd.DataFrame(plot_data)

# ==========================================
# 2. Print Academic Standard Data Table (CORRECTED)
# ==========================================
print("\n" + "="*85)
print("TABLE I: EXPERIMENTAL CROSS-SECTIONAL DATA UNDER DIFFERENT NETWORK SCALES (N)")
print("="*85)
print(f"{'Leaf (N)':<10}{'Su (T=50)':<12}{'So (T=50)':<12}{'Su (T=300)':<15}{'So (T=300)':<15}{'CR (T=300)':<10}")
print("-"*85)
for N in N_range: # FIXED: Added N_range object here
    su_50 = df[(df['N']==N) & (df['T']==50)]['S_u'].values[0]
    so_50 = df[(df['N']==N) & (df['T']==50)]['S_o'].values[0]
    su_300 = df[(df['N']==N) & (df['T']==300)]['S_u'].values[0]
    so_300 = df[(df['N']==N) & (df['T']==300)]['S_o'].values[0]
    cr_300 = df[(df['N']==N) & (df['T']==300)]['CR'].values[0]
    print(f"{N:<10}{int(su_50):<12}{int(so_50):<12}{int(su_300):<15}{int(so_300):<15}{cr_300:<10.2f}")
print("="*85 + "\n")

# ==========================================
# 3. High-Quality Academic Plotting (Dual Y-Axis)
# ==========================================
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(15, 6.5))

colors_u = ['#ff7675', '#d63031', '#2d3436']  # Warm colors for heavy Mu
colors_o = ['#74b9ff', '#0984e3', '#273c75']  # Cool colors for lightweight Mo
markers = ['o', 's', '^']

# --- Fig 2(a): State Space Overhead with Dual Y-Axis ---
# Primary Y-axis for Physical Model (Mu)
for i, T in enumerate(T_samples):
    sub_df = df[df['T'] == T]
    ax1.plot(sub_df['N'], sub_df['S_u'], color=colors_u[i], marker=markers[i], 
             linewidth=2, linestyle='-', label=f'$M_u$ (Physical, $T$={T})')
ax1.set_xlabel('Physical Network Scale (Leaf Count $N$)', fontsize=12)
ax1.set_ylabel('State Space Overhead of $M_u$ (Left Axis)', color='#d63031', fontsize=12)
ax1.tick_params(axis='y', labelcolor='#d63031')
ax1.grid(True, linestyle='--', alpha=0.5)

# Secondary Y-axis for Proposed Logical Model (Mo) -> Solving the stacking issue!
ax2 = ax1.twinx()
for i, T in enumerate(T_samples):
    sub_df = df[df['T'] == T]
    ax2.plot(sub_df['N'], sub_df['S_o'], color=colors_o[i], marker=markers[i], 
             linewidth=2, linestyle='--', label=f'$M_o$ (Proposed, $T$={T})')
ax2.set_ylabel('State Space Overhead of $M_o$ (Right Axis)', color='#0984e3', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#0984e3')

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)
ax1.set_title('(a) State Space Overhead vs. Network Scale $N$', fontsize=13, fontweight='bold')

# --- Fig 2(b): Compression Ratio (CR) ---
colors_cr = ['#55efc4', '#00b894', '#006266']
for i, T in enumerate(T_samples):
    sub_df = df[df['T'] == T]
    ax3.plot(sub_df['N'], sub_df['CR'], color=colors_cr[i], marker=markers[i], 
             linewidth=2, linestyle='-', label=f'CR ($T$={T})')

ax3.set_xlabel('Physical Network Scale (Leaf Count $N$)', fontsize=12)
ax3.set_ylabel('Resource Compression Ratio ($\mathit{CR}$)', fontsize=12)
ax3.set_title('(b) Compression Ratio Scaling Trends over $N$', fontsize=13, fontweight='bold')
ax3.grid(True, linestyle='--', alpha=0.5)
ax3.legend(fontsize=10, loc='upper left')

plt.tight_layout()
plt.savefig('fig2_simulation_results.png', dpi=300)
print("[Success] High-resolution academic figure saved as 'fig2_simulation_results.png'!")
