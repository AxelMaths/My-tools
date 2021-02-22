#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <assert.h>
#include <errno.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(int argc, char *argv[], char *envp[]) {

    int i;
    int res;
    char nom[256];
    // Creation of tab arguments with dynamic allocation
    char **argv_f; // arguments to be executed
    argv_f = (char **) malloc((argc+4)*sizeof(char *));

    // name to create a dir
    strcat(nom, "Opt");
    for (i=6;i< argc;i++){
        strcat(nom, "__");
        strcat(nom, argv[i]);
    }
    printf("%s",nom);
    res = mkdir(nom, S_IRUSR | S_IWUSR | S_IXUSR
                       | S_IRGRP | S_IWGRP | S_IXGRP
                       | S_IROTH | S_IWOTH | S_IXOTH);
    /* Ces droits peuvent être limités par umask (voir la page de
     * manuel de mkdir et celle d’umask */
    assert(res != -1);


    strcat(nom,"/results");
    //args to real command
    for(i=0; i<argc-1;i++){
        argv_f[i]=argv[i+1];
    }
    argv_f[i]="|";
    argv_f[i+1]="tee";
    argv_f[i+2]=nom;
    argv_f[i+3]=(char*)NULL;


    execve("bash", argv_f, envp);

    return EXIT_SUCCESS;

}