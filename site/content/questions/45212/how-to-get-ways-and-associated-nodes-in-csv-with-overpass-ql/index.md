+++
type = "question"
title = "How to get ways and associated nodes in CSV with Overpass QL?"
description = '''Hello, I try to use Overpass QL to get all ways in a given area in CSV. I want to have all coordinates of all nodes of each street. For example:  node_id_1 lat lon way_id_1   node_id_2 lat lon way_id_1   node_id_3 lat lon way_id_1   node_id_4 lat lon way_id_2  node_id_5 lat lon way_id_2  I tried sev...'''
date = "2015-09-12T18:28:00Z"
lastmod = "2015-09-12T20:28:00Z"
weight = 45212
keywords = [ "csv", "overpass-ql" ]
aliases = [ "/questions/45212" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get ways and associated nodes in CSV with Overpass QL?](/questions/45212/how-to-get-ways-and-associated-nodes-in-csv-with-overpass-ql)

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
<span id="post-45212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45212-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I try to use Overpass QL to get all ways in a given area in CSV. I want to have all coordinates of all nodes of each street.</p>
<p>For example:</p>
<pre><code> node_id_1 lat lon way_id_1 
 node_id_2 lat lon way_id_1 
 node_id_3 lat lon way_id_1 
 node_id_4 lat lon way_id_2
 node_id_5 lat lon way_id_2</code></pre>
<p>I tried several approaches but none worked. I can get all nodes and all ways but I found no way to have an explicit association between nodes and ways. I do not manage to add the way information to each node, and the node list does not appear for each way in the CSV output.</p>
<p>Any help would be appreciated. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '15, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/2355a09bb61d5e8bc800f5c873e950e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haltux&#39;s gravatar image" />
<p><span>haltux</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haltux has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45212" class="comments-container">
&#10;</div>
<div id="comment-tools-45212" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45212-form-container" class="comment-form-container">
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

<span id="45213"></span>

<div id="answer-container-45213" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45213-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="haltux has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At this time, it's not possible to have details originating from several OSM objects in one single line. In your case, that's the node id + details, as well as the corresponding way id.</p>
<p>I suggest to take advantage of the <code>foreach</code> statement like in the following example.</p>
<p>It will first output the way id, followed by a list of its nodes with their respective node id and lat/lon details.</p>
<pre><code>[out:csv(::type, ::id, ::lat, ::lon)]
[bbox:{{bbox}}];
way[highway];
foreach(           // for each way tagged as highway=* do...
  out;             // output way id
  node(w);         // determine respective nodes
  out;             // output all node details
);</code></pre>
<p>Try it in overpass turbo: <a href="http://overpass-turbo.eu/s/bpj">http://overpass-turbo.eu/s/bpj</a></p>
<p>In a post processing step, you'll have to transform this output to whatever format you need.</p>
<p><strong>Caveat</strong>: CSV output does <strong>NOT</strong> preserve the sequence of nodes per OSM way. Depending on your requirements, the results may therefore be completely useless to you!</p>
<p>CSV output was primarily designed to return tags for relations/way/nodes,.... Returning geometry information for ways was not a main focus. Maybe you want to check JSON/XML output with <code>out geom;</code> instead, which is also rather easily parse-able.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '15, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>12 Sep '15, 19:56</strong> </span></p>
</div>
</div>
<div id="comments-container-45213" class="comments-container">
<span id="45214"></span>
<div id="comment-45214" class="comment">
<div id="post-45214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, thank you. However, if nodes are not ordered, it is actually totally useless for me. Thanks for having pointed that out. I really have to rethink all that, probably start from JSON and generate my own CSV.</p>
</div>
<div id="comment-45214-info" class="comment-info">
<span class="comment-age">(12 Sep '15, 19:54)</span> <span class="comment-user userinfo">haltux</span>
</div>
</div>
<span id="45215"></span>
<div id="comment-45215" class="comment">
<div id="post-45215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By the way, my actual goal was to generate all pairs of nodes (X,Y) such that X and Y are two consecutive points in a way. I guess there is no direct way to do that, but if you have any idea, I would be very interested in it.</p>
</div>
<div id="comment-45215-info" class="comment-info">
<span class="comment-age">(12 Sep '15, 20:00)</span> <span class="comment-user userinfo">haltux</span>
</div>
</div>
<span id="45216"></span>
<div id="comment-45216" class="comment">
<div id="post-45216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Right, I don't see an option to have pairs of consecutive points as an Overpass result. You'll have to implement this in your favorite language based on the JSON/XML output returned by the API.</p>
</div>
<div id="comment-45216-info" class="comment-info">
<span class="comment-age">(12 Sep '15, 20:28)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-45213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45213-form-container" class="comment-form-container">
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

