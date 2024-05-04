from django.db.models import Avg, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from users.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from project.models import Project  

class ProjectFilter(django_filters.FilterSet):
    start_date = django_filters.DateFromToRangeFilter()
    end_date = django_filters.DateFromToRangeFilter()
    status = django_filters.ChoiceFilter(choices=Project.STATUS_CHOICES)
    priority = django_filters.RangeFilter()
    budget = django_filters.RangeFilter()
    efficiency_ratio = django_filters.RangeFilter()
    client_satisfaction = django_filters.RangeFilter()
    historical_data_link = django_filters.CharFilter(lookup_expr='icontains')
    forecast_accuracy = django_filters.RangeFilter()
    resource_overhead = django_filters.RangeFilter()
    skill_gap_notes = django_filters.CharFilter(lookup_expr='icontains')
    risk_level = django_filters.ChoiceFilter(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    risk_mitigation_measures = django_filters.CharFilter(lookup_expr='icontains')
    compliance_status = django_filters.CharFilter(lookup_expr='icontains')
    scrum_master = django_filters.CharFilter(field_name='scrum_master__name', lookup_expr='icontains')
    product_owner = django_filters.CharFilter(field_name='product_owner__name', lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['name', 'description', 'status', 'priority', 'scrum_master', 'product_owner']  

class DashboardAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get(self, request):
        filtered_projects = self.filterset_class(request.GET, queryset=Project.objects.all()).qs
        
        data = {
            'total_projects': filtered_projects.count(),
            'ongoing_projects': filtered_projects.filter(status='ongoing').count(),
            'completed_projects': filtered_projects.filter(status='completed').count(),
            'on_hold_projects': filtered_projects.filter(status='on_hold').count(),
            'average_budget': filtered_projects.aggregate(Avg('budget'))['budget__avg'] or 0,
            'total_budget': filtered_projects.aggregate(Sum('budget'))['budget__sum'] or 0,
            'average_efficiency': filtered_projects.aggregate(Avg('efficiency_ratio'))['efficiency_ratio__avg'] or 0,
            'total_efficiency': filtered_projects.aggregate(Sum('efficiency_ratio'))['efficiency_ratio__sum'] or 0,
            'average_client_satisfaction': filtered_projects.aggregate(Avg('client_satisfaction'))['client_satisfaction__avg'] or 0,
            'project_details': list(filtered_projects.values(
                'name', 'description', 'start_date', 'end_date', 'status',
                'priority', 'budget', 'efficiency_ratio', 'client_satisfaction',
                'historical_data_link', 'forecast_accuracy', 'resource_overhead',
                'skill_gap_notes', 'risk_level', 'risk_mitigation_measures',
                'decision_impact_analysis', 'compliance_status', 'scrum_master__name', 'product_owner__name'
            )),
        }

        return Response(data)
