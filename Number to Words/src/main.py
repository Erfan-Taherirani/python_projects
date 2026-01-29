from src.constants import UNDER_20, TENS, OVER_100


def num_2_words(num):
	if num < 20:
		return UNDER_20[num]

	if num < 100:
		remainder = num % 10
		if remainder == 0:
			return TENS[num // 10]

		return TENS[num // 10] + "-" + num_2_words(remainder)

	if num >= 100:
		pivot = max([key for key in OVER_100 if num >= key])
		remainder = num % pivot
		p1 = num_2_words(num // pivot)
		p2 = OVER_100[pivot]
		p3 = num_2_words(remainder)
		if remainder == 0:
			return p1 + "-" + p2
			
		return  p1 + "-" + p2 + "-" + p3
	

if __name__ == "__main__":
	assert num_2_words(0) == "Zero"
	assert num_2_words(1) == "One"
	assert num_2_words(10) == "Ten"
	assert num_2_words(20) == "Twenty"
	assert num_2_words(83) == "Eighty-Three"
	
	print("All tests passed!")