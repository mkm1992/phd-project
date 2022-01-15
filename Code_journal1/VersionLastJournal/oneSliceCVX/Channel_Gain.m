%% Obtain Channel Gain
x_ue = zeros(1,N_UE);
y_ue = zeros(1,N_UE);
for i_u=1:N_UE
    x_ue(i_u) = randi(R,1,1);
    y_ue(i_u) = randi(R,1,1);
end
%%
x_ru = zeros(1,N_RU);
y_ru = zeros(1,N_RU);

for i_r=1:N_RU
    x_ru(i_r) = randi(R,1,1);
    y_ru(i_r) = randi(R,1,1);
end
x_ru = [167/2, 167*3/2, 167*5/2,167/2, 167*3/2, 167*5/2];
y_ru = [125, 125, 125, 375, 375,375];
distance = zeros(N_RU,N_UE);
for i=1:N_RU
    for j=1:N_UE
       distance(i,j)= sqrt((x_ru(i)-x_ue(j))^2+(y_ru(i)-y_ue(j))^2);
       if distance(i,j)==0
           distance(i,j) = randi(R,1,1);
       end
       var_fading = db2pow(10);
       N_Ute = lognrnd(0,var_fading);
       loss(i,j) = N_Ute*1/(distance(i,j)^3);
       ChannelGain(i,j,:) = 1*(loss(i,j)^0.5)/sqrt(2).*(randn(1,4)+1i*randn(1,4));
    end
end