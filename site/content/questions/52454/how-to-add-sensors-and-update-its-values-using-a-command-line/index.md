+++
type = "question"
title = "How to add sensors and update its values using a command line?"
description = '''I looking for a way to add sensors to a map using its geolocations. What is the best object to represent a sensor in OSM? It doesn&#x27;t need to be visible, but it needs to be readable in some way. Is that a command line which I could use in order modify a OSM file adding/updating a sensor with all its ...'''
date = "2016-10-10T21:02:00Z"
lastmod = "2016-10-11T04:40:00Z"
weight = 52454
keywords = [ "sensory", "adding", "commandline", "commands", "osrm" ]
aliases = [ "/questions/52454" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to add sensors and update its values using a command line?](/questions/52454/how-to-add-sensors-and-update-its-values-using-a-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52454-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I looking for a way to add sensors to a map using its geolocations. What is the best object to represent a sensor in OSM? It doesn't need to be visible, but it needs to be readable in some way.</p>
<p>Is that a command line which I could use in order modify a OSM file adding/updating a sensor with all its characteristics, as values, name, ID, location, tag, etc?</p>
<p>The idea is to build a software that plans a route based on the values of each sensor. The OSM file will be read by the OSRM project in order to accomplish it.</p>
<p>I currently have spread sensors over a city. Each sensor has its own geolocation (lat and lng) and its own values. The values are updated at a certain frequency, which makes it impractical to open a map editor like Potlatch or JOSM every time that the values of each sensor need to be updated and for this purpose only. So it's needed a faster way to update these sensors.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sensory" rel="tag" title="see questions tagged &#39;sensory&#39;">sensory</span> <span class="post-tag tag-link-adding" rel="tag" title="see questions tagged &#39;adding&#39;">adding</span> <span class="post-tag tag-link-commandline" rel="tag" title="see questions tagged &#39;commandline&#39;">commandline</span> <span class="post-tag tag-link-commands" rel="tag" title="see questions tagged &#39;commands&#39;">commands</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '16, 21:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c5f91c781a22302edea42c4292e4d173?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pcumino&#39;s gravatar image" />
<p><span>pcumino</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pcumino has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '16, 21:06</strong> </span></p>
</div>
</div>
<div id="comments-container-52454" class="comments-container">
<span id="52457"></span>
<div id="comment-52457" class="comment">
<div id="post-52457-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>what is "in OSM" for you? Do you mean in the public, central database of openstreetmap.org? Why do you think your sensors should be in there (and usable by everybody)? How often do you want to update a sensor in the OSM database?</p>
</div>
<div id="comment-52457-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 22:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="52458"></span>
<div id="comment-52458" class="comment">
<div id="post-52458-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you just intending to navigate between sensors, or does the sensor value affect navigation somehow ? Do you expect to use OSRM as-is, or are you only using part of the OSRM software, like the extractor ?</p>
</div>
<div id="comment-52458-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 23:09)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="52461"></span>
<div id="comment-52461" class="comment">
<div id="post-52461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The sensors will be added to my local OSM file only. The OSRM engine will make use of the local OSM file only. The sensors are geolocated (lat and long) and the values measured by the sensors would be interpreted as an additional weight/cost of a street/path where the sensor is placed.</p>
<p>Each sensor measures a condition of the street, in this case, the air quality along the path. The worse is the air quality, the higher is the weight/cost of such street and the more difficult it would be for this street to be chosen by OSRM engine as a possible route for a vehicle or pedestrian.</p>
<p>I intend to use the sensors as a tool to keep track of polluted areas and use the OSRM engine to avoid such areas. The values from the sensor would be updated every 5 minutes (need to search a feasible update frequency).</p>
<p>I'm using the whole OSRM engine as the main software for such purpose. And also using a web interface in order to show the results for a user.</p>
<p>Once the OSRM identify that are a certain number of sensors in a street and, at the same time, its air quality, then the engine would evaluate if is worthy or not choose such path, depending on the total cost for the pedestrian/vehicle.</p>
</div>
<div id="comment-52461-info" class="comment-info">
<span class="comment-age">(11 Oct '16, 04:40)</span> <span class="comment-user userinfo">pcumino</span>
</div>
</div>
</div>
<div id="comment-tools-52454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52454-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

