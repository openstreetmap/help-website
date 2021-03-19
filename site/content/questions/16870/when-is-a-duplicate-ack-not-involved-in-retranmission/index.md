+++
type = "question"
title = "When is a duplicate ACK not involved in retranmission"
description = '''I have a capture file made on a unix server which has duplicate ACK&#x27;s in there which are very close in time (0.000012) to the original packet it is a duplicate for. Nor do the DUP acks in this trace ever trigger a retransmission. http://www.cs.unc.edu/~jeffay/dirt/FAQ/dupacks.html So I stumbled on t...'''
date = "2012-12-14T05:24:00Z"
lastmod = "2012-12-14T07:00:00Z"
weight = 16870
keywords = [ "ack", "duplicate" ]
aliases = [ "/questions/16870" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [When is a duplicate ACK not involved in retranmission](/questions/16870/when-is-a-duplicate-ack-not-involved-in-retranmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16870-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture file made on a unix server which has duplicate ACK's in there which are very close in time (0.000012) to the original packet it is a duplicate for. Nor do the DUP acks in this trace ever trigger a retransmission.</p><p><a href="http://www.cs.unc.edu/~jeffay/dirt/FAQ/dupacks.html">http://www.cs.unc.edu/~jeffay/dirt/FAQ/dupacks.html</a></p><p>So I stumbled on the above link, stating that "the book" actually has an explanation. Solitary Duplicate ACK with different window sizes can be part of the window update mechanism.</p><p>If the above is does the DUP ACK packet need to have a different window size value?</p></div><div id="question-tags" class="tags-container tags">ack duplicate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '12, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/d3359099b485008c4511253e1111b5bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dtor&#39;s gravatar image" /><p>dtor<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dtor has no accepted answers">0%</span></p></div></div><div id="comments-container-16870" class="comments-container"></div><div id="comment-tools-16870" class="comment-tools"></div><div class="clear"></div><div id="comment-16870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16871"></span>

<div id="answer-container-16871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16871-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you're experiencing is most likely a duplicate frame created by the way you captured the data. 12 microseconds is way too fast for a normal duplicate ACK to appear on the wire. You can easily check if it is a duplicate frame by comparing it byte by byte - if it is a normal duplicate ACK at least the IP Identification byte is different (unless you're looking at some high security trace setting it to 0 all the time).</p><p>Try running editcap -d against the trace to remove duplicates. editcap is installed with Wireshark and is a command line tool that you'll find in the program folder of Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Dec '12, 05:36</p></div></div><div id="comments-container-16871" class="comments-container"><span id="16872"></span><div id="comment-16872" class="comment"><div id="post-16872-score" class="comment-score"></div><div class="comment-text"><p>I have checked the IP ID, but they do differ.</p><p>I have uploaded a capture of a tcp session which has this behaviour</p><p><a href="http://cloudshark.org/captures/580b1f12dc02">http://cloudshark.org/captures/580b1f12dc02</a></p></div><div id="comment-16872-info" class="comment-info"><span class="comment-age">(14 Dec '12, 06:10)</span> dtor</div></div><span id="16873"></span><div id="comment-16873" class="comment"><div id="post-16873-score" class="comment-score"></div><div class="comment-text"><p>interesting... you're right, they're not duplicate frames. Where and how did you capture this trace? My guess is that it was captured locally on the server, which can lead to funny results. Can you capture again, with a 3rd PC that picks up what client and server are doing? That way we could see what really happens on the "wire".</p></div><div id="comment-16873-info" class="comment-info"><span class="comment-age">(14 Dec '12, 06:25)</span> Jasper ♦♦</div></div><span id="16874"></span><div id="comment-16874" class="comment"><div id="post-16874-score" class="comment-score"></div><div class="comment-text"><p>thank you for your comments.</p><p>The capture was made on the server (112). Your second request is harder, there are more networkdevices involved to which do not have access.</p><p>I will try and find a good spot so to do a capture. but that can take a while.</p></div><div id="comment-16874-info" class="comment-info"><span class="comment-age">(14 Dec '12, 06:31)</span> dtor</div></div><span id="16876"></span><div id="comment-16876" class="comment"><div id="post-16876-score" class="comment-score"></div><div class="comment-text"><p>Well, if you only wonder about the duplicate ACKs you can probably ignore them - they do not cost any time, and there is no packet loss either, so no harm done. My guess is they disappear as soon as the capture setup is done right without capturing locally.</p></div><div id="comment-16876-info" class="comment-info"><span class="comment-age">(14 Dec '12, 06:37)</span> Jasper ♦♦</div></div></div><div id="comment-tools-16871" class="comment-tools"></div><div class="clear"></div><div id="comment-16871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16881"></span>

<div id="answer-container-16881" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16881-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is something broken on your system or the capture setup is faulty. The <strong>SRC MAC</strong> of <strong>all packets</strong> is <strong>identical</strong>!</p><p>Unless you have found the reason for that problem, I would not care too much about the DUP-ACK as the same problem could also cause those DUP-ACKs ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Dec '12, 07:09</p></div></div><div id="comments-container-16881" class="comments-container"><span id="16888"></span><div id="comment-16888" class="comment"><div id="post-16888-score" class="comment-score"></div><div class="comment-text"><p>hello Kurt,</p><p>Well that may be my own fault, I had to scrub the data.</p></div><div id="comment-16888-info" class="comment-info"><span class="comment-age">(14 Dec '12, 07:45)</span> dtor</div></div><span id="16891"></span><div id="comment-16891" class="comment"><div id="post-16891-score" class="comment-score"></div><div class="comment-text"><p>hm.. can you please post a more concise capture file? Otherwise it's hard to analyze it.</p><p>BTW: Your "data scrubbing" did not change the time stamps, did it?</p></div><div id="comment-16891-info" class="comment-info"><span class="comment-age">(14 Dec '12, 07:50)</span> Kurt Knochner ♦</div></div><span id="16894"></span><div id="comment-16894" class="comment"><div id="post-16894-score" class="comment-score"></div><div class="comment-text"><p>not the timestamps I checked with the original it only appended 000. Just ip and mac.</p><p><a href="http://cloudshark.org/captures/d142b7fd7517">http://cloudshark.org/captures/d142b7fd7517</a></p></div><div id="comment-16894-info" class="comment-info"><span class="comment-age">(14 Dec '12, 08:05)</span> dtor</div></div><span id="16901"></span><div id="comment-16901" class="comment"><div id="post-16901-score" class="comment-score"></div><div class="comment-text"><p>O.K. as already mentioned, the DUP-ACKs are to fast to be real. So, I guess there is a bug in your OS that causes those packets to be sent twice immediately one after each other (same content, different IP ID). The system that sends the DUP-ACKs seems to be Windows. Is that correct? If so, what is your OS version (looks like Win XP).</p><p>To eliminate any interaction with the capturing software on your Unix box, I suggest to also capture on the Windows box and to check if you see the DUP-ACKs there as well.</p></div><div id="comment-16901-info" class="comment-info"><span class="comment-age">(14 Dec '12, 10:17)</span> Kurt Knochner ♦</div></div><span id="16925"></span><div id="comment-16925" class="comment"><div id="post-16925-score" class="comment-score"></div><div class="comment-text"><p>I believe our client is using windows. I will do a network capture on the client side and see what comes up.</p><p>Thank you for the input</p></div><div id="comment-16925-info" class="comment-info"><span class="comment-age">(15 Dec '12, 05:03)</span> dtor</div></div><span id="17015"></span><div id="comment-17015" class="comment not_top_scorer"><div id="post-17015-score" class="comment-score"></div><div class="comment-text"><p>We mirrored the clients port and saw the dup acks heading towards the server. We'll be looking at the clients software/drivers/firmware..</p><p>Thank you for your time and input.</p></div><div id="comment-17015-info" class="comment-info"><span class="comment-age">(18 Dec '12, 01:32)</span> dtor</div></div><span id="17016"></span><div id="comment-17016" class="comment not_top_scorer"><div id="post-17016-score" class="comment-score"></div><div class="comment-text"><p>O.K. good luck. I suggest to look at OS patches and the NIC driver if TCP offloading (or any other offloading) is enabled on that NIC. You can also try to disable TCP/IP offloading (driver feature).</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-17016-info" class="comment-info"><span class="comment-age">(18 Dec '12, 01:36)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16881" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-16881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

