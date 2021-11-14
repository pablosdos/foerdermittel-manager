import json
import logging
from django.db.models import query
from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt

from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from funding.models.funding import FundingPlace
from rest_framework.viewsets import ModelViewSet
from funding.models import FundingProgramm, FundingArea, ContactMessage
from .serializers import FundingProgramSerializer


logger = logging.getLogger(__name__)


class FundingProgrammViewSets(ModelViewSet):

    serializer_class = FundingProgramSerializer

    def get_queryset(self):
        queryset = FundingProgramm.objects.all()
        funding_area = self.request.query_params.get('area')
        funding_region = self.request.query_params.get('region')
        if funding_area:
            queryset = queryset.filter(
                area__name=funding_area)
        if funding_region:
            queryset = queryset.filter(region=funding_region)
        return queryset


@csrf_exempt
def import_funding_projects(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    file = request.FILES['file']
    if file.name != 'projects.json':
        return HttpResponseBadRequest('The provided file must be called projects.json')

    projects = json.load(file)

    logger.info("Valid file, now the processing will begin")

    for project in projects:
        funding_program, is_created = FundingProgramm.objects.get_or_create(
            url=project['url'], )
        if is_created:
            funding_program.name = project['title']
            funding_program.description = project['description']
            funding_program.type = project['type']

            # Adds areas to project
            for area in project['area']:
                funding_area = FundingArea.objects.get(name=area)
                funding_program.area.add(funding_area)

            funding_program.region = project['funding_region']

            funding_program.save()

    return HttpResponse(f"{projects}", status=201)

@csrf_exempt
def process_contact_messsage(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST'])
    
    message_dict = json.loads(request.body)
    email = get_user_model().objects.normalize_email(message_dict['email'])
    message = message_dict['message']
    first_name = message_dict['firstName']
    last_name = message_dict['lastName']
    
    response_message = ContactMessage.objects.create(first_name=first_name, last_name=last_name, message=message, email=email)
    
    return HttpResponse(response_message)