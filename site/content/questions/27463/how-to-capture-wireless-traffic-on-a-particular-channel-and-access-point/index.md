+++
type = "question"
title = "How to Capture wireless traffic on a particular channel and access point?"
description = '''I have been successful in capturing wireless traffic in monitor mode using the tcpdump -ni option and even decrypt the WEP traffic, using wireshark, on my network that I was monitoring. But my router was configured to AUTO option for the channel. While capturing this mode, am able to various other t...'''
date = "2013-11-26T22:52:00Z"
lastmod = "2013-11-29T08:32:00Z"
weight = 27463
keywords = [ "wireless", "wep", "tcpdump", "monitor-mode", "capture-setup" ]
aliases = [ "/questions/27463" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to Capture wireless traffic on a particular channel and access point?](/questions/27463/how-to-capture-wireless-traffic-on-a-particular-channel-and-access-point)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27463-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been successful in capturing wireless traffic in monitor mode using the tcpdump -ni option and even decrypt the WEP traffic, using wireshark, on my network that I was monitoring. But my router was configured to AUTO option for the channel. While capturing this mode, am able to various other traffic along with mine. How do I capture traffic from only the AP that I want to monitor and also monitor a particular channel of it?</p><p>Thanks in advance, Kartz</p></div><div id="question-tags" class="tags-container tags">wireless wep tcpdump monitor-mode capture-setup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/c930bfdb6dd68a43136fc6bf6abc408b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartzoft&#39;s gravatar image" /><p>Kartzoft<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartzoft has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '13, 22:53</p></div></div><div id="comments-container-27463" class="comments-container"></div><div id="comment-tools-27463" class="comment-tools"></div><div class="clear"></div><div id="comment-27463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27570"></span>

<div id="answer-container-27570" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27570-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use capture filters to isolate the traffic to/from a particular AP. The example provided on the <a href="http://wiki.wireshark.org/Wi-Fi">Wireshark Wi-Fi wiki page</a> is:</p><pre><code>wlan host 08:00:08:15:ca:fe</code></pre><p>For more information on the capture filter syntax, refer to the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">pcap-filter man page</a>.</p><p>As for monitoring a particular channel, from the <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">Wireshark WLAN Capture Setup wiki page</a>:</p><blockquote>Put the card into monitor mode with the command ifconfig interface monitor. You can also set the channel to monitor by adding the argument channel channel_number to that command.</blockquote><p>Refer to the wiki page for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '13, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-27570" class="comments-container"></div><div id="comment-tools-27570" class="comment-tools"></div><div class="clear"></div><div id="comment-27570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

