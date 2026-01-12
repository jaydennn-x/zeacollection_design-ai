"""
간단한 에지 검출 예제

사용법:
    python examples/simple_edge_detection.py --image path/to/image.jpg
"""

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='에지 검출 간단 예제')
    parser.add_argument('--image', type=str, required=True, help='입력 이미지 경로')
    parser.add_argument('--output', type=str, default='output_edge.png', help='출력 이미지 경로')
    
    args = parser.parse_args()
    
    # TODO: 실제 구현
    print(f"입력 이미지: {args.image}")
    print(f"출력 경로: {args.output}")
    print("에지 검출 모델 로딩 중...")
    print("추론 실행 중...")
    print("완료!")

if __name__ == '__main__':
    main()
