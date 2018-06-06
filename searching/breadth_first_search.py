# coding: utf-8

#breadth first search
#幅優先探索

#探索するデータはこんな構造を想定
#field = [[0,1,2],[0,1,2],[0,1,2]]

def copy(list):
    return [x for x in list]

#次ステップで処理すべき内容を列挙
def bf_search(pos,width,depth,hystory):
   hystory_temp = copy(hystory)
   hystory_temp.append(pos) 

   next = []
   if not pos[0] == depth-1:
       for w in range(width):
          next.append([[pos[0] + 1,w],hystory_temp])

   return next

W = 3
H = 3

next_visit = [[0,0],[0,1],[0,2]]
hystory = []

next = [ [i,hystory] for i in next_visit ]

#1ループは
#処理予定の対称を処理->次に処理する対称を集める
#から成る

while(not len(next) == 0):#処理すべきアイテムを詰めたキューが空なら終了
    temp = []
    for item in next:
        print( item[1],item[0])
        if item[0][0] < H:
            temp.extend( bf_search(item[0], W, H, item[1]) )

    next = temp


