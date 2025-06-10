+++
type = "question"
title = "Tutorials about parsing osm.pbf?"
description = '''I am currently trying to extract data from a OpenStreetMap &quot;osm.pbf&quot;-file. This data should then be used for further processing. Currently, I managed to extract a desired location from a database file using osmosis. Now, I would like to convert this area in some data structure which I can manipulate...'''
date = "2013-08-23T12:59:00Z"
lastmod = "2013-08-23T18:14:00Z"
weight = 25685
keywords = [ "graph", "pbf", "osm", "parsing" ]
aliases = [ "/questions/25685" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Tutorials about parsing osm.pbf?](/questions/25685/tutorials-about-parsing-osmpbf)

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
<span id="post-25685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25685-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently trying to extract data from a OpenStreetMap "osm.pbf"-file. This data should then be used for further processing. Currently, I managed to extract a desired location from a database file using osmosis. Now, I would like to convert this area in some data structure which I can manipulate (e.g. a graph, where each edge represents a street), so that I can insert / delete streets / buildings etc.</p>
<p>I found this post <a href="http://wiki.openstreetmap.org/wiki/PBF_Format">http://wiki.openstreetmap.org/wiki/PBF_Format</a> ,which gives some information about the pbf format for parsing. It says there, that there are Nodes/Ways/Relations and more, but I could not find any information, what a Node/Way/Relation represent or "mean". Therefore I am not completely sure, how to parse the file and extract the data I want. Are there any tutorials or sample code, which parses osm files and extract e.g. all streets in a certain location? I've seen a lot of different APIs - maybe there exist one, which converts the whole area into another datastructure - lets say e.g. a Java JGraph?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '13, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/507357a2fa5f7c83378468b4872d15ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pille456&#39;s gravatar image" />
<p><span>Pille456</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pille456 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25685" class="comments-container">
<span id="25689"></span>
<div id="comment-25689" class="comment">
<div id="post-25689-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not a tutorial, but <a href="http://www.mkgmap.org.uk/">mkgmap</a> is nicely-written (Java) code that understands PBF format files.</p>
</div>
<div id="comment-25689-info" class="comment-info">
<span class="comment-age">(23 Aug '13, 14:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25685-form-container" class="comment-form-container">
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

<span id="25698"></span>

<div id="answer-container-25698" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25698-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pille456 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In support of Vincent's answer.</p>
<p>It does not sound like you should be parsing PBF files. Your interest will be in the <a href="http://wiki.openstreetmap.org/wiki/Frameworks">frameworks/libraries</a> available for your language of choice. If you have skills with other geo data formats, you may want to use a <a href="http://wiki.openstreetmap.org/wiki/Converting_map_data_between_formats">conversion</a>.</p>
<p>If you are going to stick to OSM data then understanding Nodes/Ways/Relations will be important. These are the <a href="http://wiki.openstreetmap.org/wiki/Elements">primitive data types</a>. The meaning of these primitives are dictated by the <a href="http://wiki.openstreetmap.org/wiki/Tags">tags</a> associated with them. So roads are identified by the value in the <a href="http://wiki.openstreetmap.org/wiki/Highway">highway key</a>.</p>
<p>Since you're interested in having a graph data structure for your roads it is likely you'll be looking for a conversions which relate to <a href="http://wiki.openstreetmap.org/wiki/Routing#Developers">routing</a>.</p>
<hr />
<p>To answer the original question, the <a href="http://wiki.openstreetmap.org/wiki/PBF_Format">PBF Format</a> is the tutorial for parsing PBF files. I did a <a href="http://he-the-great.livejournal.com/47342.html">blog entry</a> describing my very basic parsing, it is basically the wiki page in code form.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '13, 18:14</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-25698" class="comments-container">
&#10;</div>
<div id="comment-tools-25698" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25698-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25688"></span>

<div id="answer-container-25688" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25688-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-25688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, you are expected to already be familliar with the OSM data structure. The wiki will tell you about <a href="http://wiki.openstreetmap.org/wiki/Node">nodes</a>, <a href="http://wiki.openstreetmap.org/wiki/Way">ways</a>, <a href="http://wiki.openstreetmap.org/wiki/Relation">relations</a>, and <a href="http://wiki.openstreetmap.org/wiki/Tag">tags</a>.</p>
<p>Second of all, you probably want to use one of the existing helper library instead of plain ProtocolBuffers. There are libraries for <a href="http://wiki.openstreetmap.org/wiki/Osmium">c++</a>, <a href="http://dev.omniscale.net/imposm.parser/">python</a>, <a href="https://github.com/planas/pbf_parser">ruby</a>, <a href="https://npmjs.org/package/osm-read">javascript</a>, and probably <a href="http://wiki.openstreetmap.org/wiki/Category:OSM_processing">others</a>. Follow the links for your tool of choice and you should find some tutorials.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Aug '13, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-25688" class="comments-container">
&#10;</div>
<div id="comment-tools-25688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25688-form-container" class="comment-form-container">
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

