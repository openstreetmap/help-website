+++
type = "question"
title = "Client Doesn&#x27;t Respond to FIN ACK"
description = '''Hi guys, I&#x27;ve done some homework, but am coming up a bit short. I&#x27;ve searched but haven&#x27;t been able to identify what might cause something like this. I&#x27;ve been working on a problem where my client application never receives the last packet of an HTTP response, which leads to timeout errors. Looking ...'''
date = "2016-09-20T16:29:00Z"
lastmod = "2017-02-14T15:36:00Z"
weight = 55683
keywords = [ "fin" ]
aliases = [ "/questions/55683" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Client Doesn't Respond to FIN ACK](/questions/55683/client-doesnt-respond-to-fin-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55683-score" class="post-score" title="current number of votes">0</div><span id="post-55683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I've done some homework, but am coming up a bit short. I've searched but haven't been able to identify what might cause something like this.</p><p>I've been working on a problem where my client application never receives the last packet of an HTTP response, which leads to timeout errors.</p><p>Looking at the packet capture, I see that the server has successfully sent all of it's data, and sends a FIN ACK. The client receives all of this data, ACKs the FIN ACK, but never FIN ACKs or resets the connection. From the client side capture:</p><p><img src="http://i68.tinypic.com/2vt1kcl.png" alt="WireShark Image" /></p><p>In packet 67, the server sends a FIN ACK, but the client never responds with a FIN ACK or a reset. The server, then expecting an FIN ACK, resends it's FIN ACK, the client then ACKS again and this repeats until the server closes the connection.</p><p>I guess my question is, what are things that can cause a client to not respond to a FIN ACK?</p><p>Edit: Here is the <a href="https://www.cloudshark.org/captures/323caf0e2899">CloudShark Link for when it fails</a> Here is the <a href="https://www.cloudshark.org/captures/a8e61dc06331">CloudShark Link for when it works</a> Here is the <a href="https://www.cloudshark.org/captures/4f468f7cd9d1">CloutShark Link server side</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '16, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/d6d2f34e8595fbcee48370c5a1d5da66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jt8786&#39;s gravatar image" /><p><span>Jt8786</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jt8786 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '16, 11:24</strong> </span></p></div></div><div id="comments-container-55683" class="comments-container"><span id="55684"></span><div id="comment-55684" class="comment"><div id="post-55684-score" class="comment-score"></div><div class="comment-text"><p>What needs to be done here is tracking TCP sequence numbers, but that's impossible with a screenshot like this. Can you sanitize your pcap (e.g. with TraceWrangler, see <a href="https://www.tracewrangler.com">https://www.tracewrangler.com</a>) and upload the sanitized file somewhere, e.g. Cloudshark?</p></div><div id="comment-55684-info" class="comment-info"><span class="comment-age">(20 Sep '16, 16:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="55685"></span><div id="comment-55685" class="comment"><div id="post-55685-score" class="comment-score"></div><div class="comment-text"><p><span>@Jasper</span> Thanks for the reply. Added the CloudShark link</p></div><div id="comment-55685-info" class="comment-info"><span class="comment-age">(20 Sep '16, 16:44)</span> <span class="comment-user userinfo">Jt8786</span></div></div></div><div id="comment-tools-55683" class="comment-tools"></div><div class="clear"></div><div id="comment-55683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55686"></span>

<div id="answer-container-55686" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55686-score" class="post-score" title="current number of votes">0</div><span id="post-55686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jt8786 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Okay, to answer the question first: nothing should cause a client to not respond to a FIN ACK, unless it's the last packet in the conversation (meaning, the teardown FIN/ACK/FIN/ACK sequence is complete).</p><p>In your capture file, the ACK in 68 (and any following ACK from 10.186.131.236) doesn't seem to get through, which is why we see the packets from 10.22.193.39 marked as "TCP Spurious Retransmission": Wireshark has seen that the FIN/ACK packets were in fact acknowledged, but that packet was lost on the way to 10.22.193.39.</p><p>What you should do (if possible at all) is to check if there is any kind of ACL/Firewall blocking those outgoing ACK packets. I can't think of any valid reason right now, but something is preventing the ACKs from getting through to 10.22.193.39. Normally I would now start capturing packets along the path to see where the ACK isn't seen anymore, to pinpoint the device that blocks the ACK. But that may not be possible, depending on the network architecture and your access to it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '16, 16:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-55686" class="comments-container"><span id="55687"></span><div id="comment-55687" class="comment"><div id="post-55687-score" class="comment-score"></div><div class="comment-text"><p>Good enough for me!</p><p>Thank you so much for looking at this.</p></div><div id="comment-55687-info" class="comment-info"><span class="comment-age">(20 Sep '16, 17:00)</span> <span class="comment-user userinfo">Jt8786</span></div></div><span id="59427"></span><div id="comment-59427" class="comment"><div id="post-59427-score" class="comment-score"></div><div class="comment-text"><p>Just to close the loop on this incase anybody else ever runs across something similar. Trend Micro Officescan's Web Reputation was the cause of the problem.</p><p>Thanks again to <span>@Jasper</span> for the sanity check.</p></div><div id="comment-59427-info" class="comment-info"><span class="comment-age">(14 Feb '17, 15:36)</span> <span class="comment-user userinfo">Jt8786</span></div></div></div><div id="comment-tools-55686" class="comment-tools"></div><div class="clear"></div><div id="comment-55686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

