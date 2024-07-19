from urllib.parse import urljoin

import requests
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from NEMO.decorators import staff_member_required
from NEMO.models import MembershipHistory, Tool, ToolQualificationGroup, User, Reservation
from NEMO.views.users import get_identity_service


@require_GET
def reservation_policy(request):
    """Present a web page to show reservation policies."""
    user: User = request.user
    tools = Tool.objects.filter(visible=True).exclude(_maximum_future_reservation_time__isnull=True)
    restime = []
    for tool in tools:
        tot = 0
        reservations = Reservation.objects.filter(user=user,tool=tool,end__gt=timezone.now(),
            cancelled=False,
            missed=False,
            shortened=False,)
        for r in reservations:
            tot += int((r.end-r.start).total_seconds()/60)
        restime.append(tot)

    return render(
            request, "reservation_policy.html", {"tools": zip(list(tools),restime)}
    )
