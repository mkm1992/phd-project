R = 500;
S1 = 1;
S2 = 0;
S = S1 + S2;
BW = 120*1e3;%10*1e6;  
n0 = -174;%-174 ; %dbm
N0 = db2pow(n0)/1000;
Pc1 = 10; %watt
Pc  = db2pow(Pc1)/1000;
Pt = 23;
Pmax = db2pow(Pt)/1000;
Rt = .1*BW;%0.1*BW;
%%
N_U1 = randi(10,1);
N_U2 = 0;
ChannelGain = zeros(N_rrh,N_Ut);
for i=1:N_rrh
    for j=1:N_Ut
       distance(i,j)= randi(R,1,1);
       if distance(i,j)==0
           distance(i,j) = randi(R,1,1);
       end
       var_fading = db2pow(10);
       N_Ute = lognrnd(0,var_fading);
       loss(i,j) = N_Ute*1/(distance(i,j)^3.8);
       ChannelGain(i,j) = 100*(loss(i,j)^0.5)/sqrt(2)*(randn(1)+1i*randn(1));
    end
end
ChannelGain2 = ChannelGain;