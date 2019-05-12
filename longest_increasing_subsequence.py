#Author : Rahul Sawra

#Q. Find the length of longest increasing subsequence

def longestCommonSubsequence(A):
	length = len(A)
	T = [1 for _ in range(length)]

	for i in range(length):
		for j in range(0,i):
			if A[j]<A[i]:
				T[i] = max(T[i],T[j]+1)
	print(T)

	return max(T)

if __name__ == '__main__':
	A = [3,4,-1,0,6,2,3]

	assert 4 == longestCommonSubsequence(A)
