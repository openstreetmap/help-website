+++
type = "question"
title = "read osm file to access direction, distance and landmarks"
description = '''Hi, as part of my PhD I have to implement a route to an audio game. I have zero GIS knowledge. I want to read data from an offline .OSM file so that I can access the distance, directions and landmarks information from it to use in further tasks. I am using python.  PS: I have looked into a number of...'''
date = "2018-11-26T15:02:00Z"
lastmod = "2018-11-27T11:49:00Z"
weight = 66921
keywords = [ "directions", "distance", "route", "landmark" ]
aliases = [ "/questions/66921" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [read osm file to access direction, distance and landmarks](/questions/66921/read-osm-file-to-access-direction-distance-and-landmarks)

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
<span id="post-66921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66921-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, as part of my PhD I have to implement a route to an audio game. I have zero GIS knowledge. I want to read data from an offline .OSM file so that I can access the distance, directions and landmarks information from it to use in further tasks. I am using python.</p>
<p>PS: I have looked into a number of packages inclusing osmium, osrm, osmnx and pyroute :/</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-directions" rel="tag" title="see questions tagged &#39;directions&#39;">directions</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-landmark" rel="tag" title="see questions tagged &#39;landmark&#39;">landmark</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '18, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/07fcd1e83b577fee2c9ec9ffd44b59a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nida%20Aziz&#39;s gravatar image" />
<p><span>Nida Aziz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nida Aziz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66921" class="comments-container">
<span id="66924"></span>
<div id="comment-66924" class="comment">
<div id="post-66924-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Hi, welcome! I guess it would be beneficial for a possible answer if you could elaborate a bit on "access the distance, directions and landmarks information from it": what would be your input and the desired output? E.g. two coordinates and you want to get the distance of the fastest route by car?</p>
<p>Furthermore, what was not satisfying about the "packages" you have looked into?</p>
</div>
<div id="comment-66924-info" class="comment-info">
<span class="comment-age">(26 Nov '18, 19:02)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="66931"></span>
<div id="comment-66931" class="comment">
<div id="post-66931-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi! thank you for responding!</p>
<p>My input would be a .osm file giving the route between any two points (or lat, lons), eg, at the moment I am taking the starting point to be my university and the endpoint to be the nearest train station giving me the "route" i can take from the university to the train station.</p>
<p>My desired output is ideally a .csv file with directions, amenity points and distances between them, from start to endpoint.</p>
</div>
<div id="comment-66931-info" class="comment-info">
<span class="comment-age">(27 Nov '18, 01:09)</span> <span class="comment-user userinfo">Nida Aziz</span>
</div>
</div>
<span id="66932"></span>
<div id="comment-66932" class="comment">
<div id="post-66932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>are you familiar with the work of Anita Graser on pedestrian routing using landmarks? see e.g. <a href="https://agile-online.org/conference_paper/cds/agile_2017/shortpapers/46_ShortPaper_in_PDF.pdf">conference paper (PDF)</a> or <a href="https://www.slideshare.net/anitagraser/landmarkbased-instructions-for-pedestrian-navigation-systems-using-osm">Slideshare presentation</a></p>
<p>Is it that kind of routing that you want to produce ?</p>
</div>
<div id="comment-66932-info" class="comment-info">
<span class="comment-age">(27 Nov '18, 04:19)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="66936"></span>
<div id="comment-66936" class="comment">
<div id="post-66936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for responding. I looked at Anita Graser's work and it is partially what I want. She is calculating routes and giving track information which is what I want, but additionally i want the "amenity" information that openstreetmaps gives. I also want to be able to import the navigation information (track points -&gt; eg, turn left after 200m onto Grover's road, etc) into my python code.</p>
<p>Im sorry if these are very basic questions, my background and work are both not in this field. My actual work starts after I have all these features.</p>
</div>
<div id="comment-66936-info" class="comment-info">
<span class="comment-age">(27 Nov '18, 11:49)</span> <span class="comment-user userinfo">Nida Aziz</span>
</div>
</div>
</div>
<div id="comment-tools-66921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66921-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

