+++
type = "question"
title = "eth.addr filter ?"
description = '''Hi, I am trying to use the eth.addr filter, i need to see only the comunication from and to this mac address i use the filter eth.addr==2c:39:96:54:89:48 but blank page... i have 2c:39:96:54:89:48 traffic, when i use sll.src.eth == 2c:39:96:54:89:48 i have a lot of packet. I am using the version 1.1...'''
date = "2013-11-27T00:47:00Z"
lastmod = "2013-11-28T00:03:00Z"
weight = 27472
keywords = [ "eth.addr", "ethernet", "sll", "cooked", "display-filter" ]
aliases = [ "/questions/27472" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [eth.addr filter ?](/questions/27472/ethaddr-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27472-score" class="post-score" title="current number of votes">0</div><span id="post-27472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to use the eth.addr filter, i need to see only the comunication from and to this mac address i use the filter eth.addr==2c:39:96:54:89:48 but blank page... i have 2c:39:96:54:89:48 traffic, when i use sll.src.eth == 2c:39:96:54:89:48 i have a lot of packet.</p><p>I am using the version 1.10.3 of wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eth.addr" rel="tag" title="see questions tagged &#39;eth.addr&#39;">eth.addr</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-sll" rel="tag" title="see questions tagged &#39;sll&#39;">sll</span> <span class="post-tag tag-link-cooked" rel="tag" title="see questions tagged &#39;cooked&#39;">cooked</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '13, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/a6d43c3927d39c82135364e14f3cd734?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pouet-Lord&#39;s gravatar image" /><p><span>Pouet-Lord</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pouet-Lord has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Nov '13, 06:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-27472" class="comments-container"></div><div id="comment-tools-27472" class="comment-tools"></div><div class="clear"></div><div id="comment-27472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27486"></span>

<div id="answer-container-27486" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27486-score" class="post-score" title="current number of votes">2</div><span id="post-27486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pouet-Lord has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You apparently have a Linux cooked-mode capture file. You can verify this in Wireshark by viewing the encapsulation entry in the <code>Statistics -&gt; Summary</code> window. This means that there is no Ethernet encapsulation, thus the <code>eth.addr</code> (or any other <code>eth</code> filter) won't match any packets. As you've discovered, you'll need to use the <code>sll</code> filters.</p><p>For further information on this topic, refer to the <a href="http://wiki.wireshark.org/SLL">Linux cooked-mode capture wiki page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '13, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27486" class="comments-container"><span id="27521"></span><div id="comment-27521" class="comment"><div id="post-27521-score" class="comment-score"></div><div class="comment-text"><p>Hello, thank you for your reply.</p></div><div id="comment-27521-info" class="comment-info"><span class="comment-age">(28 Nov '13, 00:03)</span> <span class="comment-user userinfo">Pouet-Lord</span></div></div></div><div id="comment-tools-27486" class="comment-tools"></div><div class="clear"></div><div id="comment-27486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

