#!/usr/bin/env python
import sys
from muriki.DataProperty import *
from muriki.DataEntity import *

##Usage:
#$ ./fl_to_sqlite.py stock_prices.txt stock_prices.db
@data_entity( database_engine = Sql.Sqlite, database_name=sys.argv[2]  )
class StockDay( object ):
    def __init__( self):
        pass

    @auto_data_property( fl_start=2, fl_length=8, data_type=date
        , input_format="%Y%m%d", sql_column_type=Sql.ColumnType.PRIMARY_KEY )
    def data():
        pass

    @auto_data_property( fl_start=10, fl_length=2, data_type=int )
    def codigo_bdi():
        pass

    @auto_data_property( fl_start=12, fl_length=12, data_type=str
        , sql_column_type=Sql.ColumnType.PRIMARY_KEY)
    def codigo_negociacao_papel():
        pass

    @auto_data_property( fl_start=24, fl_length=3, data_type=int )
    def tp_mercado():
        pass

    @auto_data_property( fl_start=27, fl_length=12, data_type=str)
    def nome_res():
        pass

    @auto_data_property( fl_start=39, fl_length=10, data_type=str)
    def especi():
        pass

    @auto_data_property( fl_start=49, fl_length=3, data_type=str
        , sql_column_type=Sql.ColumnType.PRIMARY_KEY)
    def prazo_tot():
        pass

    @auto_data_property( fl_start=52, fl_length=4, data_type=str)
    def mod_ref():
        pass

    @auto_data_property( fl_start=56, fl_length=13, fraction_digits=2
        , data_type=Decimal )
    def pre_abe():
        pass

    @auto_data_property( fl_start=69, fl_length=13, fraction_digits=2
        , data_type=Decimal )
    def pre_max():
        pass

    @auto_data_property( fl_start=82, fl_length=13, fraction_digits=2
        , data_type=Decimal )
    def pre_min():
        pass

    @auto_data_property( fl_start=95, fl_length=13, fraction_digits=2
        , data_type=Decimal )
    def pre_med():
        pass

    @auto_data_property( fl_start=108, fl_length=13, fraction_digits=2
        , data_type=Decimal )
    def pre_ult():
        pass

    @auto_data_property( fl_start=121, fl_length=13, fraction_digits=2
        , data_type=Decimal )
    def pre_ofc():
        pass

    @auto_data_property( fl_start=134, fl_length=13, fraction_digits=2
        , data_type=Decimal )
    def pre_ofv():
        pass

    @auto_data_property( fl_start=147, fl_length=5, data_type=int )
    def tot_neg():
        pass

    @auto_data_property( fl_start=152, fl_length=18, data_type=int )
    def qua_tot():
        pass

    @auto_data_property( fl_start=170, fl_length=18, fraction_digits=2
        , data_type=Decimal )
    def vol_tot():
        pass

    @auto_data_property( fl_start=188, fl_length=13, fraction_digits=2
        , data_type=Decimal )
    def pre_exe():
        pass

    @auto_data_property( fl_start=201, fl_length=1, data_type=int )
    def ind_opc():
        pass

    @auto_data_property( fl_start=202, fl_length=8, data_type=date
        , input_format="%Y%m%d" )
    def dat_venc():
        pass

    @auto_data_property( fl_start=210, fl_length=7, data_type=int )
    def fat_cot():
        pass

    @auto_data_property( fl_start=217, fl_length=13, fraction_digits=6
        , data_type=Decimal )
    def pto_exe():
        pass

    @auto_data_property( fl_start=230, fl_length=12, data_type=str)
    def cod_isi():
        pass

    @auto_data_property( fl_start=242, fl_length=3, data_type=int )
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
    
    stock_days=StockDay.create_from_fl( file_name=sys.argv[1] )

    StockDay.create_table()
        
    for stock_day in stock_days:
        StockDay.insert( stock_day )
        
        
        
        
if __name__ == "__main__":
    main()
