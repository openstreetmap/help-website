+++
type = "question"
title = "Why am I getting duplicate tcp acks?"
description = '''I have an application I&#x27;ve written on Windows 7 that is connecting TCP to a custom device. The device is sending status packets approx. every 25ms to the host. The device is also running code I&#x27;ve written. They are connected ethernet via a DSL router. The application is also sending data over a seco...'''
date = "2012-06-08T11:15:00Z"
lastmod = "2012-06-08T19:13:00Z"
weight = 11773
keywords = [ "tcp" ]
aliases = [ "/questions/11773" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I getting duplicate tcp acks?](/questions/11773/why-am-i-getting-duplicate-tcp-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11773-score" class="post-score" title="current number of votes">0</div><span id="post-11773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an application I've written on Windows 7 that is connecting TCP to a custom device. The device is sending status packets approx. every 25ms to the host. The device is also running code I've written. They are connected ethernet via a DSL router. The application is also sending data over a second TCP port to the device.</p><p>All works well until I get a duplicate ACK from the host. The orignal packet from device to host shows up in Wireshark. After the 3rd DUP ACK, the device sends a fast retransmit of the packet. The host keeps sending DUP ACKs for a total of 7. The device keeps sending it's status updates every 25ms. After about 1 sec. the device re-transmits these status packets. Meanwhile, a thread on the host has a recv() active with a 5sec. timeout. This recv eventually times out and then disconnects. During this time, the host is continuing to send data on the other port. So, the sequence shown in Wireshark seems OK, but the application times out waiting for data.</p><p>Thus, various questions that I hope someone can help me understand:</p><ul><li>all the packets show up in the Wireshark trace, so what might cause Windows to issue the DUP ACK (Wireshark is running on the same machine)?</li><li>what might be causing the host to not receive the data (either the original or re-trans)?</li><li>if, for some reason, the receive thread on the host is locked up, would this cause these symptoms (i.e. if the receive buffers are all full, will this cause DUP ACKs? The window size from the host never drops...).</li></ul><p>Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '12, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/a05fcf8fe8edf1173b8f240f93302b67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArFrog&#39;s gravatar image" /><p><span>ArFrog</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArFrog has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jun '12, 14:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-11773" class="comments-container"><span id="11774"></span><div id="comment-11774" class="comment"><div id="post-11774-score" class="comment-score"></div><div class="comment-text"><p>Can you upload the tracefile to <a href="http://www.cloudshark.org">www.cloudshark.org</a> and post the link to the file here? That makes discussion on what might be happening in your case a lot easier...</p></div><div id="comment-11774-info" class="comment-info"><span class="comment-age">(08 Jun '12, 14:23)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="11777"></span><div id="comment-11777" class="comment"><div id="post-11777-score" class="comment-score"></div><div class="comment-text"><p>I uploaded the capture file to <a href="http://www.cloudshark.org/captures/96ee8678c779">http://www.cloudshark.org/captures/96ee8678c779</a> 192.168.0.37 is the device, 192.168.0.3 is the host PC. Port 27015 is the command/status port, 27016 is a data port. At sequence 675 is the last received status packet, 881 - dup ack #1, 900 - fast retrans, 1793 full retrans and at 5673 is the RST due to the host application detecting the recv timeout.</p></div><div id="comment-11777-info" class="comment-info"><span class="comment-age">(08 Jun '12, 15:59)</span> <span class="comment-user userinfo">ArFrog</span></div></div></div><div id="comment-tools-11773" class="comment-tools"></div><div class="clear"></div><div id="comment-11773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11781"></span>

<div id="answer-container-11781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11781-score" class="post-score" title="current number of votes">0</div><span id="post-11781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The packets are received by the host (as can be seen in Wireshark), but they never reach the application as the TCP checksums are incorrect. Something on the device is messing up the checksums.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '12, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11781" class="comments-container"><span id="11782"></span><div id="comment-11782" class="comment"><div id="post-11782-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response. I had checksum verification off since all the host packets were flagged in error, so didn't see that these few packets from the device were in error. Now I can track the culprit down... Thanks again.</p></div><div id="comment-11782-info" class="comment-info"><span class="comment-age">(08 Jun '12, 19:13)</span> <span class="comment-user userinfo">ArFrog</span></div></div></div><div id="comment-tools-11781" class="comment-tools"></div><div class="clear"></div><div id="comment-11781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

