+++
type = "question"
title = "Get center point from Overpass via overpy"
description = '''I&#x27;m trying to get the center point with Python and overpy: api = overpy.Overpass() result = api.query(&quot;&quot;&quot;way(381501602);out center;&quot;&quot;&quot;)  but unlike to Overpass Turbo, where I get the center point 49.2559306 / 8.4525152 overpy just returns all nodes: result.nodes is empty and result.ways contains &amp;lt...'''
date = "2017-10-07T17:19:00Z"
lastmod = "2017-10-07T20:08:00Z"
weight = 59999
keywords = [ "python", "overpy", "overpass-turbo" ]
aliases = [ "/questions/59999" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get center point from Overpass via overpy](/questions/59999/get-center-point-from-overpass-via-overpy)

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
<span id="post-59999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59999-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get the center point with Python and overpy:</p>
<pre><code>api = overpy.Overpass()
result = api.query(&quot;&quot;&quot;way(381501602);out center;&quot;&quot;&quot;)</code></pre>
<p>but unlike to Overpass Turbo, where I get the center point 49.2559306 / 8.4525152 overpy just returns all nodes:</p>
<p>result.nodes is empty and result.ways contains</p>
<pre><code>&lt; overpy.Way id=381501602 nodes=[2338081031, ...]&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpy" rel="tag" title="see questions tagged &#39;overpy&#39;">overpy</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '17, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a1b49c42d8be4b8d87f3096a3622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Druzhba&#39;s gravatar image" />
<p><span>Druzhba</span><br />
<span class="score" title="150 reputation points">150</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Druzhba has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59999" class="comments-container">
&#10;</div>
<div id="comment-tools-59999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59999-form-container" class="comment-form-container">
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

<span id="60002"></span>

<div id="answer-container-60002" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60002-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass appends a center element to the way:</p>
<blockquote>
<p>&lt;?xml version="1.0" encoding="UTF-8"?&gt; &lt;osm version="0.6" generator="Overpass API"&gt; &lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt; &lt;meta osm_base="2017-10-07T18:59:02Z"/&gt; &lt;way id="381501602"&gt; &lt;center lat="49.2559306" lon="8.4525152"/&gt; &lt;nd ref="2338081031"/&gt; &lt;nd ref="2338081030"/&gt;</p>
</blockquote>
<p>You'll have to see if overpy supports this element or not. It seems to: <a href="https://python-overpy.readthedocs.io/en/latest/api.html#elements">https://python-overpy.readthedocs.io/en/latest/api.html#elements</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '17, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '17, 20:09</strong> </span></p>
</div>
</div>
<div id="comments-container-60002" class="comments-container">
&#10;</div>
<div id="comment-tools-60002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60002-form-container" class="comment-form-container">
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

