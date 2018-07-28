class SortAlgorithm:
	"""
		多种排序算法，实现对列表元素的排序
	"""

	def __init__(self, descent=False):
		"""
		类初始化方法
		:param descent: 排序方向，默认值是从小到大排序；可以通过将其设为True实现从大到小排序
		"""
		self.descent = descent

	def bubble_sort(self, data_list):
		"""
		冒泡排序方法
			len(list) = n
			轮数：n-1
			每轮两辆元素比较的次数：n - i - 1（i：已经排好序的元素个数，等于已经排序过的轮数）
		原理
			循环遍历列表，每次循环找出本次循环最大的元素排在后边（从小到大排序）
			双层循环实现，外层控制循环次数，内层负责数值比较
		:param data_list: 待排序列表
		:return: 排序后列表
		"""
		if not self.descent:
			for i in range(len(data_list) - 1):
				for j in range(len(data_list) - i - 1):
					if data_list[j] > data_list[j + 1]:
						data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
			return data_list
		else:
			for i in range(len(data_list) - 1):
				for j in range(len(data_list) - i - 1):
					if data_list[j] <= data_list[j + 1]:
						data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
			return data_list

	def select_sort(self, data_list):
		"""
		选择排序方法
			待排序元素有n个，总共需要 n-1 轮排序
		原理
			将待排序列表看成是已排序和未排序两部分
			每次从未排序列表中找出最小值放到已排序列表末尾
		:param data_list: 待排序列表
		:return: 排序后列表
		"""
		if not self.descent:		# 从小到大排序
			for i in range(len(data_list)):		# 控制排序轮数
				min_idx = i		# 初始假设最小值的脚标
				for j in range(i + 1, len(data_list)):
					min_idx = j if data_list[min_idx] >= data_list[j] else min_idx
				data_list[i], data_list[min_idx] = data_list[min_idx], data_list[i] if i != min_idx else data_list[i]
			return data_list
		else:						# 从大到小排序
			for i in range(len(data_list)):		# 控制排序轮数
				max_idx = i		# 初始假设最小值的脚标
				for j in range(i + 1, len(data_list)):
					max_idx = j if data_list[max_idx] < data_list[j] else max_idx
				data_list[i], data_list[max_idx] = data_list[max_idx], data_list[i] if i != max_idx else data_list[i]
			return data_list

	def quick_sort(self, data_list, start, end):
		"""
		快速排序方法
			基准值：默认待排序的第1个元素
			使用临时变量存储基准值
			高位游标、低位游标分别指向待排序序列的两端
		原理
			一次按照一个基准值将待排序的列表分割成两部分，基准值左边是比基准值小的元素，基准值右边是比基准值大的元素
			按照上一步的方法对基准值所有两部分数据分别进行快速排序
		:param start: 低位游标
		:param end: 高位游标
		:param data_list: 待排序列表
		:return: 排序后列表
		"""
		if not self.descent:
			if start >= end:		# 递归结束标识，低位游标大于等于高位游标时，说明该子序列排序已完成
				return data_list
			low_idx = start		# 低位游标
			high_idx = end		# 高位游标
			basic_value = data_list[low_idx]		# 基准值
			# 两个游标不重合则进入循环
			while low_idx < high_idx:
				# 如果低位游标值小于高位游标且高位游标指向的元素大于等于基准值则进入循环
				while low_idx < high_idx and data_list[high_idx] >= basic_value:
					high_idx -= 1		# 高位游标向左移动一位
				if low_idx != high_idx:		# 当高位游标指定的元素小于基准值，则移动到该值到低位游标指向的位置
					data_list[low_idx] = data_list[high_idx]
					low_idx += 1
				# 如果低位游标值小于高位游标且低位游标指向的元素小于基准值则进入循环
				while low_idx < high_idx and data_list[low_idx] < basic_value:
					low_idx += 1		# 低位游标向右移动一位
				if low_idx != high_idx:		# 如果低位游标指向的元素小于基准值，则移动到该值到高位游标指向的位置
					data_list[high_idx] = data_list[low_idx]
					high_idx -= 1
			data_list[high_idx] = basic_value		# 基准值所在位置（此时low_index == high_index）
			self.quick_sort(data_list, start, low_idx - 1)		# 对基准值左侧未排序元素采用快速排序算法
			self.quick_sort(data_list, high_idx + 1, end)		# 对基准值右侧未排序元素采用快速排序算法
		else:
			if start >= end:		# 递归结束标识，低位游标大于等于高位游标时，说明该子序列排序已完成
				return data_list
			low_idx = start		# 低位游标
			high_idx = end		# 高位游标
			basic_value = data_list[low_idx]		# 基准值
			# 两个游标不重合则进入循环
			while low_idx < high_idx:
				# 如果低位游标值小于高位游标 且 高位游标指向的元素小于基准值则进入循环
				while low_idx < high_idx and data_list[high_idx] < basic_value:
					high_idx -= 1		# 高位游标向左移动一位
				if low_idx != high_idx:		# 当高位游标指定的元素小于基准值，则移动到该值到低位游标指向的位置
					data_list[low_idx] = data_list[high_idx]
					low_idx += 1
				# 如果低位游标值小于高位游标 且 低位游标指向的元素大于等于基准值则进入循环
				while low_idx < high_idx and data_list[low_idx] >= basic_value:
					low_idx += 1		# 低位游标向右移动一位
				if low_idx != high_idx:		# 如果低位游标指向的元素小于基准值，则移动到该值到高位游标指向的位置
					data_list[high_idx] = data_list[low_idx]
					high_idx -= 1
			data_list[high_idx] = basic_value		# 基准值所在位置（此时low_index == high_index）
			self.quick_sort(data_list, start, low_idx - 1)		# 对基准值左侧未排序元素递归采用快速排序算法
			self.quick_sort(data_list, high_idx + 1, end)		# 对基准值右侧未排序元素递归采用快速排序算法
		return data_list

	def merge_sort(self, data_list):
		"""
		归并排序方法——分解函数
		原理
			先递归分解列表，在排序合并列表
		:param data_list: 待排序列表
		:return: 排序后列表
		"""
		if len(data_list) <= 1:
			return data_list
		mid_idx = len(data_list) // 2		# 根据列表长度确定拆分的中间位置
		left_list = self.merge_sort(data_list[:mid_idx])
		right_list = self.merge_sort(data_list[mid_idx:])
		return self.merge(left_list, right_list)

	def merge(self, left_list, right_list):
		"""
		归并排序方法——合并函数
		:param left_list: 左侧子列表
		:param right_list: 右侧子列表
		:return: 合并后列表
		"""
		if not self.descent:
			left_idx = 0		# 左侧列表游标
			right_idx = 0		# 右侧列表游标
			merge_list = []
			while left_idx < len(left_list) and right_idx < len(right_list):		# 左右游标均未移动到最后一个元素时进入循环
				if left_list[left_idx] < right_list[right_idx]:
					merge_list.append(left_list[left_idx])
					left_idx += 1
				else:
					merge_list.append(right_list[right_idx])
					right_idx += 1
			# 跳出循环后，左侧子序列和右侧子序列总有一列是没有添加完成的，因此全部添加一遍
			merge_list += left_list[left_idx:]
			merge_list += right_list[right_idx:]
			return merge_list
		else:
			left_idx = 0  # 左侧列表游标
			right_idx = 0  # 右侧列表游标
			merge_list = []
			while left_idx < len(left_list) and right_idx < len(right_list):  # 左右游标均未移动到最后一个元素时进入循环
				if left_list[left_idx] >= right_list[right_idx]:
					merge_list.append(left_list[left_idx])
					left_idx += 1
				else:
					merge_list.append(right_list[right_idx])
					right_idx += 1
			# 跳出循环后，左侧子序列和右侧子序列总有一列是没有添加完成的，因此全部添加一遍
			merge_list += left_list[left_idx:]
			merge_list += right_list[right_idx:]
			return merge_list


if __name__ == '__main__':
	lst = [7, 6, 3, 1, 4, 2, 5]
	sort_algorithm = SortAlgorithm(descent=True)
	print(sort_algorithm.bubble_sort(lst))
