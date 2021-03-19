+++
type = "question"
title = "TCP window full"
description = '''I&#x27;m getting a &quot;The transmission window is now completely full&quot; from local sender to server. Does this mean send&#x27;s buffer was full or receiver buffer was full? I check TCP receive window on both end, window size did not shrink. Please help to under transmission window means sender or receiver. Thanks...'''
date = "2011-06-17T08:13:00Z"
lastmod = "2014-12-23T05:26:00Z"
weight = 4610
keywords = [ "window", "full", "tcp" ]
aliases = [ "/questions/4610" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP window full](/questions/4610/tcp-window-full)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4610-score" class="post-score" title="current number of votes">0</div><span id="post-4610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting a "The transmission window is now completely full" from local sender to server. Does this mean send's buffer was full or receiver buffer was full? I check TCP receive window on both end, window size did not shrink. Please help to under transmission window means sender or receiver. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-full" rel="tag" title="see questions tagged &#39;full&#39;">full</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '11, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/7f58f98c7bb01d0827fa2ca5eecc1afb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lung&#39;s gravatar image" /><p><span>lung</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lung has no accepted answers">0%</span></p></div></div><div id="comments-container-4610" class="comments-container"></div><div id="comment-tools-4610" class="comment-tools"></div><div class="clear"></div><div id="comment-4610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4624"></span>

<div id="answer-container-4624" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4624-score" class="post-score" title="current number of votes">4</div><span id="post-4624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "TCP window is now completely full" is a Wireshark generated expert item. It tells you that Wireshark has identified that the current packet has the exact payload size that will fill up the receive buffer on the receiving end (based on the latest seen "Window Size" on a packet from that receiver in the current TCP session).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4624" class="comments-container"><span id="4627"></span><div id="comment-4627" class="comment"><div id="post-4627-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the clarification SYNbit. :)</p></div><div id="comment-4627-info" class="comment-info"><span class="comment-age">(19 Jun '11, 17:34)</span> <span class="comment-user userinfo">John_Modlin</span></div></div><span id="24494"></span><div id="comment-24494" class="comment"><div id="post-24494-score" class="comment-score"></div><div class="comment-text"><p>Is this item warning you that the receiver may have problem on data processing because the receiver window is small?</p></div><div id="comment-24494-info" class="comment-info"><span class="comment-age">(09 Sep '13, 21:37)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="24533"></span><div id="comment-24533" class="comment"><div id="post-24533-score" class="comment-score"></div><div class="comment-text"><p>Receiver's window (i.e., TCP Receive Buffer) may be too small. Or the receiver's application layer may not be processing data fast enough (or at all), causing the receive buffer to fill up. For example, if the application has encountered a record lock and is no longer accepting data from the TCP layer, increasing the receive buffer size would not resolve the problem.</p></div><div id="comment-24533-info" class="comment-info"><span class="comment-age">(10 Sep '13, 12:08)</span> <span class="comment-user userinfo">RussF</span></div></div><span id="38684"></span><div id="comment-38684" class="comment"><div id="post-38684-score" class="comment-score"></div><div class="comment-text"><p>How to increase the receive buffer size?</p></div><div id="comment-38684-info" class="comment-info"><span class="comment-age">(23 Dec '14, 04:15)</span> <span class="comment-user userinfo">ashy</span></div></div><span id="38685"></span><div id="comment-38685" class="comment"><div id="post-38685-score" class="comment-score"></div><div class="comment-text"><p>It's an operating system setting, so depending on your OS you need to find out which command you need. On Windows Vista an up take a look at the <strong>netsh</strong> command.</p></div><div id="comment-38685-info" class="comment-info"><span class="comment-age">(23 Dec '14, 05:26)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-4624" class="comment-tools"></div><div class="clear"></div><div id="comment-4624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

