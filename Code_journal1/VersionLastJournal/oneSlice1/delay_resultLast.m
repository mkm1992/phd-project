delay_proposed = [5.1787,  8.8081,  13.7045, 33.884, 72.8029] * 1e-6;
delay_proposed = [12.1787,  19.8081,  29.7045, 44.884, 67.8029] * 1e-6;
delay_baseline = [3.3218, 3.8935, 4.2824, 5.4167, 8.2755]* 1e-6 *2.5;

delay_DR = [4.9773, 6.6556, 7.7389, 9.7671, 16.3963]* 1e-6 *2.5 ;
UE_num = 5:5:25;
plot(UE_num,delay_proposed)
hold on
plot(UE_num,delay_baseline)
plot(UE_num,delay_DR)
delay_DR