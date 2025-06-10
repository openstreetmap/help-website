+++
type = "question"
title = "How to tag a building that different levels have different names and uses?"
description = '''I am about to tag a building in a university campus, of which the first level is a public bathroom, and the remaining levels (2nd level to 5th level) consitute a dormitory. The dormitory and public bathroom have their own entrance respectively, with no direct access between the two amenity, which me...'''
date = "2012-03-30T17:43:00Z"
lastmod = "2012-03-31T17:48:00Z"
weight = 11653
keywords = [ "building", "tagging" ]
aliases = [ "/questions/11653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a building that different levels have different names and uses?](/questions/11653/how-to-tag-a-building-that-different-levels-have-different-names-and-uses)

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
<span id="post-11653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11653-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am about to tag a building in a university campus, of which the first level is a public bathroom, and the remaining levels (2nd level to 5th level) consitute a dormitory. The dormitory and public bathroom have their own entrance respectively, with no direct access between the two amenity, which means that if someone in the dormitory wants to take a shower, he/she must leave the building first, walk to the other side of the building, and then enter the public bathroom. Moreover, only portions of the building have 5 levels -- there exist parts with only one level that used by the public bathroom. Is it okay to tag the two amenity respectively with building=* or building:part=yes, or just tag a building with no name, and then tag the two entrances respectively?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '12, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/129c9ce137c91c74cb3f1d84945e6a7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zzcolin&#39;s gravatar image" />
<p><span>zzcolin</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zzcolin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11653" class="comments-container">
&#10;</div>
<div id="comment-tools-11653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11653-form-container" class="comment-form-container">
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

<span id="11662"></span>

<div id="answer-container-11662" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11662-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Okay, we have two separate issues here. It sounds to me like the building as a whole would be tagged <code>building=dormitory</code> with the name of the building (assuming it has only one)</p>
<p>1) Separate entrances can be tagged with <code>building=entrance</code> and <code>entrance=</code> (the wiki encourages you to use <code>entrance</code> alone, but I prefer to have <code>building=entrance</code> too). Notes or <code>amenity</code> nodes can be used to indicate which is which. 2) If you want to indicate the structural "shape" of the building, now, it gets more complicated. The way I understand the <code>building:part=</code> documentation (which seems to me like ), these are added "on top" of the <code>building=</code> tag and receive the descriptive tags (e.g. <code>height</code> and <code>building:levels</code>), with <code>building:parts=</code> added to the same way as the main <code>building=dormitory</code> to tell whether the spli is horizontal or vertical.</p>
<p>If you do use <code>building=part</code>, then each separate part can get <code>amenity</code> tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '12, 17:48</strong></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Circeus has 2 accepted answers">7%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Mar '12, 17:53</strong> </span></p>
</div>
</div>
<div id="comments-container-11662" class="comments-container">
&#10;</div>
<div id="comment-tools-11662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11662-form-container" class="comment-form-container">
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

