+++
type = "question"
title = "How does lane detection work in OpenStreetMap"
description = '''I&#x27;m basically building an app that requires lane data or the number of lanes in a specific road. I&#x27;m new to OpenStreetMap, so I&#x27;m wondering whether it has data on lanes in a road. I also need to know which lane the car / phone / user is in, but I doubt that OSM does that (I have a work around for th...'''
date = "2019-08-19T00:51:00Z"
lastmod = "2019-08-19T04:24:00Z"
weight = 70416
keywords = [ "data", "lanes" ]
aliases = [ "/questions/70416" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does lane detection work in OpenStreetMap](/questions/70416/how-does-lane-detection-work-in-openstreetmap)

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
<span id="post-70416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70416-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm basically building an app that requires lane data or the number of lanes in a specific road. I'm new to OpenStreetMap, so I'm wondering whether it has data on lanes in a road. I also need to know which lane the car / phone / user is in, but I doubt that OSM does that (I have a work around for that using hardware). Does OSM provide this or do you know of any other sites that allow for access to this data? I'm not looking for lane detection based on satellite imagery, I need it for when a user is actually driving around.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '19, 00:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0e6d276b5602a0eebc0533bc3f042e1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harshith_1777&#39;s gravatar image" />
<p><span>harshith_1777</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harshith_1777 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70416" class="comments-container">
&#10;</div>
<div id="comment-tools-70416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70416-form-container" class="comment-form-container">
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

<span id="70419"></span>

<div id="answer-container-70419" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70419-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM only has static data, i.e. it has the number of <a href="https://wiki.openstreetmap.org/wiki/Key:lanes">lanes</a>, <a href="https://wiki.openstreetmap.org/wiki/Key:turn">turn lanes</a>, <span>change lane</span> information in so far it was mapped by the volunteers. A few years ago there was a project started in Germany to map the lane information. Those project spread a bit all over the (Western) world, so depending on where you need the data, it is possible that the coverage is good to very good.</p>
<p>This information is already used by satnav software based on OSM, such as Magic Earth and OsmAnd</p>
<p>OSM does (of course) not have dynamic information for each individual car, no open database has this information. The position of a car is something that has to be provided by the device in the car. I think the current GPS devices do not have the required precision to determine the lane in which a car is driving.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '19, 04:24</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-70419" class="comments-container">
&#10;</div>
<div id="comment-tools-70419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70419-form-container" class="comment-form-container">
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

