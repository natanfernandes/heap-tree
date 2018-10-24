class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.vector = []
	
	def calc_filho_dir(self,i):
		filho_dir = int((2*i)+2)
		return filho_dir

	def calc_filho_esq(self,i):
		filho_esq = int((2*i)+1)
		return filho_esq

	def calc_pai(self,i):
		pai = int((i-1)/2)
		return pai

	def inserir(self,Node):
		self.vector.append(Node)
		
	def imprimir(self):
		for node in self.vector:
			print(node)
			
	def subir(self,node):
		pos_pai_node = self.calc_pai(self.vector.index(node))
		if self.vector[pos_pai_node]> node:
			aux = self.vector[pos_pai_node]
			self.vector[pos_pai_node] = node
			node = aux
		else:
			print('node filho maior que o pai')
			return

tree = Tree()


tree.inserir(10)
tree.inserir(25)
tree.imprimir()
tree.subir(25)
tree.imprimir()
