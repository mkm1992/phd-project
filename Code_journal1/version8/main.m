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
alpha_m = lambda_m.*(UE_S_Admit);
for i = 1:S
    for j = 1:UE_S_Admit(i)
        t = t+1;
        Rmin_UE(t) = Rmin(i);
    end
end
ChannelGain = zeros(N_RU,N_UE);
beamForming = zeros(N_RU ,N_UE);
Popt = ones(1,N_UE)*Pmax;
PRB_UE = zeros(N_PRB,N_UE);
for i =1:N_UE
    if mod(i,N_PRB)==0
       PRB_UE(N_PRB,i)= 1;
    else
        PRB_UE(mod(i,N_PRB),i) =1 ;
    end

end
run Channel_Gain
run Precoding
run RU_association
count_max = 1;
run PRB_Pow_Alloc1
run findM
VNF_NUM

