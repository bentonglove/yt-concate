import os
import time

from .step import Step
from vtt_to_srt.vtt_to_srt import ConvertFile
from yt_concate.settings import CAPTIONS_DIR, VTT_DIR
from yt_concate.logger import logger


class Convert2Srt(Step):

    def process(self, data, inputs, utils):
        logger.info("convert srt ............")

        vtt_files = []

        # Measure the execution time of a line of code
        start_time = time.time()
        # 取得當前目錄下所有檔案
        for file in os.listdir(VTT_DIR):
            if self.is_caption_file_exist(file):
                continue
            # 如果是 vtt 檔案就加入 vtt_files 並且轉成 srt
            if os.path.splitext(file)[1] == '.vtt':
                vtt_files.append(file)
                logger.info("Converting ....................")
                file_path = os.path.join(VTT_DIR, file)
                convert_file = ConvertFile(file_path, "utf-8")

                # considering multi-processing here
                convert_file.convert()
                # 緊接著做第二次轉換，把不必要的"行"移除
                converted_file_name = os.path.splitext(file)[0] + '.srt'
                f_source = os.path.join(VTT_DIR, converted_file_name)
                f_dest = os.path.join(CAPTIONS_DIR, converted_file_name)

                logger.info("Optimizing and moving ...........")
                self.optimize_srt(f_source, f_dest)

        # 轉換完畢
        elapsed_time = time.time() - start_time
        logger.debug(f"The elapsed time is {elapsed_time}")
        logger.info(f"Total {len(vtt_files)} files had been converted")
        return data

    def optimize_srt(self, source, dest):
        with open(source, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = []
        unit_index = 0

        for i in range(0, len(lines), 5):

            try:
                line1, line2, line3, line4, line5 = lines[i:i + 5]
            except ValueError:
                continue

            if line5.strip() == '':
                # 如果第五行是空的，就整段字幕移掉
                continue

            # 重新修訂順序編號
            unit_index += 1
            new_line2 = str(unit_index) + '\n'
            new_lines.extend([line1, new_line2, line3, line5])

        # 寫入新檔案
        with open(dest, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    def is_caption_file_exist(self, filename):
        filepath = os.path.join(CAPTIONS_DIR, filename.split('.')[0]+'.en.srt')
        return os.path.exists(filepath)


# if __name__ == '__main__':
