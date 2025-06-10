+++
type = "question"
title = "Roundabout missing exits"
description = '''Hello,  this roundabout https://www.openstreetmap.org/#map=18/48.31988/18.09694 are missing some exits. It has four in total, but navigation shows only two. Any idea how can I fix this? Thank You!'''
date = "2019-04-01T08:20:00Z"
lastmod = "2019-04-02T08:18:00Z"
weight = 68570
keywords = [ "roundabout", "missing" ]
aliases = [ "/questions/68570" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Roundabout missing exits](/questions/68570/roundabout-missing-exits)

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
<span id="post-68570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68570-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, this roundabout <a href="https://www.openstreetmap.org/#map=18/48.31988/18.09694">https://www.openstreetmap.org/#map=18/48.31988/18.09694</a> are missing some exits. It has four in total, but navigation shows only two. Any idea how can I fix this? Thank You!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '19, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ffafe9ccb7395f717277f8771bb610ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AndrejKuna&#39;s gravatar image" />
<p><span>AndrejKuna</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AndrejKuna has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68570" class="comments-container">
<span id="68600"></span>
<div id="comment-68600" class="comment">
<div id="post-68600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which navigation software? Did you try others? Looks like <a href="https://www.openstreetmap.org/directions?engine=graphhopper_car&amp;route=48.31997%2C18.09631%3B48.32027%2C18.09655#map=19/48.31998/18.09703">GraphHopper</a> correctly reports 4 exits while <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=48.31997%2C18.09631%3B48.32027%2C18.09655#map=19/48.31998/18.09704">OSRM</a> only reports 3. Could be due to shared entry/exit nodes as explained by SK53.</p>
</div>
<div id="comment-68600-info" class="comment-info">
<span class="comment-age">(02 Apr '19, 08:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68570-form-container" class="comment-form-container">
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

<span id="68581"></span>

<div id="answer-container-68581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68581-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Exits and entrances share nodes which may cause them to be miscounted, as well as not allowing the router to apply appropriate penalties for entering &amp; leaving the roundabout (because a vehicle and transit directly from an entrance to an exit). Some of the geometries also look rather odd for a roundabout (notably the S exit).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '19, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-68581" class="comments-container">
&#10;</div>
<div id="comment-tools-68581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68581-form-container" class="comment-form-container">
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

