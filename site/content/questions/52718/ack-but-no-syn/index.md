+++
type = "question"
title = "ACK but no SYN"
description = '''I placed a packet capture on a particular interface of an ASA firewall with a view to establishing what a device connected to that interface was trying to do and hence what ACL I needed on the interface. Below is an extract from the packet capture, filtered on both source and destination address (an...'''
date = "2016-05-18T06:17:00Z"
lastmod = "2016-05-18T07:40:00Z"
weight = 52718
keywords = [ "ack", "syn" ]
aliases = [ "/questions/52718" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ACK but no SYN](/questions/52718/ack-but-no-syn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52718-score" class="post-score" title="current number of votes">0</div><span id="post-52718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I placed a packet capture on a particular interface of an ASA firewall with a view to establishing what a device connected to that interface was trying to do and hence what ACL I needed on the interface. Below is an extract from the packet capture, filtered on both source and destination address (anonymised). From what I know about this particular application I believe the device on 10.0.0.1 <em>is</em> trying to initiate a connection to 172.16.0.1 but I am not seeing any SYN packets, only ACK.</p><p>Can anyone explain why I might not be seeing any SYN packets?</p><pre><code>10  0.000351    10.0.0.1    172.16.0.1  TCP 58  64456 → 22 [ACK] Seq=1 Ack=1 Win=65535 Len=0
11  0.000366    10.0.0.1    172.16.0.1  TCP 58  64456 → 22 [ACK] Seq=1 Ack=2721 Win=65535 Len=0
14  0.000611    10.0.0.1    172.16.0.1  TCP 58  64456 → 22 [ACK] Seq=1 Ack=5317 Win=65535 Len=0
27  0.003830    10.0.0.1    172.16.0.1  TCP 58  64456 → 22 [ACK] Seq=1 Ack=8037 Win=65535 Len=0
113 0.013519    10.0.0.1    172.16.0.1  SSH 110 Client: Encrypted packet (len=52)
120 0.229191    10.0.0.1    172.16.0.1  TCP 58  64456 → 22 [ACK] Seq=53 Ack=46581 Win=64823 Len=0
227 4.635380    10.0.0.1    172.16.0.1  SSH 174 Client: Encrypted packet (len=116)
234 4.862343    10.0.0.1    172.16.0.1  TCP 58  64456 → 22 [ACK] Seq=169 Ack=46665 Win=64739 Len=0
931 35.263399   10.0.0.1    172.16.0.1  SSH 262 Client: Encrypted packet (len=204)
932 35.263826   10.0.0.1    172.16.0.1  TCP 58  64456 → 22 [FIN, ACK] Seq=373 Ack=46665 Win=64739 Len=0
2229    94.854500   10.0.0.1    172.16.0.1  TCP 58  64456 → 22 [ACK] Seq=374 Ack=46666 Win=64739 Len=0</code></pre><p>Thanks, Phil.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/afa9d2c224acfd1d545b8ad7e5c2b700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phil6564&#39;s gravatar image" /><p><span>phil6564</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phil6564 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 May '16, 06:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-52718" class="comments-container"></div><div id="comment-tools-52718" class="comment-tools"></div><div class="clear"></div><div id="comment-52718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52723"></span>

<div id="answer-container-52723" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52723-score" class="post-score" title="current number of votes">1</div><span id="post-52723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Don't let the fact that seq and ack numbers start from 1 mislead you. Unless you explicitly tell it not to do so, tshark (and Wireshark as well) shows relative values, and takes the values in the very first packet of each tcp session it can see as references, hence the relative values shown for them are 1. However, the first packet seen in the capture may not be the first packet in the session. So unless you are really, really, really sure that the session you've shown here has started later than the capture itself, the simplest explanation is that the session had already been established when you started to capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 May '16, 07:06</strong> </span></p></div></div><div id="comments-container-52723" class="comments-container"><span id="52726"></span><div id="comment-52726" class="comment"><div id="post-52726-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response Sindy.</p><p>So, from the output above, without seeing any SYN packets, is it possible to say for certain that connections are being initiated from 10.0.0.1?</p></div><div id="comment-52726-info" class="comment-info"><span class="comment-age">(18 May '16, 07:24)</span> <span class="comment-user userinfo">phil6564</span></div></div><span id="52730"></span><div id="comment-52730" class="comment"><div id="post-52730-score" class="comment-score"></div><div class="comment-text"><p>Well, nothing is really certain, but as tcp/22 is a "well-known" port at which the ssh service is listening on servers, while tcp/64456 is a typical client-side ephemeral port (which the client's TCP stack chooses when initiating sessions), and as the contents of those packets seems to make sense to the SSH dissector which tshark has chosen to dissect them based on the use of the tcp/22 port, we can assume that the session has really been initiated by 10.0.0.1 quite safely.</p><p>What would bother me as a network administrator would be why I can see only packets in one direction. If it is due to your use of capture filter or display filter which hides the other direction from being seen, or due to mirroring of only one direction of a switch port, allright; otherwise (i.e. if no packets are filtered out intentionally), I'd assume that the other direction bypasses the interface at which you capture, which could affect the ability of the ASA to handle the traffic properly.</p></div><div id="comment-52730-info" class="comment-info"><span class="comment-age">(18 May '16, 07:40)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52723" class="comment-tools"></div><div class="clear"></div><div id="comment-52723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

