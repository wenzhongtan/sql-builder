TABLES = [
    'f_food_metrics',
    'agg_passenger_bookings_d',
]

CATEGORY_COLUMNS = {
    'f_food_metrics' : [
        'date_id',
        'country_id',
        'reward_id'],
    
    'agg_passenger_bookings_d': [
        'passenger_id',
        'country_id',
    ]
}

METRIC_COLUMNS = {
    'f_food_metrics' : [
        'gross_merchandise_value',
        'small_order_fee',
        'convenience_fee',
        'pax_platform_fee',
        ],
    
    'agg_passenger_bookings_d': [
        'bookings_cancelled_by_driver',
        'is_new_booker_to_app',
        'is_new_promo_booker_to_app',
        'is_new_booker_to_taxi_type',
        'is_new_promo_booker_to_taxi_type',
        'is_new_rider_to_app',
        'is_new_promo_rider_to_app',
        'is_new_rider_to_taxi_type',
        'is_new_promo_rider_to_taxi_type',
    ]
}

FILTER_OPTIONS = {
    'greater or equal than': 'column_name >= value',
    'greater than': 'column_name > value',
    'equals': 'column_name = value',
    'lesser or equal than': 'column_name <= value',
    'lesser than': 'column_name < value',
    'is in a list of values': 'column_name IN (value1, value2, ...)',
    'is between': 'column_name BETWEEN value1 AND value2',
}

TEST_COLUMNS = ['1','2']
