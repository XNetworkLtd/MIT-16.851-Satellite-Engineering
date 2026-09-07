from astropy.time import Time

# --- REPLACE WITH YOUR ACTUAL VALUES ---
reference_date = '2026-08-01'      # your Reference Epoch Date
equator_cross_time = '10:30:00'    # your Equator Cross Time
initial_longitude = 78.0           # your Initial Orbit Longitude (deg, east positive)
altitude = 550.0                   # your Initial Orbit Altitude (km)
R_E = 6378.14

# Build epoch string
epoch_str = f"{reference_date}T{equator_cross_time}"

# Compute RAAN
t = Time(epoch_str, scale='utc')
t.delta_ut1_utc = 0.0   # avoid IERS server lookup
gmst = t.sidereal_time('mean', 'greenwich')
gmst_deg = gmst.deg
raan = (gmst_deg + initial_longitude) % 360.0
sma = R_E + altitude

print(f"Epoch: {epoch_str} UTC")
print(f"GMST: {gmst_deg:.6f} deg")
print(f"RAAN: {raan:.6f} deg")
print(f"Semi-major axis: {sma:.2f} km")