class node(object):
	"""docstring for node"""
	def __init__(self, val):
		super(node, self).__init__()
		self.val = val
		self.left=None
		self.right=None
class rev(object):
	"""docstring for """
	def __init__(self):
		super(rev, self).__init__()
		self.root = root
	def insert(self,x):
		y=node(x)
		if root is None:
			root=y
		else:
			p=root
			follow=None
			while p is not None:
				if x>p.val:
					follow=p
					p=p.right
				if x<p.val:
					follow=p
					p=p.left
		if follow.left is None:
			follow.left=y
		else:
			follow.right=y
	def serarch(self,x)
		p=self.root
		l=1
		while p is not None:
			if x>p.val:
				p=p.right
				l=l+1
			if x<p.val:
				p=p.left
				l=l+1
			if x==p.val
				break
		if p is not None:
			print('found at level',l)
	def inorder(self)
	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

		



		
		