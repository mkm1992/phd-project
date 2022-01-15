Intf = cvx(zeros(N_Ut,1));
rrh2ut1 = rrh2slice *transpose(service2slice1)*transpose(Ut2Service);
rrh2Ut = modifiedMat(rrh2ut1);
ChannelGain = ChannelGain .* rrh2Ut;
for i = 1: N_Ut
    if sum(rrh2Ut(:,i)) > 0
        Intf(i) = Intf(i) + var_q*abs((ChannelGain(:,i)')*ChannelGain(:,i));
        for j = 1:N_PRB
            if Ut_map(i,j)==1 
                for t = 1 : N_Ut
                    if i~=t && Ut_map(t,j)==1 && sum(rrh2Ut(:,t)) > 0
                        Intf(i) = Intf(i) + Pmax/(N_Ut)*abs((PrecodingMat(:,t)')*(ChannelGain(:,t).*rrh2Ut(:,t)))^2;
                    end
                end
            end
        end
    end
end



rate_UE = cvx(zeros(1,N_Ut));
for i = 1:N_Ut
    rate_UE(i) = BW/log(2)* log(1 + (Popt(i)*abs((PrecodingMat(:,i)')*(ChannelGain(:,i).*rrh2Ut(:,i)))^2)/( BW*N0));
end


PrecodingMat = PrecodingMat.*rrh2Ut;
Prrh = cvx(zeros(1,N_rrh));
Popt1 = cvx(eye(N_Ut));
for i=1:N_Ut
   Popt1(i,i) = Popt(i); 
end
for i = 1:N_rrh
    Prrh(i) = (abs(PrecodingMat(i,:)*Popt1*PrecodingMat(i,:).'))*+var_q;
end
R11 = sum(rate_UE);
P11 = sum(Prrh);
error =  R11 - eta01 * P11;