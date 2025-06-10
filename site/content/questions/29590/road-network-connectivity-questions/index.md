+++
type = "question"
title = "Road Network Connectivity Questions"
description = '''how can we get the details surrounding the road segment and connectivity from OSM ? For example, how can I know road A is connected to road B? Is there any attributes about these segments or nodes like speeds, number of lanes, etc? If so, where is this detail in OSM?'''
date = "2014-01-05T01:31:00Z"
lastmod = "2014-01-05T12:02:00Z"
weight = 29590
keywords = [ "connectivity", "network", "road" ]
aliases = [ "/questions/29590" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Road Network Connectivity Questions](/questions/29590/road-network-connectivity-questions)

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
<span id="post-29590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29590-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>how can we get the details surrounding the road segment and connectivity from OSM ? For example, how can I know road A is connected to road B? Is there any attributes about these segments or nodes like speeds, number of lanes, etc? If so, where is this detail in OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-connectivity" rel="tag" title="see questions tagged &#39;connectivity&#39;">connectivity</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '14, 01:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ccf44fbb8677cca8ba5989af53c8fa5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="systemjim&#39;s gravatar image" />
<p><span>systemjim</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="systemjim has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29590" class="comments-container">
&#10;</div>
<div id="comment-tools-29590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29590-form-container" class="comment-form-container">
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

<span id="29591"></span>

<div id="answer-container-29591" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29591-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure about all of your question nor how you are getting the data from OSM. But for knowing if road A is connected to road B, each road or way has a list of node IDs. If the two ways (roads) have node IDs in common then they connect. And they might connect in multiple places and thus have multiple node IDs in common.</p>
<p>On the ways themselves (actually any object which includes individual points/nodes) are an arbitrarily long list of key=value pairs. If the way is marked as highway=* then there are defined key value pairs for things like maxspeed, lanes, etc.</p>
<p>If you download a OSM file for a small area you will see that it is just an XML file with a pretty obvious schema. If you are getting any of the other types of downloads available and loading it into a GIS database, then the data will look different and you'll have to look at the tools that populate your database and what your schema is to see what is loaded.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '14, 02:40</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-29591" class="comments-container">
&#10;</div>
<div id="comment-tools-29591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29591-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29594"></span>

<div id="answer-container-29594" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29594-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Type "graph" in the search box above and read some of the responses to similar questions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '14, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29594" class="comments-container">
&#10;</div>
<div id="comment-tools-29594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29594-form-container" class="comment-form-container">
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

