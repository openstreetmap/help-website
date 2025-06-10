+++
type = "question"
title = "Update OSM locally and keep in sync with remote server"
description = '''Hi, I&#x27;have a local OSRM setup and a local Postgres of OSM (converted using osm2pgsql). Now, I&#x27;ve some GPS data for which there is no road in my OSM map. What are the correct ways to upload my GPS data into OSM data both locally and globally? I want to make a single road for my GPS trace and test it ...'''
date = "2019-05-06T15:55:00Z"
lastmod = "2019-05-10T14:17:00Z"
weight = 69105
keywords = [ "osrm", "gps", "osm", "osm2pgsql", "gps-traces" ]
aliases = [ "/questions/69105" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Update OSM locally and keep in sync with remote server](/questions/69105/update-osm-locally-and-keep-in-sync-with-remote-server)

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
<span id="post-69105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69105-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'have a local OSRM setup and a local Postgres of OSM (converted using osm2pgsql). Now, I've some GPS data for which there is no road in my OSM map. What are the correct ways to <strong>upload my GPS data into OSM data both locally</strong> and globally?</p>
<p>I want to make a single road for my GPS trace and test it before I submit it back to openstreetmap.org. So, it's preferred to update OSM data on my local server, rebuild OSRM to test it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-gps-traces" rel="tag" title="see questions tagged &#39;gps-traces&#39;">gps-traces</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '19, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/84c7c2db2575ea0c03871de1eaadc8e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gps_trace&#39;s gravatar image" />
<p><span>gps_trace</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gps_trace has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69105" class="comments-container">
&#10;</div>
<div id="comment-tools-69105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69105-form-container" class="comment-form-container">
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

<span id="69107"></span>

<div id="answer-container-69107" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69107-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to have the GPS track itself visible on openstreetmap.org there are some instructions for this on the "<a href="https://wiki.openstreetmap.org/wiki/Upload_GPS_tracks">upload GPS tracks</a>" page of the wiki. You will need to convert them to gpx format first.</p>
<p>Creating ways is normally done by hand with <a href="https://wiki.openstreetmap.org/wiki/Editors">editing software</a> of your choice, the raw GPS traces are often quite messy so you will probably want to 'smooth' things out when you make it.</p>
<p>While I can't offer advice on introducing edits into you local routing setup, I do know that <a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a> has a <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/GraphView">GraphView plugin</a> that can be used to visualise the effects of turn restrictions and routing information. This may give you enough confidence in your edit to upload to OSM without local testing. You would then be able to update your local OSRM server according to your normal process which would then include the new road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '19, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-69107" class="comments-container">
<span id="69153"></span>
<div id="comment-69153" class="comment">
<div id="post-69153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there any way I can automate submitting of GPX files on OSM either via JOSM or any other way?</p>
</div>
<div id="comment-69153-info" class="comment-info">
<span class="comment-age">(10 May '19, 14:17)</span> <span class="comment-user userinfo">gps_trace</span>
</div>
</div>
</div>
<div id="comment-tools-69107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69107-form-container" class="comment-form-container">
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

