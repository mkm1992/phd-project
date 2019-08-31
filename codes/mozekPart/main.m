clear all
clc
run var
for iter =1:iter_max
    run channel
    run precoding 
    run mappingOtherParameter 
    run MapPRB2UT
    run interference
    run rate
    run FronthaulCap
    run FindDelay % assume that each service just map to one slice if not transmission delay must recalculate
end