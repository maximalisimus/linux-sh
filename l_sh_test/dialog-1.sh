#!/bin/bash
DIALOG=${DIALOG=dialog}

$DIALOG --title " ��� ������ ������" --clear \
        --yesno "������! ����� ���� ������ ���������,\n������������ (X)dialog" 10 40

case $? in
    0)
        echo "������� '��'.";;
    1)
        echo "������� '���'.";;
    255)
        echo "������ ������� ESC.";;
esac
exit 0
