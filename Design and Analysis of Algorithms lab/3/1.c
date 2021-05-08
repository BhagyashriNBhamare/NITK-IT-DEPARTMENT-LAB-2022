#include<stdio.h>

#include<omp.h>







main()

{


	float  array[1000][24],row[1000]





	printf("The Array Elements Are \n");



	for (i = 0; i < 1000; i++)

		for (j = 0; j < 24; j++)

			printf("entre the value of temperature of %d at %d",i,j );
			svanf("%f",&arr[i][j]);

float sum=0

#pragma opm parallel num_threads(4) default(shared) schedule(guided, 10) reduction(+sum)

{

	for (i = 0; i < 1000; i++) {

	



	for (j = 0; j < 24; j++)

	{

		sum = sum + array[i][j];



	}

	row[i]=sum;

	k=sum/24

	printf("average temperature in senor %d is %f",i,k)

	}



	float average_sum =0;

	#pragma opm parallel num_threads(4) reduction(+average_sum);

	{

for (i = 0; i < 1000; i++) 

{

average_sum=average_sum+row[i];

}

m=average_sum%24000;

printf("average temperature in all senor is  %f" ,m);



}

}