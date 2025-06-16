+++
type = "question"
title = "Why does it show the Spanish name &quot;Pensilvania&quot; in a Nominatim page?"
description = '''This Nominatim page shows the Spanish Pensilvania, instead of Pennsylvania.  In case my Accept-Language is relevant, I have multiple English languages (&quot;en-US&quot;, &quot;en&quot;, &quot;eng&quot;, and more), then eventually &quot;es-es&quot; and &quot;es&quot; lower in the list. EDIT: When I use curl with no Accept-Language headers, it displ...'''
date = "2012-07-15T05:24:00Z"
lastmod = "2012-07-16T14:35:00Z"
weight = 14261
keywords = [ "default", "nominatim", "local", "accept", "language" ]
aliases = [ "/questions/14261" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why does it show the Spanish name "Pensilvania" in a Nominatim page?](/questions/14261/why-does-it-show-the-spanish-name-pensilvania-in-a-nominatim-page)

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
<span id="post-14261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14261-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This <a href="http://nominatim.openstreetmap.org/details.php?place_id=499064">Nominatim page</a> shows the Spanish Pensilvania, instead of Pennsylvania.<br />
</p>
<p>In case my Accept-Language is relevant, I have multiple English languages ("en-US", "en", "eng", and more), then eventually "es-es" and "es" lower in the list.</p>
<p><strong>EDIT</strong>: When I use curl with no Accept-Language headers, it displays the English name. Looking at the <a href="https://www.openstreetmap.org/browse/relation/162109">relation</a> looks like the issue is that <code>name</code> is Pennsylvania, but there is no <code>name:en</code>, probably because English is the primary local language.</p>
<p>My request explicitly allows en (preferred, but there is no name:en) and es (allowed, and there is name:es, but less preferred). What's the best way to address this (let me know if I should ask this follow-up separately)? Should name:en be added even though the local language is English?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-default" rel="tag" title="see questions tagged &#39;default&#39;">default</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-accept" rel="tag" title="see questions tagged &#39;accept&#39;">accept</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '12, 05:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e72946d7c81ee170b322f6e6abae3442?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mattflaschen&#39;s gravatar image" />
<p><span>mattflaschen</span><br />
<span class="score" title="226 reputation points">226</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mattflaschen has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jun '13, 02:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-14261" class="comments-container">
&#10;</div>
<div id="comment-tools-14261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14261-form-container" class="comment-form-container">
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

<span id="14287"></span>

<div id="answer-container-14287" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14287-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-14287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mattflaschen has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem is indeed with the missing name:en tag. Nominatim doesn't know that the name tag in the US should default to English. That is a bug in Nominatim not with your tagging. It is common practice in OSM to leave out the localized name tag (i.e. <code>name:en</code>) if there is only one official language in a country.</p>
<p>Nominatim will update to a new version in a few weeks where the handling of local languages has been improved. So, just ignore the problem for a while and it will hopefully go away by itself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '12, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-14287" class="comments-container">
<span id="14312"></span>
<div id="comment-14312" class="comment">
<div id="post-14312-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hopefully that'll also fix the US state name showing up in Japanese when you search for cities!</p>
</div>
<div id="comment-14312-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 14:35)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-14287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14287-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14268"></span>

<div id="answer-container-14268" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14268-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Dear Mattflaschen, I should use the original name, but I like the different lanquages. This platform however has accepted English as standard for all. Thats all and Pennsylvania should it be.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '12, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-14268" class="comments-container">
&#10;</div>
<div id="comment-tools-14268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14268-form-container" class="comment-form-container">
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

