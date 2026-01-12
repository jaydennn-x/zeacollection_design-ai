# 🎨 AI 기반 의류 설계 시스템

의류 이미지를 도식화로 변환하고 패턴을 자동 생성하는 딥러닝 기반 시스템입니다.

## 📋 개요

이 프로젝트는 다음 과정을 자동화합니다:
1. 의류 이미지 → 도식화 변환 (에지 검출 + 벡터화)
2. 도식화 구성 요소 분석 (객체 탐지)
3. 유사 패턴 검색
4. 패턴 자동 생성 및 조정

## 🛠️ 설치

### 필수 요구사항
- Python 3.8+
- CUDA (GPU 사용 시)

### 설치 방법
```bash
# 저장소 클론
git clone https://github.com/yourusername/fashion-design-ai.git
cd fashion-design-ai

# 가상환경 생성 (권장)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 사전 학습 모델 다운로드
bash scripts/download_pretrained.sh
```

## 🚀 빠른 시작

### 1. 에지 검출만 실험해보기
```python
from src.step1_edge_detection import DexiNed

model = DexiNed()
edge_map = model.detect('examples/sample_image.jpg')
edge_map.save('output_edge.png')
```

### 2. 전체 파이프라인 실행
```python
from src.pipeline import FullPipeline

pipeline = FullPipeline()
pattern = pipeline.run('input_image.jpg')
pattern.save('output_pattern.svg')
```

### 3. 커맨드라인에서 실행
```bash
python scripts/run_inference.py \
    --image sample.jpg \
    --output results/ \
    --visualize
```

## 📚 문서

- [설치 가이드](docs/setup_guide.md)
- [아키텍처 설명](docs/architecture.md)
- [API 레퍼런스](docs/api_reference.md)
- [논문 요약](docs/paper_summary.md)

## 📊 데이터셋

### FFIED Dataset
에지 검출 학습용 데이터셋입니다.
- [다운로드 링크](https://drive.google.com/...) (추후 추가)
- 용량: 약 2GB
- 저장 위치: `data/datasets/FFIED/`

### YOLO Training Dataset
도식화 구성 요소 탐지 학습용 데이터셋입니다.
- [다운로드 링크](https://drive.google.com/...) (추후 추가)
- 용량: 약 1GB
- 저장 위치: `data/datasets/yolo/`

## 🔬 학습

### DexiNed 에지 검출 모델
```bash
python src/step1_edge_detection/train.py \
    --config config/model_config.yaml \
    --data data/datasets/FFIED/
```

### YOLOv8 객체 탐지 모델
```bash
python src/step3_component_detection/train.py \
    --config config/model_config.yaml \
    --data data/datasets/yolo/
```

## 🧪 테스트

```bash
# 전체 테스트 실행
pytest tests/

# 특정 모듈만 테스트
pytest tests/test_edge_detection.py
```

## 📁 프로젝트 구조

```
fashion-design-ai/
├── src/                    # 소스 코드
│   ├── step1_edge_detection/
│   ├── step2_vectorization/
│   ├── step3_component_detection/
│   ├── step4_similarity_search/
│   └── step5_pattern_generation/
├── data/                   # 데이터 (Git 제외)
├── models/                 # 학습된 모델 (Git 제외)
├── notebooks/              # Jupyter 노트북
├── scripts/                # 실행 스크립트
└── tests/                  # 테스트 코드
```

## 📖 참고 논문

이유정 (2025). 의류 이미지의 도식화 변환과 패턴 제작을 통합한 AI 기반 의복 설계 프로세스 개발. 서울대학교 박사학위논문.

## 📄 라이선스

MIT License

## 👥 기여

버그 리포트, 기능 제안, Pull Request 모두 환영합니다!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 연락처

프로젝트 관련 문의: your.email@example.com
