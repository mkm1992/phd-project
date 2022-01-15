Rg1 =1.0e+07 *[0.6294,1.3859,2.0721,2.7961,3.4566,4.0533,4.7901,5.3535];
Rg2 =1.0e+07 *[0.6332,1.3836,1.9596,2.7035,3.3706];
Rg3=1e7*[0.6477,1.2901,1.9765,2.7088,3.3064,3.901,4.5910,5.3865];
UE_num= 2:2:16;
plot(UE_num,Rg1/1e6,'-*')
hold on
plot(UE_num,Rg3/1e6,'-o')
xlabel('Number of UE in a service')
ylabel('Aggregate Throughput (Mbps)')
title('Aggregate Throughput (Mbps) vs. Number of UE in a service')

R1 = 1.0e+07 *[0.7921 1.5831 2.4136 3.3170 4.1690];
R2 = 1.0e+07 *[0.7975, 1.5327, 2.3080, 2.9798, 4.1663];
R3 = 1e7*[0.7411,1.6243,2.4083,3.0954,3.9762];

    