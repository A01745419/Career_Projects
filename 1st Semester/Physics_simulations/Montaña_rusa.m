%% INGRESO DE DATOS INICIALES
% Mayor parte del credito a Pol y Palomitas
% Paulo Ogando, Cesar Emiliano Palome, Jose Luis Madrigal, Jorge Isidro Blanco, Fernando Emilio
% -50, 3, 100, 0.1, 35, 30, 0.03
v = input("Dame la Velocidad Inicial del carrito en m/s: ");
k = input("Medida de la resistencia del aire: ");
m= input("¿Cuánto pesa el carrito?(kg): ");
mk = input("Dame el coeficiente de friccion de la pista(menor a .5): ");
largo = input("Dame la longitud de la montaña rusa: ");
posinicial = input("Dame la posicion inicial del carrito: ");
dt = input("Dame delta t: ");
%% Grafica Montaña Rusa
X = 0:.2:largo;
Y = [];
for x = 0:.2:largo;
    paren = (pi*x)/25;
    y = 12*cos(paren) + 15;
    Y = [Y y];
end
hold on
plot(X,Y,'r');
title("Montaña Rusa");
ylabel("Altura");
xlabel("Longitud");
axis([0 largo+5 -2 50])
%% Datos Iniciales para calcular posicion 
Fun = @(x)(12*cos((pi*x)/25) + 15);
FunD = @(x)((-12*pi*sin((pi*x)/25))/25);
Fun2D = @(x)((-12*pi^2*cos((pi*x)/25))/625);
g = 9.81;
xprima = 0;
xpos = posinicial;
ypos = Fun(xpos);
xgrafica = [];
ygrafica = [];
vcompro = [];
em = [];
ep = [];
ec = [];
teta = atand(FunD(xpos));
rc = ((1 + FunD(xpos)^2)^(3/2))/Fun2D(xpos);
energiapotencial = (m * g *ypos);
energiacinetica = 1/2 * m * v^2;
energiamecanica = (m * g *ypos) + (1/2 * m * v^2);
fixed = energiamecanica + 10000;
%normal = m*(v^2/rc)+m*g*cos(teta);
%d = k*v^2

for i = 1:500
    xprimaanterior = xprima;
    vanterior = v;
    xposanterior = xpos;
    yposanterior = ypos;
    rcanterior = rc;
    energiamecanicaA = energiamecanica;
    energiapotencialA = energiapotencial;
    energiacineticaA = energiacinetica;
    xgrafica = [xgrafica xposanterior];
    ygrafica = [ygrafica yposanterior];
    em = [em energiamecanicaA];
    ep = [ep energiapotencialA];
    ec = [ec energiacineticaA];
    
    xprima = xprimaanterior + vanterior*dt;
    teta = atan(FunD(xposanterior));
    xpos = xposanterior + (xprima-xprimaanterior)*cos(teta);
    ypos = Fun(xpos);
    rc = ((1 + FunD(xpos)^2)^(3/2)/Fun2D(xpos));
    raizarriba = vanterior^2 * (1 - ((mk/rcanterior) + (k/m)) * abs(xprima-xprimaanterior)) - (2 * g * (ypos-yposanterior)) - (2 * mk * g * abs(xpos-xposanterior));
    raizabajo = (1 + ((mk/rc) + (k/m)) * abs(xprima - xprimaanterior));
    adentroraiz = raizarriba / raizabajo;
    	

    %if vanterior > 0
        %signo = 1;
    %elseif vanterior < 0
        %signo = -1;
    %end
    if (adentroraiz > 0 && xpos < largo) && (adentroraiz > 0 && xpos > 0)
       v = sign(vanterior) * (sqrt(adentroraiz));
    else
        v = -1 * vanterior;
        xprima = xprimaanterior;
        xpos = xposanterior;
        ypos = yposanterior;
        rc = rcanterior;
    end
    energiapotencial = (m * g *ypos);
    energiacinetica = 1/2 * m * v^2;
    energiamecanica = (m * g *ypos) + (1/2 * m * v^2);
    
end

for i = 1:length(xgrafica)
    hold on
    plot(X,Y,'r');
    plot(xgrafica(i)-.45,ygrafica(i)+1,'b-s');
    %plot(xgrafica(i),ygrafica(i)+.53,'b-s');
    %plot(xgrafica(i)+.45,ygrafica(i)+.53,'b-s');
    %plot(xgrafica(i)-.45,ygrafica(i)+.53,'b-s');
    plot(xgrafica(i),ygrafica(i)+1,'b-s');
    plot(xgrafica(i)+.45,ygrafica(i)+1,'b-s');
    plot(xgrafica(i)-.75,ygrafica(i)+.41,'k-o');
    plot(xgrafica(i)+.8,ygrafica(i)+.41,'k-o');
    pause(.0001);
    clf;
    plot(X,Y,'r');
    title("Montaña Rusa");
    ylabel("Altura");
    xlabel("Longitud");
    axis([0 largo+5 -2 50]);
end
    figure
    
for i = 1:length(xgrafica)
    hold on 
    bar(largo-10,em(i));
    bar(largo,ep(i));
    bar(largo+10,ec(i));
    pause(.0001);
    clf
    axis ([largo-25 largo+25 -2 fixed]);
end