

def str2report_h(line):
    if line[-1] == '\n':
        line = line[:-1]
    number_of_tickets, total_price, seller_username = line.split("|")
    report = {
        "number_of_tickets" : number_of_tickets,
        "total_price": total_price,
        "seller_username": seller_username
    }
    return report

def report_h2str(report):
    return '|'.join([report["number_of_tickets"],  report["total_price"], report["seller_username"]])