import math

# Mode toggle
Gibberlink_mode = 1  # Set to 0 to disable output

# Parameters
m = 2.0          # mass in kg
c = 3e8          # speed of light in m/s
alpha = 0.8      # efficiency factor
beta = 1e6       # log-scale energy booster
gamma = 0.5      # damping effect
tau = 5.0        # time constant
t = 10.0         # current time

# Equation
Gibberlink_Output = Gibberlink_mode * (
    (alpha * m * c**2 + beta * math.log(m + 1)) / 
    (1 + gamma * math.exp(-t / tau))
)

# Output
print(f"🔬 Gibberlink Output: {Gibberlink_Output:.2e} J")

import math

# Toggle
Gibberlink_mode = 1

# Parameters
m = 2.0            # mass in kg
c = 3e8            # speed of light
delta = 0.5        # tuning factor
zeta = 1e5         # secondary influence from sqrt(m)
theta = math.pi/4  # orientation angle (in radians)
eta = 0.3          # time oscillation strength
tau = 5.0          # time constant
t = 8.0            # time in seconds

# Equation
Gibberlink_Stability = Gibberlink_mode * (
    (delta * m * c**2 * math.sin(theta) + zeta * math.sqrt(m)) /
    (1 + eta * math.cos(t / tau))
)

# Output
print(f"📊 Gibberlink Stability: {Gibberlink_Stability:.2e}")
