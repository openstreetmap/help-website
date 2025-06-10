+++
type = "question"
title = "Determining a road/highway centerline?"
description = '''Does OSM data contain information relative to the center-line of a road or a way to determine it? In the US and elsewhere some roads change back and forth to/from dual carriage ways or are dual carriage ways for their entire length. Is there a way to determine a road &quot;center line&quot; from the OSM data,...'''
date = "2012-11-02T12:41:00Z"
lastmod = "2012-11-02T14:05:00Z"
weight = 17407
keywords = [ "centerline" ]
aliases = [ "/questions/17407" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Determining a road/highway centerline?](/questions/17407/determining-a-roadhighway-centerline)

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
<span id="post-17407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17407-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does OSM data contain information relative to the center-line of a road or a way to determine it?</p>
<p>In the US and elsewhere some roads change back and forth to/from dual carriage ways or are dual carriage ways for their entire length.</p>
<p>Is there a way to determine a road "center line" from the OSM data, i.e., a single line tracking the road?</p>
<p>Regards, Jim</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-centerline" rel="tag" title="see questions tagged &#39;centerline&#39;">centerline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '12, 12:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a91c10377b432d3352bd072df1aa4633?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="obrienj&#39;s gravatar image" />
<p><span>obrienj</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="obrienj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17407" class="comments-container">
&#10;</div>
<div id="comment-tools-17407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17407-form-container" class="comment-form-container">
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

<span id="17413"></span>

<div id="answer-container-17413" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17413-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A typical road is represented by a single osm way, which should already follow the centerline of the road. Dual carriageways are often represented by two osm mays (tagged as oneway=yes), but the principle is the same.</p>
<p>If you want to go into more details, have a look at the <em>lanes</em> <a href="http://wiki.openstreetmap.org/wiki/Lane">tag</a> and <a href="http://wiki.openstreetmap.org/wiki/Lanes">tag suffix</a>. But there are a lot of ways that lack this detailed info (especially the suffix ones, as it is a fairly new scheme).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '12, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-17413" class="comments-container">
&#10;</div>
<div id="comment-tools-17413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17413-form-container" class="comment-form-container">
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

