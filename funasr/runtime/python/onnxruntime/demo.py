
from rapid_paraformer import Paraformer

model_dir = "/Users/shixian/code/funasr2/export/damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
# model_dir = "/Users/shixian/code/funasr2/export/damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch"

model = Paraformer(model_dir, batch_size=1)

wav_path = ['/Users/shixian/code/funasr2/export/damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/example/asr_example.wav']

result = model(wav_path)
print(result)