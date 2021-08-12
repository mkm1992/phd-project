ro = 0;
for i=1:N_RU
   temp = ChannelGain(i,:,:);
   temp_a =permute(temp, [2,3,1]);
   beamForming(i,:,:) = temp_a*(temp_a'*temp_a+ro*eye(N_Antenna))^(-1);  
end

for i=1:N_UE
    for j = 1:N_RU 
         b = permute(beamForming(j,i,:),[3,2,1]);
         beamForming(j,i,:) = beamForming(j,i,:)/norm(b);
    end
end