+++
type = "question"
title = "Application RST"
description = '''I&#x27;m a newbie to Wireshark and have a question on a Reset I&#x27;m seeing in the trace with an application that&#x27;s getting intermittent connection failure. There is a firewall in the path but no other applications are having issues. I did a Follow TCP stream for a known failure transaction and a good trans...'''
date = "2011-11-01T04:20:00Z"
lastmod = "2011-11-02T03:29:00Z"
weight = 7179
keywords = [ "rst" ]
aliases = [ "/questions/7179" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Application RST](/questions/7179/application-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7179-score" class="post-score" title="current number of votes">0</div><span id="post-7179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a newbie to Wireshark and have a question on a Reset I'm seeing in the trace with an application that's getting intermittent connection failure. There is a firewall in the path but no other applications are having issues. I did a Follow TCP stream for a known failure transaction and a good transaction. I'm not sure but the failure transaction could be due to the Reset but want to confirm if it's the application that's the cause or the Firewall. For the failed transaction, a RST was sent by the Source host (SH) in the third line. I would think the RST would basically kills the transaction and the Destination host (DH)FIN,ACK in the fourth line would not be valid. Please chime in.</p><p>Failed Transaction: 1. (SH)FIN,ACK 2. (DH)PSH,ACK 3. (SH)RST 4. (DH)FIN,ACK 5. (DH)RST</p><p>Good Transaction:: 1. (SH)FIN,ACK 2. (DH)ACK 3. (SH)RST</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '11, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p><span>ws2006</span><br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div></div><div id="comments-container-7179" class="comments-container"></div><div id="comment-tools-7179" class="comment-tools"></div><div class="clear"></div><div id="comment-7179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7181"></span>

<div id="answer-container-7181" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7181-score" class="post-score" title="current number of votes">0</div><span id="post-7181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here's the sequence for the follow TCP stream</p><p>10.1.1.1 to 192.168.1.1 (FIN, ACK) Sequence number: 304 Acknowledgement number: 172</p><p>192.168.1.1 to 10.1.1.1 (ACK) Len:1248 Sequence number: 172 Next Sequence number: 1420 Acknowledgement number: 304</p><p>10.1.1.1 to 192.168.1.1 (RST) Sequence number: 304 WIN=0 Len=0</p><p>192.168.1.1 to 10.1.1.1 (ACK) Len:1248 Sequence number: 1420 Next Sequence number: 2668 Acknowledgement number: 304</p><p>192.168.1.1 to 10.1.1.1 (FIN, PSH, ACK) Len:1027 Sequence number: 2668 Next Sequence number: 3695 Acknowledgement number: 305</p><p>10.1.1.1 to 192.168.1.1 (RST) Sequence number: 305 WIN=0 Len=0</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '11, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p><span>ws2006</span><br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div></div><div id="comments-container-7181" class="comments-container"></div><div id="comment-tools-7181" class="comment-tools"></div><div class="clear"></div><div id="comment-7181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7193"></span>

<div id="answer-container-7193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7193-score" class="post-score" title="current number of votes">0</div><span id="post-7193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The only thing that I can say is that FIN packets are pretty much always generated by the actually endpoint hosts in the conversation. RST packets may be sent by the hosts, though sometimes are sent by the firewall if they aren't happy with the connection status. If a host is seems to be sending packets after a RST is seen, this could be just a timing issue, in that packets were being flushed after receiving the FIN, but before the RST. (It all depends where you do the capture, and the latency of the network)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '11, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-7193" class="comments-container"><span id="7194"></span><div id="comment-7194" class="comment"><div id="post-7194-score" class="comment-score"></div><div class="comment-text"><p>The traffic is only local LAN. A static entry was made for the inside host 10.1.1.1 on the FW recently and the RST went away. This apps that was having issue was running fine then started to experience disconnects while other applications do not have disconnects issue. The apps team blamed it on the network but it's possible the apps code were changed prior to the FW rule change.</p></div><div id="comment-7194-info" class="comment-info"><span class="comment-age">(02 Nov '11, 03:29)</span> <span class="comment-user userinfo">ws2006</span></div></div></div><div id="comment-tools-7193" class="comment-tools"></div><div class="clear"></div><div id="comment-7193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

