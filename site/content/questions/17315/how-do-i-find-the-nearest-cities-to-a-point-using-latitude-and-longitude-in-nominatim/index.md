+++
type = "question"
title = "How do I find the nearest cities to a point using latitude and longitude in nominatim?"
description = '''The thing is I need to know that both moves away from a city and that both approaches another, but the search just gives me the data where it is, I need to do this search the names of the two nearest cities. http://nominatim.openstreetmap.org/search?q=co+4.17897295000,-73.70788536667&amp;amp;format=xml&amp;...'''
date = "2012-10-30T22:29:00Z"
lastmod = "2012-10-31T14:56:00Z"
weight = 17315
keywords = [ "openstreetmap", "query", "nominatim", "osm", "streetnames" ]
aliases = [ "/questions/17315" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I find the nearest cities to a point using latitude and longitude in nominatim?](/questions/17315/how-do-i-find-the-nearest-cities-to-a-point-using-latitude-and-longitude-in-nominatim)

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
<span id="post-17315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17315-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The thing is I need to know that both moves away from a city and that both approaches another, but the search just gives me the data where it is, I need to do this search the names of the two nearest cities.</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=co+4.17897295000,-73.70788536667&amp;format=xml&amp;addressdetails=1">http://nominatim.openstreetmap.org/search?q=co+4.17897295000,-73.70788536667&amp;format=xml&amp;addressdetails=1</a></p>
<p>How do I do this query?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '12, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f155a43fd85ea4fdfa2e76d2b634f2e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="diegoug&#39;s gravatar image" />
<p><span>diegoug</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="diegoug has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17315" class="comments-container">
&#10;</div>
<div id="comment-tools-17315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17315-form-container" class="comment-form-container">
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

<span id="17327"></span>

<div id="answer-container-17327" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17327-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim is an address search engine and not really suited for your purpose. You are looking for another kind of search and <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> seems to fit a lot better.</p>
<p>Take a look at this example query for all place nodes in the area you mentioned:</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json];node[&quot;place&quot;](4.14,-73.73,4.21,-73.67);out;</code></pre>
<p>Note that this query only searches for nodes, you want to search for ways, too, to find every city. If the query doesn't return anything for a specific area, try increasing the given bounding box. You can also choose a different output format, just take a look at the documentation and the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">examples</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '12, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17327" class="comments-container">
&#10;</div>
<div id="comment-tools-17327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17327-form-container" class="comment-form-container">
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

