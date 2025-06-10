+++
type = "question"
title = "Order of Nodes for plotting a Way"
description = '''Hi. I am new to OSM. I have extracted a rectangle of data for Welwyn Garden City, with a view to experimenting with routing algorithms. I have used osm1.c as an example to extract ways, nodes, relations. My question is how do I know which order to plot nodes to draw a way. I don&#x27;t want to use any li...'''
date = "2019-06-02T21:56:00Z"
lastmod = "2019-06-14T07:16:00Z"
weight = 69414
keywords = [ "node", "order", "way" ]
aliases = [ "/questions/69414" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Order of Nodes for plotting a Way](/questions/69414/order-of-nodes-for-plotting-a-way)

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
<span id="post-69414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69414-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I am new to OSM. I have extracted a rectangle of data for Welwyn Garden City, with a view to experimenting with routing algorithms. I have used osm1.c as an example to extract ways, nodes, relations. My question is how do I know which order to plot nodes to draw a way. I don't want to use any library to do this. Is this the order in the way XML data? For example Ingles (a street name) appears to have 20 nodes and no relations. This appears to be the case (order wise) for Ingles but is it generally true? Do 'relations' give this information for some ways.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '19, 21:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ad5de24a5107cfe177b2c9c73b13c29f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20Begesford&#39;s gravatar image" />
<p><span>Mike Begesford</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike Begesford has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69414" class="comments-container">
&#10;</div>
<div id="comment-tools-69414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69414-form-container" class="comment-form-container">
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

<span id="69415"></span>

<div id="answer-container-69415" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69415-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>General information about the OSM xml format is available <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">on the wiki</a> and a simple example of how a way is recorded <a href="https://wiki.openstreetmap.org/wiki/Way#Examples">here</a>. There are a few <a href="https://wiki.openstreetmap.org/wiki/Routing#Open_source_desktop_and_server_software">open source</a> routing engines for osm data if you want to see how others have tackled the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '19, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-69415" class="comments-container">
<span id="69612"></span>
<div id="comment-69612" class="comment">
<div id="post-69612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just wanted 'yes' or 'no' from one of the experts out there!</p>
</div>
<div id="comment-69612-info" class="comment-info">
<span class="comment-age">(13 Jun '19, 12:18)</span> <span class="comment-user userinfo">Mike Begesford</span>
</div>
</div>
<span id="69614"></span>
<div id="comment-69614" class="comment">
<div id="post-69614-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Relations have nothing to do with this. This information is contained in the XML, specifically the order in which the way refers its nodes via <code>&lt;nd ref=...</code> elements (i.e. <em>not</em> the order in which the <code>&lt;node&gt;</code> elements appear in the XML!).</p>
</div>
<div id="comment-69614-info" class="comment-info">
<span class="comment-age">(13 Jun '19, 12:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69415-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69619"></span>

<div id="answer-container-69619" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69619-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Way nodes in (any format that I know are) are ordered in the data (so first node first and so on, closed ways end with a repeat of the first node).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '19, 07:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-69619" class="comments-container">
&#10;</div>
<div id="comment-tools-69619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69619-form-container" class="comment-form-container">
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

