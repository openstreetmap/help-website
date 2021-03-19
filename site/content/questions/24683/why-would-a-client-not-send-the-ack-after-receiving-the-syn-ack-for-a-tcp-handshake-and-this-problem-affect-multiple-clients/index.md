+++
type = "question"
title = "Why would a client not send the [ACK] after receiving the [SYN, ACK] for a TCP handshake and this problem affect multiple clients?"
description = '''I have been investigating a &quot;slow&quot; application complaint. When the issue happens I&#x27;ve been told it affects everyone. I did a Wireshark capture on the server and one client. On the server, I saw the [SYN],[SYN, ACK] but no [ACK] when the problem started. I went back to a capture on the client and saw...'''
date = "2013-09-14T10:05:00Z"
lastmod = "2013-09-17T12:28:00Z"
weight = 24683
keywords = [ "handshake", "tcp" ]
aliases = [ "/questions/24683" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why would a client not send the \[ACK\] after receiving the \[SYN, ACK\] for a TCP handshake and this problem affect multiple clients?](/questions/24683/why-would-a-client-not-send-the-ack-after-receiving-the-syn-ack-for-a-tcp-handshake-and-this-problem-affect-multiple-clients)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24683-score" class="post-score" title="current number of votes">0</div><span id="post-24683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been investigating a "slow" application complaint. When the issue happens I've been told it affects everyone. I did a Wireshark capture on the server and one client. On the server, I saw the [SYN],[SYN, ACK] but no [ACK] when the problem started. I went back to a capture on the client and saw the [SYN], [SYN, ACK] and no [ACK] sent. Normally, I would think that this is a problem with the client NIC or drivers. But, multiple clients are experiencing problems. I thought it might be a bad checksum on the [SYN, ACK] but Wireshark says that the checksum is good. Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '13, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/62a16882bb7093e4b5ce080f67904e84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bbulen&#39;s gravatar image" /><p><span>bbulen</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bbulen has no accepted answers">0%</span></p></div></div><div id="comments-container-24683" class="comments-container"><span id="24690"></span><div id="comment-24690" class="comment"><div id="post-24690-score" class="comment-score"></div><div class="comment-text"><p>I uploaded two captures. One from the server and one from the client. Unfortunately, they weren't captured at the same time. The server capture shows one successfully connection to the client right before two failed connections.</p><p><a href="https://www.cloudshark.org/captures/89061479e926">https://www.cloudshark.org/captures/89061479e926</a></p><p><a href="https://www.cloudshark.org/captures/a3ad9d20cae7">https://www.cloudshark.org/captures/a3ad9d20cae7</a></p></div><div id="comment-24690-info" class="comment-info"><span class="comment-age">(14 Sep '13, 13:50)</span> <span class="comment-user userinfo">bbulen</span></div></div></div><div id="comment-tools-24683" class="comment-tools"></div><div class="clear"></div><div id="comment-24683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24695"></span>

<div id="answer-container-24695" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24695-score" class="post-score" title="current number of votes">0</div><span id="post-24695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bbulen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I uploaded two captures.</p></blockquote><p>There is nothing I can detect in the capture files that might explain the behavior.</p><p>I conclude: This must be related to the client, which could be:</p><ul><li>a browser issue, if a browser was used</li><li>a software bug, if an application opens the connection to the server</li><li>an issue with the NIC</li><li>an issue with the NIC driver</li><li>Interfering software, running on the client, like the following software: Firewall, IDS, AV, VPN Client, Endpoint Protection</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24695" class="comments-container"><span id="24698"></span><div id="comment-24698" class="comment"><div id="post-24698-score" class="comment-score"></div><div class="comment-text"><p>Thank you for reviewing it.</p><p>After I posted the question, I thought I should confirm that the other clients are experiencing the same issue to confirm that there aren't multiple problems.</p></div><div id="comment-24698-info" class="comment-info"><span class="comment-age">(14 Sep '13, 16:33)</span> <span class="comment-user userinfo">bbulen</span></div></div><span id="24865"></span><div id="comment-24865" class="comment"><div id="post-24865-score" class="comment-score"></div><div class="comment-text"><p>Thank you for reviewing the captures.</p><p>It turns out that there were two different problems. The <strong>NIC of the client</strong> I looked at <strong>was bad</strong>. And, the <strong>antivirus software on the server was misbehaving</strong> causing the widespread complaints.</p></div><div id="comment-24865-info" class="comment-info"><span class="comment-age">(17 Sep '13, 12:28)</span> <span class="comment-user userinfo">bbulen</span></div></div></div><div id="comment-tools-24695" class="comment-tools"></div><div class="clear"></div><div id="comment-24695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24688"></span>

<div id="answer-container-24688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24688-score" class="post-score" title="current number of votes">0</div><span id="post-24688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, if it is the same server suddenly having problems with multiple (=all?) clients not ack-ing its syn-ack packets it should be 'something' in those 2/3 of the handshake packets. Can you post them in www.cloudshark.org for us to have a look? Some possibilities: - invalid ack number - invalid options</p><hr /><h2 id="server-trace">Server trace</h2><p>The server is receiving 3 syn request simultaneously from the (winXP?) client on the same LAN, only the first one making it into an established state with subsequent TLS handshake. The other 2 are entering retransmission from the server side only.</p><h2 id="client-trace">Client trace</h2><p>The client trace only shows one tcp session that does not get an ack from the client. There is nothing wrong with the server's syn_ack. The fact that it is seen in the client's capture excludes a network/NIC issue. So, the question is: Did the Win TCP stack see the syn-ack?</p><p>I believe it did, but for some reason discarded it, because we would have seen the client retransmitting its own syn packets otherwise. As we don't see any retransmissions by the client, the TCP stack of the must no longer be interested in setting up those sessions.</p><p>When you issue a netstat at the client, do you see any longer lasting syn_sent connections?</p><p>There have been some discussions with winXp and half-open limits, not sure if they would apply here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '13, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '13, 03:21</strong> </span></p></div></div><div id="comments-container-24688" class="comments-container"></div><div id="comment-tools-24688" class="comment-tools"></div><div class="clear"></div><div id="comment-24688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

