+++
type = "question"
title = "changeset not applied?"
description = '''Hi, I&#x27;ve not really looked at changesets before. But today I made some minor changes about 13 hours ago (changeset 103276642) and they have never showed up on the openstreetmap web map. I use JOSM. I tried updating the data in JOSM and it showed the old data. When I closed JOSM and reopened it. Down...'''
date = "2021-04-21T04:28:00Z"
lastmod = "2021-04-21T15:30:00Z"
weight = 79774
keywords = [ "josm", "updates" ]
aliases = [ "/questions/79774" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [changeset not applied?](/questions/79774/changeset-not-applied)

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
<span id="post-79774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79774-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I've not really looked at changesets before. But today I made some minor changes about 13 hours ago (changeset 103276642) and they have never showed up on the openstreetmap web map. I use JOSM. I tried updating the data in JOSM and it showed the old data. When I closed JOSM and reopened it. Downloading again it shows my changes. But on the OPENSTREETMAPS map on the web it doesn't show them. Can someone clarify for me how this works?</p>
<p>I do a lot of biking. Occasionally I go through areas and looking at my GPS I can see anomalies. Data I'd changed months earlier doesn't show. It's rare but it has happened. Is there something I should be doing to validate and confirm my changes are made correctly?</p>
<p>Thanks. Dan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '21, 04:28</strong></p>
<img src="https://secure.gravatar.com/avatar/443e731e185bff1683ec2db4d4f62cac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniel%20Ellsworth&#39;s gravatar image" />
<p><span>Daniel Ellsw...</span><br />
<span class="score" title="28 reputation points">28</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniel Ellsworth has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79774" class="comments-container">
&#10;</div>
<div id="comment-tools-79774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79774-form-container" class="comment-form-container">
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

<span id="79775"></span>

<div id="answer-container-79775" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79775-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-79775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The standard map on openstreetmap.org doesn't render <code>cycleway=lane</code> at all I believe. But on the CyclOSM layer your changes get displayed. The maps take different times to update. So usually, you just have to wait or force a re-load of the page bypassing cache (often Ctrl+F5 or Ctrl+Shift+F5 in your browser).</p>
<p>On your GPS update cycles will likely be even longer. Some phone apps like OSMAnd can update in minutes while others may take months to update (like a lot of sports tracking apps using Mapbox maps). There will be similar ranges for dedicated GPS devices.</p>
<p>Not sure why your JOSM did load the old data. If you have that problem again it's probably worth coming back here with more details on how to reproduce or opening a ticket with the JOSM developers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Apr '21, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-79775" class="comments-container">
<span id="79790"></span>
<div id="comment-79790" class="comment">
<div id="post-79790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The Main <a href="https://www.cyclosm.org/">CyclOSM</a> website has an option to use a "live" layer aimed at OSM editors that always uses freshly rendered tiles.</p>
</div>
<div id="comment-79790-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 12:39)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="79793"></span>
<div id="comment-79793" class="comment">
<div id="post-79793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The default (free?) update cycle of OsmAnd is monthly.</p>
</div>
<div id="comment-79793-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 14:27)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="79795"></span>
<div id="comment-79795" class="comment">
<div id="post-79795-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13231/h_mlet">@H_mlet</a>: That's why I wrote "can update".</p>
</div>
<div id="comment-79795-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 14:34)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="79796"></span>
<div id="comment-79796" class="comment">
<div id="post-79796-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. Yes. The principal map layer doesn't render cycleway lane as you mention. But I was using the CyclOSM layer. And aside from that I'd changed a street name and it wasn't showing up either. But this morning all was fine and apparently the changeset eventually applied.</p>
<p>I use OsmAnd not just because it's a good product. But it seems to update more frequently (if I'm interested in reloading the map). I'm using the paid version. The mapbox clients take much longer. And for awhile mapbox wasn't updating correctly. I'm not sure why. I pointed it out to them and they discovered the problem. I think they were doing some filtering on changesets for their updates. I guess that would make sense. Rather then do a complete worldwide update. But I suppose some filtering thing got them into problems. But that was a couple of years ago. When I pointed it out they wanted me to research and give them all the changesets I'd noticed that were in OPENSTREETMAPS from my changes but NOT in their mapbox clients maps! Imagine..... I told them that if it was that much of a problem then I wasn't the only one and they needed to do a more robust solution for their entire dataset. Which I guess they did because the updates eventually were applied.</p>
<p>The update of the old data in JOSM rather than from my updated changeset was the strangest one and that was what prompted me to do the post. I suppose something to do with persistence. I'd hit F5 but didn't try ctrl or ctrl shift f5. Thanks for that suggestion. I'll try it next time.</p>
<p>Dan</p>
</div>
<div id="comment-79796-info" class="comment-info">
<span class="comment-age">(21 Apr '21, 15:30)</span> <span class="comment-user userinfo">Daniel Ellsw...</span>
</div>
</div>
</div>
<div id="comment-tools-79775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79775-form-container" class="comment-form-container">
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

