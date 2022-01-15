plot( UE_num , sumR1_e+sumR1_u,'-*')
hold on
plot( UE_num , sumRB1_e+sumRB1_u,'-^')


plot( UE_num , sumR1_e/1e6,'-*')
hold on
plot( UE_num , sumR1_u/1e6,'-+')
hold on
plot( UE_num , sumRB1_e/1e6,'-^')
hold on
plot( UE_num , sumRB1_u/1e6,'--')
hold on
xlabel('Priority Factor for eMBB Service')
ylabel('Aggregate Throughput(Mbps)')
title('Aggregate Throughput vs Priority Factor for eMBB Service')
