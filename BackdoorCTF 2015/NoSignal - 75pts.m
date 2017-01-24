% https://backdoor.sdslabs.co/challenges/NO-SIGNAL

a = imread('C:\\Users\\Peeranat\\Desktop\\a.jpg');
b = imread('C:\\Users\\Peeranat\\Desktop\\b.jpg');
c = bitxor(a,b);
imshow(c);