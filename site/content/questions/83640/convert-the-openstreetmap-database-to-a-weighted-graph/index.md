+++
type = "question"
title = "convert the OpenStreetMap database to a weighted graph"
description = '''Trying to convert the OpenStreetMap database to a weighted graph in order to apply algorithms like Dijkstra or A*.  Any ideas on how to make the algorithm working on the data? The thing is to convert all the database in one time and then apply the algorithm. Right now I&#x27;m thinking of just read the d...'''
date = "2022-03-04T13:30:00Z"
lastmod = "2022-03-04T13:45:00Z"
weight = 83640
keywords = [ "graph", "dijkstra", "osmconvert", "database" ]
aliases = [ "/questions/83640" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [convert the OpenStreetMap database to a weighted graph](/questions/83640/convert-the-openstreetmap-database-to-a-weighted-graph)

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
<span id="post-83640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83640-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Trying to convert the OpenStreetMap database to a weighted graph in order to apply algorithms like Dijkstra or A*. Any ideas on how to make the algorithm working on the data? The thing is to convert all the database in one time and then apply the algorithm. Right now I'm thinking of just read the database and extract the information needed to construct the graph. Make the roads as edges. As for the nodes, it's hard to determine what kind of location to keep. Need help :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-dijkstra" rel="tag" title="see questions tagged &#39;dijkstra&#39;">dijkstra</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '22, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/55697167d87179c312fc0ee50adb0697?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wothell&#39;s gravatar image" />
<p><span>wothell</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wothell has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83640" class="comments-container">
&#10;</div>
<div id="comment-tools-83640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83640-form-container" class="comment-form-container">
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

<span id="83641"></span>

<div id="answer-container-83641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83641-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't reinvent the wheel. Use existing software like Graphhopper, OSRM, Valhalla if you want fast and powerful routing. If you are desperate to build your own (or need to because of educational project assignment etc.), at least look at Graphhopper or OSRM source code to understand how OSM data is converted into a graph. If you really really want to build your own from scratch, look at <a href="/questions/19213/how-can-i-convert-an-osm-xml-file-into-a-graph-representation">https://help.openstreetmap.org/questions/19213/how-can-i-convert-an-osm-xml-file-into-a-graph-representation</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '22, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83641" class="comments-container">
&#10;</div>
<div id="comment-tools-83641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83641-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83642"></span>

<div id="answer-container-83642" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/Tristramg/osm4routing2">osm4routing2</a> is a simple and useful tool that will take an OpenStreetMap .pbf file and convert it into a routable graph, which you can then build your routing algorithms on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '22, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-83642" class="comments-container">
&#10;</div>
<div id="comment-tools-83642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83642-form-container" class="comment-form-container">
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

