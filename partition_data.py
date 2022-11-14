import os
import numpy as np
import shutil


def convert_to_list(train_files, val_files, test_files, format):
    """provide an array of files as input, returns list of files as output"""
    train_files = [file + format for file in train_files.tolist()]
    val_files = [file + format for file in val_files.tolist()]
    test_files = [file + format for file in test_files.tolist()]
    return train_files, val_files, test_files


def store_list_in_text_files(file_array, text_file):
    """stores the list of files in a text"""
    with open(text_file, "w") as f:
        for file in file_array:
            f.write(file)
            f.write('\n')


def store_dataset(files,src_path, dest_path):
    """data partitioning"""
    for file in files:
        final_src_path = src_path + '/' + file
        final_dest_path = dest_path + '/' + file
        shutil.copy(final_src_path, final_dest_path)


if __name__ == '__main__':
    images_path = r'PAN'
    xml_path = r'xml'
    dest_image_path_list = [ r'train_images', r'val_images', r'test_images']
    dest_xml_path_list = [r'train_xml', r'val_xml', r'test_xml']
    text_files_list = ['train.txt', 'val.txt', 'test.txt']
    files = []
    for xml_files in os.listdir(xml_path):
        xml_file = xml_files.split('.xml')[0]
        files.append(xml_file)

    train_ratio = 0.71
    val_ratio = 0.86

    np.random.shuffle(files)
    train_files, val_files, test_files = np.split(np.array(files), [int(len(files) * train_ratio), int(len(files) * val_ratio)]) #60% train, 20% val and 20% test
    files_list = [train_files, val_files, test_files]
    for file_array, text_file in zip(files_list, text_files_list):
        store_list_in_text_files(file_array, text_file)
    image_train_files, image_val_files, image_test_files = convert_to_list(train_files, val_files, test_files, format = '.jpg')
    xml_train_files, xml_val_files, xml_test_files = convert_to_list(train_files, val_files, test_files, format = '.xml')

    image_dataset_files = [image_train_files, image_val_files, image_test_files]
    xml_dataset_files = [xml_train_files, xml_val_files, xml_test_files]
    for dataset_file, dest_path in zip(image_dataset_files, dest_image_path_list):
        store_dataset(dataset_file, images_path, dest_path)
    for dataset_file, dest_path in zip(xml_dataset_files, dest_xml_path_list):
        store_dataset(dataset_file, xml_path, dest_path)



