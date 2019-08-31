Ut2Slice =Ut2Service*service2slice;% modifiedMat(Ut2Service*service2slice);
Rtot_Slice = rate_UE * Ut2Slice;
for i = 1:N_Slice
 Delay_Transmission(i) = 1/(Rtot_Slice(i)-lamda) ;
 if Delay_Transmission(i)<0
     Delay_Transmission(i)=0;
 else
 Delay_Slice1(i) = 1/(mu1- alpha_m1/sum(VNF2Slice1(:,i)));
 Delay_Slice2(i) =  1/(mu2- alpha_m2/sum(VNF2Slice2(:,i)));
 end
end
Delay_Slice = Delay_Slice1 + Delay_Slice2 +Delay_Transmission;