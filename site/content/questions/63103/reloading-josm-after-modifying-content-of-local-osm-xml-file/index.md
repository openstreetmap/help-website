+++
type = "question"
title = "Reloading JOSM after modifying content of local .osm XML file"
description = '''Hi OpenStreetMap community,  I&#x27;ve been working with OpenStreetMap and JOSM recently, alongside with Pyosmium and other Python libraries, and using a local copy extracted from the OpenStreetMap webpage. My goal is to get my actual position (I already have my coordinates lon and lat), and create a new...'''
date = "2018-04-24T15:13:00Z"
lastmod = "2018-04-25T09:48:00Z"
weight = 63103
keywords = [ "josm", "osm" ]
aliases = [ "/questions/63103" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Reloading JOSM after modifying content of local .osm XML file](/questions/63103/reloading-josm-after-modifying-content-of-local-osm-xml-file)

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
<span id="post-63103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63103-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OpenStreetMap community,</p>
<p>I've been working with OpenStreetMap and JOSM recently, alongside with Pyosmium and other Python libraries, and using a local copy extracted from the OpenStreetMap webpage.</p>
<p>My goal is to get my actual position (I already have my coordinates lon and lat), and create a new node in that position. I have achieved this step using Pyosmium and modifying the .osm XML file.</p>
<p>The problem is that I want to keep repeating this step (getting new position and modifying the node previously created with the new coordinates), and I would like to have the possibility to see it in an editor such as JOSM, but it does not updates or reloads the file once I have changed it using a Python script. Do you know if there is any other editor/display that allows me to do that, or if there is any option I can manage to do so with JOSM? Right now, the only solution I have achieved is to open the file again inside JOSM to reload the content of my .osm file.</p>
<p>Just to clarify, I dont have any intention to update the OpenStreetMap database, I'm just working locally with the .osm file.</p>
<p>Thank you so much for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '18, 15:13</strong></p>
<img src="https://secure.gravatar.com/avatar/4f0e41948c858874d41d8b2c90885186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escrei1584&#39;s gravatar image" />
<p><span>escrei1584</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escrei1584 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63103" class="comments-container">
&#10;</div>
<div id="comment-tools-63103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63103-form-container" class="comment-form-container">
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

<span id="63109"></span>

<div id="answer-container-63109" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63109-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="escrei1584 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could look and see if any of the remote control commands work for what you want to do:</p>
<p><a href="https://josm.openstreetmap.de/wiki/Help/RemoteControlCommands">https://josm.openstreetmap.de/wiki/Help/RemoteControlCommands</a></p>
<p>I don't see a way to delete a point, but maybe just creating a new node at each update works for your purpose?</p>
<p>Otherwise I expect you'd have to make a JOSM plugin. Your usecase at least sounds similar to <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/LiveGPS">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/LiveGPS</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '18, 20:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63109" class="comments-container">
<span id="63121"></span>
<div id="comment-63121" class="comment">
<div id="post-63121-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much! I managed to get it working using the remote control commands and adding the node each time to JOSM.</p>
</div>
<div id="comment-63121-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 09:48)</span> <span class="comment-user userinfo">escrei1584</span>
</div>
</div>
</div>
<div id="comment-tools-63109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63109-form-container" class="comment-form-container">
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

