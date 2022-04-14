#include <QCoreApplication>
#include <QByteArray>
#include <QBitArray>
#include <QString>
#include <QDebug>
#include <iostream>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);


    QString src = "© Mikl Artamonov"; // wqkgTWlrbCBBcnRhbW9ub3Y=
    QByteArray encode = src.toUtf8().toBase64();
    QString coded = QString(encode);
    std::cout << coded.toStdString() << std::endl;
    
    QByteArray data = QByteArray::fromBase64(coded.toUtf8());
    QString decode = QString(data);
    std::cout << decode.toStdString() << std::endl;
    
    return a.exec();
}
