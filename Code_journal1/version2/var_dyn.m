%% changable variable
UE_S = randi(N_UE_max,1,S);
N_UE = sum(UE_S);
ChannelGain = zeros(N_RU,N_UE);
PrecodingMat = zeros(N_RU,N_UE);
RU_UE = zeros(N_RU,N_UE);
Popt = ones(1,N_UE)*Pmax;
Rmin_UE = zeros(1,N_UE);
t = 0;
for i = 1:S
    for j = 1:UE_S(i)
        t = t+1;
        Rmin_UE(t) = Rmin(i);
    end
end
N_PRB = 12;
RU_PRB = randi([0 1],N_RU,N_PRB);
PRB_UE = zeros(N_PRB, N_UE);