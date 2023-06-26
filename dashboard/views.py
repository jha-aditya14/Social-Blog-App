from django.shortcuts import render

from .models import User, Blogs
from datetime import timedelta
import datetime
from datetime import datetime as dt
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.db.models import Count

def dashBoard(request, user_id):
    today = timezone.now().date()
    last_month = timezone.now() - timedelta(days=30)
    last_month_blog_count = Blogs.objects.filter(
        user_id=user_id, createdAt__gte=last_month
    ).count()
    quarter_start_date = datetime.date(today.year, ((today.month - 1) // 3) * 3 + 1, 1)
    quarter_end_date = datetime.date(today.year, ((today.month - 1) // 3) * 3 + 3, 1)
    yesterday = today - timedelta(days=1)
    user_count = User.objects.count()
    user_count_yesterday = User.objects.filter(
        date_joined__gte=yesterday, date_joined__lt=today
    ).count()
    user_count_joined = User.objects.filter(
        date_joined__gte=quarter_start_date, date_joined__lt=quarter_end_date
    ).count()
    increaseUsrFromYest = ((user_count_yesterday) / user_count) * 100
    increaseFromQuater = ((user_count_joined / user_count)) * 100
    users_logged_in_today = User.objects.filter(last_login__date=today).count()
    blog_count = Blogs.objects.filter(user_id=user_id).count()
    start_date = timezone.datetime(today.year, today.month - 2, 1).date()
    end_date = timezone.datetime(today.year, today.month - 1, 1).date() - timedelta(
        days=1
    )
    now = dt.now()
    current_month = now.month

    blog_count_current_month = Blogs.objects.filter(
        createdAt__month=current_month
    ).count()
    blog_count_lasttolastMonth = Blogs.objects.filter(
        createdAt__gte=start_date, createdAt__lte=end_date
    ).count()
    diff_count_blogs = 0
    if last_month_blog_count == 0:
        diff_count_blogs = blog_count_current_month
    else:
        diff_count_blogs = (blog_count_current_month / last_month_blog_count) * 100

    last_9_months = dt.now() - timedelta(days=270)
    blog_count_by_month = (
        Blogs.objects.filter(user_id=user_id, createdAt__gte=last_9_months)
        .annotate(month=TruncMonth("createdAt"))
        .values("month")
        .annotate(count=Count("id"))
    )
    all_months = [dt.now() - timedelta(days=30 * i) for i in range(9)]
    all_months.reverse()

    result = {}

    for month in all_months:
        key = month.strftime("%B %Y")
        result[key] = 0
        for item in blog_count_by_month:
            if item["month"].strftime("%B %Y") == key:
                result[key] = item["count"]
                break

    getBlogs = Blogs.objects.filter().order_by("createdAt").reverse()
    getUserData = User.objects.get(id=user_id)
    data = {
        "userId": user_id,
        "count": user_count,
        "countIncreaseYes": increaseUsrFromYest,
        "joined": user_count_joined,
        "countIncreaseFromQuater": increaseFromQuater,
        "UserLoginToday": users_logged_in_today,
        "blogCount": blog_count,
        "BlogPercentage": diff_count_blogs,
        "graphData": result,
        "getBlogs": getBlogs,
        "userData": getUserData,
    }

    return render(request, "dashboard.html", context=data)
