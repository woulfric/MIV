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
    vec2 texture;
};


static void cursor_position(GLFWwindow* window, double x, double y)
{
double diffX,diffY;

diffX = Xpos - x;
diffY = y - Ypos;

Model = rotate(Model,radians(float(diffX)),vec3(0.0f,0.0f,1.0f));
Model = rotate(Model,radians(float(diffY)),vec3(1.0f,0.0f,0.0f));


}

GLuint text; // une seule texture
void InitTexture(const char* path){
    char data[128*128*3];
    FILE *f = fopen(path, "rb");
    if(f){
        fread(data, 128*128*3, 1, f);
        fclose(f);
        glGenTextures(1, &text);
        glBindTexture(GL_TEXTURE_2D, text);
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 128, 128, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        }
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


    //loadOBJ("C:/Users/LEGION/Desktop/TP/SIM/TP SIM/model/torus.obj", position, texture, normals);

STRVertex vertices[] = {
         vec3(1.0f, -1.0f, 1.0f), vec3(0.0f, 0.0f, 1.0f), vec2(0.f, 0.f),
         vec3(-1.0f, -1.0f, 1.0f), vec3(0.0f, 0.0f, 1.0f), vec2(0.5f, 1.f),
         vec3(-1.0f, -1.0f, -1.0f), vec3(0.0f, 0.0f, 1.0f), vec2(1.f, 0.f),
         vec3(1.0f, -1.0f, -1.0f), vec3(0.0f, 0.0f, 1.0f), vec2(0.f, 1.f),
         vec3(0.0f, 1.0f, 0.0f), vec3(1.0f, 0.0f, 1.0f), vec2(0.f, 0.f),

 };

GLuint vertex_index []={0,1,2,2,3,0,4,3,0,4,1,2,4,2,3,4,1,0};

    unsigned int VBO, VBOColor,VAO, VBOTexture, ibo;

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


   glGenBuffers(1, &VBOTexture);
    glBindBuffer(GL_ARRAY_BUFFER, VBOTexture);
    glBufferData(GL_ARRAY_BUFFER, normals.size() * sizeof(glm::vec2), &texture[0], GL_STATIC_DRAW);
    glEnableVertexAttribArray(2);
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, sizeof(STRVertex), (void*) offsetof(STRVertex,texture));

    glGenBuffers(1, &ibo);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,ibo);
    glBufferData(GL_ARRAY_BUFFER,18 * sizeof(GLuint), &vertex_index, GL_STATIC_DRAW);

    glBindVertexArray(0);





    GLuint ShaderProgram;
    ShaderProgram = LoadShaders( "shader/SimpleVertexShader.vertexshader", "shader/SimpleFragmentShader.fragmentshader" );

GLuint TextureID = glGetUniformLocation(ShaderProgram, "ourTexture");

    InitTexture("textures/herbe.raw");



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
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,ibo);
        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, text);
        glUniform1i(TextureID, 0);

       // glDrawArrays(GL_TRIANGLES, 0, 3456);
        glDrawElements(GL_TRIANGLES,18,GL_UNSIGNED_INT,0);
        glfwSwapBuffers(window);

        glfwPollEvents();
    }

    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);

    glfwTerminate();
    return 0;
}
