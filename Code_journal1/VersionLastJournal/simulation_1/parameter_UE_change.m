UE_S = i_count*ones(1,S);%randi(N_UE_max,1,S);
N_UE = sum(UE_S);
%RU_UE = zeros(N_RU,N_UE,N_Antenna);
%Popt = ones(1,N_UE)*Pmax;
Rmin_UE = zeros(1,N_UE);
t = 0;
for i = 1:S
    for j = 1:UE_S(i)
        t = t+1;
        Rmin_UE(t) = Rmin(i);
    end
end
ChannelGain = zeros(N_RU,N_UE,N_Antenna);
beamForming = zeros(N_RU ,N_UE,N_Antenna);
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
%RU_UE = ones(N_RU,N_UE);
count_max = 1;