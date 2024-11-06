import pandas as pd
from django.core.management.base import BaseCommand
from your_app.models import Stage, Task, Preference

class Command(BaseCommand):
    help = "Load data from Excel sheet into Django models"

    def handle(self, *args, **kwargs):
        # Adjust the path to your actual Excel file
        df = pd.read_excel('Playable_model_development_stage.xlsx')

        for _, row in df.iterrows():
            stage, _ = Stage.objects.get_or_create(
                name=row['Stage'],
                description=row['Description'],
                start_date=row['Start Date'],
                end_date=row['End Date'],
                progress=row['Progress']
            )
            Task.objects.create(
                stage=stage,
                name=row['Task'],
                status=row['Status'],
                assigned_to=row['Assigned To'],
                due_date=row['Due Date']
            )
            Preference.objects.create(
                stage=stage,
                paper_type=row['Paper Type'],
                other_criteria=row['Other Criteria']
            )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
