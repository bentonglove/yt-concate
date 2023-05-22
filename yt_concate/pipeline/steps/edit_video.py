from yt_concate.pipeline.steps.step import Step
from moviepy.editor import VideoFileClip, concatenate_videoclips
from yt_concate.logger import logger


class EditVideo(Step):

    def process(self, data, inputs, utils):
        logger.info("Edit videos ......")
        logger.info(data)
        # data is a found list which has the video filepath needed to be merged
        # https://zulko.github.io/moviepy/
        video_clips = []
        for found in data:
            logger.info(f"work for {found} now ... ")
            start, end = self.parse_caption_time(found.time)
            video_clips.append(VideoFileClip(found.yt.video_filepath).subclip(start, end))
            if len(video_clips) >= inputs['limit']:
                break
        final_clip = concatenate_videoclips(video_clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        # output_filepath = inputs['channel_id'] + inputs['search_word'] + '.mp4'
        logger.info(output_filepath)
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time: str) -> tuple:
        start_str, end_str = caption_time.split(" --> ")
        return self.parse_time_str(start_str), self.parse_time_str(end_str)

    def parse_time_str(self, time_str: str):
        hh, mm, ss = time_str.split(":")
        return int(hh), int(mm), float(ss.replace(',', '.'))
