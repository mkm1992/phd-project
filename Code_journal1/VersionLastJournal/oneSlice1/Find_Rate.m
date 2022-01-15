function [out] = Find_Rate(BW,Popt,ChannelGain,beamForming,PRB_UE,N_PRB,N_UE,N0,Intf,zz)
rate_UE = cvx(zeros(1,N_UE));
for i = 1:N_UE
    %for j = 1:N_RU
        for z = 1:N_PRB
            if PRB_UE(z,i)==1
                rate_UE(i) =  BW* log(1 + (Popt(i)*abs((ChannelGain(:,i))'*beamForming(:,i))^2)/(Intf(i)+BW*N0));%*PRB_UE(z,i);
            end
        end
    %end
end
out = rate_UE(zz);
end

