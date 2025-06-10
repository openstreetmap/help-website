+++
type = "question"
title = "Identify limited access areas like theme parks, zoos and military?"
description = '''Hi, is there a generic way to identify these: Access only by fee:  Theme parks Zoos National parks Aquaparks and public swimming pool areas etc  No access:   Military areas  Basically every facility being an &quot;ecosystem in the ecosystem&quot;. In specific I am wondering how these areas got their red bound...'''
date = "2022-11-15T15:42:00Z"
lastmod = "2022-11-16T10:39:00Z"
weight = 86153
keywords = [ "access", "military", "tourism" ]
aliases = [ "/questions/86153" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Identify limited access areas like theme parks, zoos and military?](/questions/86153/identify-limited-access-areas-like-theme-parks-zoos-and-military)

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
<span id="post-86153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86153-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>is there a generic way to identify these:</p>
<p>Access only by fee:</p>
<ul>
<li>Theme parks</li>
<li>Zoos</li>
<li>National parks</li>
<li>Aquaparks and public swimming pool areas</li>
<li>etc</li>
</ul>
<p>No access:</p>
<ul>
<li>Military areas</li>
</ul>
<p>Basically every facility being an "ecosystem in the ecosystem". In specific I am wondering how these areas got their red boundary, as there's no "access" tag value maintained for them or only partially:</p>
<p>Examples:</p>
<p><a href="https://overpass-turbo.eu/s/1nMS">https://overpass-turbo.eu/s/1nMS</a></p>
<p><a href="https://overpass-turbo.eu/s/1nMU">https://overpass-turbo.eu/s/1nMU</a></p>
<p><a href="https://overpass-turbo.eu/s/1nMV">https://overpass-turbo.eu/s/1nMV</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-military" rel="tag" title="see questions tagged &#39;military&#39;">military</span> <span class="post-tag tag-link-tourism" rel="tag" title="see questions tagged &#39;tourism&#39;">tourism</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '22, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/2a79e5dc8f6f8e48ddbc78a9f0f3dcd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stelufl&#39;s gravatar image" />
<p><span>Stelufl</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stelufl has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '22, 15:50</strong> </span></p>
</div>
</div>
<div id="comments-container-86153" class="comments-container">
&#10;</div>
<div id="comment-tools-86153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86153-form-container" class="comment-form-container">
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

<span id="86159"></span>

<div id="answer-container-86159" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86159-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-86159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Stelufl has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "red boundary" isn't derived from an access key in OSM's standard style. The relevant bit of the style definition for zoom seems to be:</p>
<pre><code>https://github.com/gravitystorm/openstreetmap-carto/blob/master/style/landcover.mss#L908</code></pre>
<p>You could query OSM objects that you think might restrict access in this way, such as zoos.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '22, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86159" class="comments-container">
<span id="86160"></span>
<div id="comment-86160" class="comment">
<div id="post-86160-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this is exactly what I was looking for!</p>
</div>
<div id="comment-86160-info" class="comment-info">
<span class="comment-age">(16 Nov '22, 10:39)</span> <span class="comment-user userinfo">Stelufl</span>
</div>
</div>
</div>
<div id="comment-tools-86159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86159-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86157"></span>

<div id="answer-container-86157" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86157-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not aware of a generic way. Access restrictions tend to be tagged more often on ways or barriers than on areas.</p>
<p>By "red boundary" are you referring to something that appears in the "standard" layer on openstreetmap.org? In your first example there are boundaries shown for Heide-Park Resort, and within that for Transsilvanien. As far as I know, that reflects a decision by the maintainers of that style to display the boundary of certain "tourism" areas such as theme parks and zoos in that way. It is not directly related to access restrictions. If you look at other layers such as Cycle Map or Transport Map you can see that not all renderers choose to do the same.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '22, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-86157" class="comments-container">
<span id="86158"></span>
<div id="comment-86158" class="comment">
<div id="post-86158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I was referring to the "red boundaries" illustrated on the standard layer of OSM. These red boundaries seem to be unrelatable to a specific OSM tag, at least not one that I know of. Hence, I was already assuming that the map layer utilized "tourism=theme_park", "tourism=zoo" to draw these red fences as displayed on the map. Thanks for your answer, it helps already.</p>
</div>
<div id="comment-86158-info" class="comment-info">
<span class="comment-age">(16 Nov '22, 10:16)</span> <span class="comment-user userinfo">Stelufl</span>
</div>
</div>
</div>
<div id="comment-tools-86157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86157-form-container" class="comment-form-container">
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

