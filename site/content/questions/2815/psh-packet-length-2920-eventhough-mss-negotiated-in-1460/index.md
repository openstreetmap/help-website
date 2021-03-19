+++
type = "question"
title = "PSH packet Length 2920 eventhough MSS negotiated in 1460"
description = '''Hi Team, I am seeing a TCP connection where the the MSS is negotiated as 1460 but there are few PSH packets which have the length 2920. I have also confirmed that the MTU of the windows box which is sending the data is 1500. So there is no way that the windows box can send a packet of such length. F...'''
date = "2011-03-14T21:43:00Z"
lastmod = "2011-03-15T01:03:00Z"
weight = 2815
keywords = [ "pshlength" ]
aliases = [ "/questions/2815" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [PSH packet Length 2920 eventhough MSS negotiated in 1460](/questions/2815/psh-packet-length-2920-eventhough-mss-negotiated-in-1460)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2815-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team,</p><p>I am seeing a TCP connection where the the MSS is negotiated as 1460 but there are few PSH packets which have the length 2920. I have also confirmed that the MTU of the windows box which is sending the data is 1500. So there is no way that the windows box can send a packet of such length.</p><p>Following ping test ensures that the windows box has max MTU of 1500.</p><pre><code>C:\Documents and Settings\Administrator&gt;ping 172.16.199.105 -f -l 1472
Pinging 172.16.199.105 with 1472 bytes of data:
Reply from 172.16.199.105: bytes=1472 time&lt;1ms TTL=64
Ping statistics for 172.16.199.105:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
Control-C
^C

C:\Documents and Settings\Administrator&gt;ping 172.16.199.105 -f -l 1473
Pinging 172.16.199.105 with 1473 bytes of data:
Packet needs to be fragmented but DF set.
Packet needs to be fragmented but DF set.
Ping statistics for 172.16.199.105:
    Packets: Sent = 2, Received = 0, Lost = 2 (100% loss),
Control-C
^C
C:\Documents and Settings\Administrator&gt;</code></pre><p>I also disabled the following in the wireshark, so that wireshark is not combining two packets in to one.</p><pre><code>Reassamble fragmented IP datagrams

Allow subdissector to reassemble TCP streams</code></pre><p>The capture was taken from the same windows PC which is supposedly sending the packet of Length 2920. Has anyone encountered such issue. Is this a problem with the windows box or the wireshark tool.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">pshlength</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '11, 21:43</strong></p><img src="https://secure.gravatar.com/avatar/8fce8613a234a32d052a59b0b788b8aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prab&#39;s gravatar image" /><p>Prab<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prab has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Mar '11, 00:59</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-2815" class="comments-container"></div><div id="comment-tools-2815" class="comment-tools"></div><div class="clear"></div><div id="comment-2815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2818"></span>

<div id="answer-container-2818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2818-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, what you see is a typical result of capturing on the sending PC equipped with a network card that has the "large send offload" option. What happens is that Wireshark captures the outgoing data before it is actually completely processed for transmission in the network card, meaning that you see large chunks of data in your trace that get chopped down to the real network packets in the network card only after you've already recorded it.</p><p>You can verify this by capturing on the receiver at the same time - you'll see that all packets that actually arrive have the correct size. Or you can go into the advanced settings of your network card and turn of the large offsend feature to see the difference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2818" class="comments-container"></div><div id="comment-tools-2818" class="comment-tools"></div><div class="clear"></div><div id="comment-2818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2819"></span>

<div id="answer-container-2819" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2819-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>This can happen on systems that support TCP segmentation offloading on the NIC. Wireshark captures packets between the NIC-driver and the NIC. Since the TCP segmenting is now done on the NIC, wireshark sees a large frame going out, but the NIC splits it up into multiple packets on the wire.</p><p>(see: <a href="http://wiki.wireshark.org/CaptureSetup/Offloading#Segmentation_Offload">http://wiki.wireshark.org/CaptureSetup/Offloading#Segmentation_Offload</a>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2819" class="comments-container"><span id="2821"></span><div id="comment-2821" class="comment"><div id="post-2821-score" class="comment-score"></div><div class="comment-text"><p>Hi SYNbit, Jasper,</p><p>Thanks for the comments. Now i understand this.</p></div><div id="comment-2821-info" class="comment-info"><span class="comment-age">(15 Mar '11, 02:50)</span> Prab</div></div><span id="2837"></span><div id="comment-2837" class="comment"><div id="post-2837-score" class="comment-score"></div><div class="comment-text"><p>You're welcome :-)</p><p>Could you accept either Jaspers or my answer by clicking on the "checkmark" on the left of the answer? That way the question will be removed from the list of "unanswered questions". Thx!</p></div><div id="comment-2837-info" class="comment-info"><span class="comment-age">(15 Mar '11, 10:40)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-2819" class="comment-tools"></div><div class="clear"></div><div id="comment-2819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

