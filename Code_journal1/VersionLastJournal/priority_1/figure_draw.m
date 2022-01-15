plot( UE_num , (sumR1_e+sumR1_u)/1e6,'-*')
hold on
plot( UE_num , (sumRB1_e+sumRB1_u)/1e6,'-^')

r1 = sumR1_e;
r2 = sumR1_u;
r3 = sumRB1_e;
r4 = sumRB1_u;

plot( UE_num , r1/1e6,'-*')
hold on
plot( UE_num , r2/1e6,'-+')
hold on
plot( UE_num , r3/1e6,'-^')
hold on
plot( UE_num , r4/1e6,'--')
hold on
xlabel('Priority Factor for URLLC Service')
ylabel('Aggregate Throughput(Mbps)')
title('Aggregate Throughput vs Priority Factor for URLLC Service')