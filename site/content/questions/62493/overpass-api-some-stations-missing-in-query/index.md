+++
type = "question"
title = "Overpass API: Some stations missing in query"
description = '''I have a query to pull back narrow gauge railways and associated features (stations, crossings etc). Most places it works well, but I have seen a few stations are missing. Here&#x27;s a missing station: https://overpass-turbo.eu/s/wEj When I compare this station to one that works (https://overpass-turbo....'''
date = "2018-03-02T12:43:00Z"
lastmod = "2018-03-02T12:43:00Z"
weight = 62493
keywords = [ "overpassapi", "overpass-api", "overpass-ql" ]
aliases = [ "/questions/62493" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: Some stations missing in query](/questions/62493/overpass-api-some-stations-missing-in-query)

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
<span id="post-62493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62493-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a query to pull back narrow gauge railways and associated features (stations, crossings etc). Most places it works well, but I have seen a few stations are missing.</p>
<p>Here's a missing station: <a href="https://overpass-turbo.eu/s/wEj">https://overpass-turbo.eu/s/wEj</a></p>
<p>When I compare this station to one that works (<a href="https://overpass-turbo.eu/s/wEk),">https://overpass-turbo.eu/s/wEk),</a> their properties look very similar: <a href="https://www.openstreetmap.org/node/1836922925">https://www.openstreetmap.org/node/1836922925</a> (ignored by the query) <a href="https://www.openstreetmap.org/node/471077795">https://www.openstreetmap.org/node/471077795</a> (fetched by the query)</p>
<p>Can anyone tell why this station isn't matched?</p>
<p>To fix I tried to use an <code>(around:20)[railway=station]</code> query applied to all results from my main query, and then filtered to stations, halts etc. It works but when run over a bigger area (country level) is noticeably slower than the original query.</p>
<p><a href="https://overpass-turbo.eu/s/wEn">https://overpass-turbo.eu/s/wEn</a></p>
<p>Is there a faster way to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '18, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/35a2bb718c63cd27b1823ad6721b8f87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20K9&#39;s gravatar image" />
<p><span>Peter K9</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter K9 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62493" class="comments-container">
&#10;</div>
<div id="comment-tools-62493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62493-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

