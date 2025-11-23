import cv2
import numpy as np

def osmoteme(vertices):

    def afinize(p):
        return np.round([x/p[-1] for x in p])

    p1 = vertices[0]
    p2 = vertices[1]
    p3 = vertices[2]
    p5 = vertices[3]
    p6 = vertices[4]
    p7 = vertices[5]
    p8 = vertices[6]

    xb1 = afinize(np.cross(np.cross(p2, p6), np.cross(p1, p5)))
    xb2 = afinize(np.cross(np.cross(p2, p6), np.cross(p7, p3)))
    xb3 = afinize(np.cross(np.cross(p7, p3), np.cross(p5, p1)))
    xb = np.round((xb1 + xb2 + xb3) / 3)

    yb1 = afinize(np.cross(np.cross(p6, p5), np.cross(p7, p8)))
    yb2 = afinize(np.cross(np.cross(p2, p1), np.cross(p6, p5)))
    yb3 = afinize(np.cross(np.cross(p7, p8), np.cross(p2, p1)))
    yb = np.round((yb1 + yb2 + yb3) / 3)

    zb1 = afinize(np.cross(np.cross(p2, p3), np.cross(p6, p7)))
    zb2 = afinize(np.cross(np.cross(p5, p8), np.cross(p6, p7)))
    zb3 = afinize(np.cross(np.cross(p2, p3), np.cross(p5, p8)))
    zb = np.round((zb1 + zb2 + zb3) / 3)

    p41 = afinize(np.cross(np.cross(xb, p8), np.cross(yb, p3)))
    p42 = afinize(np.cross(np.cross(xb, p8), np.cross(zb, p1)))
    p43 = afinize(np.cross(np.cross(yb, p3), np.cross(zb, p1)))
    p4 = np.round((p41 + p42 + p43) / 3)

    return int(p4[0]), int(p4[1])

def display(x, y, idx):
    cv2.circle(image, (x, y), 5, (0, 0, 255), 3)
    if idx == 5 or idx == 1:
        cv2.putText(image, f'{idx}: {x}, {y}', (x - 190, y + 10), cv2.FONT_HERSHEY_TRIPLEX, 0.67, (0, 0, 255), 2)
    else:
        cv2.putText(image, f'{idx}: {x}, {y}', (x + 25, y), cv2.FONT_HERSHEY_TRIPLEX, 0.67, (0, 0, 255), 2)
    cv2.imshow('Osmo teme', image)

def process_click(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        vertices.append([x, y, 1])
        display(x, y, counter)
        counter += 1
        if (len(vertices) == 3):
            counter += 1

    if len(vertices) == 7:
        x0, y0 = osmoteme(vertices)
        display(x0, y0, 4)

if __name__ == '__main__':
    image = cv2.imread(r"Homework_1.jpg")
    cv2.imshow('Osmo teme', image)
    counter = 1
    vertices = []

    cv2.setMouseCallback('Osmo teme', process_click)
    cv2.waitKey(0)
    cv2.destroyAllWindows()