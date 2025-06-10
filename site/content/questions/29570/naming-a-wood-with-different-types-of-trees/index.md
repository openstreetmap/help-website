+++
type = "question"
title = "Naming a wood with different types of trees"
description = '''It is not uncommon for a named area of woodland to consist of parcels or compartments of different tree types. When these consist of solid blocks of coniferous trees on the one hand, and of broad-leaved deciduous trees on the other, it does not seem to be straightforward to map the complete wood wit...'''
date = "2014-01-03T17:47:00Z"
lastmod = "2014-01-03T19:54:00Z"
weight = 29570
keywords = [ "one_feature_rule", "woodland", "name" ]
aliases = [ "/questions/29570" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Naming a wood with different types of trees](/questions/29570/naming-a-wood-with-different-types-of-trees)

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
<span id="post-29570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29570-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It is not uncommon for a named area of woodland to consist of parcels or compartments of different tree types. When these consist of solid blocks of coniferous trees on the one hand, and of broad-leaved deciduous trees on the other, it does not seem to be straightforward to map the complete wood without duplicating the name. The example I have in mind is <a href="http://www.openstreetmap.org/#map=16/53.1127/-4.1162">Coed Victoria, Llanberis</a>, which consists of oak woodland on the south and spruce plantations to the north.</p>
<p>Has anyone got better ideas of how to map such places than my current attempt?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-one_feature_rule" rel="tag" title="see questions tagged &#39;one_feature_rule&#39;">one_feature_rule</span> <span class="post-tag tag-link-woodland" rel="tag" title="see questions tagged &#39;woodland&#39;">woodland</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '14, 17:47</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-29570" class="comments-container">
&#10;</div>
<div id="comment-tools-29570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29570-form-container" class="comment-form-container">
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

<span id="29571"></span>

<div id="answer-container-29571" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29571-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For starters, I wouldn't distinguish them by using landuse=forest for one and natural=wood for the other, unless you really have just the west parcel used for forestry / harvesting (or whatever your position on the <a href="http://wiki.openstreetmap.org/wiki/Tag:natural=wood#Notes">wood/forest debate</a> may be).</p>
<p>To me, the cleanest way to represent this is a multipolygon relation containing two outer ways. Put the common tags (name=Coed Victoria, source:name=*, natural=wood) on the multipolygon, and the differing tags (wood=*, deciduous=*, coniferous=*) on the individual ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '14, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-29571" class="comments-container">
<span id="29572"></span>
<div id="comment-29572" class="comment">
<div id="post-29572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually I throroughly agree with your first point. Totally on the wood side!</p>
</div>
<div id="comment-29572-info" class="comment-info">
<span class="comment-age">(03 Jan '14, 19:54)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-29571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29571-form-container" class="comment-form-container">
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

