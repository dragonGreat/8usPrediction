close all;
clc;

fprintf('come on! lets go!\n');
%readTxt(1);
    file1=fopen('oriData/gd_weather_report.txt','r');
    a=textscan(file1,'%s %s %s %s %s','delimiter', ',');
   %   a=textscan(file1,'%s%s%s%d%s','delimiter', ',');
    outData=1;
    a{1}
    a{2}
    a{3}
    fprintf('\n');
    size(a{1})
 