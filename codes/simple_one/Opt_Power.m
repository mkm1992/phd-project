%% Optimum Power Allocation

close all; clear; clc;
%% Parameter Initializing

N_rrh = 1;  N_Ut = 4;  Itr_max = 10; var_q = 1;
Etha = 1; Rate_min = 1e4; P_max = 0.2;

Channel_Gain = randi(N_rrh, N_Ut);
Pre_Coding = conj(Channel_Gain)./norm(Channel_Gain) ;
Pre_Coding = Pre_Coding ./ norm(Pre_Coding);

%% CVX --- Procedure

for k = 1 : Itr_max
    
    cvx_begin
        variable P_opt(N_Ut, N_rrh)
        [error, R, R1, P1, Prrh] = Power_Rate( P_opt, Etha, N_Ut, N_rrh,...
            Channel_Gain, Pre_Coding);
        maximize error
        subject to
            Prrh(:,:) <= P_max;
            P_opt(:,:) > 0; 
            R(:,:) > Rate_min;  
            %CP(:,:)<2000;
            %Prrh(:,:) <= var_q * ( 2.^(CP(:,:)));           
    cvx_end
    
    Etha = R1/P1;
    
    q = rand(N_Ut,1);
    Cr = log(Prrh./q);
    
end

%% Function for Calculating Power and Rate
function [error, R, R1, P1, Prrh] = Power_Rate( P_opt, Etha, N_Ut, N_rrh,...
    Channel_Gain, Pre_Coding)
    
    R= cvx(zeros(N_Ut, N_rrh));  BW = cvx(10 * 1e6) ;
    N0_dbm = -174 ;     N0 = cvx(10^(N0_dbm/10)/1000);
    P_dbm = 23;         P_max = (10^(P_dbm/10))/1000;
     
    [Iu] = interference(P_opt, Channel_Gain, Pre_Coding, P_max, N_Ut, N_rrh);
    
    for i = 1:N_Ut
            g1 = Channel_Gain(i,:);
            w1 = Pre_Coding(i,:);
            R(i)= BW * log(1+ ( P_opt(i) .* abs(g1 * w1')^2 /(Iu(i) + BW*N0) ) );
    end
    
    
    Prrh = cvx(zeros(N_Ut, N_rrh));
    for i = 1:N_Ut
            w22 = Pre_Coding(i, :);
            wrrh = permute(w22, [3,2,1]);
%             PU = permute(Pus(i,:),[2,3,1]);
            Prrh (i, :)= cvx(0);
%             Prrh(i,:)= ( abs(wrrh)' * PU * PU * abs(wrrh) );
            for tt = 1:N_Ut
                Prrh(i,:)= ( wrrh(tt).^2 ) .* P_opt(i,:)+ Prrh(i,:);
            end
    end
    
    R1 = sum(sum(R));   P1 = sum(sum(Prrh));
    error = R1 - (Etha * P1);
            
end

%% Calculating Interference

function [Int] = interference(P_opt, Channel_Gain, Pre_Coding, P_max, N_Ut, N_rrh)
    
    I1 = 0; Pus = cvx(zeros(N_Ut, N_rrh));
    Int = cvx(zeros(N_Ut, N_rrh));
    
    for i = 1:N_Ut
            Pus(i,:) = sqrt(P_opt(i,:));
            g1 = Channel_Gain(i,:);
            w1 = Pre_Coding(i,:);
            I1 = P_opt(i) * ( abs(g1 * w1').^2 ) + I1;
            w2 = permute( Pre_Coding(i,:), [2 3 1] );           
            
            Int(i) =  P_max * sum( abs(g1 * w2).^2 ); 
    end
    
end

