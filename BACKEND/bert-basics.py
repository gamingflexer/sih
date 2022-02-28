#save
import torch
torch.save(
    {
        "epoch": epochs,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
    },
    'path/model_le.tar',
)


#loading
MAX_LEN = 512
DEVICE = torch.device("cpu")
MODEL_PATH = 'bert-large-uncased'
STATE_DICT = torch.load(
    'C:\\WindowServer\\Flask-app\\v.1.0\\DeepBlue\\flask\\models\\model_e10.tar', map_location=DEVICE)
TOKENIZER = BertTokenizerFast.from_pretrained(MODEL_PATH, lowercase=True)
MODEL = BertForTokenClassification.from_pretrained(
    MODEL_PATH, state_dict=STATE_DICT['model_state_dict'], num_labels=12)

#predict
