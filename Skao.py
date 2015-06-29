bl_info = {
	"name": "Shape Key From Active Object", 
	"category": "Mesh"
}

import bpy
import math

def DeltaVector(vA,vB):
	vC = []
	vC.append((vB.co[0] - vA.co[0]))
	vC.append((vB.co[1] - vA.co[1]))
	vC.append((vB.co[2] - vA.co[2]))
	return vC

def Distance(Delta):
	d = math.sqrt((Delta[0]*Delta[0]) + (Delta[1]*Delta[1]) + (Delta[2]*Delta [2]))
	return d


class VertexDistanceMap: 	#This will map a vertices index to a minimum distance value

	def __init__(self,i,d):
		self.index = i
		self.distance = d
	
	def __del__(self):
		self.index = 0
		self.distance = 0
	
	def __lt__(self,other):	#Less than method, defining it like this allows sort() to operate on this class properly
		return self.distance < other.distance
	
	def set(i,d):
		self.index = i
		self.distance = d

class VertexClone:		#Used to clone vertices in the MeshClone class
	def __init__(self,x,y,z):
		self.co = []
		self.co.append(x)
		self.co.append(y)
		self.co.append(z)
		
	def __del__(self):
		self.co[0] = 0
		self.co[1] = 0
		self.co[2] = 0

class MeshClone:	#I'll use this to create clones of the active mesh that can have vertices removed from them
	
	def __init__(self,t):		#t is the target meshes vertices array, t should be an object.data.vertices instance
		self.vtx = []
		for v in t:
			p = VertexClone(v.co[0],v.co[1],v.co[2])	#Clone the vertex data
			self.vtx.append(p)	#Append to the vtx list

class ShapeKeyActiveObject(bpy.types.Operator):		#My operator!
	"""Create a Shape Key in the Selected Object, from the Active Object"""			#Tooltip for menu items and buttons
	bl_idname = "object.active_shape"				#Unique ID for buttons and menu items
	bl_label = "Shape Key: Active Object"					#Display name in the interface
	bl_options = {'REGISTER','UNDO'}				#Enable undo for the operator
	
	def execute(self,context):						#execute() is called by Blender when running the operator
		
		act = bpy.context.active_object				#Active object
		sel = [] 									#Selected object array
		for obj in bpy.context.selected_objects:	#Make sure only selected mesh objects are within the sel array
			if obj != act and obj.type == "MESH":
				sel.append(obj)
		print("Selected Objects:%i" % len(sel))
		print("Checking that all meshes have identical vertex counts...")
		print("Active Object Vertices:%i" % len(act.data.vertices))
		for m in sel:
			if len(m.data.vertices) != len(act.data.vertices):
				print("A selected mesh has too many vertices!")
				return {'FINISHED'}
		
		#Sel should now only have meshes with the proper vertex count now
		print("All meshes have the same number of vertices!")
		
		for i,obj in enumerate(sel):	#Object Level
			#i is the index
			#obj is the object
			vdm = []		#At the object level because it maps vertices within an object to their minimum distance
			for j,vA in enumerate(obj.data.vertices):	#Object Vertex Level
				#j is the index
				#vA is the vertex of obj
				dist = 1000000000
				for k,vB in enumerate(act.data.vertices):	#Active Vertex Level
					#k is the index
					#vB is the vertex of act
					dst = Distance(DeltaVector(vA,vB))
					if dst < dist:
						dist = dst
				vd = VertexDistanceMap(j,dist)
				vdm.append(vd)
				print("%i,%i"%(j,k))
			# Object Level Again
			vdm.sort()	#Sort the vdm array so that the vertex with the lowest minimum distance is first in the array
			print("Printing object distances...")
			for t in vdm:
				print(t.distance)	#print all the minimum distances, sorted from least to greatest
			
			actclone = MeshClone(act.data.vertices)	#Create active object mesh clone
			for vrt in vdm:			#iterate through vertex-distance map
				vertex = obj.data.vertices[vrt.index]	#Assign the working vertex
				avdm = VertexDistanceMap(0,1000000000)#Need a vertex-distance map
				
				for j,Avtx in enumerate(actclone.vtx):
					#calculate the difference
					dist = Distance(DeltaVector(vertex,Avtx))
					if dist < avdm.distance:
						avdm.distance = dist
						avdm.index = j		#index of the vertex the min distance is too
				#Should have the least distance now
				#Apply the transformation
				vertex.co[0] = actclone.vtx[avdm.index].co[0]
				vertex.co[1] = actclone.vtx[avdm.index].co[1]
				vertex.co[2] = actclone.vtx[avdm.index].co[2]
				
				del actclone.vtx[avdm.index]	#Remove that vertex from the active clone
				print("Active clone vertices remaining:%i" % len(actclone.vtx))
				
				
				
		
		
		return {'FINISHED'}							#This lets Blender know the operator finished successfully.

		
def register():										#Registering the operator
    bpy.utils.register_class(ShapeKeyActiveObject)
	
def unregister():									#Unregistering the operator
    bpy.utils.unregister_class(ShapeKeyActiveObject)
	



#This allows you to run the script directly from Blender's text editor
#to test the addon without having to install it.
if __name__ == "__main__":
	register()