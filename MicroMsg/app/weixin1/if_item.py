def if_item(msg):
	if msg['MsgType']=='event':
			content='Welcome,my popet!   I love you,maymack'
        elif msg['Content']=='hello':
			content="1.dfjdsfjdhfjkhdsjk\n2.djfhdhsfhsdhfh\n3.dshgfhgd\n\t(1)sgfjdf\n\t(2)dhfjdhjkfh"
        else:
			content='I love maymack!'
	return content