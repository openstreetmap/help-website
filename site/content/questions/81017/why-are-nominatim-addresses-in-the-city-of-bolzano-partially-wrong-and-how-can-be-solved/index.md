+++
type = "question"
title = "Why are Nominatim addresses in the city of Bolzano partially wrong and how can be solved?"
description = '''Hi all! as mentioned in the title, I&#x27;m running into the issue of having wrong display_name for addresses in the city of Bolzano (Italy). To be fair, only a small part of the address is incorrect. Let&#x27;s see with an example: &quot;via Torino 20 Bolzano&quot; (place id 29088043) is resolved as &quot;20, Via Torino, E...'''
date = "2021-07-17T11:37:00Z"
lastmod = "2021-07-17T14:43:00Z"
weight = 81017
keywords = [ "nominatim" ]
aliases = [ "/questions/81017" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why are Nominatim addresses in the city of Bolzano partially wrong and how can be solved?](/questions/81017/why-are-nominatim-addresses-in-the-city-of-bolzano-partially-wrong-and-how-can-be-solved)

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
<span id="post-81017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81017-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all!</p>
<p>as mentioned in the title, I'm running into the issue of having wrong display_name for addresses in the city of Bolzano (Italy). To be fair, only a small part of the address is incorrect.</p>
<p>Let's see with an example: "via Torino 20 Bolzano" (place id 29088043) is resolved as "20, Via Torino, Europa-Novacella, Bolzano, Appiano sulla strada del vino, Bolzano, Trentino-Alto Adige, 39100, Italia" which is mostly correct, the only error is "Appiano sulla strada del vino" in the middle which is absolutely wrong: Appiano is a small town near Bolzano.</p>
<p>How can this problem be solved?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '21, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/592d76467b7b4bc6816fd7e363bddd19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmaridev&#39;s gravatar image" />
<p><span>mmaridev</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmaridev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81017" class="comments-container">
&#10;</div>
<div id="comment-tools-81017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81017-form-container" class="comment-form-container">
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

<span id="81019"></span>

<div id="answer-container-81019" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81019-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-81019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This looks to be due to use of the tag <code>place=municipality</code> on <a href="https://www.openstreetmap.org/node/1576685188">the node</a> for Appiano. See the <a href="https://nominatim.openstreetmap.org/ui/details.html?osmtype=N&amp;osmid=2749577081&amp;class=place">detailed breakdown</a> provided by Nominatim.</p>
<p>I'm not familiar with this tag, but it may be quite widely used in Italy. Recently Sarah Hoffmann (lonvia), the Nominatim maintainer gave <a href="https://2021.stateofthemap.org/sessions/QUHKNR/">a talk</a> in which she broke down some of the problems with tagging which affect Nominatim's results. This may be such an example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '21, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-81019" class="comments-container">
<span id="81020"></span>
<div id="comment-81020" class="comment">
<div id="post-81020-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dear SK53,</p>
<p>thank you for your answer. I edited the node of Appiano and downgraded to the "town" entity and Nominatim now provides street name correctly. Thank you!</p>
</div>
<div id="comment-81020-info" class="comment-info">
<span class="comment-age">(17 Jul '21, 14:43)</span> <span class="comment-user userinfo">mmaridev</span>
</div>
</div>
</div>
<div id="comment-tools-81019" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81019-form-container" class="comment-form-container">
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

