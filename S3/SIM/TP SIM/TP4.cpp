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
glMatrixMode(GL_PROJECTION);
glLoadIdentity();
gluPerspective( 45, 1, 0.1, 100 );
gluLookAt(0,0,1, 0.2,0,0, 0,-1,0);

glMatrixMode(GL_MODELVIEW);
glLoadIdentity();
glTranslatef(0, 0, -10);


glBegin(GL_TRIANGLES);
glVertex2i(0,1);
glVertex2i(-1,0);
glVertex2i(1,0);
glEnd();



 glfwSwapBuffers(window);
 glfwPollEvents();

}



glfwDestroyWindow(window);
glfwTerminate();

//    printf("Hello world !\n");
    return 0;
}
