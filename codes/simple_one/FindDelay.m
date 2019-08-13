Ut2Slice = modifiedMat(Ut2Service*service2slice);
Rtot_Slice = rate_UE * Ut2Slice;
for i = 1:N_Slice
 Delay_Transmission(i) = 1/(Rtot_Slice(i)-lamda) ;
 Delay_Service1 = 1/(mu1- alpha_m1/sum(VNF2Slice1(:,i)));
 Delay_Service2 =  1/(mu2- alpha_m2/sum(VNF2Slice2(:,i)));
end
