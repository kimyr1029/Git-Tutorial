#include <stdio.h>


int main(void)
{
	int k,n,p;
	int i=0;
	scanf("%d %d %d",&k,&p,&n );
	for(i;i<n;i++)
	{

		k=(k*p)%100000000007;
	}
	printf(k);
	return 0;
}