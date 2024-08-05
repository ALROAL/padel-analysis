import torch

# Train functions
def train_one_epoch(model, dataloader, criterion, optimizer, metrics_evaluator, device):

    model.train()

    epoch_loss = 0
    for step, (inputs, labels) in enumerate(dataloader, 1):

        inputs = inputs.to(device, dtype=torch.float)
        labels = labels.to(device, dtype=torch.float)

        batch_outputs = model(inputs)

        loss = criterion(batch_outputs.view(-1), labels)

        model.zero_grad()
        loss.backward()
        optimizer.step()

        preds = (torch.nn.functional.sigmoid(batch_outputs).view(-1) > 0.5).to(torch.long)
        metrics_evaluator.update(preds, labels.to(torch.long))

        epoch_loss += loss.item()

    
    metrics = metrics_evaluator.compute()
    metrics = {f"train_{k}": v for k,v in metrics.items()}
    epoch_loss /= step

    output = {"train_loss": epoch_loss, **metrics}

    metrics_evaluator.reset()
    torch.cuda.empty_cache()

    return output


@torch.no_grad()
def valid_one_epoch(model, dataloader, criterion, metrics_evaluator, device):

    model.eval()

    epoch_loss = 0
    for step, (inputs, labels) in enumerate(dataloader, 1):

        inputs = inputs.to(device, dtype=torch.float)
        labels = labels.to(device, dtype=torch.float)

        batch_outputs = model(inputs)

        loss = criterion(batch_outputs.view(-1), labels)

        preds = (torch.nn.functional.sigmoid(batch_outputs).view(-1) > 0.5).to(torch.long)
        metrics_evaluator.update(preds, labels.to(torch.long))

        epoch_loss += loss.item()

    
    metrics = metrics_evaluator.compute()
    metrics = {f"val_{k}": v for k,v in metrics.items()}
    epoch_loss /= step

    output = {"val_loss": epoch_loss, **metrics}

    metrics_evaluator.reset()
    torch.cuda.empty_cache()

    return output