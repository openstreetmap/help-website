+++
type = "question"
title = "How to optimize requests on ways?"
description = '''Hi, I am sending this type of requests to Overpass API (http://overpass-turbo.eu/s/8p9): http://overpass-api.de/api/interpreter?data= [out:json][timeout:7]; (  way(around:5000,48.9,2.4)  [&quot;highway&quot;~&quot;cycleway|footway|path|track&quot;]  [&quot;access&quot;!=&quot;private&quot;] ); out geom;  It retrieves ways around a certain...'''
date = "2015-03-24T20:59:00Z"
lastmod = "2015-03-28T10:37:00Z"
weight = 41893
keywords = [ "overpassapi", "overpass", "optimization", "request", "overpass-api" ]
aliases = [ "/questions/41893" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to optimize requests on ways?](/questions/41893/how-to-optimize-requests-on-ways)

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
<span id="post-41893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41893-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am sending this type of requests to Overpass API (<a href="http://overpass-turbo.eu/s/8p9">http://overpass-turbo.eu/s/8p9</a>):</p>
<pre><code>http://overpass-api.de/api/interpreter?data=
[out:json][timeout:7]; (
    way(around:5000,48.9,2.4)
    [&quot;highway&quot;~&quot;cycleway|footway|path|track&quot;]
    [&quot;access&quot;!=&quot;private&quot;]
);
out geom;</code></pre>
<p>It retrieves ways around a certain set of lat/lon. And it works well as long as the number of results is reasonable. Otherwise, the timeout is reached quite easily. For this particular example, the limit seems to be 383 elements in the returned object.</p>
<p>I only need the end nodes's coordinates, i.e. <code>elements.bounds</code>, as well as <code>tags.highway</code>. In this context, do you have any idea I could optimize this request? Maybe only requesting certain elements of the default returned object if it's possible</p>
<p>Cheers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-optimization" rel="tag" title="see questions tagged &#39;optimization&#39;">optimization</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '15, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/3f17e1d05ec06cc86323ad66a30186b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="agaudin&#39;s gravatar image" />
<p><span>agaudin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="agaudin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '15, 21:08</strong> </span></p>
</div>
</div>
<div id="comments-container-41893" class="comments-container">
<span id="41924"></span>
<div id="comment-41924" class="comment">
<div id="post-41924-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What's the problem with enlarging the timeout? A 5 km radius is about 78.5 km². In a city, there's quite a lot of data in there.</p>
<p>The example you give seems to return about 2MB of data, which is too much for a 7 seconds timeout.</p>
<p>One thing I could propose is to avoid the regex. It's perfectly possible to put that query in a union instead of with a regex. But that still won't make it faster than 7 seconds. Also sorting the output per quadtile won't help enough.</p>
</div>
<div id="comment-41924-info" class="comment-info">
<span class="comment-age">(26 Mar '15, 13:15)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="41928"></span>
<div id="comment-41928" class="comment">
<div id="post-41928-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This code is meant to be part of an app and I don't want the user to wait for too long (&lt;7 seconds). Yes, I am aware of the size returned, that's why I want to exclude unuseful elements. If need be, I'd be fine if the API returns all the elements found during the timeout instead of returning an error if not finished. Is that possible?</p>
<p>Thanks for your advice on the request using unions and quadtile sorting. I'm gonna try this.</p>
</div>
<div id="comment-41928-info" class="comment-info">
<span class="comment-age">(26 Mar '15, 17:17)</span> <span class="comment-user userinfo">agaudin</span>
</div>
</div>
</div>
<div id="comment-tools-41893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41893-form-container" class="comment-form-container">
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

<span id="41954"></span>

<div id="answer-container-41954" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41954-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="agaudin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your app can handle partial results, you could introduce several <code>out geom;</code> statements. Overpass turbo will only show the final result, but when using wget, you'll notice that the download will start almost immediately: <a href="http://overpass-turbo.eu/s/8r6">http://overpass-turbo.eu/s/8r6</a> .</p>
<p>Another strategy could be to split your area into several smaller chunks and load them one by one. First results are available very early so your user won't have to wait for 10+ seconds for a first glimpse of a way.</p>
<p>Currently, there's no way to take the length of a way into account, so filtering by "short" or "long" ways is not possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '15, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-41954" class="comments-container">
&#10;</div>
<div id="comment-tools-41954" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41954-form-container" class="comment-form-container">
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

