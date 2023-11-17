from from_root import from_root


def save(data_frame, file_name, header):
    file_path = from_root('csv\\\\').joinpath(file_name + '.csv')
    data_frame.to_csv(file_path, sep=';', encoding='utf-8', index=False, header=header)
