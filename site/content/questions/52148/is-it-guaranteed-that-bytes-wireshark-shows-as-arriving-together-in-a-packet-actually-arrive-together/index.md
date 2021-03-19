+++
type = "question"
title = "Is it guaranteed that bytes Wireshark shows as arriving together in a packet actually arrive together?"
description = '''Hi I expect the answer here to be YES! but I just need a sanity check.  I&#x27;ve been using wireshark to analyse packets coming to my server. My server uses Java NIO to process incoming bytes using a ByteBuffer.  I was seeing some irregular looking data coming in on the socket, and I thought I missing s...'''
date = "2016-05-02T06:42:00Z"
lastmod = "2016-05-02T22:53:00Z"
weight = 52148
keywords = [ "data", "tcp", "wireshark" ]
aliases = [ "/questions/52148" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is it guaranteed that bytes Wireshark shows as arriving together in a packet actually arrive together?](/questions/52148/is-it-guaranteed-that-bytes-wireshark-shows-as-arriving-together-in-a-packet-actually-arrive-together)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52148-score" class="post-score" title="current number of votes">0</div><span id="post-52148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I expect the answer here to be YES! but I just need a sanity check.</p><p>I've been using wireshark to analyse packets coming to my server. My server uses Java NIO to process incoming bytes using a ByteBuffer. I was seeing some irregular looking data coming in on the socket, and I thought I missing some. What I'm doing is flashing a firmware over the air, to do this I send a command, wait for an ACK from the bootloader, send another command, wait for an ACK... and so on. However, on the very first command I didn't get an ACK (or a NACK). So while testing, I decided to not wait for the first ACK and just carry on with the process. Everything else worked as expected. This was a few months ago. Our firmwares have since been upgraded, so I decide to test again and verify everything is the same. I do some tests in wireshark to see if there's an extra ACK in there. I figure I need to run wireshark an see if it's arriving and I'm trying to read it too quickly or something.<br />
Anyway, I notice that one of the instructions returns two ACKs instead of one. So the sequence from wireshark looks like this:</p><p><strong>Send instruction 1</strong><br />
Don't check for ACK<br />
<strong>Send instruction 2</strong><br />
receive ACK<br />
<strong>Send instruction 3</strong><br />
receive 2 ACKs<br />
<strong>Send instruction 4</strong><br />
receive 1 ACK<br />
...process carries on as expected.<br />
</p><p>The buffer size being read/written by the server is two bytes, with each instruction being a 1 byte instruction and a 1 byte checksum, each ACK/NACK is 1 byte.</p><p>Now, here's where it gets odd, if I set the server to check for an ACK after the first instruction too with this new firmware (as it ideally should) then I get the following:</p><p><strong>Send instruction 1</strong><br />
receive 1 ACK<br />
<strong>Send instruction 2</strong><br />
receive 1 ACK<br />
<strong>Send instruction 3</strong><br />
receive 1 ACK<br />
<strong>Send instruction 4</strong><br />
receive 1 ACK<br />
...process carries on as expected.<br />
</p><p>So, I was initially expecting the server to wait for an ACK/NACK on the first instruction and not proceed beyond that point, like it did with the original firmware, but that isn't the case.</p><p>Is it guaranteed that these two ACKs being sent from the bootloader are actually being sent together? or is it possible they're sent separately and I'm doing something serverside that makes it look like they arrive together?</p><p>The reason I'm asking is because I would expect the two ACKs to arrive after instruction 2, but they don't.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '16, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/3ab01be5b3ec231ca1b6fee9c0c27582?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elektrovert&#39;s gravatar image" /><p><span>elektrovert</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elektrovert has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '16, 06:43</strong> </span></p></div></div><div id="comments-container-52148" class="comments-container"><span id="52149"></span><div id="comment-52149" class="comment"><div id="post-52149-score" class="comment-score"></div><div class="comment-text"><p>As you say each ACK/NAK is 1 byte, I suppose they all look the same, i.e. you cannot tell which ACK acknowledges which forward message, right? So I would expect that you send the 2nd forward message too early and thus the ACK for the 1st one arrives later and so on, and only between the 3rd and 4th forward message things settle down because the target manages to send two ACKs before the server sends the 4th forward message.</p><p>To confirm that, if you can affect the code at server side that deep, try to delay the 2nd forward message for long enough to give the ACK a chance to arrive, but don't trigger its sending by reception of the ACK, just wait.</p></div><div id="comment-52149-info" class="comment-info"><span class="comment-age">(02 May '16, 07:08)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="52164"></span><div id="comment-52164" class="comment"><div id="post-52164-score" class="comment-score"></div><div class="comment-text"><p>Yes, thanks, that's my next step. I expect that this is the case, just needed to be sure.</p></div><div id="comment-52164-info" class="comment-info"><span class="comment-age">(02 May '16, 22:53)</span> <span class="comment-user userinfo">elektrovert</span></div></div></div><div id="comment-tools-52148" class="comment-tools"></div><div class="clear"></div><div id="comment-52148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52150"></span>

<div id="answer-container-52150" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52150-score" class="post-score" title="current number of votes">1</div><span id="post-52150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="elektrovert has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To answer the question itself: if you really mean bytes in a packet, then it is 100% true, as Wireshark handles a packet (well, frame) as an indivisible unit. If an IP packet is fragmented into several frames, Wireshark shows you each of those frames, with individual timestamps. The reassembled packet is shown in the dissection &amp; packet bytes pane of the last frame, but with just a little extra effort you can still tell which of the reassembled packet's bytes has arrived in which frame.</p><p>So if both bytes share the same frame, there is no way how Wireshark could mislead you.</p><p>If they don't (which you may encounter as well), the situation is slightly more complex, because libpcap/WinPcap doesn't assign the frame timestamp at the moment of physical arrival of the packet to the Ethernet/802.11 interface but as late as when the kernel fetches it from the buffer and "shows" it to libpcap/WinPcap. So if the kernel is busy, several frames may wait in the NIC's buffers, and then the kernel fetches them almost at the same time. In this case, their order of arrival is still kept, but the timestamp resolution may be so coarse that they'll all get the same timestamp value.</p><p>But the information about the order is only reliable for frames going the same direction. Hypothetically, you could see a sent frame with a timestamp lower than the timestamp of a received frame which has actually arrived earlier than the sent frame has been sent - that could happen if the kernel has first sent the frame and only then has looked into the receive buffer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '16, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '16, 07:40</strong> </span></p></div></div><div id="comments-container-52150" class="comments-container"></div><div id="comment-tools-52150" class="comment-tools"></div><div class="clear"></div><div id="comment-52150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52151"></span>

<div id="answer-container-52151" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52151-score" class="post-score" title="current number of votes">1</div><span id="post-52151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The answer is yes, and that's the beauty of it: It shows you what's actually going on in the network.</p><p>Mind you, this is at the lowest level of the network, so to get here your data has to traverse the socket layer, TCP/IP stack and get to the network driver before being picked up for capture. Same goes for packet reception. The capture takes place at the lowest level, after which the packets with your data has to move up all the way through the TCP/IP and socket layer to your application. And all these layers can have buffers, which influence when the data is handled. The specifics of these are out of scope of this site, but looking at socket options should get you on you way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '16, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-52151" class="comments-container"></div><div id="comment-tools-52151" class="comment-tools"></div><div class="clear"></div><div id="comment-52151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

