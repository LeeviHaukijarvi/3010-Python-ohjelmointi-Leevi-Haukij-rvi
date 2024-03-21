def on_ananasta(täytteet):
    if täytteet is None:
        return False

    täytteiden_määrä = len(täytteet)

    if täytteiden_määrä == 0:
        return False
    else :
        for i in täytteet:
            if i == 'ananas':
                return True
        return False
