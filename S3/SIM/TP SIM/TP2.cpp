#include <stdio.h>
#include <stdlib.h>
#include <GLFW/glfw3.h>


int main()
{
    float i =0;
    int up = 1;

    if (!glfwInit()) {
    printf("Could not initialize glfw.\n");
    return -1;
 }
    GLFWwindow* window;
window = glfwCreateWindow(640, 480, "OpenGL TP 2", NULL, NULL);
if (!window)
{
 glfwTerminate();
 return -1;
}
glfwMakeContextCurrent(window);

glClearColor(0.5f, 0.5f, 0.5f, 1.0f);




while (!glfwWindowShouldClose(window))
{
 glClear(GL_COLOR_BUFFER_BIT);
 glMatrixMode(GL_MODELVIEW);
 glLoadIdentity();

 glPushMatrix();


glRotatef(90, 0.0, 0.0, 1.0);
glTranslatef(0.5, 0.5, 0.0) ;
glScalef(0.5, 0.5, 0.5);

 glBegin(GL_TRIANGLES);
 glColor3f(1,0,0);
 glVertex2i(0,-1);
 glVertex2i(-1,0);
 glVertex2i(0,1);

 glEnd();
glPopMatrix();




glBegin(GL_TRIANGLES);
glColor3f(0,1,0);
glVertex2f(0,-0.5);
glVertex2f(-0.5,0);
glVertex2f(0,0.5);
glEnd();


// glBegin(GL_QUADS);
// glColor3f(1,0,0);
// glVertex2f(0.5,0.5);
// glVertex2f(-0.5,-0.5);
// glVertex2f(-0.5,0.5);
// glVertex2f(0.5,-0.5);
// glEnd();


//  glBegin(GL_TRIANGLES);
//  glColor3f(0,1,0);
//  glVertex2f(0.5,0.5);
//  glVertex2f(-0.5,0.5);
//  glVertex2f(0,0);
//  glEnd();

//  if(i >= 1)
//     up = 0;
//  if (i <= 0)
//     up = 1;

//  if (up==1) i=i+0.0005;
//  if (up==0) i=i-0.0005;
//  glBegin(GL_TRIANGLES);
//  glColor3f(0,0.5,0);
//  glVertex2f(0.5,0.5);
//  glVertex2f(-0.5,0.5);
//  glVertex2f(0,i);
//  glEnd();

 glfwSwapBuffers(window);
 glfwPollEvents();

}



glfwDestroyWindow(window);
glfwTerminate();

//    printf("Hello world !\n");
    return 0;
}

