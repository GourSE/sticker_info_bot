#define _PROGRAM_NAME "Sticker Info Bot"
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include "colour.h"

const char BOT_C[] = "python3 bot.py";

const char BOT[] = "python3 ~/.local/share/sticker_info_bot/bot.py";

int getLocalConfig();



int loopScript();


int main(int argc, char **argv)
{

    int r;
    char flg[50];

    for (r = 0; r < argc; r++)
    {
        if (r == 0)
        {
            strcpy(flg, "*noFlag");
        }
        else if (r == 1)
        {
            strcpy(flg, argv[1]);
        }
        else if (r > 1)
        {
            printf("usage: sticker_info_bot <-r/--config>\n\n");
            return 1;
        }
    }

    if (strcmp(flg, "-r") == 0)
    {
        loopScript();
        return 0;
    }        
    else if (strcmp(flg, "--config") == 0)
    {
        char command[150];

        int built = getLocalConfig();

        if (built == -1)
        {
            system("nano config.cfg");
        }
        else
        {
            char *homeDir = getenv("HOME");
            char file_[] = "/.local/share/sticker_info_bot/config.cfg";
            char *fileLoc = malloc(strlen(homeDir) + strlen(file_) + 1);
            strcpy(fileLoc, homeDir);
            strcat(fileLoc, file_);

            sprintf(command, "%s %s", "nano", fileLoc);
            system(command);
        }
        return 0;
    }
    else if (strcmp(flg, "-c") == 0)
    {
        #ifdef __linux__
        char command[150];

        int built = getLocalConfig();

        if (built == -1)
        {
            system("nano config.cfg");
        }
        else
        {
            char *homeDir = getenv("HOME");
            char file_[] = "/.local/share/sticker_info_bot/config.cfg";
            char *fileLoc = malloc(strlen(homeDir) + strlen(file_) + 1);
            strcpy(fileLoc, homeDir);
            strcat(fileLoc, file_);

            sprintf(command, "%s %s", "nano", fileLoc);
            system(command);
        }
        return 0;
        #else
        ;
        #endif
    }
    else if (strcmp(flg, "*noFlag") == 0)
    {
        ;
    }
    else
    {
        printf("'%s' not recognised\n", flg);
        printf("usage: sticker_info_bot <-r/--config>\n\n");

        return 0;
    }

    system(BOT);

}


int loopScript()
{
    int built = getLocalConfig();
    int loopCount = 1;

    if (built == -1)
    {
        while(1)
        {
            if (loopCount == 1)
            {
                printf(CYAN "Initial loop\n" NONE);
                loopCount ++;
            }
            else
            {
                system("clear");
                printf(CYAN "Loop No.%d\n" NONE, loopCount);
                loopCount ++;
            }

            system(BOT_C);
        }
        
    }
    else
    {
        while(1)
        {
            if (loopCount == 1)
            {
                printf(CYAN "Initial loop\n" NONE);
                loopCount ++;
            }
            else
            {
                system("clear");
                printf(CYAN "Loop No.%d\n" NONE, loopCount);
                loopCount ++;
            }

            system(BOT);
        }
    }
}


int getLocalConfig()
{
    char *homeDir = getenv("HOME");

    char file_[] = "/.local/share/sticker_info_bot/config.cfg";

    char *fileLoc = malloc(strlen(homeDir) + strlen(file_) + 1);
    strcpy(fileLoc, homeDir);
    strcat(fileLoc, file_);

    struct stat buffer;
    int file__ = stat(fileLoc, &buffer);

    if (file__ == 0)
    {
        return 0;
    }
    else
    {
        return -1;
    }
    return 0;
}