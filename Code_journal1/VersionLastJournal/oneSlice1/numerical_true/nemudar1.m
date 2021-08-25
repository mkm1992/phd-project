sumRB1 =1.0e+07 *[1.5664,3.8545, 5.2349,5.5287,5.49124,4.6093]
sumRB2 =1.0e+07 *[1.6294,3.8940, 5.3104,5.7004,5.655920,4.95]
plot(UE_num,sumRB2/1e6,'-*')
hold on
plot(UE_num, sumRB1/1e6,'-o')
xlabel('Maximum Interference (dBm)')
ylabel('Aggregate Throughput (Mbps)')
title('Aggregate Throughput vs. Maximum Interference')
legend('maximum O-RU power 47.78dBm ','maximum O-RU power 44.7 dBm')
grid on

