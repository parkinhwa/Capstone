# 3D mapping based on ORB SLAM by using drones

프로젝트 내용 설명
최근 지하 시설 연계 복합 건축물 및 대공간 상업시설이 늘어남에 따라 실내공간과 이에 대한 이해가 복잡해졌다. 이에 따라 건축물의 내부위치를 쉽게 파악하기 위한 위치기반 서비스로 실내지도의 필요성이 두드러지고 있고, 실제로 구글이나 네이버 등 여러 곳에서 실내지도를 제공하고 있다. 그러나 현재 실내지도를 만드는 과정은 많은 시간과 비용이 들어가기 때문에 빈번한 업데이트가 어렵다는 점이 존재한다. 이 논문에서는 기존에 사용되던 지도 제작 방식에서 벗어나 드론을 활용하여 RGBD 영상을 촬영하고 이를 기반으로 ORB SLAM을 이용하여 지도를 만드는 법을 제안하여 적은 비용으로 실내지도 업데이트를 제작한다. 여기서 더 나아가 객체 인식을 접목하여 객체의 위치를 실내지도에 반영하는 것을 목표로 한다.
우리의 목적은 3차원으로 구축된 실내공간정보인 실내지도를 현실과 동기화가 지연 없이 이루어지는, 즉 지도의 업데이트가 자주 이루어질 수 있게 자동화 하는 것이 목적. 그래서 드론을 활용하여 이동의 제약을 없애고 객체 인식 또한 자동으로 이루어져 지도에 반영하여 학습된 객체의 위치를 지도에 반영해야 한다.

프로젝트 역할 분배


수행내용

1. 객체 인식

![image](https://user-images.githubusercontent.com/65644486/139801318-879ab55a-f7d5-4935-9a89-3288a5ef42fb.png)
그림  mAP 성능표


mAP(mean average percision)은 높을수록 알고리즘 성능이 높은 것을 알 수 있다.
※ mAP@0.5 : IoU≥0.5인 것들의 precision을 계산한 후 그 평균을 낸 것 => 0.99
※ mAP@0.5:0.9 : IoU가 0.5~0.95인 것들의 precision을 계산한 후 평균을 낸 것=> 0.68
※ IoU(Intersection over Union) : 보통 두 가지 물체의 위치(Bounding Box)가 얼마나 일치하는지를 수학적으로 나타내는 지표이다.



![image](https://user-images.githubusercontent.com/65644486/139801304-2a22ad80-690b-4eeb-974f-b5d9065c8eec.png)
그림  loss 표


loss (손실률)은 낮을수록 높은 성능을 지닌다.
※ Box loss : 예측Box의 loss => 0.022
※ Objectness loss : 예측Box가 Object일 확률 * 정답box와의 IOU값에 대한 loss=> 0.0003
※ Classification loss : 정답box가 겹치는 IOU값에 따른 Anchor Box에 대한 loss=> 0.0036

![image](https://user-images.githubusercontent.com/65644486/139801276-0bc5624c-92c8-40b0-8315-a4595ed50e72.png)
그림  yolov5 model mAP


  본 캡스톤에서는 mAP(0.5:0.95)의 값이 0.68이 나왔다. 환경이 다른걸 감안했어도 공식문서에 나와있는 44.5보다 높은 값이 나왔고 성능이 우수한 것을 확인할 수 있다. 

![image](https://user-images.githubusercontent.com/65644486/139801257-fdcea71b-6e5a-4ebf-9505-94972b6a12aa.png)
그림  실시간 카메라로 테스트 진행 화면


  실제로 N4동 6층 복도에서 테스트해본 결과이며 인식률이 60%~90% 성능을 보인다.

  중간보고 때는 객체를 잘못 인식하여 그림22와 같이 iou값이 0이 나오는 경우도 있었으나 이를 최종 보고(그림23)때 개선하였다. iou_average는 정답 값의 bounding box와 detect한 bounding box의 겹치는 비율을 뜻하고 평균적으로 정답과 약 80% 일치하는 것을 확인할 수 있었고 Detection rate는 탐지율로 정답을 맞힌 객체 수/detect를 실행한 전체 객체 수를 뜻한다. 약 95%로 높은 탐지율을 보인다. 이는 중간보고 때보다 성능이 높아진 것을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/65644486/139801177-29f7a9d3-d5b6-4476-a1fb-b5897d04db9c.png)
그림  중간보고 이미지 테스트 결과

![image](https://user-images.githubusercontent.com/65644486/139801185-f0c23fc8-57ed-4084-8cb4-cd00cc1527a0.png)
그림  이미지 테스트 결과

![image](https://user-images.githubusercontent.com/65644486/139801146-fbc94f47-84eb-4f3a-8f03-b26a2f504c99.png)
그림  colab환경에서 yolov5 inference time 비교표

![image](https://user-images.githubusercontent.com/65644486/139801138-adef81c4-0e82-4b20-bcf4-6cb31bebc738.png)
그림  한 장 detect하는데 걸린 시간 평균과 FPS

  그림24를 보면 본 프로젝트와 같은 환경(Tesla T4 GPU)에서 테스트한 inference time을 확인할 수 있다. 그림에서 yolov5m의 inference time은 20ms정도이며 실제 실행해본 결과 그림 25와 같이 inference time이 평균 14.05ms로 위 표보다 높은 성능을 보였고 목표 요구사항을 충족하였다.

2. 지도 개선

3. 인터페이스  
