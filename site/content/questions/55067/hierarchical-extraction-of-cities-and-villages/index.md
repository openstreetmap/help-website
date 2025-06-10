+++
type = "question"
title = "hierarchical extraction of cities and villages"
description = '''I have downloaded the pbf file for India. I would like to extract all cities and suburbs/villages within the city hierarchically. I have tried the below command in osmosis, ./osmosis --read-pbf india.osm.pbf --tf accept-nodes place=city,town,village,neighbourhood,city_district,locality --tf reject-r...'''
date = "2017-03-14T17:50:00Z"
lastmod = "2017-06-03T18:35:00Z"
weight = 55067
keywords = [ "osmosis" ]
aliases = [ "/questions/55067" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [hierarchical extraction of cities and villages](/questions/55067/hierarchical-extraction-of-cities-and-villages)

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
<span id="post-55067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55067-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded the pbf file for India. I would like to extract all cities and suburbs/villages within the city hierarchically. I have tried the below command in osmosis,</p>
<p>./osmosis --read-pbf india.osm.pbf --tf accept-nodes place=city,town,village,neighbourhood,city_district,locality --tf reject-relations --tf reject-ways --lp --wx places.osm</p>
<p>While I am able to get list of all the places, I am not able to relate which village/suburb etc,. belong to which city. Is there any way I can extract such information through osmosis? Or can it be done through any other tools?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '17, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a24776e12d0c00debee804f888f67bbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Coder123&#39;s gravatar image" />
<p><span>Coder123</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Coder123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '17, 17:51</strong> </span></p>
</div>
</div>
<div id="comments-container-55067" class="comments-container">
<span id="56428"></span>
<div id="comment-56428" class="comment">
<div id="post-56428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am also looking for the same solution. Anyone?</p>
</div>
<div id="comment-56428-info" class="comment-info">
<span class="comment-age">(03 Jun '17, 08:59)</span> <span class="comment-user userinfo">carapace</span>
</div>
</div>
</div>
<div id="comment-tools-55067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55067-form-container" class="comment-form-container">
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

<span id="56429"></span>

<div id="answer-container-56429" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56429-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that the answer is "no" with osmosis. Nominatim (which you can install locally) has an understanding of place hierarchies (based on areas at least). If you test a few searches at <a href="http://nominatim.osm.org/">http://nominatim.osm.org/</a> does it return sensible results for you? If so, perhaps install a copy of that locally and use that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '17, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56429" class="comments-container">
&#10;</div>
<div id="comment-tools-56429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56429-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56433"></span>

<div id="answer-container-56433" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56433-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With osmosis, I was able to extract all the villages and suburbs. Then i wrote a separate program which pings the osm db with the nodeid in an interval of every 20s and extracted the city/state information. It was a time consuming task but I was able to get what I needed. You could try a similar approach if you have a restricted geographical limits.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '17, 18:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a24776e12d0c00debee804f888f67bbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Coder123&#39;s gravatar image" />
<p><span>Coder123</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Coder123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56433" class="comments-container">
&#10;</div>
<div id="comment-tools-56433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56433-form-container" class="comment-form-container">
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

