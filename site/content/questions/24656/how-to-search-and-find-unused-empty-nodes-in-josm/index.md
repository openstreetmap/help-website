+++
type = "question"
title = "how to search and find unused empty nodes in JOSM"
description = '''With JOSM I have just removed some tags addr:street that were set on many nodes in a city (nodes that were the corners of buildings). I did use the search and first searched for &quot;addr:street&quot; (in quotation marks) and then for tags=1. Then I deleted this tag. But now I have also many unused nodes whi...'''
date = "2013-07-28T17:42:00Z"
lastmod = "2020-10-17T07:51:00Z"
weight = 24656
keywords = [ "unused", "josm", "search", "orphan-nodes", "empty" ]
aliases = [ "/questions/24656" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [how to search and find unused empty nodes in JOSM](/questions/24656/how-to-search-and-find-unused-empty-nodes-in-josm)

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
<span id="post-24656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24656-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>With JOSM I have just removed some tags addr:street that were set on many nodes in a city (nodes that were the corners of buildings). I did use the search and first searched for <code>"addr:street"</code> (in quotation marks) and then for <code>tags=1</code>. Then I deleted this tag.</p>
<p>But now I have also many unused nodes which are not part of ways. How can I search for them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-unused" rel="tag" title="see questions tagged &#39;unused&#39;">unused</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-orphan-nodes" rel="tag" title="see questions tagged &#39;orphan-nodes&#39;">orphan-nodes</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '13, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
</div>
<div id="comments-container-24656" class="comments-container">
<span id="24658"></span>
<div id="comment-24658" class="comment">
<div id="post-24658-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Please keep in mind before deleting those nodes (yes, you did not write that), to try to look why these nodes are existing (see object history, OWL's beta history tab, whodidit, …).</p>
<p>Sometimes</p>
<ul>
<li>you can find newbies needing help,</li>
<li>just the tags are missing and the creating user forgot to add them (mail the user),</li>
<li>you can find other problems in the related changeset,</li>
<li>(last year, but maybe still today) that could be a surviving left-over from the redaction bot (license change) which may be an indicator that there is some feature missing (could be seen in aerial imagery sometimes).</li>
</ul>
</div>
<div id="comment-24658-info" class="comment-info">
<span class="comment-age">(28 Jul '13, 18:40)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="24666"></span>
<div id="comment-24666" class="comment">
<div id="post-24666-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Yes, it were some small buildings in a small village deleted by the redaction bot I think. As I will be there tomorrow, I will possibly create them again.</p>
</div>
<div id="comment-24666-info" class="comment-info">
<span class="comment-age">(29 Jul '13, 02:48)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
</div>
<div id="comment-tools-24656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24656-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="24676"></span>

<div id="answer-container-24676" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24676-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-24676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="erik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While the OP has answered his own question, here's a simpler one-step search:</p>
<pre><code>type:node untagged -child</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '13, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-24676" class="comments-container">
<span id="24682"></span>
<div id="comment-24682" class="comment">
<div id="post-24682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for this. I suppose <code>-child</code> means »is no child«, am I rigth? As from the description of the JOSM search I thought that <code>child</code> and <code>parent</code> need an expression after them to which they apply. Strange …</p>
</div>
<div id="comment-24682-info" class="comment-info">
<span class="comment-age">(29 Jul '13, 15:56)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
<span id="24684"></span>
<div id="comment-24684" class="comment">
<div id="post-24684-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your answer is covered in the JOSM wiki help page as an example (<a href="https://wiki.openstreetmap.org/wiki/JOSM/Search_function).">https://wiki.openstreetmap.org/wiki/JOSM/Search_function).</a> But this page does not mention the <code>parent</code> token at all. And it does not cover the tokens relating to expressions written after them as seen in the JOSM program itself in the search dialog. Very strange. Is there a better reference/documentation besides the source code?</p>
</div>
<div id="comment-24684-info" class="comment-info">
<span class="comment-age">(29 Jul '13, 16:10)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
<span id="24685"></span>
<div id="comment-24685" class="comment">
<div id="post-24685-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's how I interpret it. The "-" works for other expresions too, like "building=* -source=*". But I do not understand the feature fully, for example how to use "child" with an expresion. The documentation could do with some improvements.</p>
</div>
<div id="comment-24685-info" class="comment-info">
<span class="comment-age">(29 Jul '13, 16:16)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24676-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24657"></span>

<div id="answer-container-24657" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24657-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ok, I have found a solution.</p>
<ol>
<li>First search for <code>type:node tags:0</code></li>
<li>Then search for <code>child parent type:node</code> and select <code>remove from selection</code>.</li>
</ol>
<h2 id="explanation">Explanation</h2>
<ol>
<li>Searches for all nodes which have zero tags (that includes many nodes that are part of ways).</li>
<li>Then search for nodes which have a parent (a way). And then the child of this parent (the nodes that are part of a way). By removing these from the selection, we have only the unused orphan nodes left. Voilà.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '13, 17:58</strong></p>
<img src="https://secure.gravatar.com/avatar/793c9f0cfb9f3cc6001d73f127644c67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erik&#39;s gravatar image" />
<p><span>erik</span><br />
<span class="score" title="558 reputation points">558</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erik has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '13, 17:58</strong> </span></p>
</div>
</div>
<div id="comments-container-24657" class="comments-container">
&#10;</div>
<div id="comment-tools-24657" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24657-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77129"></span>

<div id="answer-container-77129" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77129-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have made the following cheat sheet of JOSM filters and search expressions. I have them on my OSM wiki page at: <a href="https://wiki.openstreetmap.org/wiki/User:Mdelatorre#Searching_and_filtering">https://wiki.openstreetmap.org/wiki/User:Mdelatorre#Searching_and_filtering</a></p>
<p>I hope they can help!</p>
<table>
<thead>
<tr>
<th><p>Search or Filter Expression</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>building inview nodes:4-</p></td>
<td><p>Buildings in view with more than 4 nodes</p></td>
</tr>
<tr>
<td><p>highway=* name:</p></td>
<td><p>Highways that have a name</p></td>
</tr>
<tr>
<td><p>type:way highway=* name~"^[0-9]+.*"</p></td>
<td><p>Highways of any kind that the name starts with one number</p></td>
</tr>
<tr>
<td><p>type:way name:-</p></td>
<td><p>Ways that do not have a name</p></td>
</tr>
<tr>
<td><p>type:node untagged</p></td>
<td><p>Nodes that are not tagged</p></td>
</tr>
<tr>
<td><p>type:node untagged -child</p></td>
<td><p>Nodes that are not tagged neither part of a way</p></td>
</tr>
<tr>
<td><p>new tags:0-0 nodes:3-</p></td>
<td><p>New objects with no tags with more than three nodes</p></td>
</tr>
<tr>
<td><p>nodes:3- -(building=*)</p></td>
<td><p>Objects with more than three nodes that are not buildings</p></td>
</tr>
<tr>
<td><p>nodes:3- -(building=*) -(highway=*)</p></td>
<td><p>As the previous excluding highways</p></td>
</tr>
<tr>
<td><p>type:node -highway=stop</p></td>
<td><p>Nodes excluding stop signs</p></td>
</tr>
<tr>
<td><p>type:node new "addr:housenumber"</p></td>
<td><p>Nodes with new house numbers tags</p></td>
</tr>
<tr>
<td><p>type:node is_in:</p></td>
<td><p>Nodes with an is_in tag set</p></td>
</tr>
<tr>
<td><p>new modified</p></td>
<td><p>Objects that are in state new or modified</p></td>
</tr>
<tr>
<td><p>timestamp:2020-01-15/</p></td>
<td><p>Objects that were last modified after the YYYY-MM-DD date given</p></td>
</tr>
<tr>
<td><p>timestamp:2020-01-01/2020-04-30</p></td>
<td><p>Objects that were last modified in the date range given</p></td>
</tr>
<tr>
<td><p>waterway | boundary=administrative</p></td>
<td><p>Objects that are a waterway or an administrative boundary</p></td>
</tr>
<tr>
<td><p>type:relation admin_level=10</p></td>
<td><p>Relations that have an administrative level equal to 10</p></td>
</tr>
<tr>
<td><p>child(type:relation id:&lt;id&gt;) waterway=river</p></td>
<td><p>Children of the relation (the members) with the id &lt;id&gt; tagged waterway=river</p></td>
</tr>
<tr>
<td><p>closed areasize:-200</p></td>
<td><p>Closed ways (areas) with areas up to 200m² in size</p></td>
</tr>
<tr>
<td><p>closed waylength:1000-</p></td>
<td><p>Closed ways with perimeters greater than 1000m in length</p></td>
</tr>
<tr>
<td><p>type:node -untagged child closed</p></td>
<td><p>Tagged nodes which are part of closed ways</p></td>
</tr>
<tr>
<td><p>parent(child(selected)) type:way</p></td>
<td><p>Neighbouring ways of a selected way</p></td>
</tr>
<tr>
<td><p>parent child selected type:way</p></td>
<td><p>Same as above. Parentheses are optional for single-argument expressions</p></td>
</tr>
<tr>
<td><p>parent(type:node highway:stop) highway:residential</p></td>
<td><p>Residential ways that have a stop sign in a child node</p></td>
</tr>
<tr>
<td><p>child (type=route "&lt;name&gt;")</p></td>
<td><p>Everything that is member of a relation of type route with name &lt;name&gt;</p></td>
</tr>
<tr>
<td><p>type:node ways:2 child highway=residential</p></td>
<td><p>Intersection nodes of residential ways</p></td>
</tr>
<tr>
<td><p><code>type:way and highway=residential and</code> <code>name!=* and noname!=yes</code></p></td>
<td><p>Residential roads missing a name</p></td>
</tr>
<tr>
<td><p><code>type:way and (highway in (motorway,</code> <code>motorway_link, trunk, trunk_link, primary,</code></p>
<p><code>primary_link, secondary, secondary_link,</code></p>
<p><code>tertiary, tertiary_link, unclassified,</code></p>
<p><code>residential, living_street, pedestrian) or</code></p>
<p><code>(highway=service and service=alley))</code></p></td>
<td><p>All types of highways</p></td>
</tr>
<tr>
<td><p><code>building=* and building!=no and</code> <code>geometry:polygon</code></p></td>
<td><p>All buildings. This filter also excludes the (rare) objects marked with <code>building=no</code>, which is a tag used to indicate that a feature might be expected to be a building</p></td>
</tr>
<tr>
<td><p><code>leisure=park and geometry:polygon or</code> <code>amenity=bench and (geometry:point or</code></p>
<p><code>geometry:line)</code></p></td>
<td><p>Parks and park benches</p></td>
</tr>
<tr>
<td><p><code>(landuse=forest or natural=wood) and</code> <code>geometry:polygon</code></p></td>
<td><p>Forests and woods</p></td>
</tr>
</tbody>
</table>
<ol>
<li>DELATORRE, Manuel;[JOSM search and filter examples](<a href="https://pastebin.com/Qf2g5VDh);pastebin.com;2020">https://pastebin.com/Qf2g5VDh);pastebin.com;2020</a></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Oct '20, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/6783b46d5425152bbb4fc48e90eb279a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdelatorre&#39;s gravatar image" />
<p><span>mdelatorre</span><br />
<span class="score" title="177 reputation points">177</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdelatorre has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77129" class="comments-container">
&#10;</div>
<div id="comment-tools-77129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77129-form-container" class="comment-form-container">
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

