+++
type = "question"
title = "CAPWAP 801.11 Data Header FCF Swapped - why?"
description = '''I&#x27;m getting confused while trying to write code to read frames that contain a CAPWAP header. If I open the file in Wireshark, it prints &quot;(Swapped)&quot; next to the Frame Control Field of the IEEE 802.11 Data decode following the CAPWAP header, and I have no idea how Wireshark realized it needed to do th...'''
date = "2016-09-24T16:38:00Z"
lastmod = "2016-09-25T04:18:00Z"
weight = 55804
keywords = [ "decode", "capwap" ]
aliases = [ "/questions/55804" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [CAPWAP 801.11 Data Header FCF Swapped - why?](/questions/55804/capwap-80111-data-header-fcf-swapped-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55804-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting confused while trying to write code to read frames that contain a <a href="https://tools.ietf.org/html/rfc5415">CAPWAP</a> header. If I open the file in Wireshark, it prints "(Swapped)" next to the Frame Control Field of the IEEE 802.11 Data decode following the CAPWAP header, and I have no idea how Wireshark realized it needed to do that. I tried reading the packet-ieee80211.c source code file to find out what is being done, but I can't track it down...</p><p>This is how the decode of the CAPWAP frame looks like:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/CAPWAP_802.11_Header_FCF_Swapped_h8SdhC3.png" alt="CAPWAP decode" /></p><p>If you look at the hex view you'll see that it says "01 08", which would normally decode to this being a management frame (Type = 0). But somehow Wireshark knows it needs to "swap" something (what exactly? Looks like the "01" byte lower nibble is swapped?). Very confused. Maybe someone with more 802.11 skill can shed a light? Thanks!</p><p>BTW don't get confused by the "2c" byte following the "01 08", that's the value for the 44 microsecond duration following the flags. It's not the 2c mentioned for the FCF. Not sure why that value is even mentioned at that position ("0x082c (Swapped)")...</p></div><div id="question-tags" class="tags-container tags">decode capwap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '16, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-55804" class="comments-container"></div><div id="comment-tools-55804" class="comment-tools"></div><div class="clear"></div><div id="comment-55804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55805"></span>

<div id="answer-container-55805" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55805-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure that an 802.11 skill alone (not that I'd have one) is sufficient here, it has to do with the dissector code and with how it is invoked.</p><p>If you take the 802.11 part of your frame alone (from your <code>01 08</code> till the end of the frame) and import them indicating a plain <code>IEEE 802.11 Wireless LAN</code> encapsulation, the wlan dissector doesn't handle them the same - in this case, it does interpret the contents of the FCF as announcing a retransmitted control frame, with all the impact to dissection of the rest of it. If you manually swap the two bytes of the FCF, making them <code>08 01</code>, you get a much more logical interpretation as a TCP SYN packet on its way from STA to AP. Any "logical" operation (nibble or bit pair swapping) cannot explain a change from 0x1 to 0x8.</p><p>But the code, <code>packet-ieee80211.c</code>, contains the following remark:</p><pre><code>/*
 * Dissect 802.11 with a variable-length link-layer header and a byte-swapped
 * control field and with no FCS (some hardware sends out LWAPP-encapsulated
 * 802.11 packets with the control field byte swapped).
 */
...
dissect_ieee80211_common(tvb, pinfo, tree, IEEE80211_COMMON_OPT_BROKEN_FC|IEEE80211_COMMON_OPT_NORMAL_QOS, &amp;phdr);</code></pre><p>(note the <code>IEEE80211_COMMON_OPT_BROKEN_FC</code> bit, and note that the comment probably means "with a byte-swapped control field", not "with a swapped control-field byte").</p><p>LWAPP (RFC 5412) is essentially an indirect reference to CAPWAP (RFC 5415), and CAPWAP doesn't say anything regarding changing the order of FCF bytes. However, there is no heuristic testing which interpretation of the FCF yields better results - encapsulation of the 802.11 frame into CAPWAP implies swapping of the FCF's bytes, dot.</p><p>So it seems to me to be an an-initial-mistake-gone-de-facto-standard case.</p><p>BTW, the occurrence of the <code>2c</code> in the "swapped" interpretation of the Frame Control Field in the dissector is likely to be a bug, it really refers to the next byte and shows whatever is there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '16, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '16, 05:41</p></div></div><div id="comments-container-55805" class="comments-container"><span id="55806"></span><div id="comment-55806" class="comment"><div id="post-55806-score" class="comment-score"></div><div class="comment-text"><p>Thanks, @sindy, this is pretty much in line with what I suspect (mistake-gone-de-facto-standard and "2c" being a bug) - the problem I have is how I can detect/determine that what I see is such a case and not a "normal" 802.11 header...</p><p>So you think the 802.11 dissector handles the decoding differently by knowing it was sent as a CAPWAP payload?</p></div><div id="comment-55806-info" class="comment-info"><span class="comment-age">(25 Sep '16, 04:29)</span> Jasper ♦♦</div></div><span id="55807"></span><div id="comment-55807" class="comment"><div id="post-55807-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>So you think the 802.11 dissector handles the decoding differently</p></blockquote><p>I am sure that the fact that the data came CAPWAP-encapsulated alone causes the ieee80211 dissector to swap the FCF bytes while dissecting. I cannot show you the responsible line of the code but I have tested that by fiddling around with the packet data (changing the FCF byte order to the correct one in the complete frame and still getting them dissected as swapped).</p><blockquote><p>how I can detect/determine that what I see is such a case</p></blockquote><p>I'm not sure there is a reliable way to do it on a single frame. Over several (tens of) frames, trying to dissect them both ways and choosing the one which returns less errors might be sufficiently reliable.</p></div><div id="comment-55807-info" class="comment-info"><span class="comment-age">(25 Sep '16, 04:51)</span> sindy</div></div><span id="55808"></span><div id="comment-55808" class="comment"><div id="post-55808-score" class="comment-score">1</div><div class="comment-text"><p>Thanks, I think you're right... I'll try to check if the 802.11 layer was sent via CAPWAP and swap the FCF. I also converted your first comment to an answer so I can accept it ;-)</p></div><div id="comment-55808-info" class="comment-info"><span class="comment-age">(25 Sep '16, 05:38)</span> Jasper ♦♦</div></div><span id="55811"></span><div id="comment-55811" class="comment"><div id="post-55811-score" class="comment-score"></div><div class="comment-text"><p>The issue seems to have been around since a while ago:</p><p><a href="https://www.wireshark.org/lists/ethereal-dev/200309/msg00586.html">https://www.wireshark.org/lists/ethereal-dev/200309/msg00586.html</a> (it is not the first encounter of the issue, just a note that the already existing preference has been moved to a more appropriate place)</p><p><a href="http://www.cisco.com/en/US/docs/solutions/Enterprise/Mobility/emob30dg/TechArch.html">http://www.cisco.com/en/US/docs/solutions/Enterprise/Mobility/emob30dg/TechArch.html</a> (still referring to LWAPP and Ethereal rather than CAPWAP and Wireshark)</p><p><a href="http://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Mobility/emob73dg/emob73/ch2_Arch.pdf">http://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Mobility/emob73dg/emob73/ch2_Arch.pdf</a> (an evolution of the same document which still doesn't explain why the CAPWAP encapsulation swaps the bytes).</p></div><div id="comment-55811-info" class="comment-info"><span class="comment-age">(25 Sep '16, 06:17)</span> sindy</div></div></div><div id="comment-tools-55805" class="comment-tools"></div><div class="clear"></div><div id="comment-55805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

