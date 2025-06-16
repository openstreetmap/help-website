+++
type = "question"
title = "Finding a way at or around a specific coordinate"
description = '''Hello, i&#x27;ve been experimenting with Overpass and Nominatim for about a day now, but i can&#x27;t seem to find the query that would yield the results i require. I am initially given a coordinate (lat+lon) and need to find the way at this point (later on i will need to find intersections, too). I also need...'''
date = "2014-09-25T09:20:00Z"
lastmod = "2014-10-08T10:36:00Z"
weight = 37048
keywords = [ "overpassapi", "overpass", "reversegeocoding", "way" ]
aliases = [ "/questions/37048" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Finding a way at or around a specific coordinate](/questions/37048/finding-a-way-at-or-around-a-specific-coordinate)

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
<span id="post-37048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37048-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i've been experimenting with Overpass and Nominatim for about a day now, but i can't seem to find the query that would yield the results i require.</p>
<p>I am initially given a coordinate (lat+lon) and need to find the way at this point (later on i will need to find intersections, too). I also need the nodes that make up the way.</p>
<p>All the results i got from overpass were either none, in a bounding box that clearly has a way in it, or they were more than 20 MBs of data, which is clearly too much for the bounding box i used. One of the queries i used was this:</p>
<p>&lt;query type="way"&gt;</p>
<p>&lt;bbox-query e="13.384931" n="52.477775" s="52.476769" w="13.386497"/&gt;</p>
<p>&lt;/query&gt;</p>
<p>&lt;print/&gt;</p>
<p>Can anyone help me with this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '14, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/cf6788cbaa9e98bb14a6241507882ea7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leopard2A5&#39;s gravatar image" />
<p><span>Leopard2A5</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leopard2A5 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37048" class="comments-container">
<span id="37051"></span>
<div id="comment-37051" class="comment">
<div id="post-37051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think what you want is to query</p>
<p>type:way</p>
<p>which will return all ways in a bounding box. Note, it will not return nodes or relations, only ways.</p>
<p>I used the very helpful Query Wizard while you may be using the more demanding Overpass Query Language.</p>
</div>
<div id="comment-37051-info" class="comment-info">
<span class="comment-age">(25 Sep '14, 10:49)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="37053"></span>
<div id="comment-37053" class="comment">
<div id="post-37053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Dave, thx for the reply. I tried the wizard with "type:way" and it returned quite fast, marking all ways on the bbox i was currently looking at. It built the following query:</p>
<p>&lt;osm-script output="json" timeout="25"&gt; &lt;union&gt; &lt;query type="way"&gt; &lt;bbox-query {{bbox}}=""/&gt; &lt;/query&gt; &lt;/union&gt; &lt;print mode="body"/&gt; &lt;recurse type="down"/&gt; &lt;print mode="skeleton" order="quadtile"/&gt; &lt;/osm-script&gt;</p>
<p>however when i replace {{bbox}} with the bbox-spec i'm interested in, the result is empty, allthough the given coordinates contain part of a way: &lt;bbox-query e="13.384931" n="52.477775" s="52.476769" w="13.386497"/&gt;</p>
</div>
<div id="comment-37053-info" class="comment-info">
<span class="comment-age">(25 Sep '14, 11:58)</span> <span class="comment-user userinfo">Leopard2A5</span>
</div>
</div>
</div>
<div id="comment-tools-37048" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37048-form-container" class="comment-form-container">
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

<span id="37055"></span>

<div id="answer-container-37055" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37055-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leopard2A5 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You mixed east and west, <a href="http://overpass-turbo.eu/s/5aP">try</a> this instead:</p>
<pre><code>&lt;bbox-query e=&quot;13.386497&quot; n=&quot;52.477775&quot; s=&quot;52.476769&quot; w=&quot;13.384931&quot;/&gt;</code></pre>
<p>Usually this should be checked by the API but it obviously isn't for some reason.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '14, 13:20</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Sep '14, 13:21</strong> </span></p>
</div>
</div>
<div id="comments-container-37055" class="comments-container">
<span id="37056"></span>
<div id="comment-37056" class="comment">
<div id="post-37056-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><em>facepalm</em> Thanks for noticing that, scai, switching east and west yields the expected results!</p>
</div>
<div id="comment-37056-info" class="comment-info">
<span class="comment-age">(25 Sep '14, 13:31)</span> <span class="comment-user userinfo">Leopard2A5</span>
</div>
</div>
</div>
<div id="comment-tools-37055" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37055-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37076"></span>

<div id="answer-container-37076" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37076-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you need a way around a specific coordinate, you should probably take a look at the Overpass API 'around' filter rather than a bbox query. Bbox is ok'ish, but honestly it doesn't fit your use case all that well.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Relative_to_other_elements_.28around.29">link</a> for more details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '14, 18:13</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-37076" class="comments-container">
<span id="37414"></span>
<div id="comment-37414" class="comment">
<div id="post-37414-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yeah that's even better! thanks mmd!</p>
</div>
<div id="comment-37414-info" class="comment-info">
<span class="comment-age">(08 Oct '14, 10:36)</span> <span class="comment-user userinfo">Leopard2A5</span>
</div>
</div>
</div>
<div id="comment-tools-37076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37076-form-container" class="comment-form-container">
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

