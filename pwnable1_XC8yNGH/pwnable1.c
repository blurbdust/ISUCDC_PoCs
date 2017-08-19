#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>

char answer[1024];

int main(void)
{
	if (setvbuf(stdout, NULL, _IONBF, 0)) {
		perror("setvbuf");
	}

	if (setvbuf(stdin, NULL, _IONBF, 0)) {
		perror("setvbuf");
	}

	if (mprotect((char *) ((long long) answer & (long long) -4096), 
				4096, PROT_READ | PROT_WRITE | PROT_EXEC)) {
		perror("mprotect");
	}

	FILE * splash = fopen("splash.txt", "r");
	if (splash == NULL) {
		perror("fopen");
		return -1;
	}
	
	char * line = NULL;
	size_t len = 0;
	while (getline(&line, &len, splash) > 0) {
		fputs(line, stdout);
	}

	printf("Is this dinosaur cool? (yes/no): ");
	read(0, answer, 1024);


	printf("Do you want to hear your answer? (yes/no): ");
	char echo[16];
	read(0, echo, 1024);

	if (strcmp("yes", echo))
	{
		printf(answer);
	}
}
