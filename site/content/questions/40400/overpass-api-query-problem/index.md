+++
type = "question"
title = "Overpass API query problem"
description = '''I have a following query build almost same as the example at :  https://wiki.openstreetmap.org/wiki/Overpass_API It should return all town areas in the given box (second query) that are close to way from a first query, however it return a huuuge list of (?) random (?) towns and I don&#x27;t know what&#x27;s wr...'''
date = "2015-01-15T17:37:00Z"
lastmod = "2015-01-15T18:35:00Z"
weight = 40400
keywords = [ "overpassapi", "query", "area" ]
aliases = [ "/questions/40400" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API query problem](/questions/40400/overpass-api-query-problem)

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
<span id="post-40400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40400-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a following query build almost same as the example at : <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a> It should return all town areas in the given box (second query) that are close to way from a first query, however it return a huuuge list of (?) random (?) towns and I don't know what's wrong</p>
<blockquote>
&lt;query type="way"&gt; &lt;bbox-query n="50.3651" s="50.3498" w="20.013" e="20.0468"/&gt; &lt;has-kv k="highway" v="primary"/&gt; &lt;/query&gt; &lt;bbox-query n="50.3651" s="50.3498" w="20.013" e="20.0468"/&gt; &lt;query type="area"&gt; &lt;has-kv k="place" v="town"/&gt; &lt;/query&gt; &lt;print/&gt;
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '15, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c94180557aecf86091ae161baf7ac008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huberttt&#39;s gravatar image" />
<p><span>huberttt</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huberttt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jan '15, 20:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span></p>
</div>
</div>
<div id="comments-container-40400" class="comments-container">
<span id="40404"></span>
<div id="comment-40404" class="comment">
<div id="post-40404-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>areas are only created for ways and relations, if they have a name (very broadly speaking). However, in your bbox, there's neither a way with place=town nor a relation with the same tagging. Only a single node, but for that one, there's no area as I mentioned.</p>
<p>Can you rephrase a bit what you're trying to do? I didn't quite get it from your question.</p>
<p>The following query would find all nodes with place=town up to 3km distance to your way. That's about the only information you would get in your bbox: <a href="http://overpass-turbo.eu/s/733">http://overpass-turbo.eu/s/733</a></p>
</div>
<div id="comment-40404-info" class="comment-info">
<span class="comment-age">(15 Jan '15, 17:54)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="40405"></span>
<div id="comment-40405" class="comment">
<div id="post-40405-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok, maybe my goal was a bit messy. What my point is: Supposed we have a road ( highway=primary) , I want to find all the towns near that road (within some radius maybe 100-400m)</p>
</div>
<div id="comment-40405-info" class="comment-info">
<span class="comment-age">(15 Jan '15, 17:57)</span> <span class="comment-user userinfo">huberttt</span>
</div>
</div>
<span id="40409"></span>
<div id="comment-40409" class="comment">
<div id="post-40409-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, seems to work pretty nice, suffices. Regards</p>
</div>
<div id="comment-40409-info" class="comment-info">
<span class="comment-age">(15 Jan '15, 18:09)</span> <span class="comment-user userinfo">huberttt</span>
</div>
</div>
<span id="40410"></span>
<div id="comment-40410" class="comment">
<div id="post-40410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And just one more question, what if I would like to list all the cities like before but not in a box ? I'mean for all length of road?</p>
</div>
<div id="comment-40410-info" class="comment-info">
<span class="comment-age">(15 Jan '15, 18:12)</span> <span class="comment-user userinfo">huberttt</span>
</div>
</div>
<span id="40416"></span>
<div id="comment-40416" class="comment">
<div id="post-40416-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The following query will check along ref=7 in Poland (according to the existing relation) - <a href="http://overpass-turbo.eu/s/739">http://overpass-turbo.eu/s/739</a> ... Note that it takes several minutes to run this query.</p>
</div>
<div id="comment-40416-info" class="comment-info">
<span class="comment-age">(15 Jan '15, 18:35)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-40400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40400-form-container" class="comment-form-container">
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

<span id="40412"></span>

<div id="answer-container-40412" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40412-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, you can try and play around a bit with the following query: <a href="http://overpass-turbo.eu/s/734">http://overpass-turbo.eu/s/734</a> - or - <a href="http://overpass-turbo.eu/s/735">http://overpass-turbo.eu/s/735</a> (which includes highways on the map)</p>
<p>It will return all town nodes up to 5000m distance to a highway=primary in your current bbox.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '15, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-40412" class="comments-container">
&#10;</div>
<div id="comment-tools-40412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40412-form-container" class="comment-form-container">
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

