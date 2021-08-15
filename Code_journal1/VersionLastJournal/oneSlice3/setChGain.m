ChannelGain1 = zeros(N_Antenna,N_UE);
beamForming1 = zeros(N_Antenna ,N_UE);
for numUE = 1:N_UE
    numRU = find(RU_UE(:,numUE)==1);
    ChannelGain1(:,numUE)= ChannelGain(numRU,numUE,:);
    beamForming1(:,numUE)= beamForming(numRU,numUE,:);
end