x0=[0.5 0.5 0.5 0.5 0.5];
[theta,ftheta]=fsolve(@NLequations,x0);
theta1=theta(1)*180/pi;
theta2=theta(2)*180/pi;
theta3=theta(3)*180/pi;
theta4=theta(4)*180/pi;
theta5=theta(5)*180/pi;

theta=[theta1,theta2,theta3,theta4,theta5]