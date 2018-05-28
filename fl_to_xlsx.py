#!/usr/bin/env python
import sys
import os
from muriki.DataProperty import *
from muriki.DataEntity import *
## $./fl_to_xlsx.py fixed_length.txt fixed_length.xlsx

@data_entity( )
class StockDay( object ):
    def __init__( self):
        pass

    @auto_data_property( fl_start=2, fl_length=8, data_type=date
        , input_format="%Y%m%d", sql_column_type=Sql.ColumnType.PRIMARY_KEY,
        csv_position=0 )
    def data():
        pass

    @auto_data_property( fl_start=10, fl_length=2, data_type=int
        , csv_position=1 )
    def codigo_bdi():
        pass

    @auto_data_property( fl_start=12, fl_length=12, data_type=str
        , sql_column_type=Sql.ColumnType.PRIMARY_KEY, csv_position=2 )
    def codigo_negociacao_papel():
        pass

    @auto_data_property( fl_start=24, fl_length=3, data_type=int, csv_position=3  )
    def tp_mercado():
        pass

    @auto_data_property( fl_start=27, fl_length=12, data_type=str, csv_position=4 )
    def nome_res():
        pass

    @auto_data_property( fl_start=39, fl_length=10, data_type=str, csv_position=5 )
    def especi():
        pass

    @auto_data_property( fl_start=49, fl_length=3, data_type=str
        , sql_column_type=Sql.ColumnType.PRIMARY_KEY, csv_position=6 )
    def prazo_tot():
        pass

    @auto_data_property( fl_start=52, fl_length=4, data_type=str, csv_position=7 )
    def mod_ref():
        pass

    @auto_data_property( fl_start=56, fl_length=13, fraction_digits=2
        , data_type=Decimal , csv_position=8 )
    def pre_abe():
        pass

    @auto_data_property( fl_start=69, fl_length=13, fraction_digits=2
        , data_type=Decimal , csv_position=9 )
    def pre_max():
        pass

    @auto_data_property( fl_start=82, fl_length=13, fraction_digits=2
        , data_type=Decimal , csv_position=10 )
    def pre_min():
        pass

    @auto_data_property( fl_start=95, fl_length=13, fraction_digits=2
        , data_type=Decimal , csv_position=11 )
    def pre_med():
        pass

    @auto_data_property( fl_start=108, fl_length=13, fraction_digits=2
        , data_type=Decimal , csv_position=12 )
    def pre_ult():
        pass

    @auto_data_property( fl_start=121, fl_length=13, fraction_digits=2
        , data_type=Decimal , csv_position=13 )
    def pre_ofc():
        pass

    @auto_data_property( fl_start=134, fl_length=13, fraction_digits=2
        , data_type=Decimal , csv_position=14 )
    def pre_ofv():
        pass

    @auto_data_property( fl_start=147, fl_length=5, data_type=int 
        , csv_position=15 )
    def tot_neg():
        pass

    @auto_data_property( fl_start=152, fl_length=18, data_type=int
        , csv_position=16 )
    def qua_tot():
        pass

    @auto_data_property( fl_start=170, fl_length=18, fraction_digits=2
        , data_type=Decimal 
        , csv_position=17 )
    def vol_tot():
        pass

    @auto_data_property( fl_start=188, fl_length=13, fraction_digits=2
        , data_type=Decimal , csv_position=18 )
    def pre_exe():
        pass

    @auto_data_property( fl_start=201, fl_length=1, data_type=int 
        , csv_position=19 )
    def ind_opc():
        pass

    @auto_data_property( fl_start=202, fl_length=8, data_type=date
        , input_format="%Y%m%d" , csv_position=20 )
    def dat_venc():
        pass

    @auto_data_property( fl_start=210, fl_length=7, data_type=int 
        , csv_position=21 )
    def fat_cot():
        pass

    @auto_data_property( fl_start=217, fl_length=13, fraction_digits=6
        , data_type=Decimal , csv_position=22 )
    def pto_exe():
        pass

    @auto_data_property( fl_start=230, fl_length=12, data_type=str
        , csv_position=23 )
    def cod_isi():
        pass

    @auto_data_property( fl_start=242, fl_length=3, data_type=int 
        , csv_position=24 )
    def dis_mes():
        pass

    def __unicode__(self):
        return str( vars( self ) )

    def __repr__(self):
        return self.__unicode__()

def main():
    #Source of the datafile: 
    #http://www.bmfbovespa.com.br/en_us/services/market-data/historical-data/equities/historical-data/
    #data is truncated to 1000 rows
    input_file_name = sys.argv[1] 
    output_file_name=sys.argv[2] 
    
    
    stock_days=StockDay.create_from_fl( file_name=input_file_name , fl_regex=r'^01.*$' )
    StockDay.add_csv_to_xls_file( 
        input_file_name=input_file_name, 
        output_file_name=output_file_name,
         instances=stock_days
    )
    #~ print( str( StockDay.fl_properties_names() ) )
    #~ for stock_day in stock_days:
        #~ print( str( stock_day.values() ) )
        
if __name__ == "__main__":
    main()
