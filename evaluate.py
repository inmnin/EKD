import torch


# Validation on a test set
def evaluate(model, val_dataloader, device):
    model.eval()
    val_accuracy = 0
    with torch.no_grad():
        for batch in val_dataloader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            #Don't get hidden status
            outputs = model(input_ids=input_ids, attention_mask=attention_mask,output_hidden_states=False)
            logits = outputs.logits
            preds = torch.argmax(logits, dim=1)
            val_accuracy += (preds == labels).sum().item()

    val_accuracy /= len(val_dataloader.dataset)
    print(f"Validation Accuracy: {val_accuracy*100:.3f}%")
    return val_accuracy
