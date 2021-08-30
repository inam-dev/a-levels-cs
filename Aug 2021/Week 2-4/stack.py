class Stack:
	def _init_(self, length):
		self.p = 0
		self.stack = []
		self.len = length
		

	def insert(self, name):
		if self.p == self.len:
			print("Stack full")
		else:
			self.p += 1
			self.stack.append(name)
			#print(f"Inserted {name} :trollhd:")

	def pop(self):
		if self.p == 0:
			print("Stack is already Empty")
		else:
			self.p -= 1
			self.stack.pop(self.p)
			#print(self.stack)

	def find(self, search):
		for c in self.stack:
			if (c == search):
				print(f"Found {c}")

	def empty(self):
		self.p = 0

		
st = Stack(4)

print(st.p)
st.insert("hello")
st.insert("hello")
print(f"{st.p} {st.stack}")
st.empty()
print(f"{st.p} {st.stack}")
st.insert("hello")
print(f"{st.p} {st.stack}")
st.pop()
print(f"{st.p} {st.stack}")
st.pop()
st.pop()
st.pop()
print(st.p)