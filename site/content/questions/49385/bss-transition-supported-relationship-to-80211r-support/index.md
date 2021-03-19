+++
type = "question"
title = "&quot;BSS Transition: Supported&quot; relationship to 802.11r support"
description = '''I&#x27;d like to verify that the decode of the Extended Capabilities, in an 802.11 Probe Request, of &quot;BSS Transition&quot; is equal to 802.11r support. For example, see the following screenshot, (and accompanying filter of &quot;wlan_mgt.extcap.b19 == 1&quot; Screenshot here: https://drive.google.com/file/d/0B_5iR2M2La...'''
date = "2016-01-19T10:09:00Z"
lastmod = "2016-01-19T18:39:00Z"
weight = 49385
keywords = [ "802.11r" ]
aliases = [ "/questions/49385" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# ["BSS Transition: Supported" relationship to 802.11r support](/questions/49385/bss-transition-supported-relationship-to-80211r-support)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49385-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to verify that the decode of the Extended Capabilities, in an 802.11 Probe Request, of "BSS Transition" is equal to 802.11r support. For example, see the following screenshot, (and accompanying filter of "wlan_mgt.extcap.b19 == 1"</p><p>Screenshot here: <a href="https://drive.google.com/file/d/0B_5iR2M2LaJmOVl4cVViYmo0eTQ/view?usp=sharing">https://drive.google.com/file/d/0B_5iR2M2LaJmOVl4cVViYmo0eTQ/view?usp=sharing</a></p><p>Put another way, is this a client advertising it's support of FT/802.11r?</p></div><div id="question-tags" class="tags-container tags">802.11r</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '16, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/cee21d07959f54316e2e540897a9a523?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike909&#39;s gravatar image" /><p>mike909<br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike909 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jan '16, 03:47</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-49385" class="comments-container"></div><div id="comment-tools-49385" class="comment-tools"></div><div class="clear"></div><div id="comment-49385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49393"></span>

<div id="answer-container-49393" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49393-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>To answer your question simply - NO, setting the BSS Transition bit (value = 1) within the Extended Capabilities element does NOT indicate support for 802.11r (Fast BSS transition = FT).</p><p>What does indicate a client's support for FT?<br />
A client that supports the FT feature must include both of the following within an Association Request frame:</p><ol><li>The Mobility Domain information element (Element ID = 54)</li><li>The RSN information element (Element ID = 48) must contain FT authentication under the Authentication Key Management (AKM) section. <img src="https://osqa-ask.wireshark.org/upfiles/Mobility-Domain.jpg" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/RSN.jpg" alt="alt text" /></li></ol><p>So what does setting the BSS Transition bit within the Extended Capabilities element indicate?</p><p>From the IEEE 802.11-2012 specification, section 8.4.2.29 defines each bit within the Extended Capabilities element. Bit 19 is reserved for BSS Transition and the reader is then referred to section 10.23.6 (BSS transition management for network load balancing). Per the IEEE 802.11-2012 specification, section 10.23.6:</p><p>"The BSS Transition capability enables improved throughput, effective data rate and/or QoS for the aggregate of STAs in a network by shifting (via transition) individual STA traffic loads to more appropriate points of association within the ESS."</p><p>What does that mean?</p><p>Suppose a WiFi client connects to the nearest AP and has a strong signal to that AP (RSSI). The user would expect great throughput. However, the AP might be overloaded with users and/or traffic and cannot provide good throughput or QoS to the associated client. The AP is aware of another nearby AP (within the same ESS) that has a lower load. The AP can request the client to transition to the new AP (i.e., BSS transition). Although the signal strength may be lower on this other AP (lower RSSI), the overall throughput and user experience is better due to the lower traffic load on the new AP. It does NOT guarantee that the roaming to the new AP will be FT; hence, any time-sensitive connections may be lost when roaming to the new AP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '16, 18:39</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span> </br></p></img></div></div><div id="comments-container-49393" class="comments-container"><span id="49404"></span><div id="comment-49404" class="comment"><div id="post-49404-score" class="comment-score"></div><div class="comment-text"><p>That's about the best answer I've ever seen in a forum, of any kind. Really appreciate the specification reference.</p></div><div id="comment-49404-info" class="comment-info"><span class="comment-age">(20 Jan '16, 08:23)</span> mike909</div></div><span id="49409"></span><div id="comment-49409" class="comment"><div id="post-49409-score" class="comment-score"></div><div class="comment-text"><p>@mike909 - Thank you for the compliment!</p></div><div id="comment-49409-info" class="comment-info"><span class="comment-age">(20 Jan '16, 11:59)</span> Amato_C</div></div><span id="49443"></span><div id="comment-49443" class="comment"><div id="post-49443-score" class="comment-score"></div><div class="comment-text"><p>Note, "BSS Transition" is part of 802.11v (WNM), which is part of the 802.11-2012 specification (sections noted above)</p></div><div id="comment-49443-info" class="comment-info"><span class="comment-age">(21 Jan '16, 22:36)</span> mike909</div></div></div><div id="comment-tools-49393" class="comment-tools"></div><div class="clear"></div><div id="comment-49393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

