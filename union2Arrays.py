''' Union of two arrays'''
nums1=[1,2,3,4,5]
nums2=[4,5,6,7,8]
for num in nums2:
    if num not in nums1:
        nums1.append(num)
print("Union of two arrays:",nums1)