+++
type = "question"
title = "How do I make sure if TCP Retransmissions are actually not fake?"
description = '''Hi, So we´ve been having this performance issue, and on the capture I can see that maybe 50% of the DC to Core traffic are Out ot Order and TCP Retransmissions. Cisco Nexus device also shows many of these in the Socket Statistics. I do have the same TCP flow going over the same psyical link towards ...'''
date = "2015-03-21T00:54:00Z"
lastmod = "2015-06-01T07:39:00Z"
weight = 40756
keywords = [ "of", "retransmissions", "cisco", "out-of-order", "out" ]
aliases = [ "/questions/40756" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I make sure if TCP Retransmissions are actually not fake?](/questions/40756/how-do-i-make-sure-if-tcp-retransmissions-are-actually-not-fake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40756-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>So we´ve been having this performance issue, and on the capture I can see that maybe 50% of the DC to Core traffic are Out ot Order and TCP Retransmissions. Cisco Nexus device also shows many of these in the Socket Statistics.</p><p>I do have the same TCP flow going over the same psyical link towards the Checkpoint FW and back to the Core, and then over to the server... but how can I actually be sure if the TCP Retransmissions are not just the members of the same IP flow but detected twice? How does Wireshark detect the Out of order and Retransmission, there is no flag for that, so... some inside intelligence? How do I filter it and compare the packets?</p></div><div id="question-tags" class="tags-container tags">of retransmissions cisco out-of-order out</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '15, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/ec6ef44ba6a84944d98235acf55c4296?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SNArchsCOM&#39;s gravatar image" /><p>SNArchsCOM<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SNArchsCOM has no accepted answers">0%</span></p></div></div><div id="comments-container-40756" class="comments-container"><span id="40760"></span><div id="comment-40760" class="comment"><div id="post-40760-score" class="comment-score"></div><div class="comment-text"><p>I would check the IP ID field. That will tell you if you are looking at the same packet more than once or if they are indeed re-transmissions.</p></div><div id="comment-40760-info" class="comment-info"><span class="comment-age">(21 Mar '15, 12:34)</span> Steve Occhio...</div></div></div><div id="comment-tools-40756" class="comment-tools"></div><div class="clear"></div><div id="comment-40756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40758"></span>

<div id="answer-container-40758" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40758-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>With that many Out-of-orders and retransmissions I am pretty sure that you suffer from massive amounts of duplicated packets. This happens if you use a SPAN session with more than one source port or (what my current guess is) when SPANning one or more whole VLANs. What you get is the same packets twice or more when it enters and leaves the switch, which drives the TCP expert crazy.</p><p>Try deduplicating your capture with editcap. Editcap is a command line tool installed with Wireshark. I recommend running it like this:</p><pre><code>editcap -d -D 50 infile.pcapng outfile.pcapng</code></pre><p>This will check in a range of 50 packets if there are exact duplicates and remove them. After running this, check the new file with Wireshark again.</p><p>Otherwise you should read my answer in the other question you commented on: <a href="https://ask.wireshark.org/questions/22134/how-does-wireshark-recognize-tcp-retransmission-packets">https://ask.wireshark.org/questions/22134/how-does-wireshark-recognize-tcp-retransmission-packets</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '15, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Mar '15, 07:13</p></div></div><div id="comments-container-40758" class="comments-container"><span id="40769"></span><div id="comment-40769" class="comment"><div id="post-40769-score" class="comment-score"></div><div class="comment-text"><p>Yes, thanks for your answers, but I actually filtered the capture first, and then analyzed it... and my profe that these packets are not Wiresharks/SPAN fault is that: - I´m doing a SPAN of a single port - On Cisco N5k I can also see the OOO and TCP retransmissions within the TCP statistics - My Checkpoint R76 is also logging many of these OOO and Retransmissions</p></div><div id="comment-40769-info" class="comment-info"><span class="comment-age">(22 Mar '15, 10:56)</span> SNArchsCOM</div></div><span id="40783"></span><div id="comment-40783" class="comment"><div id="post-40783-score" class="comment-score"></div><div class="comment-text"><p>can you upload a capture file somewhere (google drive, dropbox, cloudshark) and post the link here? If you need/want you can anonymize the file with TraceWrangler @ http://tracewrangler.com .</p></div><div id="comment-40783-info" class="comment-info"><span class="comment-age">(23 Mar '15, 09:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-40758" class="comment-tools"></div><div class="clear"></div><div id="comment-40758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42799"></span>

<div id="answer-container-42799" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42799-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So here is an update about what happened: I used editcap to split the file, and it turns out that since the traffic flow is using the same physical link to go to the FW in 2 directions (from Client to Nexus to FW and back from FW via Nexus to the Server), it was detecting different flows as retransmissions. The IPs of Source and Destination did match, but the MAC addresses were different, which is why I´m really surprised that WireShark sees this as a re-transmission. Noone had similar experience?</p><p>PS (@Kurt): I can't just upload a capture to a dropbox, I´m not playing with a Lab here, our client is a financial institution and I´m pretty sure they wouldn't like their data capture to be just... published.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/ec6ef44ba6a84944d98235acf55c4296?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SNArchsCOM&#39;s gravatar image" /><p>SNArchsCOM<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SNArchsCOM has no accepted answers">0%</span></p></div></div><div id="comments-container-42799" class="comments-container"><span id="42800"></span><div id="comment-42800" class="comment"><div id="post-42800-score" class="comment-score">1</div><div class="comment-text"><p>See this blog post for an explanation why Wireshark doesn't care about MAC differences: <a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p><p>BTW, if you need to share captures where it all comes down to Ethernet/IP/TCP behavior, just use TraceWrangler with a anonymisation task and cut away everything after layer 4. Then randomize the IP addresses and ports, and you're good to go (you should still do a visual check after sanitization to see if it worked fine).</p></div><div id="comment-42800-info" class="comment-info"><span class="comment-age">(01 Jun '15, 07:44)</span> Jasper ♦♦</div></div><span id="42801"></span><div id="comment-42801" class="comment"><div id="post-42801-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, that´s helpful!!!</p><p>I still don´t get how Cisco Nexus Switches give me the same error in the statistics, I opened the case ... but never got the answer.</p></div><div id="comment-42801-info" class="comment-info"><span class="comment-age">(01 Jun '15, 08:16)</span> SNArchsCOM</div></div></div><div id="comment-tools-42799" class="comment-tools"></div><div class="clear"></div><div id="comment-42799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

