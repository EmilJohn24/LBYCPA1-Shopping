#ifndef GIT_H_INCLUDED
#define GIT_H_INCLUDED
#include <string>
#include <windows.h>
#include <Lmcons.h>
#include <iostream>
#include <stdio.h>
using namespace std;

char* getUserName();
char* getMessage();



void git(const char* gitCommand){
    char* command = strcat(".\\PortableGit\\bin\\git.exe ", gitCommand);
    cout << "fuck";
    system(command);
}

char* getUserName(){
    char username[UNLEN+1];
    DWORD username_len = UNLEN+1;
    GetUserName(username, &username_len);
    return username;
}

char* getMessage(){
    char* message;
    cout << "Type a message for your changes:" << endl;
    scanf("%s", &message);
    return message;
}
#endif // GIT_H_INCLUDED
