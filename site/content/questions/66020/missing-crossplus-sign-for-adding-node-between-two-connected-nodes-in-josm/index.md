+++
type = "question"
title = "Missing cross/plus sign for adding node between two connected nodes in josm"
description = '''There used to appear a plus sign between two connected nodes after selecting a path for editing in JOSM. Clicking that plus sign after selecting the path , used to add another node between two nodes. I&#x27;m not seeing this anymore for several days. I have tried many ways, also searched on internet, fou...'''
date = "2018-09-22T17:38:00Z"
lastmod = "2018-09-22T18:33:00Z"
weight = 66020
keywords = [ "node", "josm" ]
aliases = [ "/questions/66020" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Missing cross/plus sign for adding node between two connected nodes in josm](/questions/66020/missing-crossplus-sign-for-adding-node-between-two-connected-nodes-in-josm)

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
<span id="post-66020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66020-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There used to appear a plus sign between two connected nodes after selecting a path for editing in JOSM. Clicking that plus sign after selecting the path , used to add another node between two nodes. I'm not seeing this anymore for several days. I have tried many ways, also searched on internet, found nowhere about this problem. In this time, i've updated several times my josm, reset my config file {by crash or by myself }, still that plus sign never came.</p>
<p>anybody can help me about it? this feature is so needy. To add nodes on existing way, every time clicking draw node [A], then adding node and pressing esc is annoying.</p>
<p><img src="/upfiles/no_plus_sign_between_two_nodes_in_josm.png" alt="no plus sign between two nodes in josm" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '18, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/798b56f33fa254218e756526fc8b6654?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zabir&#39;s gravatar image" />
<p><span>zabir</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zabir has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Sep '18, 18:20</strong> </span></p>
</div>
</div>
<div id="comments-container-66020" class="comments-container">
&#10;</div>
<div id="comment-tools-66020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66020-form-container" class="comment-form-container">
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

<span id="66021"></span>

<div id="answer-container-66021" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66021-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-66021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zabir has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the setting you need is in:</p>
<p>Preferences (F12) &gt; OSM Data: under <em>Select and draw mode options</em> tick the box labelled "Draw virtual nodes in select mode".</p>
<p>As an aside: I find that for tweaking ways to give better alignment the <em>Improve Way Accuracy mode</em> (shortcut:w) is better as CTRL + click gives a new node wherever you want rather than having to drag a specific point to where you want it. Moving existing nodes is also easier too as when you click it automatically moves the nearest node of a selected way to your mouse pointer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '18, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-66021" class="comments-container">
<span id="66022"></span>
<div id="comment-66022" class="comment">
<div id="post-66022-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you so much. ticking "Draw virtual nodes in select mode" option and then a restart did the trick :] . After almost 2 months, it is back again :].</p>
<p>And also thanks for the Control click in Accuracy way, I didn't know that ctrl+click adds new nodes in that mode. Thanks.</p>
</div>
<div id="comment-66022-info" class="comment-info">
<span class="comment-age">(22 Sep '18, 18:33)</span> <span class="comment-user userinfo">zabir</span>
</div>
</div>
</div>
<div id="comment-tools-66021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66021-form-container" class="comment-form-container">
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

