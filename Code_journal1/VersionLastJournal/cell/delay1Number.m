a20T = (a1T+a2T+a3T+a5T)/4
a20W = (a1W+a2W+a3W+a4W+a5W)/5
b20T = (b1T+b2T+b3T+b5T)/4
C20T = (c3T+c5T)/2
plot(a20T)
hold on
plot(a20W)
numB = count_min1:count_step1:count_max1
A40T = 1e-3*[0.0284,0.0532,0.0767,0.1014,0.1279];
figure;
plot(numB/1e6,A40T/1e-3)
hold all
plot(numB/1e6,A35T/1e-3) 
plot(numB/1e6,A30T/1e-3)
plot(numB/1e6,A1T/1e-3)
plot(numB/1e6,a20T/1e-3)
xlabel('Mean Arrival Rate\lambda (Mbps)')
ylabel('Mean Total Delay of a Service (msec)')


plot(numB/1e6,C20T/1e-3)
hold all
plot(numB/1e6,a20T/1e-3)
plot(numB/1e6,b20T/1e-3)
xlabel('Mean Arrival Rate\lambda (Mbps)')
ylabel('Mean Total Delay of a Service (msec)')
title('Mean Total Delay of a Service vs. the Mean Arrival Rate')

