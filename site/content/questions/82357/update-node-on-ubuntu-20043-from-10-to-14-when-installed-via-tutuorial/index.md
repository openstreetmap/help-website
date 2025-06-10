+++
type = "question"
title = "Update Node on Ubuntu 20.04.3 from 10 to 14 when installed via tutuorial"
description = '''Hello, I successfully installed an own tileserver via https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/. For an additional service in Node.js I need Node.js V14, but Node.js V10 has been installed through the mentioned tutorial. Is it possible to Update Node.js to V14? ...'''
date = "2021-10-25T12:57:00Z"
lastmod = "2021-10-25T13:51:00Z"
weight = 82357
keywords = [ "node", "version", "update", "tileserver" ]
aliases = [ "/questions/82357" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Update Node on Ubuntu 20.04.3 from 10 to 14 when installed via tutuorial](/questions/82357/update-node-on-ubuntu-20043-from-10-to-14-when-installed-via-tutuorial)

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
<span id="post-82357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82357-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I successfully installed an own tileserver via <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/.">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/.</a> For an additional service in Node.js I need Node.js V14, but Node.js V10 has been installed through the mentioned tutorial. Is it possible to Update Node.js to V14? I also heared about nvm to install multiple versions of node.js, but how to run osm with Node.js V10 support and my service with another version simultaneusly?</p>
<p>Regards, Dom</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '21, 12:57</strong></p>
<img src="https://secure.gravatar.com/avatar/2ee56dffff70eb5c464e336817ac08a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dom771013&#39;s gravatar image" />
<p><span>Dom771013</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dom771013 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82357" class="comments-container">
&#10;</div>
<div id="comment-tools-82357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82357-form-container" class="comment-form-container">
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

<span id="82359"></span>

<div id="answer-container-82359" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82359-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dom771013 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>node.js is not required any more once you have set up the tile server, it is only needed for the compilation of the style sheet. So even if a newer version of node would be problematic, it would not impact the working of the tile server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '21, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82359" class="comments-container">
&#10;</div>
<div id="comment-tools-82359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82359-form-container" class="comment-form-container">
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

