R11 = 1e8*[2.7707,4.1597,5.1440,5.35757,5.5765]; %pmax = .1 watt 
R12 = 1e8*[2.8000,4.0130,4.7978,5.2601,5.6000];
R13 = 1e8*[2.8049,4.0949,5.1475,5.5941,5.5366];
R21 = 1e8*[2.8831,4.4026,5.50992,5.7022,6.03321]; %.3 watt
R22 = 1e8*[2.8531,4.2026,4.7992,5.3022,6.0321];
R23 = 1e8*[2.8414,4.2006,5.1183,5.2599,5.5131];
R24 = 1e8*[2.6995,4.4330,5.1286,5.2352,5.6528];
R31 = 1e8*[2.9847,4.6506,5.5651,5.45717,6.1249];%pmax= 0.5watt
R32 = 1e8*[2.9646,4.4133,5.1114,5.45322,6.1542];
R33 = 1e8*[2.9281,4.3418,5.1971,5.95390,5.4650];
UE_num = count_min1:count_step1:count_max1;
Rp4= 1e8*[2.99090,4.52975,5.40114,5.69979,6.002];
Rp1 = (R11+R12+R13)/3;
Rp2 = (R21+R22+R23+R33)/4;
Rp3 = (R31+R32+R33)/3;

plot( UE_num , Rp4/1e6,'-*')
hold on
plot(UE_num,Rp3/1e6)
plot(UE_num,Rp2/1e6)
plot(UE_num,Rp1/1e6)
xlabel('Number of UE in each Service')
ylabel('Aggregate Throughput(Mbps)')
title('Aggregate Throughput for mMTC services vs. Number of UE in each Service ')
grid on