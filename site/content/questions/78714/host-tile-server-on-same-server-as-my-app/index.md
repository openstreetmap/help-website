+++
type = "question"
title = "Host Tile Server on same server as my app ?"
description = '''Hello, I&#x27;m currently developing an app which require a lot of map displays and want to add my custom style to the map. After some research I came across a lot of tutorials about Tile Server building. So I think I can manage to do that but I have several question to grasp the concept :   Can I host t...'''
date = "2021-02-07T19:42:00Z"
lastmod = "2021-02-07T20:19:00Z"
weight = 78714
keywords = [ "tiles", "server", "tileserver" ]
aliases = [ "/questions/78714" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Host Tile Server on same server as my app ?](/questions/78714/host-tile-server-on-same-server-as-my-app)

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
<span id="post-78714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm currently developing an app which require a lot of map displays and want to add my custom style to the map. After some research I came across a lot of tutorials about Tile Server building.</p>
<p>So I think I can manage to do that but I have several question to grasp the concept :</p>
<ul>
<li><p>Can I host the Tile server on the same server that will be hosting my web app ? Because I will mostly have only one region of country (France) displayed.</p></li>
<li><p>I saw a topic about "pre-rendering" tiles which would help to avoid to calculate the tiles every time a user want the map to be displayed. Is it right or I have misunderstood something ?</p></li>
<li><p>How to host multiple custom style on the same server, to allow preference settings for user ?</p></li>
</ul>
<p>Thank you a lot for your answer.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '21, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/43b399be7dc83c32034c7d636028bf7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="senseikaii&#39;s gravatar image" />
<p><span>senseikaii</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="senseikaii has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78714" class="comments-container">
&#10;</div>
<div id="comment-tools-78714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78714-form-container" class="comment-form-container">
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

<span id="78715"></span>

<div id="answer-container-78715" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78715-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="senseikaii has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes you can run a tile server in addition to other things on the server. Essentially, you will be installing the Apache web server, and the <code>mod_tile</code> Apache module, and then you will instruct the module to respond to requests starting with some prefix, e.g. "/tiles/style1" or so. And you will be able to host other things normally outside of that path.</p>
<p>Yes, pre-rendering makes sense especially for low zoom levels e.g. 1-12. Not for all zoom levels - if you pre-render France to zoom 18 that would take weeks and use too much space. There are many regions in France that nobody will ever use your app in so it would be wasteful to pre-render everything to the highest zoom.</p>
<p>It is no problem to host multiple styles, however each style requires a separate tile storage on the server, and separate pre-rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '21, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78715" class="comments-container">
<span id="78716"></span>
<div id="comment-78716" class="comment">
<div id="post-78716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer. Do yo know where can I find a tutorial about prerendring tiles ? Also I will be using flask app, do you think I need docker inside the server to keep Tile and App separated ? Sorry it it seems like a dumb question but still willing to grasp every aspect before doing it</p>
</div>
<div id="comment-78716-info" class="comment-info">
<span class="comment-age">(07 Feb '21, 20:19)</span> <span class="comment-user userinfo">senseikaii</span>
</div>
</div>
</div>
<div id="comment-tools-78715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78715-form-container" class="comment-form-container">
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

