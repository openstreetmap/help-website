+++
type = "question"
title = "How to add User-Agent to GMap Interface"
description = '''Hello Everyone, I am trying to access OpenStreetMaps as my Map Provider through the GMaps interface, however I am getting a &quot;Exception: The remote server returned an error: (403) Forbidden&quot; I believe this is because I do not have the User-Agent or Referrer set. Can anyone please show me an example o...'''
date = "2019-06-25T20:47:00Z"
lastmod = "2019-06-26T08:15:00Z"
weight = 69749
keywords = [ "error403", "http_403_forbidden", "gmap" ]
aliases = [ "/questions/69749" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add User-Agent to GMap Interface](/questions/69749/how-to-add-user-agent-to-gmap-interface)

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
<span id="post-69749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69749-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Everyone,</p>
<p>I am trying to access OpenStreetMaps as my Map Provider through the GMaps interface, however I am getting a "Exception: The remote server returned an error: (403) Forbidden" I believe this is because I do not have the User-Agent or Referrer set.</p>
<p>Can anyone please show me an example of how I would set the User-Agent using the GMap interface.</p>
<p>Using WPF c#</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error403" rel="tag" title="see questions tagged &#39;error403&#39;">error403</span> <span class="post-tag tag-link-http_403_forbidden" rel="tag" title="see questions tagged &#39;http_403_forbidden&#39;">http_403_forbidden</span> <span class="post-tag tag-link-gmap" rel="tag" title="see questions tagged &#39;gmap&#39;">gmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '19, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/99432b53dc14b5be65324eaf08a01a95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cferreira1992&#39;s gravatar image" />
<p><span>cferreira1992</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cferreira1992 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69749" class="comments-container">
&#10;</div>
<div id="comment-tools-69749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69749-form-container" class="comment-form-container">
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

<span id="69750"></span>

<div id="answer-container-69750" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69750-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not familiar with GMap but according to <a href="http://google.de/">the Internet</a> you can use something like:</p>
<pre><code>GMap.NET.MapProviders.OpenStreetMapProvider.UserAgent = &quot;cferreira GMap tool 1.0&quot;;</code></pre>
<p>or</p>
<pre><code>GMap.NET.MapProviders.GMapProvider.UserAgent = &quot;cferreira GMap tool 1.0&quot;;</code></pre>
<p>Unsure which one works, please come back and tell us.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '19, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69750" class="comments-container">
&#10;</div>
<div id="comment-tools-69750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69750-form-container" class="comment-form-container">
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

