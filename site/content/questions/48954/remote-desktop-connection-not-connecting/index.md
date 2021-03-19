+++
type = "question"
title = "Remote Desktop Connection not connecting"
description = '''Hello, I am currently Troubleshooting 2 hosts whom are on separate LANs with a Cisco Router in between the two. Now for clarification both PCs are running windows 7, and firewalls have been configured to allow Remote Desktop connections on the PCs.All configurations on the Cisco router are set to de...'''
date = "2016-01-07T12:13:00Z"
lastmod = "2016-01-09T12:50:00Z"
weight = 48954
keywords = [ "troubleshooting", "rdp" ]
aliases = [ "/questions/48954" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Desktop Connection not connecting](/questions/48954/remote-desktop-connection-not-connecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48954-score" class="post-score" title="current number of votes">0</div><span id="post-48954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am currently Troubleshooting 2 hosts whom are on separate LANs with a Cisco Router in between the two. Now for clarification both PCs are running windows 7, and firewalls have been configured to allow Remote Desktop connections on the PCs.All configurations on the Cisco router are set to default and there are no ACL or blockings on the cisco router.Both PCs can access the internet and there is no connectivity issues other than the Remote Desktop connection. The following TCP packets were found from the local machine to the remote PC:</p><pre><code>Packet#1 Length:66, Ports:50351--&gt;3389 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
Packet#2 Length 54, Ports 3389--&gt;50351 [RST,ACK] seq=1 ack=1 win=0 len=0
Packet#3 Length 66, [TCP Spurious Retransmisson] 50351--&gt;3389 [SYN] seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1</code></pre><p>and then it repeats back to a similar packet to Packet#2.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span> <span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '16, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/1a8e4aecf559c22f886d32eb6cffee2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lhoxey&#39;s gravatar image" /><p><span>Lhoxey</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lhoxey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jan '16, 15:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48954" class="comments-container"></div><div id="comment-tools-48954" class="comment-tools"></div><div class="clear"></div><div id="comment-48954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48957"></span>

<div id="answer-container-48957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48957-score" class="post-score" title="current number of votes">0</div><span id="post-48957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What does the remote side look like? Do you see the same. The RST in the second packet says in that case that the connection is refused, either by the remote host itsself (for example the port 3389 is not open) or by an acl / firewall rule on the path.</p><p>So the easiest way will be to check the remote side.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '16, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jan '16, 22:27</strong> </span></p></div></div><div id="comments-container-48957" class="comments-container"><span id="48959"></span><div id="comment-48959" class="comment"><div id="post-48959-score" class="comment-score"></div><div class="comment-text"><p>On the Remote side i do see the same exact packet (RST). The Local port that Remote Desktop uses is port 3389 I thought?</p></div><div id="comment-48959-info" class="comment-info"><span class="comment-age">(07 Jan '16, 16:18)</span> <span class="comment-user userinfo">Lhoxey</span></div></div><span id="48964"></span><div id="comment-48964" class="comment"><div id="post-48964-score" class="comment-score"></div><div class="comment-text"><p>Oh sorry, my fault. Of course it is the port 3389.</p></div><div id="comment-48964-info" class="comment-info"><span class="comment-age">(07 Jan '16, 22:36)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="49033"></span><div id="comment-49033" class="comment"><div id="post-49033-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Now for clarification both PCs are running windows 7, and firewalls have been configured to allow Remote Desktop connections on the PCs.</p></blockquote><p>I'd bet that the Windows Firewall configuration is wrong ;-) OR there is some additional security software on the target machine (Endpoint Security), blocking the SYN request. Please disable Windows Firewall completely and try again. If it's still not working, try to identify other security software. If there is none, please check with <strong>netstat -na</strong> that the system is actually listening to port 3389 !!</p></div><div id="comment-49033-info" class="comment-info"><span class="comment-age">(09 Jan '16, 12:50)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-48957" class="comment-tools"></div><div class="clear"></div><div id="comment-48957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

