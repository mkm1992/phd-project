RU_UE = zeros(N_RU,N_UE);
ChannelGain2 = zeros(N_Antenna,N_UE);
beamForming2 = zeros(N_Antenna ,N_UE);
rate_UE_2 = zeros(N_RU,N_UE);
for u1 =  1:N_RU
    for i = 1:N_UE
        ChannelGain2(:,i)= ChannelGain(u1,i,:);
        beamForming2(:,i)= beamForming(u1,i,:);
        rate_UE_2(u1,i) =  log2(1+(Popt(i)*abs((ChannelGain2(:,i))'*beamForming2(:,i))^2)/(BW*N0));
    end  
end

for ue = 1:N_UE
   [m_val,ind_num]=max(rate_UE_2(:,ue));
   RU_UE(ind_num,ue)=1;
   
end