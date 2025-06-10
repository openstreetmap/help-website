+++
type = "question"
title = "address standardization using Nominatim search API"
description = '''Hi, is there a way to get back from search API only the address (i.e. without names of businesses in that place etc.) in a normalized way so that if I use different queries that describe the same address I will get the same address. (I&#x27;m trying to link users to their addresses even if they wrote it ...'''
date = "2016-01-05T09:31:00Z"
lastmod = "2016-01-05T17:28:00Z"
weight = 47374
keywords = [ "search", "api", "standardise", "nominatim" ]
aliases = [ "/questions/47374" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [address standardization using Nominatim search API](/questions/47374/address-standardization-using-nominatim-search-api)

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
<span id="post-47374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47374-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, is there a way to get back from search API only the address (i.e. without names of businesses in that place etc.) in a normalized way so that if I use different queries that describe the same address I will get the same address.</p>
<p>(I'm trying to link users to their addresses even if they wrote it differently on different sites)</p>
<p>edit:</p>
<p>my desired flow: 1. I'm getting a single line address (from a 3-party provider so I have no control of its structure) 2. I will use this address as a query for the search API (or a different API if there's a more suitable one) 3. the response should be a single normalized address (I don't care what's in that address) 4. by normalized I mean that if I a address is "&lt;description&gt;,CA" and one is "&lt;same description=""&gt;, California" I will get the same response 5. finnaly I will store the result in a DB.</p>
<p>can I achieve this with the search API? do I need another API? are there parameters I should use in my request to achieve this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-standardise" rel="tag" title="see questions tagged &#39;standardise&#39;">standardise</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '16, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/3b651b42a86cf4c00f2c9570aa1e1206?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tal_joffe&#39;s gravatar image" />
<p><span>tal_joffe</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tal_joffe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jan '16, 07:16</strong> </span></p>
</div>
</div>
<div id="comments-container-47374" class="comments-container">
<span id="47380"></span>
<div id="comment-47380" class="comment">
<div id="post-47380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, please EDIT your question and give us an example step-by-step what you want to achieve. Otherwise your question is too abstract, IMHO.</p>
</div>
<div id="comment-47380-info" class="comment-info">
<span class="comment-age">(05 Jan '16, 17:28)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-47374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47374-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

