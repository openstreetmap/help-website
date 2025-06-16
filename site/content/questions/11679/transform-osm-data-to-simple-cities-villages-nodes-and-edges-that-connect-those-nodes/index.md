+++
type = "question"
title = "Transform OSM data to simple cities, villages nodes and edges that connect those nodes."
description = '''Hi I need a fast algorithm and input data to it to calculate for user what cities and villages are on the track from one city to another. I realized that this is not simple especialy if speed of the calculation is crucial. I was thinking about fetching OSM data for one country and transform it to th...'''
date = "2012-04-01T10:35:00Z"
lastmod = "2012-04-01T19:54:00Z"
weight = 11679
keywords = [ "graph", "nodes", "edge", "osm", "routing" ]
aliases = [ "/questions/11679" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Transform OSM data to simple cities, villages nodes and edges that connect those nodes.](/questions/11679/transform-osm-data-to-simple-cities-villages-nodes-and-edges-that-connect-those-nodes)

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
<span id="post-11679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11679-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I need a fast algorithm and input data to it to calculate for user what cities and villages are on the track from one city to another.</p>
<p>I realized that this is not simple especialy if speed of the calculation is crucial. I was thinking about fetching OSM data for one country and transform it to the graph with nodes and edges. Let's name this graph IG - Input Graph.</p>
<p>Now I would like to proces this IG to OG (output graph) that contains only cities/villages nodes and edges that are calculated based on IG roads. In simple words I need a graph that let me calculate in fast way the answer to question: If I start from city nr 3 and want to drive to city nr 7 what city/village will I be passing? The answers are:</p>
<ol>
<li>You will be passing cities/villages: 5, 6, 7</li>
<li>You will be passing cities/villages: 2, 4, 6, 7</li>
<li>You will be passing cities/villages: 5, 4, 6, 7</li>
</ol>
<p>The city / village nodes are retrieved from OSM file. The Output Graph edges should have weight calculated based on the Input Graph edges. The measure of the weight is in general distance in meters from one node to the next.</p>
<p>My question is. Does somebody was working on something like this. I don't want to duplicate somebodys work. Ofcourse everybody are welcome to help me do it in right way.</p>
<p><img src="/upfiles/idea.gif" alt="Idea" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-edge" rel="tag" title="see questions tagged &#39;edge&#39;">edge</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '12, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/009f91df0216639687e7adcc8c9f4d6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kapuch&#39;s gravatar image" />
<p><span>Kapuch</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kapuch has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-11679" class="comments-container">
&#10;</div>
<div id="comment-tools-11679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11679-form-container" class="comment-form-container">
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

<span id="11682"></span>

<div id="answer-container-11682" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11682-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My advice: contact the developers of the many Openstreetmap routing services.</p>
<p>( <a href="https://wiki.openstreetmap.org/wiki/Routing">https://wiki.openstreetmap.org/wiki/Routing</a> )</p>
<p>Within their software developments they definitely will have dealt with the kind of graph decisions that you are thinkng about here.</p>
<p>H.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '12, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/63a3d001d166921b51b1bd82b2865726?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Herve5&#39;s gravatar image" />
<p><span>Herve5</span><br />
<span class="score" title="568 reputation points">568</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Herve5 has 3 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '12, 16:56</strong> </span></p>
</div>
</div>
<div id="comments-container-11682" class="comments-container">
<span id="11685"></span>
<div id="comment-11685" class="comment">
<div id="post-11685-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... or leave a message to the Routing mailinglist that can be found here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">https://wiki.openstreetmap.org/wiki/Mailing_lists</a></p>
</div>
<div id="comment-11685-info" class="comment-info">
<span class="comment-age">(01 Apr '12, 18:57)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="11686"></span>
<div id="comment-11686" class="comment">
<div id="post-11686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank You for advice. I just post them an email.</p>
</div>
<div id="comment-11686-info" class="comment-info">
<span class="comment-age">(01 Apr '12, 19:54)</span> <span class="comment-user userinfo">Kapuch</span>
</div>
</div>
</div>
<div id="comment-tools-11682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11682-form-container" class="comment-form-container">
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

