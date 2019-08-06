clear all
clc
run var
for iter =1:iter_max
    run channel
    run precoding 
    run interference
end