#include  <stdio.h>  
void  buf( char **s)  
 {  
        *s = "message";  
 }  
 int main()  
 {  
     char *s ;  
     buf(&s);  
     printf("%s\n",s);  
 }
 
