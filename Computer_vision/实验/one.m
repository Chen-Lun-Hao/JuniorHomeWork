clc;%clc的作用就是清屏幕
clear;%clear是删除所有的变量
close all;%close all是将所有打开的图片关掉。

%第一题，读取图像，灰度化，直方图均衡
H= imread('my.jpg');
H1= rgb2gray(H);
H2=histeq(H1);  %直方图均衡化
subplot(9,2,1);
imshow(H); title('原图');
subplot(9,2,2);
imhist(H); title('原图');
subplot(9,2,3);
imshow(H1); title('灰度图');
subplot(9,2,4);
imhist(H1);title('灰度图');
subplot(9,2,5);
imshow(H2); title('直方图');
subplot(9,2,6);
imhist(H2); title('直方图');

%第2题，计算熵
H2_shang = Shang(H2);
H1_shang = Shang(H1);
H2;
H1;

%第3题，图像分离对比
H_r = H(:,:,1);
H_g = H(:,:,2);
H_b = H(:,:,3);
H2_r=histeq(H_r);  %直方图均衡化
H2_g=histeq(H_g);
H2_b=histeq(H_b);
subplot(9,2,7);
imshow(H2); title('均衡化图');
subplot(9,2,8);
imhist(H2); title('均衡化图');
subplot(9,2,9);
imshow(H2_r); title('R');
subplot(9,2,10);
imhist(H2_r);title('R');
subplot(9,2,11);
imshow(H2_g); title('G');
subplot(9,2,12);
imhist(H2_g); title('G');
subplot(9,2,13);
imshow(H2_b); title('B');
subplot(9,2,14);
imhist(H2_b); title('B');

%第4题，计算对比度
img_lena = imread('lena.BMP');
H2_img_lena=histeq(img_lena);
img_lena_res = Computers(img_lena);
H2_img_lena_res = Computers(H2_img_lena);
img_lena_res;
H2_img_lena_res;

%第5题，直方图匹配
img_lena_H = histeq(H1,img_lena);
subplot(9,2,15);
imshow(H1); title('原图');
subplot(9,2,16);
imhist(H1); title('原图');
subplot(9,2,17);
imshow(img_lena_H); title('均衡化');
subplot(9,2,18);
imhist(img_lena_H); title('均衡化');

%第2题，计算熵
function H_x = Shang(img)
[C,L]=size(img); %求图像的规格
Img_size=C*L; %图像像素点的总个数
G=256; %图像的灰度级
H_x=0;
nk=zeros(G,1);%产生一个G行1列的全零矩阵
for i=1:C
for j=1:L
Img_level=img(i,j)+1; %获取图像的灰度级
nk(Img_level)=nk(Img_level)+1; %统计每个灰度级像素的点数
end
end
for k=1:G  %循环
Ps(k)=nk(k)/Img_size; %计算每一个像素点的概率
if Ps(k)~=0 %如果像素点的概率不为零
H_x=-Ps(k)*log2(Ps(k))+H_x; %求熵值的公式
end
end
end

%第4题，对比度
function [res] = Computers(G)
res = 0;
[m,n] = size(G);
Lc = 4*(n-2)*(m-2)+2*(m-2)*3+2*(n-2)*3+4*2; % 算出底数 
% 使用全负一矩阵进行包围
a= ones(n+2,m+2);
a=-a;
for i =2:n+1
    for j= 2:m+1
        a(i,j)=G(i-1,j-1);
    end
end
% 4近邻的四个方向。
dir = [1,0;0,1;0,-1;-1,0];
for i= 2:n+1
    for j= 2:m+1
        for k=1:4
        	% 相邻位置的坐标x，y
            x=i+dir(k,1);
            y = j+dir(k,2);
            cnt = a(x,y);%新坐标值
            if(cnt~=-1)%判断是否越界
                res  = res +(cnt-a(i,j))*(cnt-a(i,j));
            end
        end
    end
end
res = res/Lc;
end




