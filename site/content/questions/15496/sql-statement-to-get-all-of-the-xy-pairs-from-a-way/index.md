+++
type = "question"
title = "SQL Statement to get all of the X/Y pairs from a way?"
description = '''Hello OSM, I&#x27;m working on a custom application where I will eventually be running a DFS on the entire OSM DB (limited by state boundaries). FOR NOW, I&#x27;m learning OSM by writing my own map renderer. I am currently plotting all of the ways in my &quot;chunk&quot; of the OSM DB (Florida).  My current method of p...'''
date = "2012-08-25T05:48:00Z"
lastmod = "2012-08-25T08:16:00Z"
weight = 15496
keywords = [ "ways", "java", "sql" ]
aliases = [ "/questions/15496" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SQL Statement to get all of the X/Y pairs from a way?](/questions/15496/sql-statement-to-get-all-of-the-xy-pairs-from-a-way)

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
<span id="post-15496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15496-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OSM,</p>
<p>I'm working on a custom application where I will eventually be running a DFS on the entire OSM DB (limited by state boundaries). FOR NOW, I'm learning OSM by writing my own map renderer. I am currently plotting all of the ways in my "chunk" of the OSM DB (Florida).</p>
<p>My current method of plotting a way seems very inefficient, I grab a way using this:</p>
<p>SELECT nodes, id from public.ways LIMIT 1 OFFSET ...</p>
<p>Then I convert the list of nodes into an array in Java and I run the following SQL command to get the X/Y pair for each node:</p>
<p>SELECT ST_X(geom) as x, ST_Y(geom) as y from public.nodes WHERE id=" + nodes[i] + "LIMIT 1"</p>
<p>I feel as if this process could be done in one step all by the database and preferably for many ways at a time. As this seems like something that people around here likely have to do often I figured I'd ask, is there a better way to do this?</p>
<p>Any help is greatly appreciated! - Thanks -Cody</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '12, 05:48</strong></p>
<img src="https://secure.gravatar.com/avatar/aa9f28cc449a272dbd654e8edf660877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Smartkid&#39;s gravatar image" />
<p><span>Smartkid</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Smartkid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '12, 07:27</strong> </span></p>
</div>
</div>
<div id="comments-container-15496" class="comments-container">
&#10;</div>
<div id="comment-tools-15496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15496-form-container" class="comment-form-container">
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

<span id="15501"></span>

<div id="answer-container-15501" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15501-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The database schema of the Rails-port is designed for the api which is mainly used by editors. Other applications like rendering or routing usually preprocess the raw osm data into another database scheme.</p>
<p>For rendering the connectivity between ways (and areas) is irrelevant. So in a datamodel for rendering only the nodes for point features are retained with a geometry. For ways the geometry is calculated from their nodes during the prepocessing using tools like <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql">osm2pgsql</a> and <a href="http://wiki.openstreetmap.org/wiki/Imposm">Imposm</a>. Both these tools are open source, so have a look at their code.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '12, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-15501" class="comments-container">
&#10;</div>
<div id="comment-tools-15501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15501-form-container" class="comment-form-container">
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

