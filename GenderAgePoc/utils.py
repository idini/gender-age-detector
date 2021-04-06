import cv2

def draw_boxes(img, box, landmarsk, name, score=100):
    """draw a bounding box on image"""
    box = list(map(int, box))
    color = (148, 133, 0)
    tl = round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line thickness
    c1, c2 = (box[0], box[1]), (box[2], box[3])
    # draw bounding box
    cv2.rectangle(img, c1, c2, color, thickness=tl)
    # draw landmark
    for land in landmarsk:
        cv2.circle(img, tuple(land.int().tolist()), 3, color, -1)
    # draw score
    score = 100-(score*100/1.4)
    score = 0 if score < 0 else score
    bar = (box[3] + 2) - (box[1] - 2)
    score_final = int(bar - (score*bar/100))
    cv2.rectangle(img, (box[2] + 1, box[1] - 2 + score_final), (box[2] + (tl+5), box[3] + 2), color, -1)
    # draw label
    tf = max(tl - 1, 1)  # font thickness
    t_size = cv2.getTextSize(name, 0, fontScale=tl / 3, thickness=tf)[0]
    c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
    cv2.rectangle(img, c1, c2, color, -1)  # filled
    cv2.putText(img, name, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
