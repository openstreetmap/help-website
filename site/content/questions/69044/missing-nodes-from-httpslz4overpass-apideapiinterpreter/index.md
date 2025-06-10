+++
type = "question"
title = "Missing nodes from https://lz4.overpass-api.de/api/interpreter"
description = '''I&#x27;m trying to download xml data giving a coordenates from my page calling to &quot;https://overpass-api.de/api/map?bbox=-0.678492,39.657480,-0.665617,39.667391&quot;. After this I get the map.osm file. The problem begins when I call to the page mentioned above several times in a few time (maybe 10 times in 8-...'''
date = "2019-05-02T13:04:00Z"
lastmod = "2019-05-04T12:19:00Z"
weight = 69044
keywords = [ "overpassapi", "nodes", "http429", "overpass-api", "missing" ]
aliases = [ "/questions/69044" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing nodes from https://lz4.overpass-api.de/api/interpreter](/questions/69044/missing-nodes-from-httpslz4overpass-apideapiinterpreter)

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
<span id="post-69044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69044-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to download xml data giving a coordenates from my page calling to "https://overpass-api.de/api/map?bbox=-0.678492,39.657480,-0.665617,39.667391". After this I get the map.osm file.</p>
<p>The problem begins when I call to the page mentioned above several times in a few time (maybe 10 times in 8-10 minutes). When I do this, I get (not always) a "failed to open stream: HTTP request failed! HTTP/1.1 429 Too Many Requests" error in my php script. This is the map I get when it works: <img src="https://help.openstreetmap.org/upfiles/osm-ok.jpg" alt="alt text" /></p>
<p>So, as a second option I tried to call to "https://lz4.overpass-api.de/api/interpreter?data=[bbox];(node;way;relation;);out%20bb;&amp;bbox=-0.678492,39.657480,-0.665617,39.667391" in order to avoid the error on the previous URL. The problem doing this is that the downloaded map.osm file seems to miss some nodes, so they can't be found when drawing map. This is the map I get from this URL: <img src="https://help.openstreetmap.org/upfiles/osm-wrong.jpg" alt="alt text" /></p>
<p><br />
I don't know if this is my mistake, but I compared both map.osm files, and they don't have de same data.<br />
- Could it be an OSM problem?<br />
- Which URL should I use? "https://overpass-api.de/api/map" or "https://lz4.overpass-api.de/api/interpreter"?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-http429" rel="tag" title="see questions tagged &#39;http429&#39;">http429</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '19, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/fef9101b2d83bd25c1ce368c4bbc666e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r3287&#39;s gravatar image" />
<p><span>r3287</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r3287 has no accepted answers">0%</span> </br></br></p>
</img>
</div>
</div>
<div id="comments-container-69044" class="comments-container">
<span id="69074"></span>
<div id="comment-69074" class="comment">
<div id="post-69074-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I kindly invite you to read the error message, in particular the words <em>Too many requests</em>.</p>
</div>
<div id="comment-69074-info" class="comment-info">
<span class="comment-age">(03 May '19, 21:43)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-69044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69044-form-container" class="comment-form-container">
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

<span id="69075"></span>

<div id="answer-container-69075" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69075-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, this is not a problem in OSM. You ask the server to retrieve ways and relations without the node referenced there. The server faithfully sends back that data to you.</p>
<p>The script is most likely turning missing nodes into the coordinate (0,0) which explains the line segments leaving the image to the bottom.</p>
<p>I would like to encourage you to make you familiar with the OpenStreetMap data model first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '19, 21:47</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span> </br></p>
</img>
</div>
</div>
<div id="comments-container-69075" class="comments-container">
<span id="69083"></span>
<div id="comment-69083" class="comment">
<div id="post-69083-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your response. First of all, I think I'm familiar with OSM data, as I'm doing this script since some months ago. I don't know what do you mean with "the node referenced there". I thought passing bounding box was enough to get an area.</p>
<p>Secondly, it seems like the second URL returns all nodes except those that are outside the bounding area, that's the reason why my script doesn't know where it has to continue drawing more lines (because the .osm file makes reference to a node ID, but when tries to find that node, it does not exist) and goes to the bottom of the image.</p>
<p>It doesn't make much sense that asking for the same bounding area, it receives different nodes from both URLs.</p>
<p>Do you think I'm missing something when asking to the server?</p>
</div>
<div id="comment-69083-info" class="comment-info">
<span class="comment-age">(04 May '19, 12:19)</span> <span class="comment-user userinfo">r3287</span>
</div>
</div>
</div>
<div id="comment-tools-69075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69075-form-container" class="comment-form-container">
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

