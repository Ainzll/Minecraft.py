from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint
import math
mc = Minecraft.create("127.0.0.1", 4711)
#mc2 = Minecraft.create("10.183.3.17", 4711)


#clear start
mc.setBlocks(-50,-10,-50,50,100,50,0)

#purple platform
#mc.player.setPos(0,11,0)
#mc.saveCheckpoint()
#mc.setting("nametags_visible",True)
#mc.player.setting("autojump",False)
mc.setBlocks(5,10,5,-5,10,-5,35,10)
mc.setBlock(-6,10,5,1)
mc.setBlock(-6,10,4,2)
mc.setBlock(-6,10,3,3)
mc.setBlock(-6,10,2,4)
#purple left
mc.setBlock(7,11,-2,35,10)
mc.setBlock(7,11,-3,35,10)
mc.setBlock(9,12,-2,35,10)
mc.setBlock(9,12,-3,35,10)
mc.setBlock(13,14,-2,35,10)
mc.setBlock(13,14,-3,35,10)
mc.setBlock(15,15,-2,35,10)
mc.setBlock(15,15,-3,35,10)
#purple right
mc.setBlock(7,11,2,35,10)
mc.setBlock(7,11,3,35,10)
mc.setBlock(9,12,2,35,10)
mc.setBlock(9,12,3,35,10)
mc.setBlock(13,14,2,35,10)
mc.setBlock(13,14,3,35,10)
mc.setBlock(15,15,2,35,10)
mc.setBlock(15,15,3,35,10)
#purple middle
mc.setBlock(11,13,0,35,10)
mc.setBlock(11,13,0,35,10)

#blue platform
mc.setBlocks(17,16,-3,22,16,3,35,3)

#blue left
mc.setBlock(20,17,-5,35,3)
mc.setBlock(19,17,-5,35,3)
mc.setBlock(20,15,-8,35,3)
mc.setBlock(19,15,-8,35,3)
mc.setBlock(20,16,-10,35,3)
mc.setBlock(19,16,-10,35,3)
mc.setBlock(20,17,-12,35,3)
mc.setBlock(19,18,-14,35,3)
mc.setBlock(20,19,-16,35,3)
mc.setBlock(19,20,-18,35,3)
mc.setBlock(17,21,-16,35,3)
mc.setBlock(19,22,-14,35,3)
mc.setBlock(21,21,-12,35,3)
mc.setBlock(19,22,-10,35,3)
mc.setBlock(21,21,-8,35,3)
mc.setBlock(19,22,-6,35,3)
mc.setBlock(21,21,-4,35,3)
mc.setBlock(23,22,-2,35,3)

#blue right
mc.setBlock(20,17,5,35,3)
mc.setBlock(19,17,5,35,3)
mc.setBlock(20,15,8,35,3)
mc.setBlock(19,15,8,35,3)
mc.setBlock(20,16,10,35,3)
mc.setBlock(19,16,10,35,3)
mc.setBlock(20,17,12,35,3)
mc.setBlock(19,18,14,35,3)
mc.setBlock(20,19,16,35,3)
mc.setBlock(19,20,18,35,3)
mc.setBlock(17,21,16,35,3)
mc.setBlock(19,22,14,35,3)
mc.setBlock(21,21,12,35,3)
mc.setBlock(19,22,10,35,3)
mc.setBlock(21,21,8,35,3)
mc.setBlock(19,22,6,35,3)
mc.setBlock(21,21,4,35,3)
mc.setBlock(23,22,2,35,3)

#yellow platform
mc.setBlocks(25,23,0,27,23,0,35,4)
mc.setBlocks(26,23,-1,26,23,1,35,4)

#yellow right
mc.setBlock(26,24,3,65,2)
mc.setBlock(27,25,5,65,4)
mc.setBlock(28,26,3,65,3)
mc.setBlock(27,27,1,65,5)
mc.setBlock(26,28,3,65,2)
mc.setBlock(27,29,5,65,4)
mc.setBlock(28,30,3,65,3)
mc.setBlock(30,31,2,65,4)
mc.setBlock(31,32,3,65,3)
mc.setBlock(32,33,2,65,5)
mc.setBlock(31,34,1,65,2)
mc.setBlock(30,35,2,65,4)
mc.setBlock(31,36,3,65,3)
mc.setBlock(32,37,2,65,5)
mc.setBlock(30,37,0,65,3)
mc.setBlock(28,37,2,65,2)
mc.setBlock(26,37,5,65,2)
mc.setBlock(24,37,3,65,3)

#yellow left
mc.setBlock(26,23,-3,96,1)
mc.setBlock(26,25,-5,96,0)
mc.setBlock(28,27,-5,96,2)
mc.setBlock(28,29,-7,96,1)
mc.setBlock(26,31,-7,96,1)
mc.setBlock(24,33,-7,96,2)
mc.setBlock(24,35,-5,96,1)
mc.setBlock(23,37,-4,96,1)

#red platform
mc.setBlocks(24,37,0,22,37,0,35,14)
mc.setBlocks(23,37,1,23,37,-1,35,14)
mc.setBlock(24,38,-1,35,14)
mc.setBlock(22,38,-1,35,14)
mc.setBlock(24,38,1,35,14)
mc.setBlock(22,38,1,35,14)





while True:
	blocks_hit = mc.events.pollBlockHits()
	for block in blocks_hit:
		position = block.pos
		blockid = mc.getBlock(position)
		if blockid == 1:
			mc.player.setPos(0,11,0)
		if blockid == 2:
			mc.player.setPos(20,17,0)
		if blockid == 3:
			mc.player.setPos(26,24,0)
		if blockid == 4:
			mc.player.setPos(24,38,1)

#while True:
	#blocks_hit2 = mc2.events.pollBlockHits()
	#for block2 in blocks_hit2:
		#position2 = block.pos2
		#blockid2 = mc2.getBlock(position2)
		#if blockid2 == 1:
			#mc2.player.setPos(0,11,0)
		#if blockid2 == 2:
			#mc2.player.setPos(20,17,0)
		#if blockid2 == 3:
			#mc2.player.setPos(26,24,0)
		#if blockid2 == 4:
			#mc2.player.setPos(24,38,1)
