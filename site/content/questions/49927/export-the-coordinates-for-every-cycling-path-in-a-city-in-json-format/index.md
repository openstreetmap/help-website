+++
type = "question"
title = "Export the coordinates for every cycling path in a city in JSON format"
description = '''Hi there, I&#x27;m trying to export only the cycle map for the city of São Paulo (top lat: -23.3984, bottom lat: -23.7552, left lng: -46.9027, right lng: -46.2888) using the openStreetMap API in http://www.openstreetmap.org/export in JSON format but as I click the export button the API downloads only an ...'''
date = "2016-05-31T18:52:00Z"
lastmod = "2016-05-31T21:15:00Z"
weight = 49927
keywords = [ "opencyclemap", "json", "export", "error" ]
aliases = [ "/questions/49927" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export the coordinates for every cycling path in a city in JSON format](/questions/49927/export-the-coordinates-for-every-cycling-path-in-a-city-in-json-format)

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
<span id="post-49927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49927-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, I'm trying to export only the cycle map for the city of São Paulo (top lat: -23.3984, bottom lat: -23.7552, left lng: -46.9027, right lng: -46.2888) using the openStreetMap API in <a href="http://www.openstreetmap.org/export">http://www.openstreetmap.org/export</a> in JSON format but as I click the export button the API downloads only an empty html file (0 bytes) called "map.osm.html". I already tried waiting and in many different days. It's been more than 2 weeks that I'm trying everyday and the only output is this 0 bytes file. I also tryied using the Overpass API, and it works, but the output is a HUGE XML file which I can't use because of the size. Tried also reading the overpass api docs to change the output to JSON with no success.</p>
<p>Can someone help me with this?</p>
<p>Thanks in advance, Giovanni.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opencyclemap" rel="tag" title="see questions tagged &#39;opencyclemap&#39;">opencyclemap</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '16, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/eddb52ee4acdd021853b148510d8e796?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gask&#39;s gravatar image" />
<p><span>gask</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gask has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '16, 21:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-49927" class="comments-container">
<span id="49928"></span>
<div id="comment-49928" class="comment">
<div id="post-49928-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess you could be better helped if you would mention in more detail what you want to do with the exported data.</p>
</div>
<div id="comment-49928-info" class="comment-info">
<span class="comment-age">(31 May '16, 19:48)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49929"></span>
<div id="comment-49929" class="comment">
<div id="post-49929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At /export there is no OpenCycleMap export. You only get raw OSM data in XML there. You likely do not get data because the area of the city contains too much data (the city is dense!) and our resources are limited ... it is the big pile of data which you get via Overpass.</p>
</div>
<div id="comment-49929-info" class="comment-info">
<span class="comment-age">(31 May '16, 19:48)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49932"></span>
<div id="comment-49932" class="comment">
<div id="post-49932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to map the cycling paths of the city in a cycling app. So I need the geo coordinates for every cycling path in the city in JSON format, which a co-worker said he got it from there. I filtered the api with "cycle map" under the "Layers" button, set the map to focus São Paulo (the bounding box I sent you in the question" and clicked the "Export" button. If it's not possible through this button, can you help me how will I get the expected output? :)</p>
</div>
<div id="comment-49932-info" class="comment-info">
<span class="comment-age">(31 May '16, 20:53)</span> <span class="comment-user userinfo">gask</span>
</div>
</div>
</div>
<div id="comment-tools-49927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49927-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="49933"></span>

<div id="answer-container-49933" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49933-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-49933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>the <span>Layers button </span> only affects/switches the map view (the images you see). All those different maps (and much more which are not listed in the layers menu) are based on the same OSM data set. A part of that data set (which you can get for example as <span>XML</span>) are the cycle routes and cycle paths.</p>
<p>You may want to learn a bit about how some cycling paths and routes are represented in our database. See e.g. <a href="https://wiki.openstreetmap.org/wiki/Bicycle">https://wiki.openstreetmap.org/wiki/Bicycle</a> and <a href="https://wiki.openstreetmap.org/wiki/Cycle_routes">https://wiki.openstreetmap.org/wiki/Cycle_routes</a> . I am not sure which type you are looking for. Just cycleable ways, specific cycle ways, cycle routes (usually many kilometres long), ...? All of that potentially exists in the OSM data.</p>
<p>If you only want the cycle routes the data can be filtered and also transformed to other formats and interpretations. I guess it is possible via Overpass API. See e.g. the question <a href="/questions/49683/">overpass-turbo-cycle-route-with-barriers</a>. You can export as geoJSON in Overpass Turbo (which is a front end for Overpass API). Likely someone else here can provide a better answer based on the information we now have, just wait a bit. Or maybe that's already enough for you (and you can describe how it worked afterwards)?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 May '16, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 May '16, 21:25</strong> </span></p>
</div>
</div>
<div id="comments-container-49933" class="comments-container">
&#10;</div>
<div id="comment-tools-49933" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49933-form-container" class="comment-form-container">
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

