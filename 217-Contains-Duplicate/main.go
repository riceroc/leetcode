package main

// create a hash map using make. Add each visited number to the set and
// and return true if you encounter it twice
func containsDuplicate(nums []int) bool {
	hash := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		hash[nums[i]]++
		if hash[nums[i]] > 1 {
			return true
		}
	}
	return false
}
