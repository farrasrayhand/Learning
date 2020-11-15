#include <iostream>
#include <windows.h>

using namespace std;

int main()
{

    cout << "Daftar Menu" << endl;
    cout << "Kopi  = Rp. 6000" << endl;
    cout << "Teh   = Rp. 3000" << endl;
    cout << "Jeruk = Rp. 5000" << endl << endl;
    a:
    char pesan_kopi;
    int jumlah_kopi = 0;
    int kopi = 6000;
    cout << "Apakah anda ingin memesan Kopi ? y/n :";
    cin >> pesan_kopi;
    switch (pesan_kopi)
    {
        case 'y':
        cout << "Mau pesan berapa ? ";
        cin >> jumlah_kopi;
        cout << "Anda memesan " << jumlah_kopi;
        cout << " Kopi, Total Harga adalah = Rp." << kopi*jumlah_kopi<<endl;
        break;

        case 'n':
        goto b;

        default :
            system("cls");
            cout << "Hanya menerima masukan y/n Pesanan Kopi direset :";
            cout << endl<<endl;
            goto a;

    }

    b:
    char pesan_teh;
    int jumlah_teh = 0;
    int teh = 3000;
    cout << "Apakah anda ingin memesan Teh ? y/n :";
    cin >> pesan_teh;
    switch (pesan_teh)
    {
        case 'y':
        cout << "Mau pesan berapa ? ";
        cin >> jumlah_teh;
        cout << "Anda memesan " << jumlah_teh;
        cout << " Teh, Total Harga adalah = Rp." << teh*jumlah_teh<<endl;
        break;

        case 'n':
        goto c;

        default :
            system("cls");
            cout << "Hanya menerima masukan y/n Pesanan Teh direset";
            cout << endl<<endl;
            goto b;
    }
        c:
    char pesan_jeruk;
    int jumlah_jeruk = 0;
    int jeruk = 5000;
    cout << "Apakah anda ingin memesan Jeruk ? y/n :";
    cin >> pesan_jeruk;
    switch (pesan_jeruk)
    {
        case 'y':
        cout << "Mau pesan berapa ? ";
        cin >> jumlah_jeruk;
        cout << "Anda memesan " << jumlah_jeruk;
        cout << " Jeruk, Total Harga adalah = Rp." << jeruk*jumlah_jeruk<<endl;
        break;

        case 'n':
        system("cls");
        goto g;

        default :
            system("cls");
            cout << "Hanya menerima masukan y/n Pesanan Jeruk direset";
            cout << endl<<endl;
            goto c;
    }
        g:
            int total = (kopi*jumlah_kopi + teh*jumlah_teh + jeruk*jumlah_jeruk);
            cout << "Jumlah pesanan anda adalah :"<<endl;
            cout << "Kopi   = " <<jumlah_kopi;cout << " Total = Rp."<<kopi*jumlah_kopi<< endl;
            cout << "Teh    = " <<jumlah_teh;cout << " Total = Rp."<<teh*jumlah_teh<< endl;
            cout << "Jeruk  = " <<jumlah_jeruk;cout << " Total = Rp."<<jeruk*jumlah_jeruk<< endl;
            cout << "Total  = Rp."<<total<<endl<<endl;
            goto d;
        d:
            char voucher;
            cout << "Mau cek promo ? y/n : ";
            cin >> voucher;
            switch (voucher)
            {
            case 'y':
                system("cls");
                goto f;
                break;

            case 'n':
                goto e;
            }

        e:
            system("cls");
            cout << "Jumlah pesanan anda adalah :"<<endl;
            cout << "Kopi   = " <<jumlah_kopi;cout << " Total = Rp."<<kopi*jumlah_kopi<< endl;
            cout << "Teh    = " <<jumlah_teh;cout << " Total = Rp."<<teh*jumlah_teh<< endl;
            cout << "Jeruk  = " <<jumlah_jeruk;cout << " Total = Rp."<<jeruk*jumlah_jeruk<< endl;
            cout << "Total  = Rp."<<total<<endl<<endl;
            cout << "Terima Kasih Sudah berbelanja"<<endl<<endl;
            return 0;


        f:
        int diskon;
        int diskon1 = 0.05 * total;
        int diskon2 = 0.09 * total;
        int diskon3 = 0.13 * total;
                cout << "1. Diskon 5% jika belanja di atas Rp. 25000" <<endl;
                cout << "2. Diskon 9% jika belanja di atas Rp.49000" <<endl;
                cout << "3. Diskon 13% jika belanja di atas Rp.72000" <<endl;
                cout << "Silahkan pilih nomor voucher yang tersedia : ";
                cin >> diskon;
                cout <<endl<<endl;
                switch (diskon){
            case 1:
                if (total >= 25000){
                cout << "Selamat anda mendapatkan diskon sebesar 5%, Jumlah pesanan anda adalah :"<<endl;
                cout << "Kopi   = " <<jumlah_kopi;cout << " Total = Rp."<<kopi*jumlah_kopi<< endl;
                cout << "Teh    = " <<jumlah_teh;cout << " Total = Rp."<<teh*jumlah_teh<< endl;
                cout << "Jeruk  = " <<jumlah_jeruk;cout << " Total = Rp."<<jeruk*jumlah_jeruk<< endl<<endl;
                cout << "Total  = Rp." << total;cout << " diskon Menjadi = Rp." << total - diskon1<< endl<<endl;
                }else {
                system("cls");
                cout << "Total belanja anda tidak memenuhi syarat silahkan cek kembali"<<endl;
                goto g;
                }
                break;

            case 2:
                if (total >= 49000){
                cout << "Selamat anda mendapatkan diskon sebesar 9%, Jumlah pesanan anda adalah :"<<endl;
                cout << "Kopi   = " <<jumlah_kopi;cout << " Total = Rp."<<kopi*jumlah_kopi<< endl;
                cout << "Teh    = " <<jumlah_teh;cout << " Total = Rp."<<teh*jumlah_teh<< endl;
                cout << "Jeruk  = " <<jumlah_jeruk;cout << " Total = Rp."<<jeruk*jumlah_jeruk<< endl<<endl;
                cout << "Total  = Rp." << total;cout << " diskon Menjadi = Rp." << total - diskon2<< endl<<endl;
                }else {
                system("cls");
                cout << "Total belanja anda tidak memenuhi syarat silahkan cek kembali"<<endl;
                goto g;
                }
                break;

            case 3:
                if (total >= 49000){
                cout << "Selamat anda mendapatkan diskon sebesar 13%, Jumlah pesanan anda adalah :"<<endl;
                cout << "Kopi   = " <<jumlah_kopi;cout << " Total = Rp."<<kopi*jumlah_kopi<< endl;
                cout << "Teh    = " <<jumlah_teh;cout << " Total = Rp."<<teh*jumlah_teh<< endl;
                cout << "Jeruk  = " <<jumlah_jeruk;cout << " Total = Rp."<<jeruk*jumlah_jeruk<< endl<<endl;
                cout << "Total  = Rp." << total;cout << " diskon Menjadi = Rp." << total - diskon3<< endl<<endl;
                }else {
                system("cls");
                cout << "Total belanja anda tidak memenuhi syarat silahkan cek kembali"<<endl;
                goto g;
                }
                break;

            default:
                system("cls");
                cout << "Promo tersebut tidak ada"<<endl;
                goto d;
                break;
                }

    return 0;
    }
