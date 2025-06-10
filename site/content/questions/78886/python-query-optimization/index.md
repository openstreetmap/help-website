+++
type = "question"
title = "Python query optimization"
description = '''I constructed a python query to look for all the bus routes passing by a given box. However, I need to speed up the query as much as possible. I only need the lat/lon coordinates of each node representing the bus stops and the name of the routes that they belong to. My current code: import requests ...'''
date = "2021-02-16T17:51:00Z"
lastmod = "2021-02-22T11:17:00Z"
weight = 78886
keywords = [ "python", "query", "optimization", "busstops", "busroutes" ]
aliases = [ "/questions/78886" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Python query optimization](/questions/78886/python-query-optimization)

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
<span id="post-78886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78886-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I constructed a python query to look for all the bus routes passing by a given box. However, I need to speed up the query as much as possible. I only need the lat/lon coordinates of each node representing the bus stops and the name of the routes that they belong to. My current code:</p>
<pre><code>import requests
&#10;overpass_url = &quot;http://overpass-api.de/api/interpreter&quot;
&#10;bbox = [48.87542724909715, 2.1707384550740683, 48.88884184835508, 2.1821696229817267]
bbox_str = &#39;(&#39;+str(bbox)[1:-1]+&#39;)&#39;
&#10;overpass_query = &#39;&#39;&#39;
[out:json];
(
relation&#39;&#39;&#39;+bbox_str+&#39;&#39;&#39;[&#39;route&#39;=&#39;bus&#39;];
);
out body;
&gt;;
out skel;
&#39;&#39;&#39;
&#10;response = requests.get(overpass_url, params={&#39;data&#39;: overpass_query})
data = response.json()</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-optimization" rel="tag" title="see questions tagged &#39;optimization&#39;">optimization</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-busroutes" rel="tag" title="see questions tagged &#39;busroutes&#39;">busroutes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '21, 17:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a09dbb622f7d7cd28396951b306e2c60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fragodec&#39;s gravatar image" />
<p><span>fragodec</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fragodec has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '21, 17:53</strong> </span></p>
</div>
</div>
<div id="comments-container-78886" class="comments-container">
&#10;</div>
<div id="comment-tools-78886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78886-form-container" class="comment-form-container">
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

<span id="78961"></span>

<div id="answer-container-78961" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78961-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know if it is more efficient and/or faster but you could search for every bus stop in a given bounding box and then recurse back to the relations that have that stop as member:</p>
<pre><code>[out:json][timeout:25];
&#10;// query part for: “highway=bus_stop”
node[&quot;highway&quot;=&quot;bus_stop&quot;]({{bbox}})-&gt;.stops;
&#10;foreach.stops -&gt;.s(
&#10;  //get the route (stop must be a member!)
  rel(bn.s)[type=route]-&gt;.r;
&#10;  //produce output
  make stop name = s.u(t[&quot;name&quot;]),
  lat = s.u(lat()), 
  lon = s.u(lon()),
  lines = r.set(t[&quot;ref&quot;]);
&#10;  //print
  out meta;     
);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '21, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9c8957ccf79025bf749665ebec2bdfa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcoR&#39;s gravatar image" />
<p><span>MarcoR</span><br />
<span class="score" title="687 reputation points">687</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcoR has 5 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78961" class="comments-container">
<span id="78985"></span>
<div id="comment-78985" class="comment">
<div id="post-78985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. This works fine but unfortunately it is slower than my code (with the examples I tried).</p>
</div>
<div id="comment-78985-info" class="comment-info">
<span class="comment-age">(22 Feb '21, 11:17)</span> <span class="comment-user userinfo">fragodec</span>
</div>
</div>
</div>
<div id="comment-tools-78961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78961-form-container" class="comment-form-container">
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

