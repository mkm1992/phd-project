clear all
clc
%% initializing
run Var
%% UE Admission
run UE_admission
%% RU associated in Comp Way, Remove UE that are not admitted
N_UE = sum(UE_S_Admit);
ChannelGain = zeros(N_RU,N_UE);
beamForming = zeros(N_RU ,N_UE);
run Channel_Gain
run Precoding
