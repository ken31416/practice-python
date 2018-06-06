# coding: utf-8

#breadth first search
#深さ優先探索

#探索するデータはこんな構造を想定
#field = [[0,1,2],[0,1,2],[0,1,2]]

def copy(list):
    return [x for x in list]

#最大深さに達するまで再帰的に訪問する
def df_search(pos,width,depth):
    for i in range(pos[0]):
        print("--",end='')
    print(pos)

    #最大深さで打ち切り
    if pos[0] == depth-1:
       return

    #再帰的に訪問
    for w in range(width):
        next_pos = [ pos[0] +1 , w]
        df_search( next_pos, width, depth )


W = 3
H = 3

for w in range(W):
    df_search([0,w],W,H) 

