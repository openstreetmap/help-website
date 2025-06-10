+++
type = "question"
title = "Get road type and maximum speed for OSM way IDs"
description = '''I am looking for a way to get the road type (e.g. highway or urban street) and the maximum allowed speed for OSM way IDs. I am dealing with a large set of data (~100,000 way IDs) in .csv format. I am trying to implement the data transfer via CURL command and get the result if possible in JSON format...'''
date = "2016-12-05T19:50:00Z"
lastmod = "2016-12-08T16:40:00Z"
weight = 53253
keywords = [ "roadtype", "maxspeed", "id", "way", "highway" ]
aliases = [ "/questions/53253" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get road type and maximum speed for OSM way IDs](/questions/53253/get-road-type-and-maximum-speed-for-osm-way-ids)

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
<span id="post-53253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53253-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a way to get the road type (e.g. highway or urban street) and the maximum allowed speed for OSM way IDs. I am dealing with a large set of data (~100,000 way IDs) in .csv format. I am trying to implement the data transfer via CURL command and get the result if possible in JSON format. I am completely new to the matter and would be really grateful for any help. I have already figured out that there are the OSM keys "highway=<em>" and "maxspeed=</em>" which might provide my required information. But I don't know how to use them via CURL or any other automatically working data transfer.</p>
<p>Many Thanks! John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roadtype" rel="tag" title="see questions tagged &#39;roadtype&#39;">roadtype</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '16, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/e791e8a7ab2f64c7229b292ddbfade24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="john123&#39;s gravatar image" />
<p><span>john123</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="john123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '16, 20:03</strong> </span></p>
</div>
</div>
<div id="comments-container-53253" class="comments-container">
<span id="53370"></span>
<div id="comment-53370" class="comment">
<div id="post-53370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do you get the csv file? Converted from where?</p>
</div>
<div id="comment-53370-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 10:27)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
</div>
<div id="comment-tools-53253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53253-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="53373"></span>

<div id="answer-container-53373" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53373-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have an .osm/.o5m file in hand:</p>
<p>Use osmfilter</p>
<p>I am not sure what you are using, but create a nested for loop. The first loop <a href="https://wiki.openstreetmap.org/wiki/Osmfilter#Keep_only_specific_Tags">searches</a> by "maxspeed=x", with x as the speed, while the second loop <a href="https://wiki.openstreetmap.org/wiki/Osmfilter#Keep_only_specific_Tags">searches</a> by a loop with a switch-case function which includes all tag values of a highway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '16, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-53373" class="comments-container">
&#10;</div>
<div id="comment-tools-53373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53373-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53386"></span>

<div id="answer-container-53386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53386-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know where you got the OSM way ID's from, but be aware that the ways can be deleted in the meantime. So not all IDs will return an answer</p>
<p>The following <a href="http://overpass-turbo.eu/">Overpass</a> query gets the data for way 24777894 You could write a loop that makes http calls via curl for each of the IDs you have.</p>
<p><a href="http://overpass.osm.rambler.ru/cgi/interpreter?data=%5Bout:json%5D;way(24777894);out;">http://overpass.osm.rambler.ru/cgi/interpreter?data=%5Bout:json%5D;way(24777894);out;</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '16, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-53386" class="comments-container">
&#10;</div>
<div id="comment-tools-53386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53386-form-container" class="comment-form-container">
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

