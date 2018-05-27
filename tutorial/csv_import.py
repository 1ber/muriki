#!/usr/bin/env python
import sys
from muriki.DataProperty import *
from muriki.DataEntity import *

@data_entity( database_engine = Sql.Sqlite, database_name='mlb_players.db' )
class MlbPlayer( object ):
    @auto_data_property( 
                            data_type=int
                            , sql_column_type=Sql.ColumnType.AUTO_INCREMENT
                            , white_space_behaviour=WhiteSpaceBehaviour.COLLAPSE 
                        )
    def _id():
        pass

    @auto_data_property( csv_position=0 , data_type=str,  sql_column_type=Sql.ColumnType.SIMPLE
        , white_space_behaviour=WhiteSpaceBehaviour.COLLAPSE )
    def name():
        pass

    @auto_data_property( csv_position=1 , data_type=str,  sql_column_type=Sql.ColumnType.SIMPLE 
        , white_space_behaviour=WhiteSpaceBehaviour.COLLAPSE )
    def team():
        pass

    @auto_data_property( csv_position=2 , data_type=str,  sql_column_type=Sql.ColumnType.SIMPLE 
        , white_space_behaviour=WhiteSpaceBehaviour.COLLAPSE )
    def position():
        pass


    @auto_data_property( csv_position=3 , data_type=int,  sql_column_type=Sql.ColumnType.SIMPLE 
        , white_space_behaviour=WhiteSpaceBehaviour.COLLAPSE, value_on_error=0 )
    def height():
        pass


    @auto_data_property( csv_position=4 , data_type=Decimal,  sql_column_type=Sql.ColumnType.SIMPLE
        , white_space_behaviour=WhiteSpaceBehaviour.COLLAPSE, value_on_error=0   )
    def weigth():
        pass


    @auto_data_property( csv_position=5 , data_type=Decimal,  sql_column_type=Sql.ColumnType.SIMPLE
        , white_space_behaviour=WhiteSpaceBehaviour.COLLAPSE )
    def age():
        pass


    ## TODO - Improve to get default values of properties
    def __unicode__(self):
        return str( vars( self ) )

    def __repr__(self):
        return self.__unicode__()

def main():
    #Source of the datafile: https://people.sc.fsu.edu/~jburkardt/data/csv/mlb_players.csv
    mlb_players=MlbPlayer.create_from_csv( 
        file_name='mlb_players.csv', headers=True, delimiter=',', quotechar='"' )
        
    MlbPlayer.create_table()
        
    
        
    for nr_player, mlb_player in enumerate( mlb_players ):
        #~ print( 'Inserting 'str( mlb_player) )
        MlbPlayer.insert( mlb_player )

if __name__ == "__main__":
    main()
