% syms('theta1','theta2','theta3','theta4','theta5')
% syms('dtheta1','dtheta2','dtheta3','dtheta4','dtheta5')


a1=13.50; 
d1=131.20;
d2=150;
a2=5;
d3=157.35;  
d4=78.8;
a3=7.6;

% Entrée des données_______________________________________________________

% Entrée des valeurs des angles de rotation________________________________

theta1=input('entrer l''angle de rotation de la base=' );
theta1=theta1*pi/180;
theta2=input('entrer l''angle de rotation du 1er segment =' );
theta2=theta2*pi/180;
theta3=input('entrer l''angle de rotation de 2eme segment =' );
theta3=theta3*pi/180;
theta4=input('entrer l''angle de rotation de 3eme segment=' );
theta4=theta4*pi/180;
theta5=input('entrer l''angle de rotation de 4eme segment=' );
theta5=theta5*pi/180;

%calcul de la matrice homgène______________________________________________
T1=[-cos(theta1) sin(theta1) 0 0 ; -sin(theta1) -cos(theta1) 0 0 ; 0 0 1 d1 ; 0 0 0 1]; 
T2=[-sin(theta2)  -cos(theta2) 0 0 ; 0 0 -1 0 ;cos(theta2) -sin(theta2) 0 0 ; 0 0 0 1];
T3=[-cos(theta3)   sin(theta3) 0 d2 ; -sin(theta3)  -cos(theta3) 0 0 ; 0 0 1 a1 ;0 0 0 1];
T4=[-cos(theta4)  sin(theta4)  0 a2 ;0 0 -1 -d3 ; -sin(theta4) -cos(theta4) 0 0 ; 0 0 0 1];
T5=[cos(theta5)  -sin(theta5) 0 a2; 0 0 -1 0 ; sin(theta5) cos(theta5) 0 0 ; 0 0 0 1];
T6=[1 0 0 -d4 ;0 1 0 0;0 0 1 -a3;0 0 0 1];

%matrice de transformation homogene________________________________________
TH=T1*T2*T3*T4*T5*T6;

  r11=TH(1,1);
  r12=TH(1,2);
  r13=TH(1,3);
  r21=TH(2,1);
  r22=TH(2,2);
  r23=TH(2,3);
  r31=TH(3,1);
  r32=TH(3,2);
  r33=TH(3,3);
  px=TH(1,4);
  py=TH(2,4);
  pz=TH(3,4);
  
  rot0_5=[r11 r12 r13;r21 r22 r23;r31 r32 r33];
  
 
 RY=asin(-r31);

 if -pi/2<RY<pi/2
 RZ=atan2(r21,r11);
 RX=atan2(r32,r33);
 elseif RY==-pi/2
 RZ=-atan2(r23,r22);
 RX=0;
 else
 RZ=atan2(r23,r22);
 RX=0;
 end

 ry=RY*180/pi
 rx=RX*180/pi
 rz=RZ*180/pi