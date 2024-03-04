%{

    #include "syntaxique.tab.h"
    int nbrligne = 1, nrb_colone= 1;
%}

lettre [a-zA-Z]
chiffre [0-9]
idf [A-Z]([A-Za-z]|[0-9])*
cdt {0-9}+

%%

"DEC VAR"    {nrb_colone++; return DECVAR;}
"PART INST"  {nrb_colone++; return PART_INST;}
"int"        {nrb_colone++; return TYPE;}
{idf}        {nrb_colone++; return IDF;}
"{"          {nrb_colone++; return ACOLADE_OV;}
"}"          {nrb_colone++; return ACOLADE_FR;}
";"          {nrb_colone++; return PVG;}
","          {nrb_colone++; return VRG;}
[ \t]
[\n]        {nbrligne++; nrb_colone = 1;}
.           {nrb_colone++; printf("erreur lexicale a la ligne %d, colone %d\n",nbrligne,nrb_colone);}

%%
