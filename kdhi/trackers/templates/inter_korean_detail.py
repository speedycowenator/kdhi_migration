{% extends "tracker_base.html" %}


{% block content %}
 <div class="body-div">
    <div class="left-section"></div>
    <div class="center-section">
      <div class="biographic-block">
        <h1 class="event-title">{{tracker_item.event_title}}</h1>
        <h1 class="event-date">{{tracker_item.event_date}}</h1>
        <div class="institution-function-block">
            <h1 class="event-details-header">Details</h1>
            <p class="event-details-paragraph">{{tracker_item.event_description}}</p></div>
        <h1 class="institution-members-header">Participants</h1>        
            <div class="grid-container">
            {% for individual in participant_list %}
            <div class="grid-item">
            <img src="{{individual.2}}" alt="" class="institution-member-photo">           
            <a href="{{individual.1}}" class="institution-position-name">{{individual.0}}</a>
            </div>
            {% endfor %}
            </div>
    
    <h1 class="institution-members-header">Photos</h1>        
    <img src="{{tracker_item.event_photo}}" alt="" class="image-81">
   
    </div> 
    </div>
    <div class="right-section"></div>
  </div>
{% endblock %}
