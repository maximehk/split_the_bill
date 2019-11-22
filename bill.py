import collections
import dataclasses
import io


@dataclasses.dataclass
class Item(object):
    qty: int
    label: str
    price: float


def _parse_bill_line(line):
    qty, label, price, payees = line.split()
    return Item(int(qty), label, float(price)), collections.Counter(payees)


class Bill(object):
    def __init__(self, text):
        self.people = {}  # 1 letter key / label
        self.items_per_person = collections.defaultdict(list)  # 1 letter key / [(qty, item), ...]
        self._parse(io.StringIO(text))

    def _parse(self, stream):
        lines = (line.strip() for line in stream if line.strip()!='')
        names = next(lines).split()
        self.people = {name[0]: name for name in names}
        entries = (_parse_bill_line(line) for line in lines)
        for item, payees in entries:
            total_shares = sum(payees.values())
            for k, shares in payees.items():
                self.items_per_person[k].append((shares/total_shares*item.qty, item))

    def __repr__(self):
        buf = io.StringIO()
        grand_total = 0 
        for k, name in self.people.items():
            buf.write(f'\n# {name.capitalize()}\n')
            total = 0
            for qty, item in self.items_per_person[k]:
                price = qty * item.price
                total += price
                buf.write(f'{qty:.2f} {item.label} {price:.2f}\n')
            buf.write(f'Total = {total:.2f}\n')
            grand_total += total
        buf.write(f'\n# Grand total = {grand_total:.2f}\n')
        return buf.getvalue()


if __name__ == '__main__':

    bill = Bill('''
    kerry hack litv
    7 stange 4.50 hllkkkk
    2 soave_1dl 5.80 hl
    3 genovese 17.8 hhk
    1 gnocchi 17 l
    1 hofli 17.8 l
    1 pizza_carpaccio 24.8 k
    1 pizza_tonnato 19.8 k
    1 pizza_kids 10.8 hkl
    ''')

    print(bill)
            

