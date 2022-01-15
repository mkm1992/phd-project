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