Program Geron;
var xa,xb,xc, ya,yb,yc: Integer;
var P,S, a,b,c: Real;
Begin
  Write('xA: ');
  ReadLn(xa);
  Write('yA: ');
  ReadLn(ya);
  Write('xB: ');
  ReadLn(xb);
  Write('yB: ');
  ReadLn(yb);
  Write('xC: ');
  ReadLn(xc);
  Write('yC: ');
  ReadLn(yc);
  a:= sqrt(sqr(xb-xa)+sqr(yb-ya));
  b:= sqrt(sqr(xc-xb)+sqr(yc-yb));
  c:= sqrt(sqr(xa-xc)+sqr(ya-yc));
  P:= (a + b + c) / 2;
  S:= sqrt(P*(P-a)*(P-b)*(P-c));
  WriteLn('Площадь: ', S);
End.
