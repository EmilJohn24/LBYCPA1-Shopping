#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string>
#include <iostream>
#include "git.h"

using namespace std;
int main(){
    git("clone https://github.com/EmilJohn24/LBYCPA1-Shopping.git");
    system("cd .\\LBYCPA1-Shopping");
    cout << "You are now in editing mode... Leave this window and come back once you're done editing. Press any key to upload changes" << endl;
    system("pause >nul");
    git(strcat("checkout -b ",  getUserName()));
    git("add *");
    git("commit");
    git("push");
    cout << "Uploading changes..." << endl;



}
