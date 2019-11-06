a=load("../data/mnist.mat");
 dtr=a.digits_train;
 ltr=a.labels_train;
 MEAN=zeros(784,1,10);%MEAN ARRAY
 COUNT=zeros(1,10);%COUNT ARRAY
 COV=zeros(784,784,10);% respective slices store the covariances
 LAM1=zeros(1,10);%MAXIMUM EIGENVALUE
 V1=zeros(784,1,10);%CORRESPONDING EIGENVECTOR

for j=1:60000
    i = ltr(j);
    DUMMY=dtr(:,:,j);
    IMG=reshape(DUMMY,784,1);%reshape image vector
    IMGD=double(IMG);%image vector
    MEAN(:,:,i+1)=MEAN(:,:,i+1)+IMGD;%addition
    COUNT(:,i+1)=COUNT(:,i+1)+1;%required count
end

%Evaluating Mean by dividing sum by count
for i=1:10
    MEAN(:,:,i)=MEAN(:,:,i)/COUNT(:,i);
end
%MEAN COMPUTATION DONE

for j=1:60000
    %j
    i = ltr(j);
    DUMMY=dtr(:,:,j);
    IMG=reshape(DUMMY,784,1);
    IMGD=double(IMG);%image vector
    IMGD=IMGD-MEAN(:,:,i+1);
    IMGDT=transpose(IMGD);%transpose of image vector
    PROD=IMGD*IMGDT;%Evaluating sum
    COV(:,:,i+1)=COV(:,:,i+1)+PROD;
end
%Evaluate Covariance

for i=1:10
    COV(:,:,i)=COV(:,:,i)/COUNT(:,i);
end
%Covariance computation done

% 
% for i=1:10
%     MEAN1=uint8(MEAN(:,:,i));
%     IMGSHOW=reshape(MEAN1,28,28);
%     imshow(IMGSHOW);
%     pause(5);
% end

for i=1:10
    %i
    [VT,DT] = eig(COV(:,:,i));%Eigenvectors and eigenvalues
    EIGENVAL=diag(DT);%Extracting from n*n array
    [VAL,IND]=sort(EIGENVAL);%Sorting it and taking out indices
    LAM1(:,i)=VAL(784);%Maximum EigenValue
    V1(:,:,i)=VT(:,IND(784));%Eigenvector corresponding to it
    figure(i);
    plot(VAL);
    title(sprintf('Eigenvalues of Covariance matrix associated with number %d',(i-1)))
    xlabel('X');
    ylabel('Eigenvalues');
end

for i=1:10
    %i %printing the figure required in three subplots
    figure(i+10);
    subplot(3,1,1),imshow(rescale(reshape(MEAN(:,:,i)-(LAM1(:,i)^0.5)*V1(:,:,i),[28,28])))
    title(sprintf('mean - sqrt(lambda)*eigenvector associated with number %d',(i-1)))
    subplot(3,1,2),imshow(rescale(reshape(MEAN(:,:,i),[28,28])))
    title(sprintf('mean associated with number %d',(i-1)))
    subplot(3,1,3),imshow(rescale(reshape(MEAN(:,:,i)+(LAM1(:,i)^0.5)*V1(:,:,i),[28,28])))
    title(sprintf('mean + sqrt(lambda)*eigenvector associated with number %d',(i-1)))
end