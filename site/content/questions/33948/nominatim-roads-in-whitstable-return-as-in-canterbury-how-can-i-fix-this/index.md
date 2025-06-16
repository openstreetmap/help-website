+++
type = "question"
title = "Nominatim - Roads in Whitstable return as in Canterbury - how can I fix this?"
description = '''I&#x27;ve been looking at some roads in Whitstable after I was asked why Nominatim incorrectly shows them as being in Canterbury. For example Beechcroft, Thanet Way, Chestfield Road Clearly these roads are a part of Whitstable yet Nominatim seems to favour Canterbury which, based upon local knowledge, is...'''
date = "2014-06-13T10:40:00Z"
lastmod = "2014-06-13T16:53:00Z"
weight = 33948
keywords = [ "wrong", "nominatim", "address" ]
aliases = [ "/questions/33948" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - Roads in Whitstable return as in Canterbury - how can I fix this?](/questions/33948/nominatim-roads-in-whitstable-return-as-in-canterbury-how-can-i-fix-this)

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
<span id="post-33948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33948-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been looking at some roads in Whitstable after I was asked why Nominatim incorrectly shows them as being in Canterbury. For example <a href="http://nominatim.openstreetmap.org/details.php?place_id=20164214">Beechcroft</a>, <a href="http://nominatim.openstreetmap.org/details.php?place_id=21614737">Thanet Way</a>, <a href="http://nominatim.openstreetmap.org/details.php?place_id=96262258">Chestfield Road</a></p>
<p>Clearly these roads are a part of <a href="http://nominatim.openstreetmap.org/details.php?place_id=5995103518">Whitstable</a> yet Nominatim seems to favour <a href="http://nominatim.openstreetmap.org/details.php?place_id=97774540">Canterbury</a> which, based upon local knowledge, is wrong. I'm unsure of the best method of resolving it having never amended OSM data of this kind and so any guidance/explanation would be appreciated. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '14, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/68791600aba005984a3eddbd82f6c0ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Elliveny&#39;s gravatar image" />
<p><span>Elliveny</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Elliveny has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33948" class="comments-container">
&#10;</div>
<div id="comment-tools-33948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33948-form-container" class="comment-form-container">
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

<span id="33954"></span>

<div id="answer-container-33954" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33954-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reason is that the street is within the boundary relation Chestfield CP <a href="https://www.openstreetmap.org/relation/2565513,">https://www.openstreetmap.org/relation/2565513,</a> which is part of the relation Canterbury <a href="https://www.openstreetmap.org/relation/448590">https://www.openstreetmap.org/relation/448590</a></p>
<p>There is a relation for the boundary of Whitstable, <a href="https://www.openstreetmap.org/relation/2513976#map=13/51.3533/1.0340,">https://www.openstreetmap.org/relation/2513976#map=13/51.3533/1.0340,</a> but it does not have an admin_level tag. This might make sense, because there is a note "does not exist as administrative unit"</p>
<p>The "normal" solution would be to have a correctly mapped boundary-relation of Whitstable around the street. However, in this case the previous mappers have a different opinion than you about the town. I would get in touch with the editors of those 3 relations and see what's the thruth</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '14, 16:53</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '14, 18:46</strong> </span></p>
</div>
</div>
<div id="comments-container-33954" class="comments-container">
&#10;</div>
<div id="comment-tools-33954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33954-form-container" class="comment-form-container">
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

