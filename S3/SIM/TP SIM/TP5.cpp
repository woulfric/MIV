#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "shader/shader.hpp"

#include <glm.hpp>
#include <gtx/transform.hpp>
using namespace glm;

void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    glViewport(0, 0, width, height);
}

int main() {

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

        float vertices[] = {
            1.0f, 0.0f, 0.0f,
            0.0f, 1.0f, 0.0f,
            -1.0f, 0.0f, 0.0f,
    };

 /*   float vertices[] = {
            1.0f, 0.0f, 0.0f, 1.0f, 0.0f, 0.0f,
            0.0f, -1.0f, 0.0f, 0.0f, 1.0f, 0.0f,
            -1.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f,
};*/


    GLuint VAO;
    GLuint VBO;

    glGenVertexArrays(1, &VAO);
    glBindVertexArray(VAO);

    glGenBuffers(1, &VBO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);

    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat) , (void*)0 );

    glEnableVertexAttribArray(0);

    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);



    GLuint ShaderProgram;
    ShaderProgram = LoadShaders( "shader/SimpleVertexShader.vertexshader", "shader/SimpleFragmentShader.fragmentshader" );

    mat4 Projection = perspective(radians(45.0f), 4.0f / 3.0f, 0.1f, 100.0f);
    mat4 View = lookAt(vec3(2,2,5),vec3(0,0,0),vec3(0,1,0) );
    mat4 Model = mat4(1.0f);
    Model = translate(Model,vec3(-1.0f, 0.0f, 0.0f));
    Model = scale(Model,vec3(2.5f, 1.5f ,1.0f));
    Model = rotate(Model,radians(45.0f),vec3(0.0f,0.0f,1.0f));

    mat4 MVP = Projection * View * Model;
    GLuint MatrixID = glGetUniformLocation(ShaderProgram, "MVP");



    while(!glfwWindowShouldClose(window)) {

        glUseProgram(ShaderProgram);


        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glBindVertexArray(VAO);

        glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &MVP[0][0]);
        glDrawArrays(GL_TRIANGLES, 0, 3);
        glfwSwapBuffers(window);

        glfwPollEvents();
    }

    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);

    glfwTerminate();
    return 0;
}
