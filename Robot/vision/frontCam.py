			ret_val, img = self.capture.read()
			if mirror: 
				img = cv2.flip(img, 1)
				kernel = np.ones((5,5), np.uint8)
				img = cv2.erode(img, kernel, iterations=1)
				img = cv2.dilate(img, kernel, iterations=1)
				img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
				_, cnts,_ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
				
				if 1==1:
					for c in cnts:
						#For debug
						#print(c)
						# If contours are too small or large, ignore them:
						if cv2.contourArea(c)<100:
							print("Too small")	
							continue
						cv2.drawContours(img, [c], -1, (0,255,0), 3)
						#x,y,w,h = cv2.boundingRect(cnts)
						#cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
						# Find center point of contours:
						M = cv2.moments(c)
						centers = []
						cX = int(M['m10'] /M['m00'])
						cY = int(M['m01'] /M['m00'])
						centers.append([cX,cY])		
						if len(centers) >=2:
							dx= centers[0][0] - centers[1][0]
							dy = centers[0][1] - centers[1][1]
							D = np.sqrt(dx*dx+dy*dy)
							print(D)	
							#Display Num of Units
							'''cv2.putText(image, "units" % D,
								(img.shape[1] - 200, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
								2.0, (0, 255, 0), 3)
							'''
						height, width = img.shape
						bytesPerLine = 3 * width
						image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)						
						#image = QImage(img,img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
						#cv2.imshow("vision",img)
						#return setPixmap(QPixmap.fromImage(image))
						self.label.setPixmap(QtGui.QPixmap.fromImage(image))
