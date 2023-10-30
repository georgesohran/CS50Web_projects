#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long n = get_long("Number: ");

    int first_sum = 0;

    int second_sum = 0;

    for (int power = 1, power <= 8, power += 2)
    {
        second_sum += n % pow(10, power) / pow(10, (power - 1));
    }

    for (int power = 2, power <= 8, power += 2)
    {
        int x = (n % pow(10, power) / pow(10, (power - 1))) * 2;

        first_sum += x % 10;
        first_sum += (x % 100) / 10;

        }


    int final_sum = second_sum + first_sum;

    if (final_sum % 10 != 0)
    {
        printf("INVALID\n");

    }
    else
    {
        if ((n >= pow(10, 15)) & (n < pow(10,16)) & (n % pow(10, 15) / pow(10, (power - 1))))
        {
            printf("VISA\n");
        }
        else if ((n >= pow(10, 12)) & (n < pow(10,13)))
        {
            printf("VISA\n");
        }
        else if ((n >= pow(10, 14)) & (n < pow(10,15)))
        {
            printf("AMEX\n");
        }
        else if ((n >= pow(10, 15)) & (n < pow(10,16)))
        {
            printf("MASTERCARD\n");
        }
    }

}
