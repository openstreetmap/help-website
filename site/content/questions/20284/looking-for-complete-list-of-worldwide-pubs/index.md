+++
type = "question"
title = "Looking for complete list of worldwide pubs"
description = '''Hi all. It used to be possible to download a complete list of amenity (or other locations) by not specifying a border. It doesn&#x27;t seem to be possible now. How/where can I get a list of all the pubs or [amenity=pub] please? Thanks.'''
date = "2013-02-25T21:49:00Z"
lastmod = "2013-02-27T21:34:00Z"
weight = 20284
keywords = [ "amenity" ]
aliases = [ "/questions/20284" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Looking for complete list of worldwide pubs](/questions/20284/looking-for-complete-list-of-worldwide-pubs)

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
<span id="post-20284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20284-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all.</p>
<p>It used to be possible to download a complete list of amenity (or other locations) by not specifying a border. It doesn't seem to be possible now. How/where can I get a list of all the pubs or [amenity=pub] please?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '13, 21:49</strong></p>
<img src="https://secure.gravatar.com/avatar/d86c5f3df77644d0d28c6a661f897d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twistedfirestarter&#39;s gravatar image" />
<p><span>twistedfires...</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twistedfirestarter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20284" class="comments-container">
&#10;</div>
<div id="comment-tools-20284" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20284-form-container" class="comment-form-container">
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

<span id="20297"></span>

<div id="answer-container-20297" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20297-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible by using the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>. An example query is:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[timeout:900];(node[&quot;amenity&quot;=&quot;pub&quot;];way[&quot;amenity&quot;=&quot;pub&quot;];rel[&quot;amenity&quot;=&quot;pub&quot;];);(._;&gt;;);out;</code></pre>
<p>(copy the link by hand, the parser broke it). But I couldn't test it successfully because I always get a <em>504 Gateway Time-Out</em>. This is also a really heavy query.</p>
<p>An alternative is to get <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">the planet</a> or an <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">extract</a> and use <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> / <a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a> to generate this list.</p>
<p>Also keep in mind that the result will never be a <em>complete</em> list because OSM's data (and any other data available) will never be complete and changes continuously.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '13, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '13, 09:14</strong> </span></p>
</div>
</div>
<div id="comments-container-20297" class="comments-container">
<span id="20298"></span>
<div id="comment-20298" class="comment">
<div id="post-20298-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Thank you for the URL, but it needs an "out" in the end:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[timeout:3600];(node[&quot;amenity&quot;=&quot;pub&quot;];way[&quot;amenity&quot;=&quot;pub&quot;];rel[&quot;amenity&quot;=&quot;pub&quot;];);(._;&gt;;);out;</code></pre>
<p>I've also increased the timeout.</p>
<p>The 504 happens if too much other queries run on the server. You can then try overpass-api.de instead of the rambler instance:</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[timeout:3600];(node[&quot;amenity&quot;=&quot;pub&quot;];way[&quot;amenity&quot;=&quot;pub&quot;];rel[&quot;amenity&quot;=&quot;pub&quot;];);(._;&gt;;);out;</code></pre>
</div>
<div id="comment-20298-info" class="comment-info">
<span class="comment-age">(26 Feb '13, 08:31)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="20299"></span>
<div id="comment-20299" class="comment">
<div id="post-20299-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the information, I updated the query in my answer.</p>
</div>
<div id="comment-20299-info" class="comment-info">
<span class="comment-age">(26 Feb '13, 09:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20338"></span>
<div id="comment-20338" class="comment">
<div id="post-20338-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi guys..thanks a lot. That seems to have worked!</p>
</div>
<div id="comment-20338-info" class="comment-info">
<span class="comment-age">(27 Feb '13, 13:47)</span> <span class="comment-user userinfo">twistedfires...</span>
</div>
</div>
<span id="20354"></span>
<div id="comment-20354" class="comment">
<div id="post-20354-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It would be nice if you accepted the answer then</p>
</div>
<div id="comment-20354-info" class="comment-info">
<span class="comment-age">(27 Feb '13, 21:34)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20297-form-container" class="comment-form-container">
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

