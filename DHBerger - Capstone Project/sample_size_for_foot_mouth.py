#pull basline from provided info
baseline = 15
#compute minimum_detectable_effect
minimum_detectable_effect = 100.0 * 5 / baseline
print "minimum_detectable_effect: %f" % minimum_detectable_effect

# sample size determined from sample size calculator
sample_size_per_variant = 870

# sample size divided by the observations per week 
yellowstone_weeks_observing = sample_size_per_variant / 507.0
print "yellowstone_weeks_observing: %f" % yellowstone_weeks_observing

bryce_weeks_observing = sample_size_per_variant / 250.0
print "bryce_weeks_observing: %f" % bryce_weeks_observing

