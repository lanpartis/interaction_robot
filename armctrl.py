import rospy
from std_msgs.msg import Int16MultiArray

class Action():
	def __init__(self,a):
		assert len(a) == 7
		self.left = a
		self.regulize()

	def regulize(self):
		if self.left[1] < 0:
			self.left[1] = 0
		if self.left[1] > 160:
			self.left[1] = 160
		if self.left[2] < 70:
			self.left[2] = 70
		if self.left[2] >165:
			self.left[2] = 165
		if self.left[3] < 95:
			self.left[3] = 95
		if self.left[3] >180:
			self.left[3] = 180
		if self.left[4] < 120:
			self.left[4] = 120
		if self.left[4] >180:
			self.left[4] = 180
		if self.left[5] < 0:
			self.left[5] = 0
		if self.left[5] > 180:
			self.left[5] = 180
		if self.left[6] < 10:
			self.left[6] = 10
		if self.left[6] > 73:
			self.left[6] = 73

	@property
	def right(self):
		act = self.left[:]
		act[1] = 180 - act[1]
		act[5] = 108 - act[5]
		return act


class Controller():

	def __init__(self):
		self.left,self.right = self.init_publisher()

	def init_publisher(self):
		left =rospy.Publisher('dlactleft',Int16MultiArray,queue_size = 10)
		right = rospy.Publisher('dlactright',Int16MultiArray,queue_size = 10)
		rospy.init_node('dlactpub')
		return left,right

	def left_publisher(self,action):
		arr4pub = Int16MultiArray(data = action)
		self.left.publish(arr4pub)

	def right_publisher(self,action):
		arr4pub = Int16MultiArray(data = action)
		self.right.publish(arr4pub)


def main():
	ctr = Controller()
	while(1):
		a = raw_input('action?[t,m1,m2,m3,m4,m5,m6]:')
		a = map(int,a.split(','))

		act = Action(a)
		ctr.left_publisher(act.left)
		ctr.right_publisher(act.right)

if __name__ == '__main__':
	main()