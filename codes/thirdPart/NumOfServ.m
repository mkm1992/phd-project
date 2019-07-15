function [Num] = NumOfServ(mappingVar, N_server)
    Num = 0;
    for i=1: N_server
        if sum(mappingVar(:,i))>0
            Num = Num +1;
        end
    end
            
        
end

