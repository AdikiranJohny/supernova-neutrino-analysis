import os
import numpy as np
import matplotlib.pyplot as plt
deltap_values = ["000", "023", "083", "434", "834", "933"]
distances = np.arange(1, 21)
results_ar40 = {}
results_elastic = {}
results_nuebar_ar40 = {}
for dp in deltap_values:
    sigma_values1, sigma_values2, sigma_values3 = [], [], []
    for i in distances:
        f1 = f"/home/cuk-physics-hep-04/Desktop/program/snowglobes/out/negativity_mo/{dp}/ih/total_fluence{dp}_ih_d{i}kpc_nue_Ar40_ar40kt_events_smeared_unweighted.dat"
        f2 = f"/home/cuk-physics-hep-04/Desktop/program/snowglobes/out/negativity_mo/{dp}/nh/total_fluence{dp}_nh_d{i}kpc_nue_Ar40_ar40kt_events_smeared_unweighted.dat"
        if os.path.exists(f1) and os.path.exists(f2):
            with open(f1, "r") as f:
                last1 = float(f.readlines()[-1].strip().split()[-1])
            with open(f2, "r") as f:
                last2 = float(f.readlines()[-1].strip().split()[-1])
            chi2 = 2 * (last1 - last2 - last2 * np.log(last1 / last2))
            sigma_values1.append(np.sqrt(chi2))
        else:
            sigma_values1.append(np.nan)
        f3 = f"/home/cuk-physics-hep-04/Desktop/program/snowglobes/out/negativity_mo/{dp}/ih/total_fluence{dp}_ih_d{i}kpc_nue_e_ar40kt_events_smeared_unweighted.dat"
        f4 = f"/home/cuk-physics-hep-04/Desktop/program/snowglobes/out/negativity_mo/{dp}/nh/total_fluence{dp}_nh_d{i}kpc_nue_e_ar40kt_events_smeared_unweighted.dat"

        if os.path.exists(f3) and os.path.exists(f4):
            with open(f3, "r") as f:
                last3 = float(f.readlines()[-1].strip().split()[-1])
            with open(f4, "r") as f:
                last4 = float(f.readlines()[-1].strip().split()[-1])
            chi2 = 2 * (last3 - last4 - last4 * np.log(last3 / last4))
            sigma_values2.append(np.sqrt(chi2))
        else:
            sigma_values2.append(np.nan)
        f5 = f"/home/cuk-physics-hep-04/Desktop/program/snowglobes/out/negativity_mo/{dp}/ih/total_fluence{dp}_ih_d{i}kpc_nuebar_Ar40_ar40kt_events_smeared_unweighted.dat"
        f6 = f"/home/cuk-physics-hep-04/Desktop/program/snowglobes/out/negativity_mo/{dp}/nh/total_fluence{dp}_nh_d{i}kpc_nuebar_Ar40_ar40kt_events_smeared_unweighted.dat"
        if os.path.exists(f5) and os.path.exists(f6):
            with open(f5, "r") as f:
                last5 = float(f.readlines()[-1].strip().split()[-1])
            with open(f6, "r") as f:
                last6 = float(f.readlines()[-1].strip().split()[-1])
            chi2 = 2 * (last5 - last6 - last6 * np.log(last5 / last6))
            sigma_values3.append(np.sqrt(chi2))
        else:
            sigma_values3.append(np.nan)
    results_ar40[dp] = np.array(sigma_values1)
    results_elastic[dp] = np.array(sigma_values2)
    results_nuebar_ar40[dp] = np.array(sigma_values3)
import matplotlib.pyplot as plt
linestyles = ["-", "--",":","-.",(0, (3, 5, 1, 5)),(0, (5, 10))         ]
colors = ["red","slategrey","cyan","black","blue","green" ]
plt.figure(figsize=(12, 10))
for i, dp in enumerate(deltap_values):
    ls = linestyles[i % len(linestyles)]
    color = colors[i % len(colors)]  # Cycle through the colors
    plt.plot(distances, results_ar40[dp], linestyle=ls, color=color, label=fr"Δp = 0.{dp}", linewidth=3.5)
plt.xlabel("Distance (kpc)", fontsize=40)
plt.ylabel(r"$\sigma = \sqrt{\Delta \chi^2}$", fontsize=40)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlim(1, 20)
plt.ylim(0, 50)
plt.title(r"$\nu_e\_Ar40$" , fontsize = 36)
plt.legend(fontsize=30 , frameon = False)
plt.grid(False)
plt.tight_layout()
plt.text(0.5, 0.95, 'NEG',fontsize=36,color='black',ha='right', va='top',transform=plt.gca().transAxes,bbox=dict(facecolor='lavender', edgecolor='none', boxstyle='round,pad=0.2'))
#plt.savefig("sensitivity_nue_ar40.png", dpi=1300)
plt.show()
plt.figure(figsize=(12, 10))
for i, dp in enumerate(deltap_values):
    ls = linestyles[i % len(linestyles)]
    color = colors[i % len(colors)]  # Cycle through the colors
    plt.plot(distances, results_elastic[dp], linestyle=ls, color=color, label=fr"Δp = 0.{dp}" , linewidth=3.5)
plt.xlabel("Distance (kpc)" , fontsize=40)
plt.ylabel(r"$\sigma = \sqrt{\Delta \chi^2}$", fontsize=40)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlim(1, 20)
plt.ylim(0, 1.4)
plt.title(r"$\nu_e\_e$" , fontsize = 36)
plt.legend(fontsize=30 , frameon = False)
plt.grid(False)
plt.tight_layout()
plt.text(0.5, 0.95, 'NEG',fontsize=36,color='black', ha='right', va='top', transform=plt.gca().transAxes, bbox=dict(facecolor='lavender', edgecolor='none', boxstyle='round,pad=0.2'))

#plt.savefig("sensitivity_nue_elastic.png", dpi=1300)
plt.show()
plt.figure(figsize=(12, 10))
for i, dp in enumerate(deltap_values):
    ls = linestyles[i % len(linestyles)]
    color = colors[i % len(colors)]
    plt.plot(distances, results_nuebar_ar40[dp], linestyle=ls, color=color , label=fr"Δp = 0.{dp}" , linewidth=3.5)
plt.xlabel("Distance (kpc)" , fontsize=40)
plt.ylabel(r"$\sigma = \sqrt{\Delta \chi^2}$", fontsize=40)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlim(1, 20)
plt.ylim(0, 9)
plt.title(r"$\bar{\nu}_e\_Ar40$" , fontsize = 36)
plt.legend(fontsize=30 , frameon = False)
plt.grid(False)
plt.tight_layout()
plt.text(0.5, 0.95, 'NEG',fontsize=36,color='black',ha='right', va='top',transform=plt.gca().transAxes,bbox=dict(facecolor='lavender', edgecolor='none', boxstyle='round,pad=0.2'))
plt.savefig("sensitivity_nuebar_ar40.png", dpi=1300)
plt.show()
