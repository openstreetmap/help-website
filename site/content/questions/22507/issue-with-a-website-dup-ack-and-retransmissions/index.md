+++
type = "question"
title = "Issue with a website - dup ack and retransmissions"
description = '''I’m currently having a problem with one particular website. The load times just to view the main page can take upwards to 20 seconds. To see what was taking so long I did a packet capture and found many retransmissions and dup ack (seems to make up the majority of the capture). The thing is it only ...'''
date = "2013-07-01T06:43:00Z"
lastmod = "2013-07-03T01:51:00Z"
weight = 22507
keywords = [ "dup-ack", "website", "retransmissions" ]
aliases = [ "/questions/22507" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Issue with a website - dup ack and retransmissions](/questions/22507/issue-with-a-website-dup-ack-and-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22507-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I’m currently having a problem with one particular website. The load times just to view the main page can take upwards to 20 seconds. To see what was taking so long I did a packet capture and found many retransmissions and dup ack (seems to make up the majority of the capture). The thing is it only seems to be happening to our office and the website administrator reports no problems from any other customers, this seems like a true statement. Doing the same packet capture from home I receive no errors and the website loads on an average of 2 – 3 seconds. I’ve also used websites that test load times from different geographical locations and given similar results. I’ve also done a tracert from home and office and the only difference in hops are the first couple, after the first couple hops it’s the exact same. The difference in the first hops is I have residential service where the office has business class service. We have BGP setup with two different service providers. Forcing the connection over either ISP doesn’t produce any different results.</p><p>This capture is from a client PC going to the website.</p><p><a href="http://cloudshark.org/captures/e7a9522b9b91">http://cloudshark.org/captures/e7a9522b9b91</a></p><p>I'm thinking it's how the packets are being routed from the website to our office but this is me just guessing. Is there anything in the packet capture that I’m missing? Or something I can do to narrow the problem down a little more?</p></div><div id="question-tags" class="tags-container tags">dup-ack website retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '13, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/32534ee2e569f95a13b4a4f8b039863e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aziz&#39;s gravatar image" /><p>Aziz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aziz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jul '13, 07:00</p></div></div><div id="comments-container-22507" class="comments-container"><span id="22508"></span><div id="comment-22508" class="comment"><div id="post-22508-score" class="comment-score"></div><div class="comment-text"><p>@Aziz: Your cloudshark trace contains seemingly unanonymized information like public IP addresses and the Certificates indicating the name of your company/target company. I removed the link to the cloudshark trace.</p><p>If you are sure this information is ok to be spread, feel free to edit your post and re-insert the link.</p></div><div id="comment-22508-info" class="comment-info"><span class="comment-age">(01 Jul '13, 06:49)</span> Landi</div></div><span id="22511"></span><div id="comment-22511" class="comment"><div id="post-22511-score" class="comment-score"></div><div class="comment-text"><p>Thank you for double checking. I did change the mac and IP addresses and I'm OK with people knowing the website.</p></div><div id="comment-22511-info" class="comment-info"><span class="comment-age">(01 Jul '13, 07:02)</span> Aziz</div></div><span id="22512"></span><div id="comment-22512" class="comment"><div id="post-22512-score" class="comment-score"></div><div class="comment-text"><p>@Landi FYI, removing a link from a page here does not really delete it, it can always be seen in the revisions of the page.</p></div><div id="comment-22512-info" class="comment-info"><span class="comment-age">(01 Jul '13, 07:04)</span> SYN-bit ♦♦</div></div><span id="22513"></span><div id="comment-22513" class="comment"><div id="post-22513-score" class="comment-score"></div><div class="comment-text"><p>@SYN-bit: THX and good 2 know - so how to handle next time ? ;)</p></div><div id="comment-22513-info" class="comment-info"><span class="comment-age">(01 Jul '13, 07:11)</span> Landi</div></div><span id="22525"></span><div id="comment-22525" class="comment"><div id="post-22525-score" class="comment-score"></div><div class="comment-text"><p>@Landi: I don't see a way of editing (or deleting) a question permanently without the original content being available though revisions (or old link).</p></div><div id="comment-22525-info" class="comment-info"><span class="comment-age">(01 Jul '13, 14:21)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-22507" class="comment-tools"></div><div class="clear"></div><div id="comment-22507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="22589"></span>

<div id="answer-container-22589" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22589-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are actually not that many lost packets as wireshark makes us believe. A lot of packets are arriving out of order because full MSS size packets get delayed by 14-19ms whereas small packets seem to arrive without any additional delay. <img src="https://osqa-ask.wireshark.org/upfiles/delays.jpg" alt="alt text" /> This can be observed throughout the trace. The really 'lost' packets seem to be all full-mss (tcp.len==1380) packets so I wonder whether a 'traffic-shaper' is involved here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p>mrEEde2<br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></img></div></div><div id="comments-container-22589" class="comments-container"></div><div id="comment-tools-22589" class="comment-tools"></div><div class="clear"></div><div id="comment-22589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22509"></span>

<div id="answer-container-22509" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22509-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you anonymized the trace? The MAC addresses make no sense and the IP addresses look like you've hashed them.</p><p>It sure looks like you've got tons of packet loss; right at the start you have 3 packets lost that have to be retransmitted in frames 10, 14 and 12, and the one in frame 10 looks like it is RTO based (because of a delta time of almost 3 seconds). No surprise that loading the page takes forever; you should try to find the spot where the packets are lost (if you can) by moving the capture point closer to the server until you have a location.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jul '13, 06:58</p></div></div><div id="comments-container-22509" class="comments-container"></div><div id="comment-tools-22509" class="comment-tools"></div><div class="clear"></div><div id="comment-22509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22535"></span>

<div id="answer-container-22535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22535-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Forcing the connection over either ISP doesn’t produce any different results.</p></blockquote><p>as there are a lot of 'lost packets' in the capture file <strong>and</strong> you ruled out the ISPs <strong>and</strong> you see the same problem with other sites, what remains?</p><ul><li>your internet router</li><li>your internet firewall</li><li>your switches/routers (internal)</li><li>your clients (OS, driver, etc.)</li></ul><p>I would start to look at the the internet router and/or firewall. Maybe one of those drops packets. A common problem is a mismatch in speed and duplex setting of the involved links. Please check those first. Try to capture traffic near to the client <strong>and</strong> in parallel in front of the internet router (internal/external side) and/or the internet firewall (internal/external side) and then compare the two capture files.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22535" class="comments-container"></div><div id="comment-tools-22535" class="comment-tools"></div><div class="clear"></div><div id="comment-22535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

