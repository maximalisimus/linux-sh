#!/bin/sh
PS3='Please, select to love ovosh: '
echo
choice_of()
{
select vegetable
# ������ ������ [in list] �����������, ������� 'select' ���������� ������� ��������� �������.
do
  echo
  echo "Yes to $vegetable."
  echo ";-))"
  echo
  break
done
}
choice_of Bobi Ris Morkovj Redis Tomat Shpinat
#         $1   $2  $3      $4    $5    $6
#         �������� ������ ������ � ������� choice_of()
exit 0
