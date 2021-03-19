+++
type = "question"
title = "Interface data from file"
description = '''Hello, can I somehow simulate an interface with a file? That is, I have a file with sniffed data (not sniffed with Wireshark) that consists of a bunch of hex numbers which symbolize the data going through the interface. Can I somehow input this data in Wireshark and dissect it with the protocols tha...'''
date = "2012-12-05T02:59:00Z"
lastmod = "2012-12-05T10:58:00Z"
weight = 16579
keywords = [ "interface", "file" ]
aliases = [ "/questions/16579" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Interface data from file](/questions/16579/interface-data-from-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16579-score" class="post-score" title="current number of votes">0</div><span id="post-16579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>can I somehow simulate an interface with a file? That is, I have a file with sniffed data (not sniffed with Wireshark) that consists of a bunch of hex numbers which symbolize the data going through the interface. Can I somehow input this data in Wireshark and dissect it with the protocols that I wish?</p><p>Thank you very much!</p><p>Best regards, Matheus Priebe Bertram</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/b15e02964ce3e65a7e667354809a33e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matheus%20Priebe%20Bertram&#39;s gravatar image" /><p><span>Matheus Prie...</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matheus Priebe Bertram has one accepted answer">100%</span></p></div></div><div id="comments-container-16579" class="comments-container"></div><div id="comment-tools-16579" class="comment-tools"></div><div class="clear"></div><div id="comment-16579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16581"></span>

<div id="answer-container-16581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16581-score" class="post-score" title="current number of votes">0</div><span id="post-16581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use a traffic generator/replay tool like bittwist, tcpreplay or ostinato to generate "life" traffic from a capture file, and recapture it with Wireshark.</p><p>Warning: you should isolate the traffic generator in a network with no vital/production systems, or you might wreak havoc on your life network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16581" class="comments-container"></div><div id="comment-tools-16581" class="comment-tools"></div><div class="clear"></div><div id="comment-16581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16603"></span>

<div id="answer-container-16603" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16603-score" class="post-score" title="current number of votes">0</div><span id="post-16603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap</a>. Format the data in a way that text2pcap understands and you might be able to dissect that data in Wireshark.</p><blockquote><p><code>http://www.wireshark.org/docs/man-pages/text2pcap.html</code><br />
</p></blockquote><p>If your data (hex numbers) is only the TCP/UDP payload, you can tell text2pcap to add dummy IP+UDP/TCP headers (option -i, -u, -T).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16603" class="comments-container"></div><div id="comment-tools-16603" class="comment-tools"></div><div class="clear"></div><div id="comment-16603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

