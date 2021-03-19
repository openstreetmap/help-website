+++
type = "question"
title = "Capturing on GigE Headend Network"
description = '''I am trying to capture the video interface on an Arris ad server. Using Wireshark I CAN see pings and I CAN see FTP frames from it and i can capture that data on wireshark. When it sends a video file I can NOT see the UDP frames that are known to be coming from it because it is airing an ad to a spl...'''
date = "2011-10-04T13:18:00Z"
lastmod = "2011-10-04T13:55:00Z"
weight = 6717
keywords = [ "gige", "capture", "udp" ]
aliases = [ "/questions/6717" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing on GigE Headend Network](/questions/6717/capturing-on-gige-headend-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture the video interface on an Arris ad server. Using Wireshark I CAN see pings and I CAN see FTP frames from it and i can capture that data on wireshark. When it sends a video file I can NOT see the UDP frames that are known to be coming from it because it is airing an ad to a splicer. I have NO filters on. How can it be that I CAN see data coming from that port BUT I can not see the MPEG coming out in UDP frames?</p></div><div id="question-tags" class="tags-container tags">gige capture udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '11, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/e801d8e1558a4375c2c15dc9bbac75c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scottjthomas&#39;s gravatar image" /><p>scottjthomas<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scottjthomas has no accepted answers">0%</span></p></div></div><div id="comments-container-6717" class="comments-container"><span id="6718"></span><div id="comment-6718" class="comment"><div id="post-6718-score" class="comment-score"></div><div class="comment-text"><p>In this case I am connected to a small gige switch right at the Arris output, I am right across the device that is sending the video packets.</p></div><div id="comment-6718-info" class="comment-info"><span class="comment-age">(04 Oct '11, 13:21)</span> scottjthomas</div></div><span id="6721"></span><div id="comment-6721" class="comment"><div id="post-6721-score" class="comment-score"></div><div class="comment-text"><p>Adding the text from the second question you raised for this issue:</p><p>I am trying to capture IP packets to/from two ports. One port is a splicer on the other side of a 7609 switch and the other port is a small netgear gige switch and to that a PC and an Arris ad server are connected. I am trying to capture communciation between the ad server and splicer using the PC on the switch.</p></div><div id="comment-6721-info" class="comment-info"><span class="comment-age">(04 Oct '11, 13:53)</span> SYN-bit ♦♦</div></div><span id="6722"></span><div id="comment-6722" class="comment"><div id="post-6722-score" class="comment-score"></div><div class="comment-text"><p>The Arris IS known to be sending control messages to the splicers but I can NOT see any messages go back and forth between the splicer and ad server. I CAN ping the splicer port and SEE the pings BOTH ways on the PC running wireshark. I CAN also SEE pings to and from the Arris ad server. However the PC never sees ANY of the actual control messages that are being sent between the two devices. I am using NO filters and it is in promicuous mode.</p><p>What kinds of data can Wireshark NOT capture?</p></div><div id="comment-6722-info" class="comment-info"><span class="comment-age">(04 Oct '11, 13:53)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-6717" class="comment-tools"></div><div class="clear"></div><div id="comment-6717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6724"></span>

<div id="answer-container-6724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6724-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The NetGear is a switch, so it will not forward traffic to your Wireshark PC unless you can configure it to do port-mirroring.</p><p>Have a look at <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a> for more info on how your capture setup influences what you can and can not see in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '11, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6724" class="comments-container"><span id="6725"></span><div id="comment-6725" class="comment"><div id="post-6725-score" class="comment-score"></div><div class="comment-text"><p>It is one of those dumb switches..is that bad? It doesn't have any configuration.</p></div><div id="comment-6725-info" class="comment-info"><span class="comment-age">(04 Oct '11, 14:02)</span> scottjthomas</div></div><span id="6726"></span><div id="comment-6726" class="comment"><div id="post-6726-score" class="comment-score"></div><div class="comment-text"><p>Also I CAN see PINGS and FTP FROM the ad server through the small switch. Is there some reason WHY the UDP frames would be the ONLY thing that I can NOT see?</p></div><div id="comment-6726-info" class="comment-info"><span class="comment-age">(04 Oct '11, 14:09)</span> scottjthomas</div></div><span id="6727"></span><div id="comment-6727" class="comment"><div id="post-6727-score" class="comment-score"></div><div class="comment-text"><p>Do you mean you DO see ping and ftp packets between the "ad server" and the "splicer" on the Wireshark PC, but you DON'T see the udp packets between the "ad server" and the "splicer"? If so, that is indeed strange. However, that is not due to Wireshark not being able to show you the udp traffic.</p><p>If you DO see ping and ftp packets between the Wireshark PC and the "ad server" (or the "splicer"), then this is indeed normal, please carefully read the link I provided earlier as it explains this in more detail.</p></div><div id="comment-6727-info" class="comment-info"><span class="comment-age">(04 Oct '11, 15:24)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-6724" class="comment-tools"></div><div class="clear"></div><div id="comment-6724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

