%% changable variable
UE_S = randi(N_UE_max,1,S);
N_UE = sum(UE_S);
ChannelGain = zeros(N_RU,N_UE);
PrecodingMat = zeros(N_RU,N_UE);
RU_UE = zeros(N_RU,N_UE);