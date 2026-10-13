import csv
import os
from django.core.management.base import BaseCommand
from core.models import DiseaseCode


class Command(BaseCommand):
    help = '건강보험심사평가원 상병마스터 CSV 파일에서 질병 코드를 읽어와 DB에 저장합니다.'

    def handle(self, *args, **options):
        # CSV 파일명 (backend/건강보험심사평가원_상병마스터_20250930.csv)
        csv_filename = '건강보험심사평가원_상병마스터_20250930.csv'
        csv_file_path = os.path.join(csv_filename)

        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR(f'파일을 찾을 수 없습니다: {csv_file_path}'))
            return

        # 공공기관 CSV 파일 특성에 맞춰 cp949 인코딩으로 오픈
        try:
            f = open(csv_file_path, 'r', encoding='cp949')
            reader = csv.DictReader(f)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'파일 읽기 실패: {e}'))
            return

        diseases_to_create = []

        for row in reader:
            code = row.get('상병기호')
            name_ko = row.get('한글명')
            name_en = row.get('영문명')

            if code and name_ko:
                diseases_to_create.append(
                    DiseaseCode(
                        disease_code=code.strip(),
                        disease_name_ko=name_ko.strip(),
                        disease_name_en=name_en.strip() if name_en else None,
                        category=None  # 필요한 경우 별도 분류 로직 추가 가능
                    )
                )

        f.close()

        # 중복 방지 및 대량 한 번에 Insert (ignore_conflicts=True)
        DiseaseCode.objects.bulk_create(diseases_to_create, ignore_conflicts=True)

        self.stdout.write(self.style.SUCCESS(f'성공적으로 {len(diseases_to_create)}개의 상병 코드를 DB에 저장했습니다!'))