sumR1 =1.0e+07 *[1.8325,3.6071,5.3412,6.9798,8.5835]; %delay sensitive power 10 delay 0.01ms
sumR2 =1.0e+07 *[1.8035,3.6942,5.4465,7.1987,8.8051]; % delay not sensitive power 3    delay 10ms
sumR2 =1.0e+07 *[1.9002,3.5756,5.3107,7.1641,8.5290];% delay sensitive power 30 delay 0.01ms
plot( UE_num , sumR2/1e6,'-+')
hold on
plot( UE_num , sumR1/1e6,'--')



sumRB1 = 1.0e+07 *[4.3544    4.4055    4.3079    4.4731]; % 12 UE 1e-3 delay