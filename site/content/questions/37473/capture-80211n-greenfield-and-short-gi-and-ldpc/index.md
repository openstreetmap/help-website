+++
type = "question"
title = "Capture 802.11n Greenfield and Short GI and LDPC"
description = '''I was using AirPcap to capture 802.11n frames in mode HT Greenfield with short GI but AirPcap losses these kind of frames. I also capture with a Macbook pro airport (Broadcom BPM4360 802.11ac radio card) and all frames was captured correctly.  There is any other solution to capture all 802.11n frame...'''
date = "2014-10-30T12:37:00Z"
lastmod = "2014-10-31T01:24:00Z"
weight = 37473
keywords = [ "capture", "airpcap", "radio", "greenfield", "802.11n" ]
aliases = [ "/questions/37473" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture 802.11n Greenfield and Short GI and LDPC](/questions/37473/capture-80211n-greenfield-and-short-gi-and-ldpc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37473-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was using AirPcap to capture 802.11n frames in mode HT Greenfield with short GI but AirPcap losses these kind of frames. I also capture with a Macbook pro airport (Broadcom BPM4360 802.11ac radio card) and all frames was captured correctly. There is any other solution to capture all 802.11n frames despite which HT mode, GI, and coding used? Is there any product like AirPcap as a better and chipper option than a Macbook? Thank you.</p></div><div id="question-tags" class="tags-container tags">capture airpcap radio greenfield 802.11n</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '14, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/07e0e0eea8a9b3775715db281868d50f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jpg%20ceibal&#39;s gravatar image" /><p>jpg ceibal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jpg ceibal has no accepted answers">0%</span></p></div></div><div id="comments-container-37473" class="comments-container"></div><div id="comment-tools-37473" class="comment-tools"></div><div class="clear"></div><div id="comment-37473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37487"></span>

<div id="answer-container-37487" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37487-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume your AirPcap adapter is an AirPcap NX adapter; an AirPcap adapter that's not an AirPcap NX adapter won't capture <em>any</em> 802.11n frames, but you seem to be saying it captures some 802.11n frames, just not greenfield short-GI frames. ( If it's <em>not</em> an AirPcap NX adapter, you'll need to get an AirPcap NX adapter and use that._</p><p>With that assumption, the only solutions are:</p><ol><li>ask Riverbed support why your AirPcap NX doesn't capture those packets;</li><li>get some other packet capture application for Windows that supports Wi-Fi and that writes files that Wireshark can read, such as <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a> or <a href="http://www.tamos.com/products/commwifi/">CommView for Wi-Fi</a> or <a href="http://www.wildpackets.com/products/omnipeek_network_analyzer">OmniPeek</a>, and hope that it supports the Wi-Fi adapter on your Windows machine;</li><li>put Linux on that machine by dual-booting, hope that it supports the Wi-Fi adapter on that machine, and try capturing there;</li><li>put Linux on that machine by running in some virtual-machine software such as VMware Workstation or Parallels Workstation or VirtualBox, get some USB 802.11n-capable Wi-Fi adapter (not your AirPcap adapter, that's not supported on Linux), and use that with Linux to capture packets.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '14, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37487" class="comments-container"></div><div id="comment-tools-37487" class="comment-tools"></div><div class="clear"></div><div id="comment-37487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

