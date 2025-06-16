+++
type = "question"
title = "How to embed a map with activated Content-Security-Policy?"
description = '''Hi, i try to embed a OSM Map via the Share Option on openstreetmap.org If i enable CSP on my Server, the Map will not be loaded. My problem is: I can&#x27;t figure out which Policies are needed so that https://www.openstreetmap.org/export/embed.html will be loaded on my site. I already tried &quot;frame-src &#x27;s...'''
date = "2014-11-05T09:37:00Z"
lastmod = "2014-11-24T08:21:00Z"
weight = 38326
keywords = [ "embed", "csp" ]
aliases = [ "/questions/38326" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to embed a map with activated Content-Security-Policy?](/questions/38326/how-to-embed-a-map-with-activated-content-security-policy)

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
<span id="post-38326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38326-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>i try to embed a OSM Map via the Share Option on openstreetmap.org If i enable CSP on my Server, the Map will not be loaded. My problem is: I can't figure out which Policies are needed so that <a href="https://www.openstreetmap.org/export/embed.html">https://www.openstreetmap.org/export/embed.html</a> will be loaded on my site. I already tried "frame-src 'self' openstreetmap.org; img-src 'self' *.tile.openstreetmap.org" and also "script-src 'self' openstreetmap.org" but nothing helped.</p>
<p>Could someone tell me the correct settings soi can use OSM Maps and activate CSP?</p>
<p>Kind regard</p>
<p>Tapsiturtle</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-embed" rel="tag" title="see questions tagged &#39;embed&#39;">embed</span> <span class="post-tag tag-link-csp" rel="tag" title="see questions tagged &#39;csp&#39;">csp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '14, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/cd353e426fa7ba13b304245528a2ec21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tapsiturtle&#39;s gravatar image" />
<p><span>Tapsiturtle</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tapsiturtle has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38326" class="comments-container">
&#10;</div>
<div id="comment-tools-38326" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38326-form-container" class="comment-form-container">
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

<span id="38742"></span>

<div id="answer-container-38742" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38742-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After trying a bit around it seems that this is helping in .htaccess: Header set Content-Security-Policy "default-src 'self'; frame-src www.openstreetmap.org; style-src 'self'; script-src 'self' www.openstreetmap.org;"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Nov '14, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/cd353e426fa7ba13b304245528a2ec21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tapsiturtle&#39;s gravatar image" />
<p><span>Tapsiturtle</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tapsiturtle has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '14, 12:14</strong> </span></p>
</div>
</div>
<div id="comments-container-38742" class="comments-container">
&#10;</div>
<div id="comment-tools-38742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38742-form-container" class="comment-form-container">
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

