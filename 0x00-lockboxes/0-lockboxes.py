#!/usr/bin/python3
def function(index, boxes, keys_dict):
    for i in boxes[index]:
        if i in list(keys_dict.keys()):
            continue
        keys_dict.update({i: None})
        function(i, boxes, keys_dict)
def canUnlockAll(boxes):
    """Know if can entry to all sublists"""
    keys_dict = {}
    keys_dict[0] = None
    for keys in boxes[0]:
        keys_dict[keys] = None

    for index in boxes[0]:
        function(index, boxes, keys_dict)

    list_boxes = []
    for index in list(keys_dict.keys()):
        list_boxes.append(boxes[index])
    
    print("Dictionary: {}".format(keys_dict))
    print("len(list_boxes): {}".format(len(list_boxes)))
    print("len(boxes): {}".format(len(boxes)))
    if len(list_boxes) == len(boxes):
        return True
    return False

boxes = [[0,1,2], [0,1,2], [0,1,2]]
print(canUnlockAll(boxes))