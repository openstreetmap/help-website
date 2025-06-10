+++
type = "question"
title = "fast OSRM routing for a large number of queries"
description = '''Good morning fellows, I have around 50.000 lists of GPS coordinates, and for each list I&#x27;d like to use the osrm routing engine to get the exact path taken, and pass it to a python script. I I&#x27;m currently making 50.000 successive calls to the routing API (on my own server), which is quite slow becaus...'''
date = "2020-03-26T09:59:00Z"
lastmod = "2020-03-26T10:19:00Z"
weight = 73763
keywords = [ "osrm", "routing" ]
aliases = [ "/questions/73763" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [fast OSRM routing for a large number of queries](/questions/73763/fast-osrm-routing-for-a-large-number-of-queries)

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
<span id="post-73763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73763-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good morning fellows,</p>
<p>I have around 50.000 lists of GPS coordinates, and for each list I'd like to use the osrm routing engine to get the exact path taken, and pass it to a python script.</p>
<p>I I'm currently making 50.000 successive calls to the routing API (on my own server), which is quite slow because of the overhead involved for each API call</p>
<p>What is the fastest way to use the osrm routing engine in this case, for instance is there a possibility to pass a list of path to the API instead of just one path a time?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '20, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/5b4d8236126cc818e7ea75e7ceb6d76a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hyppocrate&#39;s gravatar image" />
<p><span>Hyppocrate</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hyppocrate has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Mar '20, 10:13</strong> </span></p>
</div>
</div>
<div id="comments-container-73763" class="comments-container">
&#10;</div>
<div id="comment-tools-73763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73763-form-container" class="comment-form-container">
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

<span id="73764"></span>

<div id="answer-container-73764" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73764-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I hope you're making these calls to your own server and not to one of the donation-funded public machines! There isn't an API for running several track matchings at once, however you can use the node-osrm integration to call the OSRM backend directly from Javascript code executed by nodejs, potentially bypassing some of the network latency and encoding/decoding of messages.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '20, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-73764" class="comments-container">
<span id="73766"></span>
<div id="comment-73766" class="comment">
<div id="post-73766-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer, the routes are computed in local. I thin I have found this node-osrm integration <a href="https://github.com/Project-OSRM/osrm-backend/blob/master/docs/nodejs/api.md">here</a>, do you know if it's usable from python or command line?</p>
</div>
<div id="comment-73766-info" class="comment-info">
<span class="comment-age">(26 Mar '20, 10:19)</span> <span class="comment-user userinfo">Hyppocrate</span>
</div>
</div>
</div>
<div id="comment-tools-73764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73764-form-container" class="comment-form-container">
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

