+++
type = "question"
title = "RSSI value in wireshark"
description = '''hello, i wanted to know how is wireshark able to capture packets of another computer and how is it able to calculate the rssi values of the packets. where is the rssi value stored in the computer and in which frame format is it saved??thank you..'''
date = "2016-10-05T21:17:00Z"
lastmod = "2016-10-09T05:36:00Z"
weight = 56175
keywords = [ "rssi" ]
aliases = [ "/questions/56175" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [RSSI value in wireshark](/questions/56175/rssi-value-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56175-score" class="post-score" title="current number of votes">0</div><span id="post-56175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, i wanted to know how is wireshark able to capture packets of another computer and how is it able to calculate the rssi values of the packets. where is the rssi value stored in the computer and in which frame format is it saved??thank you..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rssi" rel="tag" title="see questions tagged &#39;rssi&#39;">rssi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '16, 21:17</strong></p><img src="https://secure.gravatar.com/avatar/11d703ea8508cf72c52f1718280bb7bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misbah&#39;s gravatar image" /><p><span>misbah</span><br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misbah has no accepted answers">0%</span></p></div></div><div id="comments-container-56175" class="comments-container"></div><div id="comment-tools-56175" class="comment-tools"></div><div class="clear"></div><div id="comment-56175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56182"></span>

<div id="answer-container-56182" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56182-score" class="post-score" title="current number of votes">0</div><span id="post-56182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="misbah has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To capture on air, you need a wireless network adapter for which a driver exists for your operating system which supports monitoring and promiscuous mode at the same time. This is currently only sure for Mac, on Windows and Linux you have to carefully choose the hardware and drivers. On Windows, you need a release of NPcap which supports monitoring mode on top of the above. Plus there are some further issues related to 802.11 modes supported for normal operation and for monitoring mode.</p><p>The driver in monitoring mode normally provides a radiotap or other (e.g. TZSP) pseudo-header which, among other metadata related to the captured 802.11 frame, contains the RSSI value as your network adapter has measured it at the moment of capturing the frame. Wireshark shows you the value twice - once in the dissector of the pseudo-header itself, second time in the "802.11 radio information" set of fields which is always the same regardless what pseudo-header they've arrived in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '16, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Oct '16, 03:18</strong> </span></p></div></div><div id="comments-container-56182" class="comments-container"><span id="56183"></span><div id="comment-56183" class="comment"><div id="post-56183-score" class="comment-score"></div><div class="comment-text"><p>Totally agree with <span>@Sindy</span>, here is a screenshot of RSSI value presented in a beacon frame captured with a wireless adapter in monitor mode.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/RSSI.png" alt="alt text" /></p></div><div id="comment-56183-info" class="comment-info"><span class="comment-age">(06 Oct '16, 03:43)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="56208"></span><div id="comment-56208" class="comment"><div id="post-56208-score" class="comment-score"></div><div class="comment-text"><blockquote><p>once in the dissector of the pseudo-header itself,</p></blockquote><p>...unless the particular packet file format keeps radio information separate from packet data; pcap, pcapng, and Network Monitor files don't, they have a pseudo-header at the beginning of the packet data, but the {Airo,Omni}Peek formats from WildPackets^WSavvius do keep them separate.</p><p>The "802.11 radio information" section (which is new in 2.2) is probably the best place to look for radio information in most cases, as it's not cluttered up with the details of the pseudo-header.</p></div><div id="comment-56208-info" class="comment-info"><span class="comment-age">(06 Oct '16, 15:48)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="56248"></span><div id="comment-56248" class="comment"><div id="post-56248-score" class="comment-score"></div><div class="comment-text"><p><span>@Guy</span></p><p>The screenshot is from an Omnipeek capture (pkt file) opened in Wireshark and it has the radio information in the header. This is good - but when I try to subset the capture the file and either SaveAs or Export in Wireshark, I lose this information. From your comment, I think I now know why. Is there a format I can move to when subsetting in Wireshark to allow me to keep the radio information?</p></div><div id="comment-56248-info" class="comment-info"><span class="comment-age">(09 Oct '16, 03:38)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="56254"></span><div id="comment-56254" class="comment"><div id="post-56254-score" class="comment-score"></div><div class="comment-text"><p><span>@Bob Jones</span>, the precise meaning of "header" matters here.</p><p>In the narrow sense, it is part of the actual packet data (i.e. it can be actually captured on the wire or in the air) which contains the overhead data of a protocol layer - such as an IP header or a TCP header.</p><p>In a wider sense, it may also be some information prefixed to the actual captured data into the container intended to carry the captured data because the capture format doesn't provide any other container for that information. This is the case of radiotap or TZSP "headers", and where distinction is important, this type of "header" is called a "pseudo-header", just as <span>@Guy Harris</span> refers to it above.</p><p>Only in the widest sense (which you have used above) it is the information which is relevant to a single particular packet, regardless how it is transported or encapsulated. Some formats, such as pcapng or the Airo/Omnipeek formats, provide for logical separation between actual captured data and the metadata which are related to the packet but not part of its actual contents.</p><p>The <code>802.11 radio information</code> part of the dissection tree is a unified view of the radio related information regardless how it is stored in the capture file.</p><p>Unfortunately, no pcapng extension (similar to the epb_flags option to the Enhanced Packet Block) has been proposed yet to accommodate the radio related information. So as of current, Wireshark would have to either change the contents of each packet by prefixing it with a pseudo-header and migrating the radio related data there, or use the Airo/OmniPeek format directly, to be able to export these data along with the packets.</p><p>BTW, similar situation exists for other types of metadata - namely, in the mobile networks area where bandwidth efficiency is one of primary design constraints, the packet data itself are not enough to identify the protocol, so automated identification is only possible if the necessary information is available as metadata in the capturing analyzer's own capture file. Here again Wireshark cannot export data without losing this information or without learning to write the complete original format.</p><p>Filing an enhancement bug for adding a radio-related Option to pcapng draft proposal and handling it in Wireshark might be the cleanest way to get the ability to export packets from Airo/OmniPeek without losing the radio-related information.</p></div><div id="comment-56254-info" class="comment-info"><span class="comment-age">(09 Oct '16, 05:36)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-56182" class="comment-tools"></div><div class="clear"></div><div id="comment-56182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

