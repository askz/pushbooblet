# -*- Coding: utf-8 -*-
import time
import schedule
from pprint import pprint
from pushbullet import Pushbullet
from weboob.core import Weboob
from weboob.capabilities.bank import CapBank


def send_push(title, text):
	pb = Pushbullet('YOUPUSHBULLETACCESSTOKEN')
	pprint('Sending push...')
	push = pb.push_note(title, text)

def get_balance():
	w = Weboob()
	backends = w.load_backends(CapBank)
	acc = next(iter(w.iter_accounts()))
	balance = float(acc.balance)
	pprint("Current balance : %0.2f E" % balance)
	return {'label':acc.label, 'balance':str(balance)}


def compute():
	b = get_balance()
	send_push("Current balance", b['label'][:15] +".. : "+ b['balance'])



compute()
schedule.every(60).minutes.do(compute)
# schedule.every(30).minutes.do(compute)

while True:
    schedule.run_pending()
    pprint("Next run in %d" % schedule.idle_seconds())
    time.sleep(1)
