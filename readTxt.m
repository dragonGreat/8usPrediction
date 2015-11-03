function outData= readTxt( flag)
%% txt文件提取
if(flag==1)
    file1=fopen('oriData\gd_line_desc.txt','rb');
   a=textscan(file1,'%s%s%s%s%s','delimiter', ',');
   %   a=textscan(file1,'%s%s%s%d%s','delimiter', ',');
    outData=1;
    a{1}
    a{2}
    a{3}
      fprintf('\n');
    size(a{1})
    fclose(file1);
    %fprintf('%s%s%s\n',a1,a2,a3);


else
    outData=0;
    
end

end

