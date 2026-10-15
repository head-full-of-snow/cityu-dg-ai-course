# Stereo reconstruction pipeline

# • Steps

— Calibrate cameras

— Rectify images

— Compute disparity

— Estimate depth

# What will cause errors?

• Camera calibration errors

• Poor image resolution

• Occlusions

• Violations of brightness constancy (specular reflections)

• Large motions

# Low-contrast image regions

# V ariants of stereo

# Real-time stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F34cc332de41748f6a435c99399ac177d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=kmoy76MZ6kPITgg4qBqDgC%2FAk8A%3D)

Nomad robot searches for meteorites in Antartica

• Used for robot navigation (and other tasks)

– Several real-time stereo techniques have been developed (most based on simple discrete search)

# Active stereo with structured light

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F0965f464d3f34077967d367af6d3b49e.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=DxrR1ELZ0jbUGCMNIHvdD5tfhAU%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Fc62f5398208a49c2b5ace425bcdd5fba.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=em92mxT7Pj5tivWqLD%2BJATz9D28%3D)

Li Zhang's one-shot stereo

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Fda7878bd84a54b08a982728883c89140.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=ymFCIeJBTQ8DbX%2F6zPtVXFnNLVU%3D)

projector

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F8300bda86b2d47dda02d5908e52b1b1a.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=Fa%2FT97aWJKSfrUxxTU9j8DpWP0I%3D)

projector

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F5b469ee085e54022b371210a3d511af3.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=P48a57Y1IhcsOSuJXgfwA%2F74ptU%3D)

• Project "structured" light patterns onto the object

– simplifies the correspondence problem

– basis for active depth sensors, such as Kinect and iPhone X (using IR)

# Active stereo with structured light

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F9aabc093ed804c318615a6e0b13af75f.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=UiC7impiir%2BVupQDs%2BzTz4Q0%2BxQ%3D)

https://ios.gadgethacks.com/news/watch-iphone-xs-30k-ir-dots-scan-your-face-0180944/

# Laser scanning

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Fb21c30ab12b44b269186c97e1183e088.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=aFDYDFyyj%2FNGApRRSY%2FWa6jUhqk%3D)

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Ffc597e45bc60426ba6051460be7baaeb.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256978&Signature=RQmDpJDx0N2dG77TjPHoz0h0kI0%3D)

Digital Michelangelo Project

http://graphics.stanford.edu/projects/mich/

• Optical triangulation

– Project a single stripe of laser light

– Scan it across the surface of the object

— This is a very precise version of structured light scanning

# Laser scanned models

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2Fd4f975471665429293686eac7c1184ec.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256979&Signature=qvLpRmwEgVHngZivQiuOu1g7Lik%3D)

The Digital Michelangelo Project, Levoy et al.

# Laser scanned models

![](http://maas-model-u2-ocr.oss-cn-beijing.aliyuncs.com/kms-data-manager%2F992fd7f6fc1a4f68816980b675a31608%2Fmedia%2F2ba0fea4246f4b20bb8ffe77dad44d5d.jpg?OSSAccessKeyId=LTAI5tNcMEY7TGXWsdNGEppS&Expires=1799256979&Signature=thilrcyv17qsNe9HRE7VQ1%2BdzAA%3D)

The Digital Michelangelo Project, Levoy et al.
