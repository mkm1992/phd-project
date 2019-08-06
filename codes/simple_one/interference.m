Intf = zeros(N_Ut,1);
rrh2ut1 = rrh2slice *transpose(service2slice)*transpose(Ut2Service);
rrh2Ut = modifiedMat(rrh2ut1);
for i = 1: N_Ut
    for j = 1:N_PRB
        for t = 1 : N_Ut
            if Ut_map(i,j)==1 && i~=t && Ut_map(t,j)==1 
                Intf(i) = Intf(i) + Popt(t)*abs((PrecodingMat()')*ChannelGain())^2;
            end
        end
    end
    
end