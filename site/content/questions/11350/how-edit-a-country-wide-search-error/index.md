+++
type = "question"
title = "How edit a country-wide search error?"
description = '''Hi: I&#x27;ve discovered an error every time a search is performed in many places of Costa Rica. No matter what you look for, the result always include &quot;Vázquez de Coronado, San José, Costa Rica&quot;. That place does exist, however it is a specific &quot;city&quot; (Vázquez de Coronado) and a specific &quot;state&quot; (San Jos...'''
date = "2012-03-19T22:02:00Z"
lastmod = "2012-03-20T23:35:00Z"
weight = 11350
keywords = [ "search", "error" ]
aliases = [ "/questions/11350" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How edit a country-wide search error?](/questions/11350/how-edit-a-country-wide-search-error)

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
<span id="post-11350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11350-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi:</p>
<p>I've discovered an error every time a search is performed in many places of Costa Rica. No matter what you look for, the result always include "Vázquez de Coronado, San José, Costa Rica".</p>
<p>That place does exist, however it is a specific "city" (Vázquez de Coronado) and a specific "state" (San José). I've quoted state and city because they're not exactly as they are -for example- in the United States but quite equivalent.</p>
<p>The problem is like if for any search at the USA, "Miami, Florida" appeared.</p>
<p>I wonder if that info was included in the whole country polygon, but I'm not able to edit that.</p>
<p>Any help appreciated.</p>
<p>EXAMPLES:</p>
<p>-- If you look fo the City "San Isidro", in the State of "Heredia", in the country "Costa Rica" I mean, if you look for "San Isidro, Heredia, Costa Rica", I've got as result:</p>
<p>Town San Isidro, Vázquez de Coronado, San José, Costa Rica</p>
<p>-- Looking for: "Manuel Antonio, Quepos, Puntrenas"</p>
<p>OSM returns: Manuel Antonio, Quepos, Vázquez de Coronado, Puntarenas, Costa Rica</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '12, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/69d8b2e35c8b8f9ec1ccace260cc6707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Luis%20Carlos%20Solano&#39;s gravatar image" />
<p><span>Luis Carlos ...</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Luis Carlos Solano has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11350" class="comments-container">
&#10;</div>
<div id="comment-tools-11350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11350-form-container" class="comment-form-container">
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

<span id="11355"></span>

<div id="answer-container-11355" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11355-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To troubleshoot Nominatim search errors, go to <a href="http://nominatim.openstreetmap.org">the Nominatim web site</a> and perform the search. Now on the search results, click on the 'details' link. I believe the problem is that Vázquez de Coronado is placed as a 'region' node and not as a polygon, or as a 'region' instead of a city.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '12, 11:37</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-11355" class="comments-container">
<span id="11374"></span>
<div id="comment-11374" class="comment">
<div id="post-11374-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer, that was the problem. I removed the node, as a polygon already exist.</p>
</div>
<div id="comment-11374-info" class="comment-info">
<span class="comment-age">(20 Mar '12, 23:35)</span> <span class="comment-user userinfo">Luis Carlos ...</span>
</div>
</div>
</div>
<div id="comment-tools-11355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11355-form-container" class="comment-form-container">
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

