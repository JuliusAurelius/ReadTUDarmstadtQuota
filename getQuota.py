# Pulls the current quota from the internet

import pandas as pd


def get_data():
    try:
        tables = pd.read_html("http://volumen.hrz.tu-darmstadt.de/acct-v4/myTraffic.php#myTraffic")
    except:
        return -1

    vals = tables[0].values

    ip_num = vals[0, 0]
    data_max = vals[0, 11]
    data_in = vals[0, 3]
    data_out = vals[0, 4]

    # Convert string into usable number
    # Data in
    if data_in[len(data_in) - 2:] == 'GB':
        data_in_num = float(data_in[:-3]) * 1000
    elif data_in[len(data_in) - 2:] == 'KB':
        data_in_num = float(data_in[:-3]) * 0.001
    else:
        data_in_num = float(data_in[:-3])

    # Data out
    if data_out[len(data_out) - 2:] == 'GB':
        data_out_num = float(data_out[:-3]) * 1000
    elif data_out[len(data_out) - 2:] == 'KB':
        data_out_num = float(data_out[:-3]) * 0.001
    else:
        data_out_num = float(data_out[:-3])

    # Data Maximum
    if data_max[len(data_max) - 2:] == 'GB':
        data_max_num = float(data_max[:-3]) * 1000
    elif data_max[len(data_out) - 2:] == 'KB':
        data_max_num = float(data_max[:-3]) * 0.001
    else:
        data_max_num = float(data_max[:-3])

    # Data total
    data_total_num = data_out_num + data_in_num

    results = []
    results.extend([data_in_num, data_out_num, data_total_num, data_max_num])
    return results


if __name__ == '__main__':
    res = get_data()
    if res == -1:
        print('No value could be read')
    else:
        print('In    (in MB): ', res[0])
        print('Out   (in MB): ', res[1])
        print('Total (in MB): ', res[2])
        print('Limit (in MB): ', res[3])
