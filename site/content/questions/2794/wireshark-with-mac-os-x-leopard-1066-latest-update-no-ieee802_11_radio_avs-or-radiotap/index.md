+++
type = "question"
title = "wireshark with mac os x leopard 10.6.6 (latest update): no IEEE802_11_RADIO_AVS or radiotap"
description = '''Hello, I&#x27; ve been trying to capture packets using IEEE802_11_RADIO_AVS or radiotap data link type but wireshark is unable to change the airport extreme card to this mode and so is tcpdump using the -y option (the -L option only shows the ethernet dlt). Since I do not possess the necessary background...'''
date = "2011-03-13T08:05:00Z"
lastmod = "2011-03-14T11:20:00Z"
weight = 2794
keywords = [ "radiotap", "leopard", "10.6.6", "ieee802_11_radio_avs", "dlt" ]
aliases = [ "/questions/2794" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark with mac os x leopard 10.6.6 (latest update): no IEEE802\_11\_RADIO\_AVS or radiotap](/questions/2794/wireshark-with-mac-os-x-leopard-1066-latest-update-no-ieee802_11_radio_avs-or-radiotap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2794-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I' ve been trying to capture packets using IEEE802_11_RADIO_AVS or radiotap data link type but wireshark is unable to change the airport extreme card to this mode and so is tcpdump using the -y option (the -L option only shows the ethernet dlt). Since I do not possess the necessary background working with these drivers could you please confirm that it is due to the latest update that I cannot capture using this dlt (perhaps there have been other cases like mine)? In the past I have done so but not since this last update. Yet, using the "airport sniff" utility in Terminal produces a pcap file with the appropriate IEEE 802.11 headers. Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">radiotap leopard 10.6.6 ieee802_11_radio_avs dlt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '11, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/1d431e0d5df247a32cfec5ebbf7d8600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vellerefond&#39;s gravatar image" /><p>Vellerefond<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vellerefond has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '11, 08:06</p></div></div><div id="comments-container-2794" class="comments-container"></div><div id="comment-tools-2794" class="comment-tools"></div><div class="clear"></div><div id="comment-2794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2807"></span>

<div id="answer-container-2807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2807-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In Mac OS X, in order to get 802.11 headers, you must capture in monitor mode.</p><p>OS X 10.6 has libpcap 1.x; libpcap 1.x has an API to switch to monitor mode, supported on Linux, *BSD, and Mac OS X, and, on OS X, only allows you to select 802.11 headers if you've selected monitor mode.</p><p>The Wireshark 1.4.x 64-bit binaries for Mac OS X use the new APIs, so they do not let you select 802.11 headers unless you select monitor mode; if an interface supports monitor mode, there's a checkbox in the "Capture Options" dialog to capture in monitor mode. Check that check box, and it should offer you a choice of 802.11 headers with or without various radio headers.</p><p>The version of tcpdump that ships with 10.6, and the 64-bit binaries for Wireshark and TShark 1.4.x, also support a command-line option to request monitor mode - "-I" (capital-I). In order to capture with 802.11 headers with tcpdump, TShark, or, if you start the capture from the command line, Wireshark, you must pass the "-I" flag. That will automatically select 802.11 with radiotap if it's available, otherwise 802.11 with AVS if it's available, otherwise 802.11; you can use "-y" to choose link-layer headers other than the default.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '11, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2807" class="comments-container"></div><div id="comment-tools-2807" class="comment-tools"></div><div class="clear"></div><div id="comment-2807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

