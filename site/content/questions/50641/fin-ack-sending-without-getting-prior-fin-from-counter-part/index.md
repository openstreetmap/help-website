+++
type = "question"
title = "[FIN, ACK]  sending without getting prior [FIN] from counter part"
description = '''Recently I got a strange phenomenon that is server sends FIN/ACK at the same time without getting prior FIN from client(There was no FIN from client in my Wireshark dump at least.) As far as I know, normal TCP disconnection is 4 way hand shaking like FIN-ACK-FIN-ACK or 3 way like FIN - ACK/FIN - ACK...'''
date = "2016-03-02T00:56:00Z"
lastmod = "2016-09-16T16:14:00Z"
weight = 50641
keywords = [ "disconnection" ]
aliases = [ "/questions/50641" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[FIN, ACK\] sending without getting prior \[FIN\] from counter part](/questions/50641/fin-ack-sending-without-getting-prior-fin-from-counter-part)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50641-score" class="post-score" title="current number of votes">0</div><span id="post-50641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently I got a strange phenomenon that is server sends FIN/ACK at the same time without getting prior FIN from client(There was no FIN from client in my Wireshark dump at least.)</p><p>As far as I know, normal TCP disconnection is 4 way hand shaking like FIN-ACK-FIN-ACK or 3 way like FIN - ACK/FIN - ACK, so if some one sends FIN/ACK there should be prior FIN to notify 'no more sending data &amp; connection will be closed' from the counter part.</p><p>I'm not sure this is just missing packet because I used port mirroring to grab the packets, or it is possible to happen normally.</p><p>Any idea for this? No body experienced this before?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disconnection" rel="tag" title="see questions tagged &#39;disconnection&#39;">disconnection</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '16, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/1cd8cecb2a1eefb001a7a4c31a0adddd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quatrefoil&#39;s gravatar image" /><p><span>Quatrefoil</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quatrefoil has no accepted answers">0%</span></p></div></div><div id="comments-container-50641" class="comments-container"></div><div id="comment-tools-50641" class="comment-tools"></div><div class="clear"></div><div id="comment-50641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50659"></span>

<div id="answer-container-50659" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50659-score" class="post-score" title="current number of votes">2</div><span id="post-50659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no requirement for the client to send the first FIN. Either side (client or server) can send it whenever they want to signal "that's it, I have nothing more to say". It also doesn't mean that the other side has to signal the same - it can continue to send data as much as it likes.</p><p>In the end you should see the connection terminate with 2 FINs and 2 ACKs belonging to the FINs. Sometimes you also see FIN - ACK - RST, where one side closes the connection with a rather harsh reset flag. If you have only one FIN flag (and no RST) your connection is technically still open.</p><p>Be aware that FIN flags are often piggy-packed on data packets, which makes them easy to overlook. You should isolate your TCP connection first, and then search for FIN flagged packets within the connection to check if there are two FINs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '16, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-50659" class="comments-container"><span id="50690"></span><div id="comment-50690" class="comment"><div id="post-50690-score" class="comment-score"></div><div class="comment-text"><p>Thank you for answer my question Jasper, I wasn't saying that there are any rule or order to initiate FIN first, yes, either side can send FIN whenever they want to terminate the connection. As you mentioned I should see two FINs or FIN-RST at the end of the packets if the connection terminated firmly, but I couldn't so I guess there's something wrong in implementation.</p><p>For your information, regarding piggy-packed FIN flags, I think it's enough to isolate with applying a filter such as "tcp.flags.fin==1", however I couldn't see any other FIN or RST besides one from Server. In this case, does it mean the server tried to terminate connection by sending FIN but the client didn't send corresponding FIN or RST yet?</p><p>I'm little bit confused about representation of '[FIN, ACK]' in Wireshark info column, because I thought it was an answer for prior FIN from counter part. And I still have doubt that prior FIN from client was missed(not caught while grabbing the packets). Do you think this ACK just means ACK of other packet received previously, and nothing to do with prior FIN(something I doubt missed)?</p></div><div id="comment-50690-info" class="comment-info"><span class="comment-age">(02 Mar '16, 16:16)</span> <span class="comment-user userinfo">Quatrefoil</span></div></div><span id="50702"></span><div id="comment-50702" class="comment"><div id="post-50702-score" class="comment-score"></div><div class="comment-text"><p>ACK (the flag and the corresponding sequence number) is present in almost all TCP packets, with two exceptions: the client's SYN packet (as there is nothing to ACK yet), and the client's RST packet in case that the server has not responded to the client's SYN (i.e. the session has not been established yet).</p><p>Data reception acknowledging in TCP does not work packet by packet (or message by message) like in older, mostly point-to-point, protocols where you would not send the next message until you've received an ACK for the last sent one. One of the reasons is that doing so would terribly slow down the transfers as the network path round trip would elapse between any two messages sent.</p><p>Instead, while sending your own packets, you use the ACK sequence number to inform the remote party about the sequence number of the last payload octet you have received from them without a gap in the data. So if a party has not received any payload during the time it has itself sent three packets, the ACK sequence number in all these three packets is the same, but it is always there.</p><p>Presence of the FIN flag is counted, for the purpose of TCP sequence numbers, as an additional octet of payload. So when the TCP stack receives a packet with FIN flag set and with payload whose last octet's sequence number is N, it sends an ACK for N+1. Whether it sends, in the same packet, its own FIN flag or not, depends on the particular situation as Jasper has written above.</p></div><div id="comment-50702-info" class="comment-info"><span class="comment-age">(03 Mar '16, 03:16)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50659" class="comment-tools"></div><div class="clear"></div><div id="comment-50659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55612"></span>

<div id="answer-container-55612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55612-score" class="post-score" title="current number of votes">0</div><span id="post-55612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The closing of TCP connection is never 3-way handshake but rather 2-way. Any of the device can initiate closing the session by sending the FIN packet, and it gets in to the FIN-WAIT1 state. Then it expect the other device to send the FIN afterwards for that it gets into the FIN-WAIT2 state. in this case connection can be resumed by the other devices if he is not wish to terminate the connection. When both devices are agreed to terminate the connection by sending their FIN and gets the ACK for them. The connection is terminated. That is the reason you are seeing four packets (that's not four-way handshake but two-way.</p><p>For, ACK you are seeing along with FIN is the acknowledge for the last byte received. you can check the acknowledgement number as well to ensure that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '16, 16:14</strong></p><img src="https://secure.gravatar.com/avatar/8e01eee9e1cf6b9aa45e74f49a1efe19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sukhjit&#39;s gravatar image" /><p><span>sukhjit</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sukhjit has no accepted answers">0%</span></p></div></div><div id="comments-container-55612" class="comments-container"></div><div id="comment-tools-55612" class="comment-tools"></div><div class="clear"></div><div id="comment-55612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

