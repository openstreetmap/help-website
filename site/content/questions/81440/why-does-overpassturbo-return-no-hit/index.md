+++
type = "question"
title = "Why does OverpassTurbo return no hit?"
description = '''Hello, I&#x27;m puzzled as to why OT returns no hit for this road that is in OSM. Any idea? Thank you. '''
date = "2021-08-24T13:58:00Z"
lastmod = "2021-08-24T18:50:00Z"
weight = 81440
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/81440" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does OverpassTurbo return no hit?](/questions/81440/why-does-overpassturbo-return-no-hit)

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
<span id="post-81440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81440-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm puzzled as to why OT returns no hit for <a href="https://www.openstreetmap.org/way/6925059#map=15/51.8391/5.5973">this road</a> that <em>is</em> in OSM.</p>
<p>Any idea?</p>
<p>Thank you.</p>
<p><img src="https://i.postimg.cc/QdQ6y8PQ/image.png" alt="https://i.postimg.cc/QdQ6y8PQ/image.png" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '21, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/222fc1ad4f1993620a21cb57fa816f16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shohreh&#39;s gravatar image" />
<p><span>Shohreh</span><br />
<span class="score" title="85 reputation points">85</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shohreh has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-81440" class="comments-container">
&#10;</div>
<div id="comment-tools-81440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81440-form-container" class="comment-form-container">
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

<span id="81442"></span>

<div id="answer-container-81442" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81442-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Shohreh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to your screenshot your query just consists of one large comment. Comments start with <code>/*</code> and end with <code>*/</code>. Somehow you managed to delete the last part, so that the automatically added comment from the wizard never ends.</p>
<p>To fix this, either add a <code>*/</code> at the end of your forth line. Or remove everything before the start of your query, i.e. everything before <code>[out:json]...</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '21, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-81442" class="comments-container">
<span id="81447"></span>
<div id="comment-81447" class="comment">
<div id="post-81447-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sharp eyes!</p>
<p>It's odd that OT didn't complain that the /* had no closing section, though.</p>
<p>Thank you.</p>
<p><img src="https://i.postimg.cc/DyjgypVJ/image.png" alt="https://i.postimg.cc/DyjgypVJ/image.png" /></p>
</div>
<div id="comment-81447-info" class="comment-info">
<span class="comment-age">(24 Aug '21, 18:50)</span> <span class="comment-user userinfo">Shohreh</span>
</div>
</div>
</div>
<div id="comment-tools-81442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81442-form-container" class="comment-form-container">
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

