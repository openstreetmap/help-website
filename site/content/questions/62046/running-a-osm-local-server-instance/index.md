+++
type = "question"
title = "Running a OSM Local server instance"
description = '''Hello, I need to access the endpoint https://api.openstreetmap.org/api/0.6/node/ locally (in my case this would be localhost:3000/api/0.6/node/)to get node details by nodeID. Any guide how to setup a local server on Ubuntu 17.10? Thanks.'''
date = "2018-02-11T03:08:00Z"
lastmod = "2018-02-11T08:38:00Z"
weight = 62046
keywords = [ "node", "api", "local", "server" ]
aliases = [ "/questions/62046" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Running a OSM Local server instance](/questions/62046/running-a-osm-local-server-instance)

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
<span id="post-62046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62046-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I need to access the endpoint <a href="https://api.openstreetmap.org/api/0.6/node/">https://api.openstreetmap.org/api/0.6/node/</a> locally (in my case this would be localhost:3000/api/0.6/node/)to get node details by nodeID. Any guide how to setup a local server on Ubuntu 17.10?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '18, 03:08</strong></p>
<img src="https://secure.gravatar.com/avatar/8e69eee546779bbb2c813e4faa58d231?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KlausD94&#39;s gravatar image" />
<p><span>KlausD94</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KlausD94 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '18, 23:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-62046" class="comments-container">
&#10;</div>
<div id="comment-tools-62046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62046-form-container" class="comment-form-container">
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

<span id="62047"></span>

<div id="answer-container-62047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62047-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you want is the "openstreetmap website" software. Installation instructions for older Ubuntu versions are here <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md">https://github.com/openstreetmap/openstreetmap-website/blob/master/INSTALL.md</a> and if you don't get it to work on 17.10 out of the box, consider running it in a Docker container.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '18, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62047" class="comments-container">
&#10;</div>
<div id="comment-tools-62047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62047-form-container" class="comment-form-container">
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

