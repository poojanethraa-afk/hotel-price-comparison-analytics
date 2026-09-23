import numpy as np 
import scipy.stats

control_rate=0.0699
treatment_rate=0.09
sample_size= 1000

control_bookings= np.random.binomial(sample_size, control_rate)
treatment_bookings=np.random.binomial(sample_size, treatment_rate)

print("Control group bookings:", control_bookings, "out of", sample_size)
print("Treatment group bookings:", treatment_bookings, "out of", sample_size)

control_observed = control_bookings / sample_size
treatment_observed = treatment_bookings / sample_size

print("Control observed rate:", control_observed)
print("Treatment observed rate:", treatment_observed)

pooled_rate = (control_bookings + treatment_bookings) / (sample_size + sample_size)
print("Pooled rate:", pooled_rate)

standard_error= (pooled_rate * (1 - pooled_rate) * (2/sample_size))**0.5
print("Standard error:", standard_error)

z_score= (treatment_observed - control_observed) / standard_error
print("Z-score:", z_score)

p_value = 2 * (1 - scipy.stats.norm.cdf(abs(z_score)))
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: statistically significant")
else:
    print("Result: not statistically significant")