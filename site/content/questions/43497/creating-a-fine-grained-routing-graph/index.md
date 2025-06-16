+++
type = "question"
title = "Creating a fine-grained routing graph"
description = '''For an academic project involving road maintenance, I need to create a routing graph from geographical data. I was wondering whether someone could tell me whether creating the following graph is possible using OSM data. A &#x27;traditional&#x27; routing graph would be something like: a vertex is an intersecti...'''
date = "2015-06-09T21:06:00Z"
lastmod = "2015-06-19T22:15:00Z"
weight = 43497
keywords = [ "graph", "osm", "routing" ]
aliases = [ "/questions/43497" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Creating a fine-grained routing graph](/questions/43497/creating-a-fine-grained-routing-graph)

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
<span id="post-43497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For an academic project involving road maintenance, I need to create a routing graph from geographical data. I was wondering whether someone could tell me whether creating the following graph is possible using OSM data. A 'traditional' routing graph would be something like: a vertex is an intersection, an edge between 2 vertices connects 2 intersections. In my application I need something more fine-grained. I need to create the following multigraph:</p>
<ul>
<li>an arc (=directed edge) models a driving lane.</li>
<li>an edge models a street consisting of 1 lane which can be driven in both directions</li>
<li>When there are two arcs say (i,j) and (j,k), it must be allowed to drive from lane (i,j) to (j,k).</li>
</ul>
<p>Example. Given the following intersection at the top of the picture. Let's assume that u-turns are not permitted. The arrows indicate driving directions for each lane. At the bottom you see the resulting routing graph which implements all traffic rules. U-turns are easily incorporated by 'merging' two nodes. <img src="http://i.imgur.com/8u0Asze.png" alt="alt text" /></p>
<p>For each lane I need to know it's length and the allowed driving speed. I'm only interested in roads for cars (no walkways/bicycle lanes). It would be great if someone could tell me whether it is possible to extract this kind of data from OSM. Any examples, references to existing code or references to relevant documentation are highly appreciated. If this is not possible in OSM, do you know other data sources which I could use instead (e.g. Google maps, HERE maps, etc)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jun '15, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/6feb1ed05cdbdc6c0d788f514fd07e1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorisK&#39;s gravatar image" />
<p><span>JorisK</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorisK has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-43497" class="comments-container">
&#10;</div>
<div id="comment-tools-43497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43497-form-container" class="comment-form-container">
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

<span id="43601"></span>

<div id="answer-container-43601" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43601-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43601-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43601-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In those locations where OSM has lane data (which is far from everywhere), generating a graph according to your specifications is possible.</p>
<p>Relevant documentation can be found here:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Lanes">On representing lanes in OSM</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Key:maxspeed">On the maxspeed attribute</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Key:turn">On turn lanes</a></li>
</ul>
<p>I don't know any library that does this for you, however. So if the suggestions by <a href="https://help.openstreetmap.org/users/4984/iii">@iii</a> don't do what you want, you would have to do it yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '15, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-43601" class="comments-container">
&#10;</div>
<div id="comment-tools-43601" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43601-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43498"></span>

<div id="answer-container-43498" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43498-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A lane based directed routing graph is possible, even if I don't know which toolset can help you. You might check out <a href="http://code.google.com/p/trafficmining/">TrafficMining</a> framework or start using pgrouting and tune <a href="https://wiki.openstreetmap.org/wiki/Osm2pgrouting">osm2pgrouting</a>. Also <a href="http://eworld.sf.net">eWorld</a> might be an idea?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '15, 21:59</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-43498" class="comments-container">
&#10;</div>
<div id="comment-tools-43498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43498-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43656"></span>

<div id="answer-container-43656" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43656-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use GraphHopper as a starting point for this. Then you already have a good routing graph for cars. For detailed lane support you'll need to tweak it a bit, but as GraphHopper supports any directed graph in its <a href="https://github.com/graphhopper/graphhopper/blob/master/docs/core/low-level-api.md">lower level Java API</a> you can model nearly anything with it.</p>
<p>Disclaimer: I'm the author</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '15, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/fec61c70a4cc98b1e84a5dfbde1e9a6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peatar&#39;s gravatar image" />
<p><span>peatar</span><br />
<span class="score" title="351 reputation points">351</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peatar has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-43656" class="comments-container">
&#10;</div>
<div id="comment-tools-43656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43656-form-container" class="comment-form-container">
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

