#!/bin/sh
PS3='Please, select to love ovosh: ' # ������ ����������� � ����� (prompt)
echo
select vegetable in "Bobi" "Morkovj" "Kartoha" "Luk" "Briukva"
do
  echo
  echo "Yes to $vegetable."
  echo ";-))"
  echo
  break  # ���� 'break' ������, �� ��������� ����������� ����.
done
exit 0
