clear all
clc
%% initializing
run Var
%% UE Admission
run UE_admission
%% RU associated in Comp Way, Remove UE that are not admitted
N_UE = sum(UE_S_Admit);
Rmin_UE = zeros(1,N_UE);
t = 0;
for i = 1:S
    for j = 1:UE_S_Admit(i)
        t = t+1;
        Rmin_UE(t) = Rmin(i);
    end
end
ChannelGain = zeros(N_RU,N_UE);
beamForming = zeros(N_RU ,N_UE);
Popt = ones(1,N_UE)*Pmax;
%PRB_UE = randi([0,1],N_PRB,N_UE);
PRB_UE = zeros(N_PRB,N_UE);
run Channel_Gain
run Precoding
run RU_association
%run PRB2UEAllocate
%run PRB_Pow_Alloc
run PRB_P
(rate_UE)>Rmin_UE
Pow_RU(:)' <= Pmax
(RU_UE*rate_UE')' < Capacity_RU