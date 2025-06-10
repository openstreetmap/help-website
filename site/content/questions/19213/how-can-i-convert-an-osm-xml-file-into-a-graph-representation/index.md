+++
type = "question"
title = "How can I convert an OSM XML file into a graph representation?"
description = '''How can I convert an OSM XML file into a graph representation (such that ways become edges of the graph and intersections/junctions become the nodes of the graph)?'''
date = "2013-01-19T16:56:00Z"
lastmod = "2016-02-27T22:39:00Z"
weight = 19213
keywords = [ "xml", "graph", "development", ".osm", "routing" ]
aliases = [ "/questions/19213" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I convert an OSM XML file into a graph representation?](/questions/19213/how-can-i-convert-an-osm-xml-file-into-a-graph-representation)

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
<span id="post-19213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19213-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-19213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I convert an OSM XML file into a graph representation (such that ways become edges of the graph and intersections/junctions become the nodes of the graph)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '13, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/361e0b98020ca3f3d7db7baa2ec6c590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sadeer&#39;s gravatar image" />
<p><span>Sadeer</span><br />
<span class="score" title="176 reputation points">176</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sadeer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '15, 15:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-19213" class="comments-container">
<span id="30440"></span>
<div id="comment-30440" class="comment">
<div id="post-30440-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This <a href="https://www.mapbox.com/blog/smart-directions-with-osrm-graph-model/">blog post</a> by the author of <a href="http://project-osrm.org/">OSRM</a> might be helpful.</p>
</div>
<div id="comment-30440-info" class="comment-info">
<span class="comment-age">(04 Feb '14, 11:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19213-form-container" class="comment-form-container">
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

<span id="19214"></span>

<div id="answer-container-19214" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19214-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-19214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming you want only roads, then a possible algorithm is this:</p>
<ol>
<li>parse all ways; throw away those that are not roads, and for the others, remember the node IDs they consist of, by incrementing a "link counter" for each node referenced.</li>
<li>parse all ways a second time; a way will normally become one edge, but if any nodes apart from the first and the last have a link counter greater than one, then split the way into two edges at that point. Nodes with a link counter of one and which are neither first nor last can be thrown away unless you need to compute the length of the edge.</li>
<li>(if you need geometry for your graph nodes) parse the nodes section of the XML now, recording coordinates for all nodes that you have retained.</li>
</ol>
<p>If you are only working on a small data set you can of course simply read everything into memory and do the above analysis in memory.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '13, 17:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-19214" class="comments-container">
<span id="19228"></span>
<div id="comment-19228" class="comment">
<div id="post-19228-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"throw away those that are not roads" the devil is in the details. You can't search for ways tagged with car=yes. So if you need a graph for only cars you will probably need to look at filters used by available routers.</p>
</div>
<div id="comment-19228-info" class="comment-info">
<span class="comment-age">(21 Jan '13, 11:19)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="22073"></span>
<div id="comment-22073" class="comment">
<div id="post-22073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/188/emj"></a><a href="http://help.openstreetmap.org/users/188/emj">@emj</a>: Correct. You should search for ways with highway tag other than pedestrian,footway,cycleway,bridleway. And eliminate oneways with final point unconnected.</p>
</div>
<div id="comment-22073-info" class="comment-info">
<span class="comment-age">(03 May '13, 12:28)</span> <span class="comment-user userinfo">erkinalp</span>
</div>
</div>
<span id="43921"></span>
<div id="comment-43921" class="comment">
<div id="post-43921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,i am wondering why exactly we need to execute step #2 from above?</p>
<p>The logic is mainly implemented in the python script here : <a href="https://gist.github.com/aflaxman/287370">https://gist.github.com/aflaxman/287370</a></p>
<p>So if I remove lines 144-159 from the script in the link (i.e. omit the step #2 from above) I get a fine graph as well.</p>
</div>
<div id="comment-43921-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 16:21)</span> <span class="comment-user userinfo">rajanskus</span>
</div>
</div>
<span id="44079"></span>
<div id="comment-44079" class="comment">
<div id="post-44079-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Depends on your definition of "graph". Usually, a graph consists of nodes and edges, where each edge connects to exactly two nodes. If you leave out step 2, you will end up with something where an edge can go from node A across node B to node C. This is not a graph, and various graph-based routing engines or network analyzers will have trouble working with that.</p>
</div>
<div id="comment-44079-info" class="comment-info">
<span class="comment-age">(09 Jul '15, 18:11)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="44096"></span>
<div id="comment-44096" class="comment">
<div id="post-44096-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, one short question...what do you exactly mean with "link counter"?</p>
</div>
<div id="comment-44096-info" class="comment-info">
<span class="comment-age">(10 Jul '15, 06:33)</span> <span class="comment-user userinfo">madalina_ias...</span>
</div>
</div>
<span id="44416"></span>
<div id="comment-44416" class="comment not_top_scorer">
<div id="post-44416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>link counter := number of ways by which one node is used.</p>
</div>
<div id="comment-44416-info" class="comment-info">
<span class="comment-age">(24 Jul '15, 21:09)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="48286"></span>
<div id="comment-48286" class="comment not_top_scorer">
<div id="post-48286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Link counter means degree of the vertex.</p>
</div>
<div id="comment-48286-info" class="comment-info">
<span class="comment-age">(22 Feb '16, 10:45)</span> <span class="comment-user userinfo">Ankita_Mehta</span>
</div>
</div>
</div>
<div id="comment-tools-19214" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-19214-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48391"></span>

<div id="answer-container-48391" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48391-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Working with OSM and Java implementation using Jgrapht library</p>
<p><a href="http://www.sandeepsas.com/how-do-i-start-working-with-openstreetmap-osm/">http://www.sandeepsas.com/how-do-i-start-working-with-openstreetmap-osm/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '16, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/650cca1a12804bb72fad1092d2a545e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandeep40&#39;s gravatar image" />
<p><span>Sandeep40</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandeep40 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '16, 22:41</strong> </span></p>
</div>
</div>
<div id="comments-container-48391" class="comments-container">
&#10;</div>
<div id="comment-tools-48391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48391-form-container" class="comment-form-container">
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

