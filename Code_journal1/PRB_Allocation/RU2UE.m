for j=1:N_UE
    RU2UE1 = 0;
    temp = 0;
    for i=1:N_RU
        if abs(ChannelGain(i,j))> abs(temp)
            temp = ChannelGain(i,j);
            RU2UE1 = i;
        end
    end
    RU_UE(RU2UE1,j) = 1;
end