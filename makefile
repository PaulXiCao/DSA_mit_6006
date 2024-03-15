.PHONY: download

download:
	curl https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/6.006-spring-2020.zip -o resources.zip
	unzip resources.zip -d courseData
	rm resources.zip
