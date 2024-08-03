from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime, timezone
from JobPortalApp.models import JobRole, Company, User, Skills
from django.contrib.auth.decorators import login_required
from JobPortalApp.forms import CompanyLoginForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def company_login(request):
    if request.method=="POST":
        email = request.POST.get("companyEmail")
        password = request.POST.get("companyPass")
        print(email, password)
        try:
            company = Company.objects.get(company_email=email)
            print(company)
            if company.company_password==password:
                request.session['company_id'] = company.company_id
                request.session['company_name'] = company.company_name
                request.session['company_email'] = company.company_email
                print("Login successful")
                return redirect("all_jobs")
            else:
                print("Wrong password")
        except:
            print("Error in login")

    return render(request, "company_login.html")

def company_register(request):
    if request.method=="POST":
        email = request.POST.get("companyEmail")
        password = request.POST.get("companyPass")
        name = request.POST.get("companyName")
        about = request.POST.get("companyAbout")
        link = request.POST.get("companyLink")

        if email!=Company.objects.filter(company_email=email).exists():
            newCompany = Company(company_email=email, company_password=password,
                                                    company_name=name, company_about=about, website_link=link)
        newCompany.save()
        return redirect("company_login")
    return render(request, "company_register.html")


def user_register(request):
    if request.method=="POST":
        email = request.POST.get("userEmail")
        password = request.POST.get("userPass")
        name = request.POST.get("userName")
        about = request.POST.get("userAbout")
        skills = request.POST.getlist("skills")
        resume = request.FILES.get("userRes")
        edu = request.POST.get("userEdu")
        uploaded_file_url = ""
        skills = ','.join(skills)
        if resume:
            fs = FileSystemStorage()
            filename = fs.save(resume.name, resume)
            uploaded_file_url = fs.url(filename)
        else:
            uploaded_file_url = None
        print(email, name, password, about, skills, edu, resume)
        
        if email!=User.objects.filter(user_email=email).exists():
            user = User(user_name=name,user_email=email,user_pass=password,user_desc=about,user_education=edu,  user_resume=uploaded_file_url, user_skills=skills)
            print(user)
            user.save()
            return redirect("user_login")
        else:
            print("User already exists")
            
    return render(request, "user_register.html")

def user_login(request):
    if request.method=='POST':
        email = request.POST.get("userEmail")
        password = request.POST.get("userPass")
        print(email, password)
        try:
            user = User.objects.get(user_email=email)
            print(user)
            if user.user_pass==password:
                request.session['user_name'] = user.user_name
                request.session['user_email'] = user.user_email
                print("Login successful")
                return redirect("display_all_jobs")
            else:
                print("Wrong password")
        except:
            print("Error in login")
        
    return render(request, "user_login.html")

def display_all_jobs(request):
    jobs = JobRole.objects.all()
    user_name = request.session.get("user_name", None)
    return render(request, "display_all_jobs.html", {'jobs': jobs, 'company_name': user_name})

def all_jobs(request):
    if 'company_id' not in request.session:
        return redirect("company_login")

    company_name = request.session.get("company_name", None)
    company_id = request.session.get("company_id", None)
    company = get_object_or_404(Company, pk=company_id)
    print("Login - ", company_name)
    jobs = JobRole.objects.filter(job_role_company=company)
    print(jobs)
    return render(request, "all_jobs.html", {'jobs': jobs, 'company_name': company_name})

def post_job(request):
    if request.method=="POST":
        role = request.POST.get("jobRole")
        # company = request.POST.get("jobCompany")
        desc = request.POST.get("jobDesc")
        location = request.POST.get("jobLocation")
        salary = request.POST.get("jobSalary")
        qualification = request.POST.get("qualification")
        skills = request.POST.get("jobSkills")
        roleType = request.POST.get("roleType")
        roleMode = request.POST.get("roleMode")
        deadline = request.POST.get("deadline")
        application_deadline = datetime.strptime(deadline, '%Y-%m-%dT%H:%M')
        company = Company.objects.get(company_name = request.POST['jobCompany'])

        newRole = JobRole(job_role_name=role, job_role_company=company, job_role_desc=desc, job_role_location=location, job_role_salary=salary, job_role_qualifications=qualification, job_role_type=roleType, job_role_mode=roleMode, job_role_skills=skills, job_role_deadline=application_deadline)
        
        newRole.save()
        return redirect("all_jobs")

    return render(request, 'post_job.html')




