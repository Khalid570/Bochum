import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

# Baryons and their quark compositions (including anti-quarks for demonstration)
charmed_hadrons = {
    "D$^+$": ["$c$", "$|d|$"],
    "D$^-$": ["$|c|$", "$d$"],
    "D$^0$": ["$c$", "$|u|$"],
    "|D|$^0$": ["$|c|$", "$u$"],
    "Λ$_c^+$": ["$c$", "$u$", "$d$"],
    "Ξ$_c^0$": ["$c$", "$d$", "$s$"],
    "Ξ$_c^+$": ["$c$", "$s$", "$u$"],
    "Ω$_c^0$": ["$c$", "$s$", "$s$"],
    
}
# "$\Sigma_c^0$": ["$c$", "$d$", "$d$"],
# "$\Sigma_c^+$": ["$c$", "$d$", "$u$"],
# "$\Sigma_c^++$": ["$c$", "$u$", "$u$"]
# Arbitrary lifetimes for the particles (you should replace with real values)
lifetimes = {
    "D$^+$": 1.033,
    "D$^-$": 1.033,
    "D$^0$": 0.4103,
    "|D|$^0$": 0.4103,
    "Λ$_c^+$": 0.2015,
    "Ξ$_c^0$": 0.1519,
    "Ξ$_c^+$": 0.453,
    "Ω$_c^0$" : 0.268,
}

# Colors for the quarks (for visualization purposes)
colors = {
    "$c$": "red",
    "$u$": "blue",
    "$d$": "green",
    "$s$": "yellow"
}

# Function to darken a color
def darken_color(color_str, scale_factor=0.5):
    rgb = mcolors.to_rgb(color_str)
    return [x * scale_factor for x in rgb]

# Normalize the lifetimes
max_lifetime = max(lifetimes.values())
normalized_lifetimes = {b: lt / max_lifetime for b, lt in lifetimes.items()}

scaling_factor = 3  # Adjust as needed

rows = 4
cols = (len(charmed_hadrons) + 1) // 4  # This will take care of both odd and even number of hadrons

# Adjust the figure size here
fig, axes = plt.subplots(rows, cols, figsize=(15, 15))

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n".format(pct)

for ax, (baryon, quarks) in zip(axes.ravel(), charmed_hadrons.items()):
    quark_colors = []
    for q in quarks:
        if '|' in q:  # Check if anti-quark
            quark_colors.append(darken_color(colors[q.replace('|', '')]))
        else:
            quark_colors.append(colors[q])
    
    radius = scaling_factor * normalized_lifetimes[baryon]
    font_scale = 1.5 * normalized_lifetimes[baryon]
    patches, texts, autotexts = ax.pie([1] * len(quarks), labels=quarks, colors=quark_colors, startangle=90, autopct=lambda pct: func(pct, [1]*len(quarks)), radius=radius)
    
    for t in texts:
        t.set_size(12 * font_scale)
    for t in autotexts:
        t.set_size(10 * font_scale)
        t.set_color('white')
    
    ax.set_title(baryon)
    ax.set_aspect("equal")

# Adjust the spacing between subplots here
plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.tight_layout()
plt.show()

