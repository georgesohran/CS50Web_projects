#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    char* input_file_name = argv[1];
    char* output_file_name = argv[2];

    //if (strcmp(&input_file_name[strlen(input_file_name)-3], "wav") != 0)
    //{
    //    printf("Input is not a WAV file.\n");
    //    return 2;
    //}

    // Open input file for reading
    // TODO #2
    FILE* input_file = fopen(input_file_name, "r");
    if (input_file == NULL)
    {
        printf("Could not open %s.\n", input_file_name);
        return 1;
    }

    fclose(input_file);

    // Read header
    // TODO #3

    WAVHEADER wavhead;
    fread(&wavhead, sizeof(WAVHEADER), 1, input_file);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(wavhead) != 0)
    {
        return 69;
    }

    // Open output file for writing
    // TODO #5

    // Write header to file
    // TODO #6

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.)
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return 0;
}
