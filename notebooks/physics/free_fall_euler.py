# %% [markdown]
# # Exercise 01: Free fall with Euler's method
#
# In this exercise, model an object thrown straight upward and then falling back to the ground.
# You will calculate its height one small time step at a time, compare the result with the
# exact physics equation, and see how the time step changes the error.
#
# **What you will practice**
#
# - Turning a motion equation into a Python function
# - Updating position and velocity with a loop
# - Checking results with simple assertions
# - Comparing numerical and exact results in an interactive Plotly graph
#
# **Milestones**
#
# 1. Write the exact height equation and calculate when the object reaches the ground.
# 2. Build a simple Euler simulation using lists and a while loop.
# 3. Check the simulation and compare a coarse and a fine time step.
# 4. Plot the paths and the error.
#
# We use the sign convention that upward is positive. Acceleration is therefore -g, and
# the exact height is \(y(t) = y_0 + v_0t - \frac{1}{2}gt^2\).

# %% [markdown]
# ## Milestone 1: Set up the physics model
#
# The object starts 20 m above the ground with an upward velocity of 12 m/s.
# Gravity is approximately 9.81 m/s². The positive solution of \(y(t)=0\) gives
# the exact time when it returns to ground level.

# %%
gravity = 9.81
start_height = 20.0
initial_velocity = 12.0


def exact_height(time_seconds, start_height, initial_velocity, gravity):
    """Return the height from the exact constant-acceleration equation."""
    height = start_height + initial_velocity * time_seconds
    height = height - 0.5 * gravity * time_seconds**2
    return height


impact_time = (initial_velocity + (initial_velocity**2 + 2 * gravity * start_height) ** 0.5) / gravity

print(f"Exact impact time: {impact_time:.2f} s")
print(f"Height at the start: {exact_height(0, start_height, initial_velocity, gravity):.1f} m")

# %% [markdown]
# **Pause and predict:** Should the height first increase or decrease? What do you expect
# to happen to the numerical result if we make the time step smaller?

# %% [markdown]
# ## Milestone 2: Build Euler's method
#
# At each time step, use the current velocity to update the height, then use gravity to
# update the velocity:
#
# - new height = old height + old velocity × time step
# - new velocity = old velocity - gravity × time step
#
# This is Euler's method. It is an approximation because it treats the velocity as constant
# during each short time step.

# %%
def euler_simulation(start_height, initial_velocity, gravity, time_step):
    """Return lists of times, heights, and velocities from an Euler simulation."""
    if time_step <= 0:
        raise ValueError("time_step must be greater than zero")

    times = [0.0]
    heights = [start_height]
    velocities = [initial_velocity]

    while heights[-1] >= 0:
        next_height = heights[-1] + velocities[-1] * time_step
        next_velocity = velocities[-1] - gravity * time_step
        next_time = times[-1] + time_step

        times.append(next_time)
        heights.append(next_height)
        velocities.append(next_velocity)

    return times, heights, velocities


# %% [markdown]
# ## Milestone 3: Run and check the simulation
#
# A coarse step gives fewer calculations. A fine step gives more calculations and should
# usually track the exact curve more closely. The last Euler point may pass slightly below
# the ground because the simulation advances by a whole time step.

# %%
coarse_step = 0.20
fine_step = 0.05

coarse_times, coarse_heights, coarse_velocities = euler_simulation(
    start_height, initial_velocity, gravity, coarse_step
)
fine_times, fine_heights, fine_velocities = euler_simulation(
    start_height, initial_velocity, gravity, fine_step
)

# Simple checks: the model starts correctly and ends just after crossing ground level.
assert exact_height(0, start_height, initial_velocity, gravity) == start_height
assert abs(exact_height(impact_time, start_height, initial_velocity, gravity)) < 1e-10
assert coarse_heights[0] == start_height
assert coarse_heights[-1] < 0
assert coarse_heights[-2] >= 0
assert fine_heights[-1] < 0
assert fine_heights[-2] >= 0
assert abs(fine_times[-1] - impact_time) < abs(coarse_times[-1] - impact_time)

print("All checks passed.")
print(f"Exact impact time: {impact_time:.3f} s")
print(f"Euler impact estimate (step {coarse_step:.2f} s): {coarse_times[-1]:.3f} s")
print(f"Euler impact estimate (step {fine_step:.2f} s): {fine_times[-1]:.3f} s")

# %% [markdown]
# The Euler impact estimate is the time of its first point below zero. Its error is less
# than one time step here. The smaller step should give a closer estimate for these values.

# %% [markdown]
# ## Milestone 4: Visualize the path and numerical error
#
# The top graph compares the exact curve with both Euler simulations. The lower graph shows
# the absolute height error at matching time points before impact.

# %%
import plotly.graph_objects as go
from plotly.subplots import make_subplots

exact_times = []
for time_seconds in fine_times:
    if time_seconds <= impact_time:
        exact_times.append(time_seconds)
exact_times.append(impact_time)

exact_heights = []
for time_seconds in exact_times:
    exact_heights.append(
        exact_height(time_seconds, start_height, initial_velocity, gravity)
    )

coarse_error_times = []
coarse_errors = []
for index in range(len(coarse_times)):
    if coarse_times[index] <= impact_time:
        coarse_error_times.append(coarse_times[index])
        exact_value = exact_height(
            coarse_times[index], start_height, initial_velocity, gravity
        )
        coarse_errors.append(abs(coarse_heights[index] - exact_value))

fine_error_times = []
fine_errors = []
for index in range(len(fine_times)):
    if fine_times[index] <= impact_time:
        fine_error_times.append(fine_times[index])
        exact_value = exact_height(
            fine_times[index], start_height, initial_velocity, gravity
        )
        fine_errors.append(abs(fine_heights[index] - exact_value))

figure = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.12,
    subplot_titles=("Height above ground", "Absolute height error"),
)

figure.add_trace(
    go.Scatter(x=exact_times, y=exact_heights, mode="lines", name="Exact equation"),
    row=1,
    col=1,
)
figure.add_trace(
    go.Scatter(
        x=coarse_times,
        y=coarse_heights,
        mode="lines+markers",
        name=f"Euler, dt={coarse_step:.2f} s",
    ),
    row=1,
    col=1,
)
figure.add_trace(
    go.Scatter(
        x=fine_times,
        y=fine_heights,
        mode="lines+markers",
        name=f"Euler, dt={fine_step:.2f} s",
    ),
    row=1,
    col=1,
)
figure.add_trace(
    go.Scatter(x=coarse_error_times, y=coarse_errors, mode="lines+markers", name="Coarse step error"),
    row=2,
    col=1,
)
figure.add_trace(
    go.Scatter(x=fine_error_times, y=fine_errors, mode="lines+markers", name="Fine step error"),
    row=2,
    col=1,
)

figure.update_xaxes(title_text="Time (s)", row=2, col=1)
figure.update_yaxes(title_text="Height (m)", row=1, col=1)
figure.update_yaxes(title_text="Absolute error (m)", rangemode="tozero", row=2, col=1)
figure.update_layout(
    title="Free fall: Euler's method compared with the exact equation",
    height=700,
    legend_title_text="Model",
)
figure.show()

# %% [markdown]
# ## Reflect
#
# 1. Which Euler curve follows the exact curve more closely?
# 2. Why can the final Euler point be below zero?
# 3. What happens to the number of calculation steps when you reduce the time step?
#
# **Next small challenge:** Change the starting height or initial velocity and predict the
# new path before running the notebook. After this exercise, a natural extension is to compare
# this loop with SciPy's \`solve_ivp\`, which solves the same differential equations for you.