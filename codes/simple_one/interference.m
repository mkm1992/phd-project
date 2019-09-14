Intf = zeros(N_Ut,1);
rrh2ut1 = rrh2slice *transpose(service2slice)*transpose(Ut2Service);
rrh2Ut = modifiedMat(rrh2ut1);
ChannelGain = ChannelGain .* rrh2Ut;
for i = 1: N_Ut
    if sum(rrh2Ut(:,i)) > 0
        Intf(i) = Intf(i) + var_q*abs((ChannelGain(:,i)')*ChannelGain(:,i));
        for j = 1:N_PRB
            if Ut_map(i,j)==1 
                for t = 1 : N_Ut
                    if i~=t && Ut_map(t,j)==1 && sum(rrh2Ut(:,t)) > 0
                        Intf(i) = Intf(i) + Popt(t)*abs((PrecodingMat(:,t)')*(ChannelGain(:,t).*rrh2Ut(:,t)))^2;
                    end
                end
            end
        end
    end
end