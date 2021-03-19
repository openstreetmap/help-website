+++
type = "question"
title = "wireshark-RTP stream play- G.711"
description = '''Hello, i am trying to play RTP stream on wireshark but having trouble.  I load the file in wireshark (.pcap file with udp packets) Telephony &amp;gt; VOIP calls &amp;gt; seperate window pops up to recalculate statistics but nothing to select here.  please guide..'''
date = "2015-10-19T10:51:00Z"
lastmod = "2015-10-24T12:51:00Z"
weight = 46704
keywords = [ "wireshark-rtp-g.711" ]
aliases = [ "/questions/46704" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark-RTP stream play- G.711](/questions/46704/wireshark-rtp-stream-play-g711)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46704-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i am trying to play RTP stream on wireshark but having trouble. I load the file in wireshark (.pcap file with udp packets) Telephony &gt; VOIP calls &gt; seperate window pops up to recalculate statistics but nothing to select here. please guide..</p></div><div id="question-tags" class="tags-container tags">wireshark-rtp-g.711</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/f6088320c8e267127ac346c441a66473?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jigrami&#39;s gravatar image" /><p>jigrami<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jigrami has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Oct '15, 10:53</p></div></div><div id="comments-container-46704" class="comments-container"></div><div id="comment-tools-46704" class="comment-tools"></div><div class="clear"></div><div id="comment-46704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46709"></span>

<div id="answer-container-46709" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46709-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On the one hand you talk about RTP streams, but then you say that the VoIP calls dialog doesn't show anything. Even though they are related it's not a given that just about any RTP stream shows up in there. Or rather, non at all will show up. Only VoIP call signalling packets will lead to entries in the VoIP calls dialog. From there, and only if the media negotiation information can be dissected, are RTP streams identified and can be feed to the player.</p><p>So, since you obviously have no VoIP call signalling packets there is another way to go about it. First of all you'll need to go into the RTP dissector preferences and tick the option 'Try to decode RTP outside of conversations'. This will dissect eligable UDP packets as RTP packets. Now go into the menu item Telephony -&gt; RTP -&gt; Show All Streams. This will give you a dialog to select a stream, analyse it and subsequently play it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46709" class="comments-container"><span id="46765"></span><div id="comment-46765" class="comment"><div id="post-46765-score" class="comment-score"></div><div class="comment-text"><p>hello, thanks Jaap. here is what's going on. The file I have captured is from our VM environment to a local PC. I loaded the file in wireshark under info column it shows source port PCoIP (pc over ip).<br />
</p><p>And other tool I use it CA/NetQoS-Observer, which shows these packets as RTP Payload: PCMU (G.711)Audio at 8000Hz</p><p>These UDP packets may not be VOIP calls; but its streaming from the VM machine to a local machine and I am trying to see that...</p><p>Thank You</p></div><div id="comment-46765-info" class="comment-info"><span class="comment-age">(20 Oct '15, 10:04)</span> jigrami</div></div><span id="46799"></span><div id="comment-46799" class="comment"><div id="post-46799-score" class="comment-score"></div><div class="comment-text"><p>I don't follow. Can you share the capture file?</p></div><div id="comment-46799-info" class="comment-info"><span class="comment-age">(21 Oct '15, 06:13)</span> Jaap ♦</div></div></div><div id="comment-tools-46709" class="comment-tools"></div><div class="clear"></div><div id="comment-46709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46906"></span>

<div id="answer-container-46906" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46906-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you upload the packetcapture? you can use <a href="https://www.cloudshark.org/">https://www.cloudshark.org/</a></p><p>My suggestion is to filter the stream and only then decode/play the .wav file.</p><p>More information here - <a href="https://wiki.wireshark.org/VoIP_calls">https://wiki.wireshark.org/VoIP_calls</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '15, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/94630d1ea1108afeafb344e884044d15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boaz%20Galil&#39;s gravatar image" /><p>Boaz Galil<br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boaz Galil has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '15, 12:51</p></div></div><div id="comments-container-46906" class="comments-container"></div><div id="comment-tools-46906" class="comment-tools"></div><div class="clear"></div><div id="comment-46906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

