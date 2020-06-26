import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kdhi.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from trackers.models import inter_korean_tracker, inter_korean_category, inter_korean_subcategory, inter_korean_level
from main_site.models import rok_individual, individual
import csv
import string

unslugable_characters = ['.', ',', '/', '?', ';', ':', '"', "'", '|', '/', '\\', '#', '@', '$', '%', '^', '&', '*', '(', ')', '~', '`', ]
rok = 'rok'
dprk = 'dprk'

def slugify(raw_text):
	raw_text =  raw_text.lower()
	slug_temp = ''
	for character in raw_text:
		if character.isalpha() == True or character == ' ' or character.isdigit():
			slug_temp += character
	slug = slug_temp.replace(' ', '-')
	return(slug)

def lookup_or_create_rok(self_slug):
	self_slug = self_slug.lower()
	self_slug = self_slug.replace(" ", "-")
	try:
		self_object = rok_individual.objects.get(name_slug=self_slug)
		print("Individual found")

	except:
		self_name_list = self_slug.split("-")
		character_count = 0
		for name_character in self_name_list:
			if character_count == 0:
				self_name = name_character
			elif character_count == 1:
				self_name += " " + name_character
			elif character_count ==2:
				self_name += "-" + name_character
			character_count += 1
		self_name = string.capwords(self_name) 
		self_object = rok_individual(name_slug=self_slug, name=self_name)
		self_object.save()
		print("Individual created")
	return(self_object)


def lookup_or_create_dprk(self_slug):
	self_name_lower = self_slug.replace("-", " ")
	self_name = string.capwords(self_name_lower)
	try:
		self_object = individual.objects.get(name=self_name)
		print("Individual found")

	except:
		self_object = individual(name=self_name)
		print("Individual created")
		self_object.save()
	return(self_object)



def check_veriable(input_variable):
	if len(input_variable) > 0:
		variable_defined = True
	else:
		variable_defined = False
	return(variable_defined)

def listify_delegation(input_variable):
	delegate_list = []
	initial_list = input_variable.split(";")
	for delegate in initial_list:
		delegate = delegate.replace(" ", "")
		delegate_list.append(delegate)
	return(delegate_list)


row_count = 0
base_dir = 'C:/Users/Sam/Documents/GitHub/kdhi_migration/kdhi'
file_name = 'ik_events_ross.csv'
file_location_true = base_dir + '/' + file_name
with open(file_location_true, newline='', encoding='utf-8') as csvfile:
	tracker_sheet = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in tracker_sheet:
		if row_count == 0:
			#row_count = 1  
			# Enable the row_count line to limit import to a single item
			title					= row[0] 
			category				= row[1] 
			subcategory_1			= row[2] 
			subcategory_2 			= row[3] 
			subcategory_3 			= row[4] 
			itteration				= row[5] 
			rok_delegation_head 	= row[6] 
			rok_delegation 			= row[7] 
			dprk_delegation_head 	= row[8] 
			dprk_delegation 		= row[9] 
			level					= row[10] 
			date_start				= row[11] 
			date_end				= row[12] 
			host 					= row[13] 
			location 				= row[14] 
			venue 					= row[15] 
			media_coverage 			= row[16] 
			document_name 			= row[17] 
			document_file 			= row[18] 
			icon_photo 				= row[19] 
			photo_credit 			= row[20] 
			description 			= row[21] 

			if itteration == "None":
				itteration = "0"
			if description == "None":
				description = "No event description available."
			slug_title = slugify(title)
			#------- Create Delegation Lists --------
			listified_rok = listify_delegation(rok_delegation)
			listified_dprk = listify_delegation(dprk_delegation)
			delegate_object_list_rok = []
			delegate_object_list_dprk = []
			#------- Check for Individual ----------
			rok_delegation_head_object = lookup_or_create_rok(rok_delegation_head)
			dprk_delegation_head_object = lookup_or_create_dprk(dprk_delegation_head)
			
			for delegate in listified_rok:
				delegate_object = lookup_or_create_rok(delegate)
				delegate_object_list_rok.append(delegate_object)

			for delegate in listified_dprk:
				delegate_object = lookup_or_create_dprk(delegate)
				delegate_object_list_dprk.append(delegate_object)

			#------- Check Level -------
			if check_veriable(level) == True:
				try:
					level_object = inter_korean_level.objects.get(name=level)
				except:
					level_object = inter_korean_level(name=level)
					level_object.save()	

			#------- Check Category -------
			if check_veriable(category) == True:
				try:
					category_object = inter_korean_category.objects.get(name=category)
				except:
					category_object = inter_korean_category(name=category)
					category_object.save()	

			#------- Check Subcategories -------
			subcategory_list_raw = [subcategory_1, subcategory_2, subcategory_3]
			subcategory_objects_list = []
			for sub_category in subcategory_list_raw:
				if check_veriable(sub_category) == True:
					try:
						subcategory_object = inter_korean_subcategory.objects.get(name=sub_category)
					except:
						subcategory_object = inter_korean_subcategory(name=sub_category)
						subcategory_object.save()
					subcategory_objects_list.append(subcategory_object)	
				

			try: 
				ik_tracker_item = inter_korean_tracker.objects.get(name=title)
				print("Event with title {} already exists?".format(title))
			except:
				pass
			if date_start == "None":
				ik_tracker_item = inter_korean_tracker(
				    name                = title,
				    slug                = slug_title,
				    event_category      = category_object,
					event_level         = level_object,
				    ROK_head            = rok_delegation_head_object,
				    DPRK_head           = dprk_delegation_head_object,
				    MOU_description     = description,
				    event_location      = level,
				    event_venue         = venue,
				    event_itteration	= itteration,
				    document_link       = document_file,
				    document_name       = document_name,
				    event_photo         = icon_photo,
				    event_photo_credit  = photo_credit,
					)
					

				ik_tracker_item.save()
				for subcategory in subcategory_objects_list:
					ik_tracker_item.event_subcategory.add(subcategory)

				for delegate in delegate_object_list_rok:
					ik_tracker_item.participant_ROK.add(delegate)

				for delegate in delegate_object_list_dprk:
					ik_tracker_item.participant_DPRK.add(delegate)
			else:
				ik_tracker_item = inter_korean_tracker(
				    name                = title,
				    slug                = slug_title,
				    event_category      = category_object,
					event_level         = level_object,
				    ROK_head            = rok_delegation_head_object,
				    DPRK_head           = dprk_delegation_head_object,
				    MOU_description     = description,
				    event_location      = level,
				    event_venue         = venue,
				    event_itteration	= itteration,
				    event_date          = date_start,
				    document_link       = document_file,
				    document_name       = document_name,
				    event_photo         = icon_photo,
				    event_photo_credit  = photo_credit,
					)
					

				ik_tracker_item.save()
				for subcategory in subcategory_objects_list:
					ik_tracker_item.event_subcategory.add(subcategory)

				for delegate in delegate_object_list_rok:
					ik_tracker_item.participant_ROK.add(delegate)

				for delegate in delegate_object_list_dprk:
					ik_tracker_item.participant_DPRK.add(delegate)

		#------- Check for Empty Columns ----------


'''
print(title)				
print(category)
print(subcategory_1)
print(subcategory_2)
print(subcategory_3)
print(itteration)
print(rok_delegation_head)
print(rok_delegation)
print(dprk_delegation)
print(dprk_delegation_head)
print(level)
print(date_start	)
print(date_end)
print(host)
print(location)
print(venue)
print(media_coverage)
print(document_name)
print(document_file )
print(icon_photo)
print(photo_credit)
print(description)
    name                = models.CharField(max_length=500)
    slug                = models.CharField(max_length=500, blank=True)
    ROK_head            = models.ForeignKey(rok_individual, on_delete=models.PROTECT, related_name = 'rok_head', null=True, blank=True)
    DPRK_head           = models.ForeignKey(individual, on_delete=models.PROTECT, related_name = 'dprk_head', null=True, blank=True)
    participant_ROK     = models.ManyToManyField(rok_individual, related_name = 'rok_delegation', blank=True, default="Kim Jong Un")
    participant_DPRK    = models.ManyToManyField(individual, related_name = 'dprk_delegation', blank=True)
    meeting_topics      = models.ManyToManyField(overseas_topic, blank=True)
    MOU_description     = models.TextField(max_length=20000)
    event_location      = models.CharField(max_length=200)
    event_venue         = models.CharField(max_length=200)
    event_date          = models.DateField(null=True, blank=True)
    document_link       = models.URLField(max_length=200, blank=True)
    event_photo         = models.URLField(max_length=200, blank=True)
    event_photo_add_1   = models.URLField(max_length=200, blank=True)
    event_photo_add_2   = models.URLField(max_length=200, blank=True)
    event_photo_add_3   = models.URLField(max_length=200, blank=True)
    update_date          = models.DateField(auto_now=True)
    created_date          = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    event_photo_credit  = models.CharField(max_length=100, blank=False, default="MOU")
'''