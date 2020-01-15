def get_preferences(file_name):
    '''Takes a test file (in prescribed format)
    returns two lists of preferences:
    applicant_pref, employer_pref.
    Each preferences list has length n+1,
    where n is the number of applicants/jobs
    index 0 is a dummy entry; to simplify indices.
    for a in 1,...,n, applicant pref[a][r] gives the
    employer ranked r in applicant a's preferences.
    Similarly for employer_pref.'''

    f = open(file_name, "r")
    all_prefs = [x.split() for x in f.readlines()]

    applicant_prefs = ["applicant preferences"]
    i = 0
    while all_prefs[i]:
        applicant_prefs.append([int(x) for x in all_prefs[i]])
        i += 1
    i += 1
    employer_prefs = ["employer preferences"]
    while i < len(all_prefs):
        employer_prefs.append([int(x) for x in all_prefs[i]])
        i += 1
    return applicant_prefs, employer_prefs

def get_rankings(preferences):
    '''takes a the applicant's preference list
    returns a dictionary, can look up rank of job j
    in applicant a's preference list.
    if applicant a has job j ranked r (r can be
    0,...,n-1, 0 the top choice), then
    ranking[str(a) + ',' + str(j)] gets r.'''

    applicant = 1
    rankings = {}
    while applicant < len(preferences):
        rank = 0
        while rank < len(preferences[applicant]):
            rankings[str(applicant) + ',' + str(preferences[applicant][rank])] = rank
            rank += 1
        applicant += 1
    return rankings

def display_matches(current_job):
    '''takes the list of current jobs for applicants,
    and prints the matches.'''

    i = 1
    while i < len(current_job):
        print(str(i) + ":" + str(current_job[i]))
        i = i+1

applicant_prefs, employer_prefs = get_preferences("test1.txt")
rankings = get_rankings(applicant_prefs)

#n is the number of jobs/applicants
n = len(applicant_prefs) - 1

#open jobs starts as a list of all jobs: [1,...,n]
#use open_jobs.pop() to get an open job in constant time.
open_jobs = list(range(1, n+1))

#current_job[a] gives the current job of applicant a. If applicant a does not have a job yet, current_job[a] is -1.
#Since all applicants are unemployed at the beginning, these all start at -1.
#current_job[0] will never be used - it's there to simplify indexing.
current_job = [-1 for applicant in applicant_prefs]


 #while job is open pick an apllicant to fill in job

while open_jobs:
	employer = open_jobs.pop() # each employer takes an open job from the list
	applicant = employer_prefs[employer].pop() # the applicant is assigned (hired) the job from the employer
	if current_job[applicant] == -1: # if applicant does not have a job, they accept job offer
		current_job[applicant] = employer
	else:
		# else if applicant already has a job then they see if they like new job better then their old job
		if rankings[str(applicant) + "," + str(current_job[applicant])] < rankings[str(applicant) + "," + str(employer)]: 
			open_jobs.append(current_job[applicant]) #appliacnt takes the new job     
			current_job[applicant] = employer # the applicant is hired by new employer
		else:
			open_jobs.append(employer) # appliacant declines and employer still has an open job

#display jobs at the end
display_matches(current_job)
