+++
type = "question"
title = "Detect p2p (torrent) traffic in console with tshark"
description = '''Hello, What are the methods of determining the torrent traffic in console, using a utility tshark? At the moment I use the following command: tshark tcp portrange 6881-6889 Are there other ways?'''
date = "2012-10-11T04:34:00Z"
lastmod = "2012-10-11T05:16:00Z"
weight = 14918
keywords = [ "p2p", "torrent" ]
aliases = [ "/questions/14918" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Detect p2p (torrent) traffic in console with tshark](/questions/14918/detect-p2p-torrent-traffic-in-console-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14918-score" class="post-score" title="current number of votes">0</div><span id="post-14918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>What are the methods of determining the torrent traffic in console, using a utility tshark? At the moment I use the following command:</p><p>tshark tcp portrange 6881-6889</p><p>Are there other ways?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-p2p" rel="tag" title="see questions tagged &#39;p2p&#39;">p2p</span> <span class="post-tag tag-link-torrent" rel="tag" title="see questions tagged &#39;torrent&#39;">torrent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '12, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/d5352b436bf8a484e32225c91054f913?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dkorzhevin&#39;s gravatar image" /><p><span>dkorzhevin</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dkorzhevin has no accepted answers">0%</span></p></div></div><div id="comments-container-14918" class="comments-container"></div><div id="comment-tools-14918" class="comment-tools"></div><div class="clear"></div><div id="comment-14918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14921"></span>

<div id="answer-container-14921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14921-score" class="post-score" title="current number of votes">0</div><span id="post-14921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can try this: <strong>bittorrent</strong> is a valid display filter and you can use it with tshark.</p><blockquote><p><code>tshark -R "bittorrent" -any_other_options</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14921" class="comments-container"></div><div id="comment-tools-14921" class="comment-tools"></div><div class="clear"></div><div id="comment-14921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

