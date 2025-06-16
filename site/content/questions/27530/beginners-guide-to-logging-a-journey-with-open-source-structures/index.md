+++
type = "question"
title = "Beginners guide to logging a journey with open source structures"
description = '''hi, i want to start working with gps data to create routes and build maps of my journeys for blogs, travelogues, etc. i also want to create future journeys for planning (i suppose like itineraries)... i know a journey consists of trackpoints, so that a very simple record of journey may look (in prin...'''
date = "2013-10-27T14:09:00Z"
lastmod = "2013-12-20T14:45:00Z"
weight = 27530
keywords = [ "journey" ]
aliases = [ "/questions/27530" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Beginners guide to logging a journey with open source structures](/questions/27530/beginners-guide-to-logging-a-journey-with-open-source-structures)

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
<span id="post-27530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27530-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi,</p>
<p>i want to start working with gps data to create routes and build maps of my journeys for blogs, travelogues, etc. i also want to create future journeys for planning (i suppose like itineraries)...</p>
<p>i know a journey consists of trackpoints, so that a very simple record of journey may look (in principle) like::</p>
<pre><code>&lt;journey&gt;
&lt;trackpoint&gt;
 &lt;lat&gt;x&lt;/lat&gt;
 &lt;long&gt;y&lt;/long&gt;
 &lt;alt&gt;z&lt;/alt&gt;
 &lt;timestamp&gt;
   &lt;date&gt;yyyymmdd&lt;/date&gt;
   &lt;time&gt;hh:mm:ss.xxx&lt;/time&gt;
 &lt;/timestamp&gt;
&lt;/trackpoint&gt;
&lt;trackpoint&gt;
 &lt;lat&gt;x&lt;/lat&gt;
 &lt;long&gt;y&lt;/long&gt;
 &lt;alt&gt;z&lt;/alt&gt;
 &lt;timestamp&gt;
   &lt;date&gt;yyyymmdd&lt;/date&gt;
   &lt;time&gt;hh:mm:ss.xxx&lt;/time&gt;
 &lt;/timestamp&gt;
&lt;/trackpoint&gt;
   ......
&lt;/journey&gt;</code></pre>
<p>i appreciate also i may have to translate co-ords from different formats, and time from utc(or maybe just leave as utc), but what i cannot find is a basics howto that starts at this simple level and builds from there, showing me the correct standard structure to use.</p>
<p>i want at start to be able to represent my journeys in gpx, kml, osm_xml formats, so i want to know hot to take the raw data and translate it into these formats e.g. via an api:</p>
<p>gpx_file.gpx = journey.get_gpx(raw_journey_data)</p>
<p>osm_file.gpx = journey.get_osm(raw_journey_data)</p>
<p>obviously, then i need to understand these standards.</p>
<p>i have tried reading around, but there is so much about getting data out from a map, and i can't find a good 'basics' guide to plotting a diary event {ie a journey over a set time}... help?...</p>
<p>thanks,</p>
<p>iain</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-journey" rel="tag" title="see questions tagged &#39;journey&#39;">journey</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '13, 14:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d6fa1141d4bb4ac4ad7b3937156980bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iainmacgigamac&#39;s gravatar image" />
<p><span>iainmacgigamac</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iainmacgigamac has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '13, 15:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-27530" class="comments-container">
&#10;</div>
<div id="comment-tools-27530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27530-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="28348"></span>

<div id="answer-container-28348" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28348-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://osrm.at/">OSRM</a>, the most popular routing software for OSM data, allows you to export a GPX file from a planned journey. You could then write a script in the programming language of your choice to add the additional data you're talking about.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '13, 16:33</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-28348" class="comments-container">
&#10;</div>
<div id="comment-tools-28348" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28348-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28345"></span>

<div id="answer-container-28345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28345-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I highly recommend to <strong>use a manual solution</strong> ("drawing by hand") to do journey planing<br />
<a href="https://wiki.openstreetmap.org/wiki/Maps">https://wiki.openstreetmap.org/wiki/Maps</a><br />
This is still not a usecase that is currently well supported, but cause a lot of manual processing and a lot of tools:<br />
</p>
<ol>
<li>Create .GPX files using a custom script or what ever fits best</li>
<li>You need a tool/service that supports input a GPX track and does a routing that creates a route along the track for the right vehicle. Otherwise you might manually create via points<br />
<a href="https://wiki.openstreetmap.org/wiki/Software/Desktop#Navigating_features">https://wiki.openstreetmap.org/wiki/Software/Desktop#Navigating_features</a> ("follow predefined track")<br />
<a href="https://wiki.openstreetmap.org/wiki/Routing/online_routers">https://wiki.openstreetmap.org/wiki/Routing/online_routers</a><br />
</li>
<li>Get from the directions the OSM ids from the routing graph.</li>
<li>Download OSM data in the area, match IDs and create a map style with highlighting this features</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '13, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-28345" class="comments-container">
&#10;</div>
<div id="comment-tools-28345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28345-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29224"></span>

<div id="answer-container-29224" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29224-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't speak to displaying routes, but I may have some partial answers.</p>
<p>For converting your .gpx files into other formats I would recommend GPSBabel (<a href="http://www.gpsbabel.org/">http://www.gpsbabel.org/</a>) which seems to speak just about every GPS format in the world. For complicated operations the documentation can be rather opaque, but for simple things it's easy enough to use. It's primarily a command line utility, so it shouldn't be difficult to call it from whatever you're planning on writing. You seem mostly interested in writing your own utilities, but you might not need to reinvent the wheel.</p>
<p>As far as planned gpx routes go, other than the things already mentioned in other answers, I do know that OSMAnd can save GPX out gpx routes based on what it uses for navigation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '13, 14:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span> </br></br></p>
</div>
</div>
<div id="comments-container-29224" class="comments-container">
&#10;</div>
<div id="comment-tools-29224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29224-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

