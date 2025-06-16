+++
type = "question"
title = "Obtaining adjacent intersections?"
description = '''First, I&#x27;m using the BasicOSMParser by Panier Avide to obtain the info in Java. After that, I followed this solution to get all the nodes. I also did some additional testing for triple intersections and unnamed stuff such as roundabouts. Now, I need to obtain adjacent/precedent intersections, to sor...'''
date = "2018-03-28T13:03:00Z"
lastmod = "2018-03-28T13:55:00Z"
weight = 62850
keywords = [ "openstreetmap", "intersection", "street" ]
aliases = [ "/questions/62850" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Obtaining adjacent intersections?](/questions/62850/obtaining-adjacent-intersections)

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
<span id="post-62850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62850-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>First, I'm using the <a href="https://github.com/PanierAvide/BasicOSMParser">BasicOSMParser by Panier Avide</a> to obtain the info in Java.</p>
<p>After that, I followed <a href="/questions/15442/detection-of-intersections-in-the-maps">this solution</a> to get all the nodes. I also did some additional testing for triple intersections and unnamed stuff such as roundabouts.</p>
<p>Now, I need to obtain adjacent/precedent intersections, to sort of make a graph of how the intersections connect. Is this possible? After digging, <a href="/questions/32276/how-to-detect-two-adjacent-intersections">I found this question from 2014</a>, but it does not have answers.</p>
<p>How can I make this graph (not necessarily a graph chart, but the precedence relations) or obtaining/linking intersections?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '18, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/cbb99215ffcbcc93a57eb11da1c1ba37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mel&#39;s gravatar image" />
<p><span>mel</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62850" class="comments-container">
&#10;</div>
<div id="comment-tools-62850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62850-form-container" class="comment-form-container">
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

<span id="62851"></span>

<div id="answer-container-62851" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62851-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps <a href="/questions/19213/how-can-i-convert-an-osm-xml-file-into-a-graph-representation">How can I convert an OSM XML file into a graph representation?</a> is helpful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '18, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62851" class="comments-container">
&#10;</div>
<div id="comment-tools-62851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62851-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62852"></span>

<div id="answer-container-62852" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62852-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I also just found this tool: <a href="http://osm-traffic.com/index.html">http://osm-traffic.com/index.html</a> It provides information on top of OSM, and can generate the graph in JSON format directly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '18, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/cbb99215ffcbcc93a57eb11da1c1ba37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mel&#39;s gravatar image" />
<p><span>mel</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62852" class="comments-container">
&#10;</div>
<div id="comment-tools-62852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62852-form-container" class="comment-form-container">
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

