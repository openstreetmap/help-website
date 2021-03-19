+++
type = "question"
title = "Wireshark Blocks When Connecting to RPCAP Server"
description = '''I&#x27;m using the latest stable version 2.2.1 (32-bit) on Windows with WinPcap from the installer. I&#x27;m starting rpcapd with: rpcapd.exe -b 127.0.0.1 -p 3333 -n and then I try to connect from Wireshark -&amp;gt; Remote Interfaces to the above - Host: 127.0.0.1, Port: 3333, Null auth. Wireshark blocks and I h...'''
date = "2016-11-14T10:36:00Z"
lastmod = "2016-11-14T13:57:00Z"
weight = 57381
keywords = [ "rpcapd", "rpcap" ]
aliases = [ "/questions/57381" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Blocks When Connecting to RPCAP Server](/questions/57381/wireshark-blocks-when-connecting-to-rpcap-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57381-score" class="post-score" title="current number of votes">0</div><span id="post-57381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using the latest stable version 2.2.1 (32-bit) on Windows with WinPcap from the installer. I'm starting rpcapd with:</p><p><code>rpcapd.exe -b 127.0.0.1 -p 3333 -n</code></p><p>and then I try to connect from Wireshark -&gt; Remote Interfaces to the above - Host: 127.0.0.1, Port: 3333, Null auth. Wireshark blocks and I have to end the process. After this I still have a Dumpcap process in the task manager which is consuming 100% of a core. I sniffed the loopback interface using RawCap and the communication is as follows:</p><ol><li>Authentication request and reply</li><li>Find all interfaces request and reply</li><li>Authentication request and reply, again</li><li>Open request and reply</li></ol><p>IIRC the next packet should've been Start Capture, but I'm not seeing it. Any hints?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpcapd" rel="tag" title="see questions tagged &#39;rpcapd&#39;">rpcapd</span> <span class="post-tag tag-link-rpcap" rel="tag" title="see questions tagged &#39;rpcap&#39;">rpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '16, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/96e719a162b10d33fccc5ebe11da01df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adrian-nicolau&#39;s gravatar image" /><p><span>adrian-nicolau</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adrian-nicolau has no accepted answers">0%</span></p></div></div><div id="comments-container-57381" class="comments-container"></div><div id="comment-tools-57381" class="comment-tools"></div><div class="clear"></div><div id="comment-57381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57382"></span>

<div id="answer-container-57382" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57382-score" class="post-score" title="current number of votes">1</div><span id="post-57382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="adrian-nicolau has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is tracked by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13102">bug 13102</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '16, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-57382" class="comments-container"></div><div id="comment-tools-57382" class="comment-tools"></div><div class="clear"></div><div id="comment-57382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

