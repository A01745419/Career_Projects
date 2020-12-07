%% INGRESO DE DATOS INICIALES
% Mayor parte del credito a Pol y Palomitas
% Paulo Ogando, Cesar Emiliano Palome, Jose Luis Madrigal, Jorge Isidro Blanco, Fernando Emilio
% 45, 100, 5426, 5, 1.5, 250
angulo = input("Dame el angulo de salida del proyectil en grados: ");
velocidad_inicial = input("Dame la Velocidad Inicial del Proyectil en m/s: ");
altura_volcan = input("¿Cuánto mide el Volcan?(m): ");
resistencia_aire_b = input("Medida de la resistencia del aire: ");
exponente_velocidad_n = input("Exponente de la Velocidad entre 1.1 y 1.9: ");
masa_proyectil = input("¿Cuánto pesa el proyectil?(kg): ");
%% CALCULO DE OTROS DATOS RELEVANTES PARA EL CALCULO DE LA TRAYECTORIA
Voy = velocidad_inicial * sind(angulo);
Vox = velocidad_inicial * cosd(angulo);
tiempo_recorrido = (-(-Voy)+sqrt(Voy^2-(4*(4.9)*-altura_volcan)))/(2*4.9);
Axj = (-resistencia_aire_b*(Vox^2+Voy^2)^((exponente_velocidad_n-1)/2)*Vox)/masa_proyectil;
Ayj = ((-resistencia_aire_b*(Vox^2+Voy^2)^((exponente_velocidad_n-1)/2)*Voy)/masa_proyectil)-9.81;
dt = tiempo_recorrido/5000;
c = 1;
t = 0;
x = 0;
Verlet = [c t x altura_volcan Vox Voy Axj Ayj];
%% METODO DE VERLET 
for i = 1:20000;
    Verlet(c+1,:) = [c+1
        t+dt
        Verlet(c,3)+Verlet(c,5)*dt+1/2*Verlet(c,7)*dt^2
        Verlet(c,4)+Verlet(c,6)*dt+1/2*Verlet(c,8)*dt^2
        Verlet(c,5)+Verlet(c,7)*dt
        Verlet(c,6)+Verlet(c,8)*dt
        0 
        0
        ];
    Verlet(c+1,7) = (-resistencia_aire_b*(Verlet(c+1,5)^2+Verlet(c+1,6)^2)^((exponente_velocidad_n-1)/2)*Verlet(c+1,5))/masa_proyectil;
    Verlet(c+1,8) = ((-resistencia_aire_b*(Verlet(c+1,5)^2+Verlet(c+1,6)^2)^((exponente_velocidad_n-1)/2)*Verlet(c+1,6))/masa_proyectil)-9.81;
    c = c + 1;
    t = t + dt;
end
%% METODO SIN RESISTENCIA DEL AIRE
Sin_Verlet_Y = [altura_volcan];
tiempo_impacto = (-(-Voy)+sqrt(Voy^2-(4*(4.9)*-altura_volcan)))/(2*4.9);
espacio_X = (0+(Vox*tiempo_impacto))/20;
espacio_X_base = (0+(Vox*tiempo_impacto))/20;
Sin_Verlet_X = [0];
for j = 1:20
    Sin_Verlet_X = [Sin_Verlet_X espacio_X];
    Sin_Verlet_Y = [Sin_Verlet_Y altura_volcan+(espacio_X*tand(angulo)-((9.81*espacio_X^2)/(2*velocidad_inicial^2*cosd(angulo)^2)))];
    espacio_X = espacio_X + espacio_X_base;
end
%% ANIMACIÓN DE LA GRÁFICA
hold on
for z = 1:length(Sin_Verlet_X)
    plot(Sin_Verlet_X(1,z),Sin_Verlet_Y(1,z),'r-o')
    plot(Verlet(z,3),Verlet(z,4),'b-x')
    axis([0 max(Sin_Verlet_X)+250 -100 max(Sin_Verlet_Y)+250])
    legend("Sin Resistencia del Aire","Con resistencia del aire")
    xlabel("Distancia Recorrida")
    ylabel("Altura del proyectil")
    pause(.05)
end
for q = length(Sin_Verlet_X):200:20001
    plot(Verlet(q,3),Verlet(q,4),'b-x')
    axis([0 max(Sin_Verlet_X)+250 -100 max(Sin_Verlet_Y)+250])
    legend("Sin Resistencia del Aire","Con resistencia del aire")
    pause(.05)
end