+++
type = "question"
title = "what does access tag vehicle = no"
description = '''What does vehicle = &quot;no&quot; mean? documentation says that vehicle tag is for access permission for all vehicles. So, I assume when it says vehicle = &quot;yes&quot;, it means that all types of vehicles like trucks, cars, buses, emergency vehicles, bicycles, etc... have access. But what does vehicle = &quot;no&quot; mean? ...'''
date = "2013-03-12T18:49:00Z"
lastmod = "2013-03-12T22:54:00Z"
weight = 20675
keywords = [ "vehicle", "tags" ]
aliases = [ "/questions/20675" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [what does access tag vehicle = no](/questions/20675/what-does-access-tag-vehicle-no)

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
<span id="post-20675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20675-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What does vehicle = "no" mean? documentation says that vehicle tag is for access permission for all vehicles. So, I assume when it says vehicle = "yes", it means that all types of vehicles like trucks, cars, buses, emergency vehicles, bicycles, etc... have access. But what does vehicle = "no" mean? does it mean that not "all" types have access or "NO" types of vehicles allowed? If its not types of vehicles, does that include bicycles, pedestrians? or is it just motorized vehicles?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-vehicle" rel="tag" title="see questions tagged &#39;vehicle&#39;">vehicle</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '13, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20675" class="comments-container">
&#10;</div>
<div id="comment-tools-20675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20675-form-container" class="comment-form-container">
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

<span id="20682"></span>

<div id="answer-container-20682" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20682-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The wiki page about the access key has a nice <a href="https://wiki.openstreetmap.org/wiki/Key:access#Transport_mode_restrictions">transportation mode hierarchy</a>. The tree shows that the <em>vehicle</em> key both includes <em>motorized vehicles</em> and <em>non-motorized vehicles</em> but not pedestrians.</p>
<p><em>vehicle=no</em> forbids <em>all</em> motorized and non-motorized vehicles <em>unless</em> specified otherwise.</p>
<p><em>vehicle=yes</em> allows <em>all</em> motorized and non-motorized vehicles <em>unless</em> specified otherwise.</p>
<p>Examples:</p>
<ul>
<li><em>vehicle=no</em>, <em>psv=yes</em> would forbid <em>all</em> motorized and non-motorized vehicles <em>except</em> those for public services (bus, taxi)</li>
<li><em>vehicle=yes</em>, <em>hgv=no</em> would allow <em>all</em> motorized and non-motorized vehicles <em>except</em> heavy goods vehicles</li>
</ul>
<p>Update:</p>
<p><span><span>@Andy</span></span> I'm going to reply to your comment in my question because more users might be interested in country-specific access restrictions. The wiki has a whole page about <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">default and country-specific implicit access restrictions</a>. But I don't know of any worldwide (online) router taking care of all these different rules. Most of them will just use the default access restrictions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '13, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '13, 07:25</strong> </span></p>
</div>
</div>
<div id="comments-container-20682" class="comments-container">
<span id="20684"></span>
<div id="comment-20684" class="comment">
<div id="post-20684-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>An exceptions in England if not other countries is bridleways do not allow vehicles but do allow cycles, foot and horses. Motorways sensibly exclude cycles, foot and horses which I assume applies in the most of Europe, or does it?</p>
</div>
<div id="comment-20684-info" class="comment-info">
<span class="comment-age">(12 Mar '13, 22:54)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-20682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20682-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20679"></span>

<div id="answer-container-20679" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20679-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>vehicle=no means no vehicles are allowed. "Vehicles" generally includes bicycles, but excludes wheelchairs and strollers. A pedestrian is not a vehicle.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '13, 20:53</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Mar '13, 23:09</strong> </span></p>
</div>
</div>
<div id="comments-container-20679" class="comments-container">
<span id="20681"></span>
<div id="comment-20681" class="comment">
<div id="post-20681-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-20681-info" class="comment-info">
<span class="comment-age">(12 Mar '13, 21:09)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
</div>
<div id="comment-tools-20679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20679-form-container" class="comment-form-container">
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

