+++
type = "question"
title = "Ways (roads) with multiple end points"
description = '''From what I understand, a &quot;way is an ordered list of nodes&quot; that can only have two end points (which may or may not overlap). How should single roads with multiple end points be treated? It&#x27;s possible for a road to go a certain direction while having offshoots or loops etc. in different directions. ...'''
date = "2018-07-27T11:11:00Z"
lastmod = "2018-07-27T19:52:00Z"
weight = 64962
keywords = [ "ways", "split" ]
aliases = [ "/questions/64962" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ways (roads) with multiple end points](/questions/64962/ways-roads-with-multiple-end-points)

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
<span id="post-64962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64962-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>From what I understand, a "way is an ordered list of nodes" that can only have two end points (which may or may not overlap).</p>
<p>How should single roads with multiple end points be treated? It's possible for a road to go a certain direction while having offshoots or loops etc. in different directions. It's a "single" road in the sense that all information for these "parts" is the same (street name, surface, speed limit etc.), so it seems like bad practice to duplicate that information.</p>
<p>See <a href="https://www.openstreetmap.org/way/27784000">this example</a>: the street is incorrectly shown to simply go in and then turn south; in fact, it has that south offshoot, but it continues further in and splits again to two parts. But in every sense, this is a single road: it has the same name, and all addresses along its different parts are on a common numbering system.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '18, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bdd9d6e93d006258d2c39355a29659f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stylianus&#39;s gravatar image" />
<p><span>Stylianus</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stylianus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64962" class="comments-container">
&#10;</div>
<div id="comment-tools-64962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64962-form-container" class="comment-form-container">
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

<span id="64965"></span>

<div id="answer-container-64965" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64965-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please note that a real world street does not correspond to a single OSM way. What you describe is represented by multiple OSM ways, all with the same name.</p>
<p>The opposite is also possible, a simple street represented by multiple OSM ways, because e.g. the road surface is different, the maximum speed changes, etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jul '18, 12:30</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-64965" class="comments-container">
<span id="64967"></span>
<div id="comment-64967" class="comment">
<div id="post-64967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So to confirm, the name/information would need to be duplicated across the different ways and there is no link between them (i.e., a name or tag change on part of that road will not affect the other parts, which need to be updated independently)?</p>
</div>
<div id="comment-64967-info" class="comment-info">
<span class="comment-age">(27 Jul '18, 12:44)</span> <span class="comment-user userinfo">Stylianus</span>
</div>
</div>
<span id="64968"></span>
<div id="comment-64968" class="comment">
<div id="post-64968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15443/stylianus">@Stylianus</a>: yes, that is the usual method. In addition you can group the street parts with e.g. <a href="https://wiki.openstreetmap.org/wiki/Relation:associatedStreet">https://wiki.openstreetmap.org/wiki/Relation:associatedStreet</a> , but this is rather uncommon.</p>
</div>
<div id="comment-64968-info" class="comment-info">
<span class="comment-age">(27 Jul '18, 14:32)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="64975"></span>
<div id="comment-64975" class="comment">
<div id="post-64975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to be clear, the associatedStreet relation mentioned by aseerel4c26 is intended for the purpose of assigning addresses to objects, not as a tidy way of collecting separate ways that compose a single road.</p>
</div>
<div id="comment-64975-info" class="comment-info">
<span class="comment-age">(27 Jul '18, 16:54)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="64976"></span>
<div id="comment-64976" class="comment">
<div id="post-64976-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> thanks, yes, it is rather a side-effect that you collect all parts of <em>one</em> street.</p>
</div>
<div id="comment-64976-info" class="comment-info">
<span class="comment-age">(27 Jul '18, 19:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64965-form-container" class="comment-form-container">
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

