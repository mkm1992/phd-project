%% Optimum Power Allocation

close all; clear; clc;
%% Parameter Initializing

N_Service = 3;
NumOfUtInService = randi([1 10],1, N_Service);
N_rrh = 3;  N_Ut = sum(NumOfUtInService);  Itr_max = 10; var_q = 1e-6; imax = 1; 
Etha = 0; Rate_min = 1e4; P_max = 1; R = 500; N_Slice =  3; N_PRB = 8;
 
Ut2Service = rand(sum(NumOfUtInService),N_Service);
Ut_map = randi([0 imax],N_Ut, N_PRB);
%%

ChannelGain = channel_gain(N_rrh, N_Ut, R);
PrecodingMat = precoding_cal(N_rrh, N_Ut, ChannelGain);
rrh2slice = randi([0 imax],N_rrh, N_Slice);
service2slice = randi([0 1], N_Service, N_Slice); 

%% CVX --- Procedure

%for k = 1 : Itr_max
    
    cvx_begin
        variable Popt(1, N_Ut)
        [error, R, R1, P1, Prrh] = Power_Rate( Popt, Etha, N_Ut, N_rrh,...
            ChannelGain, PrecodingMat, rrh2slice, service2slice, Ut2Service,...
                var_q, Ut_map, N_PRB);
        maximize error
        subject to
            Prrh(:,:) <= P_max*10;
            Popt(:,:) > 0; 
            R(:,:) > Rate_min;  
            %CP(:,:)<2000;
            %Prrh(:,:) <= var_q * ( 2.^(CP(:,:)));           
    cvx_end
    
    Etha = R1/P1;
    
    q = rand(N_Ut,1);
    Cr = log(Prrh./q);
    
%end
%% Calculation of Channel Gain

function ChannelGain = channel_gain(N_rrh, N_Ut, R)
    ChannelGain = zeros(N_rrh,N_Ut);
    for i=1:N_rrh
        for j=1:N_Ut
           distance(i,j)= randi(R,1,1);
           if distance(i,j)==0
               distance(i,j) = randi(R,1,1);
           end
           var_fading = db2pow(10);
           N_Ute = lognrnd(0,var_fading);
           loss(i,j) = N_Ute*1/(distance(i,j)^3.8);
           ChannelGain(i,j) = 1000*(loss(i,j)^0.5)/sqrt(2)*(randn(1)+1i*randn(1));
        end
    end
end

%% Calculation of Pre Coding Matrix
    
function PrecodingMat = precoding_cal(N_rrh, N_Ut, ChannelGain)
        
        PrecodingMat = zeros(N_rrh,N_Ut);
        for i=1:N_Ut
            g = ChannelGain(:,i);
            PrecodingMat(:,i) = conj(g)/norm(g);
        end
        ro = 0;
        %v = H*(H'*H+ro*eye(K*S))^(-1);
        PrecodingMat(:,:) = PrecodingMat(:,:)/norm(PrecodingMat(:,:));
end

%% Function for Calculating Power and Rate
function [error, R, R1, P1, Prrh] = Power_Rate( Popt, Etha, N_Ut, N_rrh,...
    ChannelGain, PrecodingMat, rrh2slice, service2slice, Ut2Service,...
    var_q, Ut_map, N_PRB)
    
    R= cvx(zeros(N_Ut, N_rrh));  BW = cvx(10 * 1e6) ;
    N0_dbm = -174 ;     N0 = cvx(10^(N0_dbm/10)/1000);
    P_dbm = 23;         P_max = (10^(P_dbm/10))/1000;
     
    [Intf, rrh2Ut] = interference(N_Ut, rrh2slice, service2slice, Ut2Service, ...
                            ChannelGain, var_q, PrecodingMat, Popt, Ut_map, N_PRB );
    
    rate_UE = Rate_cal(N_Ut, BW, PrecodingMat, ChannelGain, ...
                            rrh2Ut, Intf, N0, Popt);
     
%     [Prrh, Crrh] = power_cap(N_rrh, Popt, rrh2Ut, var_q, PrecodingMat);
    Prrh = rand(1,N_rrh);
    Crrh = rand(1,N_rrh);
    
    R1 = sum(sum(rate_UE));   P1 = sum(sum(Prrh));
    error = R1 - (Etha * P1);
            
end

%% Calculating Interference

function [Intf, rrh2Ut] = interference(N_Ut, rrh2slice, service2slice, Ut2Service, ...
                            ChannelGain, var_q, PrecodingMat, Popt, Ut_map, N_PRB )
    
    Intf = cvx(zeros(N_Ut,1));
    rrh2ut1 = rrh2slice * transpose(service2slice) * transpose(Ut2Service);
    rrh2Ut = modifiedMat(rrh2ut1);
    ChannelGain = ChannelGain .* rrh2Ut;

    for i = 1: N_Ut
        if sum(rrh2Ut(:,i)) > 0
            Intf(i) = Intf(i) + var_q * abs((ChannelGain(:,i)')*ChannelGain(:,i));
            for j = 1:N_PRB
                if Ut_map(i,j)==1 
                    for t = 1 : N_Ut
                        if i~=t && Ut_map(t,j)==1 && sum(rrh2Ut(:,t)) > 0
                            Intf(i) = 0;%Intf(i) + Popt(t)*abs((PrecodingMat(:,t)')*(ChannelGain(:,t).*rrh2Ut(:,t)))^2;
                        end
                    end
                end
            end
        end
    end
    
end

%% Calculating Rate

function rate_UE = Rate_cal(N_Ut, BW, PrecodingMat, ChannelGain, ...
                            rrh2Ut, Intf, N0, Popt)
    rate_UE = cvx(zeros(1,N_Ut));
    for i = 1:N_Ut
        rate_UE(i) = BW* log(1 + (Popt(i)*abs((PrecodingMat(:,i)')*(ChannelGain(:,i).*rrh2Ut(:,i)))^2)/(Intf(i)+ BW*N0));
    end
end

%% Calculating Power

function [Prrh, Crrh] = power_cap(N_rrh, Popt, rrh2Ut, var_q, PrecodingMat)
    Popt1 = Popt.^0.5;
    PrecodingMat = PrecodingMat.*rrh2Ut;

    for i = 1:N_rrh
        Prrh(i) = abs(norm(PrecodingMat(i,:) * Popt1') ^2 ) + var_q;
        Crrh(i) = log(Prrh(i)/var_q);
    end

end