ro = 0;
beamForming = ChannelGain*(ChannelGain'*ChannelGain+ro*eye(N_UE))^(-1);
for i=1:N_UE
 beamForming(:,i) = beamForming(:,i)/norm(beamForming(:,i));
end