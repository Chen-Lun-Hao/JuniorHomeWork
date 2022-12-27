clc; 
clear all; close all;
I = imread('./images/sweden_input.jpg');
J = histeq(I);
figure; 
subplot(2, 2, 1); imshow(I, []); title('原图');
subplot(2, 2, 2); imshow(J, []); title('原图均衡化后的图像');
subplot(2, 2, 3); imhist(I, 64); title('原图的直方图');
subplot(2, 2, 4); imhist(J, 64); title('均衡化后的直方图');