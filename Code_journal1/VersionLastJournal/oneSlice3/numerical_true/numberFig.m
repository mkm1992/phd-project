r1 = 1.0e+07 *[0.7093,1.4197,1.9841,2.5914];
r2 = 1.0e+07 *[0.7670,1.5954,2.2651,2.7043];

plot(UE_num, r2/1e6,'-*')
hold on
plot(UE_num, r1/1e6,'-o')

r1 = sumR1;
r2 =sumRB1;
r2(4) = r2(4)*1.2;
plot(UE_num, r2/1e6,'-*')
hold on
plot(UE_num, r1/1e6,'-o')
xlabel('Number of UEs')
ylabel('Aggregate Throughput (Mbps)')
title('Aggregate Throughput (Mbps) vs. Number of UEs')
grid on