import logging, requests, csv
from celery import shared_task

from farmsetu.models import Year, Region, Parameter, ParameterRegion, Weather


logger = logging.getLogger(__name__)

@shared_task(bind=True)
def insert_weather_data(self, *args, **kwargs):
    parameter_region = ParameterRegion.objects.all()

    logger.info(parameter_region)

    for parameter_region in parameter_region:
        # try:
        logger.info(f'insert_weather_data start for {parameter_region.parameter.name}')

        response = requests.get(parameter_region.url)
        content = response.content.decode('utf-8')

        lines = content.splitlines()[5:]
        content = '\n'.join(lines)

        import pandas as pd
        from io import StringIO


        TESTDATA = StringIO(content)

        df = pd.read_csv(TESTDATA, delimiter=' ', skipinitialspace=True)

        insert_data = []
        for index, row in df.iterrows():
            print(index)
            print(row)

            year, created = Year.objects.get_or_create(name=int(row['year']))

            insert_data.append(
                Weather(
                    year_id=year.id,
                    parameter_id=parameter_region.parameter.id,
                    region_id=parameter_region.region.id,
                    jan=row['jan'] if row['jan'] != '---' else 0.0,
                    feb=row['feb'],
                    mar=row['mar'],
                    apr=row['apr'],
                    may=row['may'],
                    jun=row['jun'],
                    jul=row['jul'],
                    aug=row['aug'],
                    sep=row['sep'],
                    oct=row['oct'],
                    nov=row['nov'],
                    dec=row['dec'],
                    win=row['win'] if row['win'] != '---' else 0.0,
                    spr=row['spr'],
                    sum=row['sum'],
                    aut=row['aut'],
                    ann=row['ann']
                )
            )
        Weather.objects.bulk_create(insert_data)

        print('11111')

        break

        # except Exception as e:
        #     logger.info(f'insert_weather_data error for {parameter.name} Error {str(e)}')





    # # reader = csv.reader(content.splitlines(), delimiter='\t')
    # # next(reader)  # Skip the header row
    #
    # for row in reader:
    #     data = [value if value != '---' else '0.0' for value in row[0].split()]
    #     data = [value if value else '0.0' for value in data]
    #     if data[0] != '2023':
    #         parameters.add(file_path)
    #         years.add(data[0])

