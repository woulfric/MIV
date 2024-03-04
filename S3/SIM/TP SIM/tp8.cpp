#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "shader/shader.hpp"
#include <vector>
#include "model/objload.hpp"

#include <glm.hpp>
#include <gtx/transform.hpp>
using namespace glm;
double Xpos,Ypos;
double diffX = 0, diffY = 0;

mat4 Model = mat4(1.0f);
mat4 View = mat4(1.0f);

void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    glViewport(0, 0, width, height);
}

static void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods){
 if (action == GLFW_PRESS)
 switch (key)
 {
 case GLFW_KEY_R :
 glClearColor(1.0f, 0.0f, 0.0f, 0.5f);
 break;
 case GLFW_KEY_V :
 glClearColor(0.0f, 1.0f, 0.0f, 0.5f);
 break;
 case GLFW_KEY_B :
 glClearColor(0.0f, 0.0f, 1.0f, 0.5f);
 break;
 case GLFW_KEY_ESCAPE:
 glfwSetWindowShouldClose(window, GLFW_TRUE);
 break;
 default:
 glClearColor(0.0f, 0.0f, 0.0f, 0.5f);

 }
 else
    if(action == GLFW_RELEASE){
     glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
 }
 }

void mouse_button (GLFWwindow* window, int button, int action, int mods)
{
if (action == GLFW_PRESS)
 switch (button)
 {
 case GLFW_MOUSE_BUTTON_RIGHT :
Model = scale(Model,vec3(1.5f, 1.5f ,1.5f));
 break;
 case GLFW_MOUSE_BUTTON_LEFT :
Model = scale(Model,vec3(0.5f, 0.5f ,0.5f));
 break;
 case GLFW_MOUSE_BUTTON_MIDDLE :
Model = scale(Model,vec3(2.5f, 1.5f ,1.0f));
 break;
 }
 }

struct STRVertex{
    vec3 position;
    vec3 color;
};


static void cursor_position(GLFWwindow* window, double x, double y)
{
double diffX,diffY;

diffX = Xpos - x;
diffY = y - Ypos;

Model = rotate(Model,radians(float(diffX)),vec3(0.0f,0.0f,1.0f));
Model = rotate(Model,radians(float(diffY)),vec3(1.0f,0.0f,0.0f));


}

int main() {

    std::vector<vec3> position;
    std::vector<vec2> texture;
    std::vector<vec3> normals;


    glfwInit();
//    glfwWindowHint(GLFW_FSAA_SAMPLES, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    //glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);

    GLFWwindow* window = glfwCreateWindow(800, 600, "LearnOpenGL", NULL, NULL);
    if (window == NULL) {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    glViewport(0, 0, 800, 600);

    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);


    loadOBJ("C:/Users/LEGION/Desktop/TP/SIM/TP SIM/model/torus.obj", position, texture, normals);

    unsigned int VBO, VBOColor,VAO;

    glGenVertexArrays(1, &VAO);
    glBindVertexArray(VAO);

    glGenBuffers(1, &VBO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, position.size() * sizeof(glm::vec3), &position[0], GL_STATIC_DRAW);
    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (void*)0);

    glGenBuffers(1, &VBOColor);
    glBindBuffer(GL_ARRAY_BUFFER, VBOColor);
    glBufferData(GL_ARRAY_BUFFER, normals.size() * sizeof(glm::vec3), &normals[0], GL_STATIC_DRAW);
    glEnableVertexAttribArray(1);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (void*)0);

    glBindVertexArray(0);


STRVertex vertices[] = {
         vec3(1.0f, -1.0f, 1.0f), vec3(0.0f, 0.0f, 1.0f),
         vec3(-1.0f, -1.0f, 1.0f), vec3(0.0f, 0.0f, 1.0f),
         vec3(-1.0f, -1.0f, -1.0f), vec3(0.0f, 0.0f, 1.0f),
         vec3(1.0f, -1.0f, -1.0f), vec3(0.0f, 0.0f, 1.0f),
         vec3(0.0f, 1.0f, 0.0f), vec3(1.0f, 0.0f, 1.0f),

 };





    GLuint ShaderProgram;
    ShaderProgram = LoadShaders( "shader/SimpleVertexShader.vertexshader", "shader/SimpleFragmentShader.fragmentshader" );

    mat4 Projection = perspective(radians(45.0f), 4.0f / 3.0f, 0.1f, 100.0f);
    mat4 View = lookAt(vec3(3,1,3),vec3(0,0,0),vec3(0,1,0) );

    mat4 MVP = Projection * View * Model;
    GLuint MatrixID = glGetUniformLocation(ShaderProgram, "MVP");


    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);

    glfwSetKeyCallback(window, key_callback) ;
    glfwSetCursorPosCallback(window, cursor_position);
    glfwSetMouseButtonCallback(window, mouse_button);


    while(!glfwWindowShouldClose(window)) {

        /*
        int state = glfwGetKey(window, GLFW_KEY_E);
        if (state == GLFW_PRESS) printf(" le E ") ;
        */

        glfwGetCursorPos (window, &Xpos, &Ypos );
        mat4 MVP = Projection * View * Model;
        GLuint MatrixID = glGetUniformLocation(ShaderProgram, "MVP");


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) ;

        glUseProgram(ShaderProgram);



        glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &MVP[0][0]);

        glBindVertexArray(VAO);

    glDrawArrays(GL_TRIANGLES, 0, 3456);

        glfwSwapBuffers(window);

        glfwPollEvents();
    }

    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);

    glfwTerminate();
    return 0;
}
