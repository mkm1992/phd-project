rate_UE = cvx(zeros(1,N_UE));
for i = 1:N_UE
    for j = 1:N_RU
        %for z = 1:N_PRB
            rate_UE(i) = rate_UE(i) + BW* log(1 + (Popt(i)*abs((ChannelGain(j,i).*RU_UE(j,i)))^2)/(Intf(i)+BW*N0));
        %end
    end
end