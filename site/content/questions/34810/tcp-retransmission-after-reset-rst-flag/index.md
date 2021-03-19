+++
type = "question"
title = "TCP Retransmission after Reset RST flag"
description = '''I have around 20 clients communicating together with a central server in the same LAN. The clients can make transaction simultaneously with the server. The server forward each transaction to external appliance in the network. Sometimes it works, sometimes my application shows a &quot;time out&quot; message in...'''
date = "2014-07-22T01:08:00Z"
lastmod = "2014-08-01T01:39:00Z"
weight = 34810
keywords = [ "rst", "ack", "retransmissions", "tcp", "wireshark" ]
aliases = [ "/questions/34810" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmission after Reset RST flag](/questions/34810/tcp-retransmission-after-reset-rst-flag)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34810-score" class="post-score" title="current number of votes">0</div><span id="post-34810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have around 20 clients communicating together with a central server in the same LAN. The clients can make transaction simultaneously with the server. The server forward each transaction to external appliance in the network. Sometimes it works, sometimes my application shows a "time out" message in a client screen (randomly)</p><p>I mirrored all traffic and found TCP Retransmission after TCP Reset packets for the first TCP Sequence. I immediately thought about packet loss but all my cables/NIC are fine, and I do not see DUP ACK in the capture.</p><p>It seems that RST packets may have different significations.<br />
<strong>What causes those TCP Reset?<br />
Where should I focus my investigation: network or application design ?</strong></p><p>I would appreciate any help. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '14, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/655926f64e07a73b158d10fdf0739398?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Julien&#39;s gravatar image" /><p><span>Julien</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Julien has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Aug '14, 00:49</strong> </span></p></div></div><div id="comments-container-34810" class="comments-container"><span id="34811"></span><div id="comment-34811" class="comment"><div id="post-34811-score" class="comment-score"></div><div class="comment-text"><p>can you provide a capture file, e.g. on www.cloudshark.org? I doubt anyone will read/analyze that many packets in an ASCII dump.</p></div><div id="comment-34811-info" class="comment-info"><span class="comment-age">(22 Jul '14, 01:22)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="34812"></span><div id="comment-34812" class="comment"><div id="post-34812-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper. Thanks for the suggestion. I've updated the post.</p></div><div id="comment-34812-info" class="comment-info"><span class="comment-age">(22 Jul '14, 01:54)</span> <span class="comment-user userinfo">Julien</span></div></div></div><div id="comment-tools-34810" class="comment-tools"></div><div class="clear"></div><div id="comment-34810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34815"></span>

<div id="answer-container-34815" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34815-score" class="post-score" title="current number of votes">0</div><span id="post-34815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your clients do connect to 137.56.64.31 at port 2200. Those connections work fine, according to the data in the capture file. But then the clients do connect to the same server on ports 11007,11008,11012,11014 and 11015. Those are connection attempts that get a RESET. The client seems to either ignore the RESET, as it sends the SYN again, or the RESET does not reach the client.</p><p>To me it looks like those ports are dynamically negotiated in your application, similar to FTP, where a dynamic port is "negotiated" in the control channel on port 21.<br />
</p><p>Maybe the server did not open a socket (fast enough) for the 'announced' port (110xx) and thus the OS sends a RESET. Without an in-depth understanding of your application, it's impossible to explain why this happens.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '14, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-34815" class="comments-container"><span id="34827"></span><div id="comment-34827" class="comment"><div id="post-34827-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Kurt! Could RESET be due to the network or physical layer? Ive updated my post with some info about the application (if it helps) If needed I can provide a capture from the server (more packets exchanges)</p></div><div id="comment-34827-info" class="comment-info"><span class="comment-age">(22 Jul '14, 06:41)</span> <span class="comment-user userinfo">Julien</span></div></div><span id="34828"></span><div id="comment-34828" class="comment"><div id="post-34828-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Could RESET be due to the network or physical layer?</p></blockquote><p>Physical layer? Well..., no. How should send the RESET at the physical layer? The cable? I don't think so ;-))</p><p>Network layer? Well...., yes or maybe. There <strong>could</strong> be a device between the client and the server that blocks the connections, like a firewall. However, in your case it must be a transparent firewall, as the MAC addresses are all the same, so that does not sound very reasonable to me either.</p><p><strong>More likely</strong> it's the server (firewall on the server) or your application (bug), and according to <a href="http://en.wikipedia.org/wiki/Occam&#39;s_razor">Occam's razor</a>:</p><ul><li>"among competing hypotheses, the one with the fewest assumptions should be selected" ;-)</li></ul><blockquote><p>Where should I focus my investigation: network or application design ?</p></blockquote><p>If you capture on the server and if you see the RESET there as well, it's pretty clear that it's most likely an application problem, which I believe, based on you capture file.</p><p>So, I suggest to concentrate on the application!</p></div><div id="comment-34828-info" class="comment-info"><span class="comment-age">(22 Jul '14, 08:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35046"></span><div id="comment-35046" class="comment"><div id="post-35046-score" class="comment-score"></div><div class="comment-text"><p>any progress here?</p></div><div id="comment-35046-info" class="comment-info"><span class="comment-age">(01 Aug '14, 01:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-34815" class="comment-tools"></div><div class="clear"></div><div id="comment-34815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

