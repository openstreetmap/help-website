+++
type = "question"
title = "Toll Booths"
description = '''I&#x27;m having a problem where OSM says that &quot;[Road]&quot; crosses &quot;toll booth.&quot; How can I fix that without removing the building, or road?'''
date = "2020-04-02T06:03:00Z"
lastmod = "2020-04-02T09:01:00Z"
weight = 73940
keywords = [ "issue", "road", "toll" ]
aliases = [ "/questions/73940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Toll Booths](/questions/73940/toll-booths)

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
<span id="post-73940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73940-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm having a problem where OSM says that "[Road]" crosses "toll booth." How can I fix that without removing the building, or road?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-issue" rel="tag" title="see questions tagged &#39;issue&#39;">issue</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-toll" rel="tag" title="see questions tagged &#39;toll&#39;">toll</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '20, 06:03</strong></p>
<img src="https://secure.gravatar.com/avatar/b5868b476e46281d48855dc281357d01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timbot4x4&#39;s gravatar image" />
<p><span>Timbot4x4</span><br />
<span class="score" title="101 reputation points">101</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timbot4x4 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73940" class="comments-container">
<span id="73945"></span>
<div id="comment-73945" class="comment">
<div id="post-73945-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Could you please link to an example where that happens? Then we can check if that is an issue with the mapping of the toll booth or if it is your router/satnav giving confusing instructions.</p>
</div>
<div id="comment-73945-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 07:55)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-73940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73940-form-container" class="comment-form-container">
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

<span id="73948"></span>

<div id="answer-container-73948" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73948-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think Timbot4x4 might be referring to the Changeset: 82955289 where they added barrier=tollbooth area=yes to three existing buildings over three existing tollbooth nodes.</p>
<p>The tollbooth nodes on the highway are the actual barriers. The buildings are structures over the barriers, they ought not to be tagged as barrier=toll_booth as they are not barriers to the highway (they're not connected to the highway). The area tag is not needed on a building polygon, (a polygon is a bounded area).</p>
<p>The tollbooth node on the highway should hold all restriction, barrier and toll fee information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '20, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-73948" class="comments-container">
<span id="73949"></span>
<div id="comment-73949" class="comment">
<div id="post-73949-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I see. Looking at some imagery those seem to be booth for getting/paying parking tickets. Do we tag those as toll booths?</p>
<p>height=15.7 seems to be way off, too. On Google images I see clearance heights of 6'8" to 7'10".</p>
</div>
<div id="comment-73949-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 08:43)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="73951"></span>
<div id="comment-73951" class="comment">
<div id="post-73951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The tag tollbooth is used to describe a barrier to a highway. In this case the tollbooth barrier is the existing tagged node on the highway as per :-<a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dtoll_booth">https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dtoll_booth</a> The building isn't connected to the highway so isn't a barrier to the highway. The building could be described as building=tollbooth but not barrier=tollbooth.</p>
</div>
<div id="comment-73951-info" class="comment-info">
<span class="comment-age">(02 Apr '20, 09:01)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-73948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73948-form-container" class="comment-form-container">
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

