+++
type = "question"
title = "Interesting TCP segment-ACK pattern"
description = '''I&#x27;ve a Windows 7 laptop on which I&#x27;m viewing a YouTube video using Mozilla Firefox web browser.  There is nothing else being viewed on the internet except YouTube. No other browser/browser tab is open. The laptop is connected to the internet over an Ethernet connection.  Here is what I see: after a ...'''
date = "2017-07-07T10:53:00Z"
lastmod = "2017-07-07T15:56:00Z"
weight = 62607
keywords = [ "ack", "tcp-mss-options", "tcp_delayed_ack", "tcp", "tcp-bytes-in-flight" ]
aliases = [ "/questions/62607" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Interesting TCP segment-ACK pattern](/questions/62607/interesting-tcp-segment-ack-pattern)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62607-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've a Windows 7 laptop on which I'm viewing a YouTube video using Mozilla Firefox web browser. There is nothing else being viewed on the internet except YouTube. No other browser/browser tab is open. The laptop is connected to the internet over an Ethernet connection.</p><p>Here is what I see: after a few initial packets, I notice that there is a pattern in TCP's segment - ACK transmission. Around 10 TCP segments are being ACKed via a single TCP ACK. This pattern keeps on repeating. All the TCP segments have the same source IP address so I'm assuming that they come from the same server.</p><p>My initial guess was that this could be due to TCP delayed ACK mechanism. However, that does not seem to be the case. According to RFC 1122, with a stream of full-sized incoming segments, ACK responses must be sent for every second segment. Additionally, I checked the packets that constitute the initial SYN-ACK handshake. The MSS that is agreed upon is 1460 Bytes. So this means that there should have been 5 ACKs instead of just one.</p><p>I know that Windows 7 uses Compound TCP. But I'm not sure that this is something to do with a TCP version since all version must be RFC compliant, correct?</p><p>I also performed another experiment and took a couple of traces for the following sources: YouTube, Amazon Prime Video, Pandora. I see a similar trend. In fact, I always see a set of 10 segments being ACKed by a single TCP ACK.</p><p>What is it that I'm missing here?</p><p>I'm attaching a snapshot of what I saw. I've also added a bytes in flight column as well. <img src="https://osqa-ask.wireshark.org/upfiles/TCP_weird_pattern.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ack tcp-mss-options tcp_delayed_ack tcp tcp-bytes-in-flight</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '17, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/f28c5a6b8a72fbfc0ca5c5a333572f5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alphasneaky&#39;s gravatar image" /><p>alphasneaky<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alphasneaky has no accepted answers">0%</span></p></img></div></div><div id="comments-container-62607" class="comments-container"></div><div id="comment-tools-62607" class="comment-tools"></div><div class="clear"></div><div id="comment-62607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62610"></span>

<div id="answer-container-62610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62610-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>That screenshot is quite useless unfortunately, so it would be better to share a PCAP instead - the reason is that your question is SEQ/ACK number related, but we don't see those numbers except for a few packets. Bytes in flight is not always relevant as this issue is also depending on the point of capture, RTT and distance.</p><p>It is also quite possible (and not at all illegal) to ACK more than two packets - I've seen many stacks do that. RFCs are guidelines and not always respected, and in this case the rule you're quoting from RFC 1122 is a "SHOULD" rule, not a "MUST" (section 4.2.3.2, second paragraph). Also note that RFC 1122 was published in 1989 (which is an eternity ago in network technology) and has been updated in RFCs 1349, 4379, 5884, 6093, 6298, 6633, 6864, and 8029. I didn't check but it is very likely that most of the things in 1122 are long updated with newer findings and guidelines.</p><p>So: no, unfortunately you are mistaken. "All version" do not need to be RFC compliant, and often cannot be, because there are different approaches that may even contradict each other. In the end, it comes down to "whatever works efficiently" - and if there is no packet loss, ACKing 10 packets instead of 2-2-2-2-2 is pretty efficient, and many modern stacks adjust their ACK ration according to the transmission success. I bet you'll see that 2-packet-ACK pattern again when packets are lost, because a faster ACK rhythm helps detecting packet loss faster.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '17, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '17, 02:54</p></div></div><div id="comments-container-62610" class="comments-container"><span id="62613"></span><div id="comment-62613" class="comment"><div id="post-62613-score" class="comment-score">1</div><div class="comment-text"><p>Thanks for your reply. I really appreciate it. I do have a couple of follow up questions to make sure my understanding is accurate:</p><ol><li><p>Doesn't the calculations for bytes in flight in Wireshark take into account the sequence numbers already? I was assuming that the bytes in flight at time t1 is calculated by summing up length of unACKed TCP segments upto t1. If this is true, then in the snapshot above, the bytes in flight grows from 1460 -&gt; 14600 (~10 segments) before it goes down to 0 after the ACK transmission and starts again from 1460 bytes after the next TCP segment. From this, one can conclude that all those 10 segments were ACKed by this particular ACK. Is this correct?</p></li><li><p>I did go through RFCs 1349, 4379, 5884, 6093, 6298, 6633, 6864 and 8029 prior to posting since they were referenced in RFC 1122. I could not find an explicit update on the particular TCP delayed ACK feature ('ACK every other packet') in any of the following RFCs. If anyone knows of any other updates which might have changed this behavior or anything I might have missed, please do post here. But I'm guessing that if there were other RFC updates that affected this, the RFC would have cited them already.</p></li><li><p>You've made a great point about the difference between SHOULD and MUST. If I had to check how different TCP implementations vary their ACK ratios based on transmission success, could you please point me to any good resource that might help me out?</p></li><li><p>If particular details of TCP implementations are not relevant to this forum, can anyone point me to any other forums that might be helpful. Thanks a lot in advance!</p></li></ol><p>Again, thanks a lot for your response. It was very informative and useful.</p></div><div id="comment-62613-info" class="comment-info"><span class="comment-age">(07 Jul '17, 18:35)</span> alphasneaky</div></div><span id="62615"></span><div id="comment-62615" class="comment"><div id="post-62615-score" class="comment-score">1</div><div class="comment-text"><ol><li><p>yes, correct (it was a little late yesterday when I answered) - I was trying to say that the packet timing depending on the capture location sometimes leads to fast growing bytes-in-flight values on the sender side when ACKs arrive only after some time due to higher RTT, so that value can be misleading.</p></li><li><p>It's still true for most stacks to ACK every other packet, but I wanted to point out that RFCs aren't as strictly followed as assumed by many. And *nix stacks have been known to ACK longer chains of packets for quite some time - Windows was (so far) the one OS that usually ACked every other packet. Delayed ACK hasn't changed either as far as I know. The most interesting stack right now could be BBR: <a href="https://queue.acm.org/detail.cfm?id=3022184">https://queue.acm.org/detail.cfm?id=3022184</a></p></li><li><p>Unfortunately, comparing stack implementations is not an easy task (many have tried :-)), as detailed information about their differences in behavior is surprisingly hard to find. What you'll usually find is that the information available focuses on the different handling of packet loss and congestion control, and rarely (if at all) about ACK frequency. If you want to have a list you can start from, try <a href="https://en.wikipedia.org/wiki/TCP_congestion_control">https://en.wikipedia.org/wiki/TCP_congestion_control</a></p></li></ol></div><div id="comment-62615-info" class="comment-info"><span class="comment-age">(08 Jul '17, 03:16)</span> Jasper ♦♦</div></div><span id="62619"></span><div id="comment-62619" class="comment"><div id="post-62619-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much.</p></div><div id="comment-62619-info" class="comment-info"><span class="comment-age">(08 Jul '17, 14:06)</span> alphasneaky</div></div></div><div id="comment-tools-62610" class="comment-tools"></div><div class="clear"></div><div id="comment-62610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

