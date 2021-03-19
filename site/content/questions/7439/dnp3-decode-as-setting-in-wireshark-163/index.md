+++
type = "question"
title = "DNP3 Decode As setting in Wireshark 1.6.3"
description = '''What should be setting in Wireshark 1.6.3 [Version 1.6.3 (SVN Rev 39702 from /trunk-1.6)] in Decode As, to properly analyze or capture DNP3 communication? In specific, what selection should be under &quot;Decode As&quot; in right window for each of the tabs:  -Link;  -Network;  -Protocol. When I tried default...'''
date = "2011-11-15T06:34:00Z"
lastmod = "2011-11-15T07:08:00Z"
weight = 7439
keywords = [ "decode_as", "dnp3" ]
aliases = [ "/questions/7439" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DNP3 Decode As setting in Wireshark 1.6.3](/questions/7439/dnp3-decode-as-setting-in-wireshark-163)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What should be setting in Wireshark 1.6.3 [Version 1.6.3 (SVN Rev 39702 from /trunk-1.6)] in Decode As, to properly analyze or capture DNP3 communication?</p><p>In specific, what selection should be under "Decode As" in right window for each of the tabs: -Link; -Network; -Protocol.</p><p>When I tried default selection, it is not decoding any DNP3 traffic</p><p>Any suggestion or help is greatly appreciated. Stanko K. [email protected]<a href="http://siemens.com">siemens.com</a></p></div><div id="question-tags" class="tags-container tags">decode_as dnp3</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '11, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/21000796d4d8be45c6270510eff632af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StankoK&#39;s gravatar image" /><p>StankoK<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StankoK has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 21:19</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-7439" class="comments-container"></div><div id="comment-tools-7439" class="comment-tools"></div><div class="clear"></div><div id="comment-7439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7442"></span>

<div id="answer-container-7442" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7442-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The DNP3 dissector has a default port of 20000 as per the IANA registration, so any traffic (TCP or UDP) arriving on this port should be dissected. For traffic on other ports, use the "Decode As ..." option and on the Transport tab select the source or destination (or both) ports and "DNP3.0" as the protocol for those ports. You shouldn't need to change anything on the Link or Network tabs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '11, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-7442" class="comments-container"><span id="7445"></span><div id="comment-7445" class="comment"><div id="post-7445-score" class="comment-score"></div><div class="comment-text"><p>Thanks for quick answer, Question is how to force Wireshark to listen port 20000. My colleague in USA is using same Wireshark and his default setting in "Decode As" Tabs are: Link: Ethertype 0x800; Network: IP Protocol 6; Transport: TCP source(20000)....</p><p>My Default setting is completely different: Ethertype 0x800; Network: IP Protocol 1; Transport: TCP source(10??).... I was trying many different selection under link, network, transport to match my colleague setting and decode DNP3 but no luck so far?!?!? Also, I have tried: "Decode As": Do Not Decode option but that one give me all raw frames...</p><p>Any Suggestion or help is greatly appreciated.</p><p>Thx. Stanko</p></div><div id="comment-7445-info" class="comment-info"><span class="comment-age">(15 Nov '11, 07:42)</span> StankoK</div></div><span id="7464"></span><div id="comment-7464" class="comment"><div id="post-7464-score" class="comment-score"></div><div class="comment-text"><p>Errm, have you actually captured any DNP3 traffic? What port is your field device using? Examine the capture with no display filters set and identify the traffic to and from your field device using the IP and port. If the field device is using port 20000 then you have nothing further to do, any DNP3 traffic will be displayed, if its using another port, then right click on a frame containing traffic to/from the field device, select "Decode As ..." and on the transport tab select the port the field device is using.</p><p>If you still have issues can you post your capture somewhere, e.g. CloudShark</p></div><div id="comment-7464-info" class="comment-info"><span class="comment-age">(16 Nov '11, 02:18)</span> grahamb ♦</div></div><span id="9259"></span><div id="comment-9259" class="comment"><div id="post-9259-score" class="comment-score"></div><div class="comment-text"><p>DNP3 runs over TCP and UDP; TCP and UDP have IP protocol numbers assigned to them, and probably almost never, or never, use other IP protocol numbers, so there is no need to do <em>anything</em> with the network-layer setting.</p><p>TCP and UDP run over IPv4 and IPv6; those protocols have Ethernet type numbers assigned to them, and probably almost never, or never, use different Ethernet type numbers, so there is no need to do <em>anything</em> with the link-layer setting.</p><p>The Wireshark DNP dissector registers for TCP and UDP ports 20000 by default, so there's no need to change that, either.</p></div><div id="comment-9259-info" class="comment-info"><span class="comment-age">(27 Feb '12, 13:55)</span> Guy Harris ♦♦</div></div><span id="9260"></span><div id="comment-9260" class="comment"><div id="post-9260-score" class="comment-score"></div><div class="comment-text"><p>The DNP-over-TCP dissector will check whether the TCP segment it's handed has at least 2 bytes of data, equal to 0x05 0x64; if the TCP segments you're capturing don't look like that, they won't be recognized as DNP. I'd have to check if this is a problem for DNP packets that require more than one TCP segment.</p></div><div id="comment-9260-info" class="comment-info"><span class="comment-age">(27 Feb '12, 13:57)</span> Guy Harris ♦♦</div></div><span id="57005"></span><div id="comment-57005" class="comment"><div id="post-57005-score" class="comment-score"></div><div class="comment-text"><p>Wireshark capture traffic DNP3 without any further adjustment, the problem is the version of Wireshark to win 7, to install an earlier version win 7 the problem remains not see traffic DNP3, it has installed the x86 version and not to run into 7. what win I had to do is enable a virtual machine on an x64 processor, run and install winXP commensurate for this operating system version and it worked. In the win XP you can see DNP3 packages without making any adjustments in Wireshark.</p></div><div id="comment-57005-info" class="comment-info"><span class="comment-age">(04 Nov '16, 17:37)</span> Marcos Valarezo</div></div><span id="57007"></span><div id="comment-57007" class="comment not_top_scorer"><div id="post-57007-score" class="comment-score"></div><div class="comment-text"><p>No need to post the same comment as an "answer" twice. Please start a new question for your issue.</p></div><div id="comment-57007-info" class="comment-info"><span class="comment-age">(04 Nov '16, 17:51)</span> grahamb ♦</div></div><span id="57008"></span><div id="comment-57008" class="comment not_top_scorer"><div id="post-57008-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Wireshark capture traffic DNP3 without any further adjustment</p></blockquote><p>Wireshark has always been able to <em>capture</em> DNP3 traffic. What matters is whether it <em>recognizes</em> that it's DNP3 traffic, rather than just TCP payload.</p><blockquote><p>the problem is the version of Wireshark to win 7, to install an earlier version win 7 the problem remains not see traffic DNP3, it has installed the x86 version and not to run into 7.</p></blockquote><p>So are you saying that if you run Wireshark on Windows 7, it's not recognizing DNP3 traffic, but if you save a capture file that should contain DNP3 traffic but doesn't show any DNP3 traffic in Wireshark, run the <em>same</em> version of Wireshark, and read that <em>same</em> capture file, on Windows XP, it <em>does</em> recognize DNP3 traffic in that file?</p></div><div id="comment-57008-info" class="comment-info"><span class="comment-age">(04 Nov '16, 17:56)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-7442" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-7442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

