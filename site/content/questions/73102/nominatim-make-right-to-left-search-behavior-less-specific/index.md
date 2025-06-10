+++
type = "question"
title = "Nominatim make right to left search behavior less specific"
description = '''The Nominatim docs say that &quot;Free-form queries are processed first left-to-right and then right-to-left if that fails.&quot;.  My understanding is that if query=&quot;part1, part2, part3&quot; fails, it then searches for query=&quot;part3, part2, part1&quot;. What I&#x27;m trying to achieve is if that fails, the database then tr...'''
date = "2020-02-16T12:10:00Z"
lastmod = "2020-02-19T14:35:00Z"
weight = 73102
keywords = [ "nominatim" ]
aliases = [ "/questions/73102" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim make right to left search behavior less specific](/questions/73102/nominatim-make-right-to-left-search-behavior-less-specific)

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
<span id="post-73102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73102-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <a href="https://nominatim.org/release-docs/latest/api/Search/">Nominatim docs</a> say that "Free-form queries are processed first left-to-right and then right-to-left if that fails.". My understanding is that if query="part1, part2, part3" fails, it then searches for query="part3, part2, part1". What I'm trying to achieve is if that fails, the database then tries to return a less specific result so that we get some data.</p>
<p>I've seen multiple cases where query="house number street name, town, city, country" returns no results, but query="street name, town, city, country" or query="town, city, country" returns results. I'd like to get this less specific result without having to do multiple queries.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '20, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0aa6d807c6f317f02f7837c01e2afa7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryaner&#39;s gravatar image" />
<p><span>ryaner</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryaner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73102" class="comments-container">
&#10;</div>
<div id="comment-tools-73102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73102-form-container" class="comment-form-container">
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

<span id="73104"></span>

<div id="answer-container-73104" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73104-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ryaner has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim doesn't support this (yet), it looks for all part of the query. Like spellcheck it's a long requested feature, as old as Nominatim itself (10 years). The next best option is doing multiple queries. If you administer your own Nominatim server you can enable <code>CONST_Search_BatchMode</code> (see <code>search.php</code>) where you can run multiple queries in one request. It's disabled on nominatim.openstreetmap.org</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '20, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-73104" class="comments-container">
<span id="73142"></span>
<div id="comment-73142" class="comment">
<div id="post-73142-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there any way to make the result set fields returned from batch queries match that of a single query? Specifically when querying an address with get back a field called 'class' and via batch that field seems to be called 'category'. The lack of documentation around batch mode means I'm not sure if this is intentional or a bug somewhere?</p>
</div>
<div id="comment-73142-info" class="comment-info">
<span class="comment-age">(19 Feb '20, 14:28)</span> <span class="comment-user userinfo">ryaner</span>
</div>
</div>
<span id="73144"></span>
<div id="comment-73144" class="comment">
<div id="post-73144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's an undocumented and unsupported feature. There is probably a way if you change the PHP source code.</p>
</div>
<div id="comment-73144-info" class="comment-info">
<span class="comment-age">(19 Feb '20, 14:35)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-73104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73104-form-container" class="comment-form-container">
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

