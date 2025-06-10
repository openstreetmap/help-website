+++
type = "question"
title = "Extract nodes from way"
description = '''Hi,  I have an &#x27;way id&#x27; of my route. I want to extract all nodes which belongs to this specific route. I can make a query e.g.: http://api.openstreetmap.org/api/0.6/way/xxxyyzz In response I receive series of node reference id&#x27;s. Then I need to make recursive lookup to search each single point to ge...'''
date = "2010-12-22T18:24:00Z"
lastmod = "2010-12-22T18:41:00Z"
weight = 1896
keywords = [ "api" ]
aliases = [ "/questions/1896" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Extract nodes from way](/questions/1896/extract-nodes-from-way)

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
<span id="post-1896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have an 'way id' of my route. I want to extract all nodes which belongs to this specific route. I can make a query e.g.: <a href="http://api.openstreetmap.org/api/0.6/way/xxxyyzz">http://api.openstreetmap.org/api/0.6/way/xxxyyzz</a> In response I receive series of node reference id's. Then I need to make recursive lookup to search each single point to get GPS data. Do you know automatic tool to extract such data? I will provide way_id and in response get series of GPS coordinates. It is fair easy to write such tool but maybe you know readily available software.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '10, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a1f37da2dbb424bc78b0c0457c80071b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="razor85&#39;s gravatar image" />
<p><span>razor85</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="razor85 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '11, 09:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1896" class="comments-container">
&#10;</div>
<div id="comment-tools-1896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1896-form-container" class="comment-form-container">
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

<span id="1897"></span>

<div id="answer-container-1897" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1897-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="razor85 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an API request that returns the way <em>and</em> all its nodes:</p>
<pre><code>http://api.openstreetmap.org/api/0.6/way/xxxyyzz/full</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '10, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-1897" class="comments-container">
&#10;</div>
<div id="comment-tools-1897" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1897-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1898"></span>

<div id="answer-container-1898" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1898-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download <code>http://api.openstreetmap.org/api/0.6/way/xxxyyzz/full</code> instead of <code>http://api.openstreetmap.org/api/0.6/way/xxxyyzz/</code>. This will contain all the nodes that are in this way, thus avoiding the need for further queries.</p>
<p>You can use something like</p>
<pre><code>wget -q -O - http://api.openstreetmap.org/api/0.6/way/xxxyyzz/full | sed -ne &#39;s/&lt;node.*lat=&quot;\(.*\)&quot; lon=&quot;\(.*\)&quot; version.*/\1 \2/p&#39;</code></pre>
<p>to limit output to the latitude and longitude of the node. (And yes I know that parsing XML with regex is evil.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '10, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-1898" class="comments-container">
&#10;</div>
<div id="comment-tools-1898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1898-form-container" class="comment-form-container">
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

