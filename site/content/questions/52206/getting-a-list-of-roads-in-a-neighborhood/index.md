+++
type = "question"
title = "Getting a list of roads in a neighborhood."
description = '''I&#x27;d like to get a to-do list for all the roads in a neighborhood and go one by one. How can i list all the roads in a specified area if they were not Tagged as being part of that neighborhood? Going through 1 by 1 and tagging them seems counter productive because if i&#x27;m there, i might as well just f...'''
date = "2016-09-23T19:44:00Z"
lastmod = "2016-09-24T17:56:00Z"
weight = 52206
keywords = [ "roads", "neighborhood.", "updates" ]
aliases = [ "/questions/52206" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting a list of roads in a neighborhood.](/questions/52206/getting-a-list-of-roads-in-a-neighborhood)

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
<span id="post-52206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52206-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to get a to-do list for all the roads in a neighborhood and go one by one. How can i list all the roads in a specified area if they were not Tagged as being part of that neighborhood? Going through 1 by 1 and tagging them seems counter productive because if i'm there, i might as well just finish all the edits.</p>
<p>Thanks for any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-neighborhood." rel="tag" title="see questions tagged &#39;neighborhood.&#39;">neighborhood.</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '16, 19:44</strong></p>
<img src="https://secure.gravatar.com/avatar/b986d0956f9a1ecce7ae7e6226c60b09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tuliotroche&#39;s gravatar image" />
<p><span>tuliotroche</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tuliotroche has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52206" class="comments-container">
<span id="52215"></span>
<div id="comment-52215" class="comment">
<div id="post-52215-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This query somewhat confuses me, assuming your want add the neighbourhood name to each road. Why would tags be added to individual roads showing which neighbourhood they are in? Surely a boundary polygon is more sensible and also meets all needs or is this a way to define portions of some places when the boundary is unknown to the mapper and has not been mapped yet. What tags would be used.....is_in or addr tags?</p>
</div>
<div id="comment-52215-info" class="comment-info">
<span class="comment-age">(24 Sep '16, 14:48)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-52206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52206-form-container" class="comment-form-container">
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

<span id="52209"></span>

<div id="answer-container-52209" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52209-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-52209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tuliotroche has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This type of problem is best tackled using Overpass/Overpass-Turbo.</p>
<p>If your neighbourhood is mapped as a polygon then you can use this as an area for constraining the query. Otherwise use around with, say, a value of 500-1000 metres. You'll probably get some false positives, but remember that unless the neighbourhood is precisely defined people living there will have rather different perspectives of what it includes. Therefore tagging individual roads is unlikely to meet OSM's repeatably observable criterion.</p>
<p>Suitable example queries of this type are shown on the OSM <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Special_clauses:_around_and_poly">wiki</a>.</p>
<p>You can arrange for the output to be produced ia csv format. Here's <a href="http://overpass-turbo.eu/s/ixO">an example</a> for Overpass-turbo.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '16, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-52209" class="comments-container">
<span id="52214"></span>
<div id="comment-52214" class="comment">
<div id="post-52214-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I took your example, and where Bingham was, put in my neighborhoods name. Out popped all the streets. THANK YOU A TON. I guess i have a lot of work ahead of me :)</p>
</div>
<div id="comment-52214-info" class="comment-info">
<span class="comment-age">(24 Sep '16, 12:24)</span> <span class="comment-user userinfo">tuliotroche</span>
</div>
</div>
<span id="52216"></span>
<div id="comment-52216" class="comment">
<div id="post-52216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You probably need to dedup names to make it look better!</p>
</div>
<div id="comment-52216-info" class="comment-info">
<span class="comment-age">(24 Sep '16, 17:56)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52209-form-container" class="comment-form-container">
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

