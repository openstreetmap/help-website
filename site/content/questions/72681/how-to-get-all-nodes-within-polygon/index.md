+++
type = "question"
title = "how to get all nodes within polygon?"
description = '''How can I get a list of all streets and their respective street number from an input polygon (not rectangular) that is defined as langitude and longitude from a csv file? Probably would want to work with overpass api and python here.'''
date = "2020-01-25T22:08:00Z"
lastmod = "2020-01-26T01:17:00Z"
weight = 72681
keywords = [ "python", "overpass", "polygons", "multipolygon" ]
aliases = [ "/questions/72681" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to get all nodes within polygon?](/questions/72681/how-to-get-all-nodes-within-polygon)

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
<span id="post-72681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I get a list of all streets and their respective street number from an input polygon (not rectangular) that is defined as langitude and longitude from a csv file? Probably would want to work with overpass api and python here.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jan '20, 22:08</strong></p>
<img src="https://secure.gravatar.com/avatar/744aa287418e8332fe453528c54c1f22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="montagsmodell&#39;s gravatar image" />
<p><span>montagsmodell</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="montagsmodell has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72681" class="comments-container">
<span id="72682"></span>
<div id="comment-72682" class="comment">
<div id="post-72682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are the co-ordinates in the csv likely to vary or can you copy paste them to Overpass as a one off process?</p>
</div>
<div id="comment-72682-info" class="comment-info">
<span class="comment-age">(25 Jan '20, 22:31)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-72681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72681-form-container" class="comment-form-container">
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

<span id="72683"></span>

<div id="answer-container-72683" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72683-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Pass the coordinates in as part of the query:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_polygon_.28poly.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_polygon_.28poly.29</a></p>
<p>I usually use requests (or just urllib.request) to fetch an Overpass-API script from python, I don't rely on any extra module, so I can't say if one of them supports doing the poly filter.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '20, 23:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-72683" class="comments-container">
&#10;</div>
<div id="comment-tools-72683" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72683-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72684"></span>

<div id="answer-container-72684" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72684-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Uncomment the out:csv line to get a list</p>
<pre><code>   //[out:csv(&quot;addr:street&quot;, &quot;addr:housenumber&quot;; false; &quot;, &quot;)];
    way[highway][name](poly:&quot;51.61268 -0.2871 51.6126 -0.2834 51.6108 -0.2834 51.6108 -0.2871&quot;);
    out geom;
&#10;    foreach-&gt;.highway(
      way[building]
        (around.highway:20)
        [&quot;addr:housenumber&quot;]    
      ;
      out geom;
    );</code></pre>
<p><a href="http://overpass-turbo.eu/s/Q5L">http://overpass-turbo.eu/s/Q5L</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '20, 01:17</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '20, 11:24</strong> </span></p>
</div>
</div>
<div id="comments-container-72684" class="comments-container">
&#10;</div>
<div id="comment-tools-72684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72684-form-container" class="comment-form-container">
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

