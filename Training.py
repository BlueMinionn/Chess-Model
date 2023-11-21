from tqdm.auto import tqdm
# Define your model, optimizer, loss function, and data loaders
# Number of classes for accuracy calculation (modify based on your specific model)
num_classes = ...

# Training loop
epochs = 3

for epoch in tqdm(range(epochs)):
    print(f"Epoch: {epoch}\n-------")

    train_loss = 0
    for batch, (x, y) in enumerate(data_train_loader):
        model_0.train()

        y_pred = model_0(x)
        loss_from = metric_from(y_pred[:, 0, :], y[:, 0, :])
        loss_to = metric_to(y_pred[:, 1, :], y[:, 1, :])
        loss = loss_from + loss_to
        train_loss += loss.item()  # Use .item() to get the scalar value from the loss tensor

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 400 == 0:
            print(f"Looked at {batch * len(x)}/{len(data_train_loader.dataset)} samples")
            print(f"\nTrain loss: {train_loss:.5f}")

    train_loss /= len(data_train_loader)

    test_loss, test_acc = 0, 0
    model_0.eval()
    with torch.no_grad():  # Use torch.no_grad() to disable gradient calculation during evaluation
        for X, y in data_test_loader:
            test_pred = model_0(X)
  # 1. Calculate loss (no need to accumulate as it's calculated per batch)
            loss_from = metric_from(test_pred[:, 0, :], y[:, 0, :])
            loss_to = metric_to(test_pred[:, 1, :], y[:, 1, :])
            loss = loss_from + loss_to
            test_loss += loss.item()  # Use .item() to get the scalar value from the loss tensor

            # 2. Calculate accuracy (use torch.argmax to get predicted class index)
            pred_class_from = torch.argmax(test_pred[:, 0, :], dim=1)
            true_class_from = torch.argmax(y[:, 0, :], dim=1)
            pred_class_to = torch.argmax(test_pred[:, 1, :], dim=1)
            true_class_to = torch.argmax(y[:, 1, :], dim=1)

            acc_from = torch.mean((pred_class_from == true_class_from).float())
            acc_to = torch.mean((pred_class_to == true_class_to).float())
            test_acc += (acc_from.item() + acc_to.item()) / 2  # Average accuracy for 'from' and 'to' predictions

        # Calculations on test metrics need to happen inside torch.no_grad()
        # Divide total test loss and accuracy by the length of test dataloader (per batch)
        test_loss /= len(data_test_loader)
        test_acc /= len(data_test_loader)

    ## Print out what's happening
    print(f"\nTrain loss: {train_loss:.5f} | Test loss: {test_loss:.5f}, Test acc: {test_acc * 100:.2f}%\n")

    # Additional code for saving the model, plotting the results, etc.

    print(f"\nTrain loss: {train_loss:.5f}")
