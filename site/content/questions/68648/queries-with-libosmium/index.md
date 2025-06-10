+++
type = "question"
title = "Queries with libosmium"
description = '''I was reading some parts of the doc of this c++ lib, and was wondering if there was a way to query the osm server to get the result (for example) of this query in json:  [out:json][timeout:25]; // gather  results ( // query part for:  “type=route and route=bus”   relation[&quot;type&quot;=&quot;route&quot;][&quot;route&quot;=&quot;bu...'''
date = "2019-04-04T18:46:00Z"
lastmod = "2019-04-05T08:28:00Z"
weight = 68648
keywords = [ "osmium", "c++" ]
aliases = [ "/questions/68648" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Queries with libosmium](/questions/68648/queries-with-libosmium)

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
<span id="post-68648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68648-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was reading some parts of the doc of this c++ lib, and was wondering if there was a way to query the osm server to get the result (for example) of this query in json:</p>
<pre><code> [out:json][timeout:25]; // gather
 results (   // query part for:
 “type=route and route=bus”  
 relation[&quot;type&quot;=&quot;route&quot;][&quot;route&quot;=&quot;bus&quot;]({{bbox}});
 );</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '19, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ade183c36369bbe7c63410792ea63b71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clement&#39;s gravatar image" />
<p><span>Clement</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clement has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Apr '19, 10:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-68648" class="comments-container">
&#10;</div>
<div id="comment-tools-68648" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68648-form-container" class="comment-form-container">
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

<span id="68649"></span>

<div id="answer-container-68649" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Libosmium does not have a networking component, it doesn't talk to any servers. If you want to process the result of the overpass query in your question with libosmium then you'd have to use a different library to execute the HTTP query and then you could feed the response into libosmium for parsing. However, you would not use JSON output for that but raw OSM output - libosmium reads OSM, not JSON.</p>
<p>Libosmium provides you with a framework that would allow you to easily extract all bus routes from a country-wide OSM file or even the planet file, without having to query any servers. The osmium command line utility, which is built with the libosmium library, has a "tags-filter" mode that can do what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '19, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68649" class="comments-container">
<span id="68659"></span>
<div id="comment-68659" class="comment">
<div id="post-68659-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>On Linux and MacOS (but not on Windows), you can give a URL to libosmium instead of a file name and it will use <code>curl</code> in the background to get the data for you. It is still better to use a HTTP library, because the libosmium-internal way doesn't tell you about errors, but for quick-and-dirty code it is rather convenient.</p>
</div>
<div id="comment-68659-info" class="comment-info">
<span class="comment-age">(05 Apr '19, 08:28)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
</div>
<div id="comment-tools-68649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68649-form-container" class="comment-form-container">
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

