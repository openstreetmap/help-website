+++
type = "question"
title = "Nominatim keyord for italian missing"
description = '''Hi all, Where can I add keyword translations for search terms nominatim?  An example: If I look for &quot;ufficio postale&quot; I correctly find post offices in the area I&#x27;m considering Instead, if I look for &quot;farmacia&quot; I dont&#x27; find the pharmacies (and I find them if I look for &quot;pharmacy&quot;) So I guess that som...'''
date = "2020-05-15T08:44:00Z"
lastmod = "2020-05-15T12:14:00Z"
weight = 74825
keywords = [ "translation", "nominatim", "keyword", "loalization" ]
aliases = [ "/questions/74825" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim keyord for italian missing](/questions/74825/nominatim-keyord-for-italian-missing)

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
<span id="post-74825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74825-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>Where can I add keyword translations for search terms nominatim?</p>
<p>An example: If I look for "ufficio postale" I correctly find post offices in the area I'm considering Instead, if I look for "farmacia" I dont' find the pharmacies (and I find them if I look for "pharmacy")</p>
<p>So I guess that someone inserted the correspondence of "uffcio postale" to postoffices ameneties, while this correpsondece for pharamcies is missing</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-translation" rel="tag" title="see questions tagged &#39;translation&#39;">translation</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-keyword" rel="tag" title="see questions tagged &#39;keyword&#39;">keyword</span> <span class="post-tag tag-link-loalization" rel="tag" title="see questions tagged &#39;loalization&#39;">loalization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '20, 08:44</strong></p>
<img src="https://secure.gravatar.com/avatar/45814029815083fa610e054e4c079a3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="livmilan&#39;s gravatar image" />
<p><span>livmilan</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="livmilan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74825" class="comments-container">
<span id="74828"></span>
<div id="comment-74828" class="comment">
<div id="post-74828-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I found out that if i search for example: "farmacie a Pioltello" where Pioltello is a tow, it works, while if I look for "farmacie, Pioltello" it doesn't work. I found the tranlsations in <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/IT">https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/IT</a> and they are correct. It's a question of how the search query is written, apparently.</p>
<p>I still don't understand why the post office query works...</p>
</div>
<div id="comment-74828-info" class="comment-info">
<span class="comment-age">(15 May '20, 10:14)</span> <span class="comment-user userinfo">livmilan</span>
</div>
</div>
</div>
<div id="comment-tools-74825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74825-form-container" class="comment-form-container">
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

<span id="74829"></span>

<div id="answer-container-74829" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74829-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're looking at the right file, the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/IT">https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/IT</a> list has those translatations. "farmacia" and "farmacie". For combination with a place it's best to add an 'in' or 'nearby' ("a" in Italian?).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '20, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74829" class="comments-container">
&#10;</div>
<div id="comment-tools-74829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74829-form-container" class="comment-form-container">
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

