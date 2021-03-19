+++
type = "question"
title = "Using Wireshark for troubleshooting unknown protocol drops on a router interface"
description = '''Hello, Is there a way within Wireshark to capture traffic between a router and a switch between two interfaces without being physically connected to any of these devices? I would like to find out what protocols the router keeps dropping (please see below).   50486066 packets input, 11916465873 bytes...'''
date = "2015-07-03T19:03:00Z"
lastmod = "2015-07-03T19:03:00Z"
weight = 43856
keywords = [ "unknown-protocols" ]
aliases = [ "/questions/43856" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using Wireshark for troubleshooting unknown protocol drops on a router interface](/questions/43856/using-wireshark-for-troubleshooting-unknown-protocol-drops-on-a-router-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43856-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is there a way within Wireshark to capture traffic between a router and a switch between two interfaces without being physically connected to any of these devices? I would like to find out what protocols the router keeps dropping (please see below).<br />
</p><pre><code> 50486066 packets input, 11916465873 bytes, 0 no buffer
     Received 1030652 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 252636 multicast, 0 pause input
     58872028 packets output, 36007876614 bytes, 0 underruns
     0 output errors, 0 collisions, 0 interface resets
     **247772 unknown protocol drops**
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out</code></pre><p>Thanks for the help.</p></div><div id="question-tags" class="tags-container tags">unknown-protocols</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '15, 19:03</strong></p><img src="https://secure.gravatar.com/avatar/0b5da87461395b0190a36ba3fb9d7579?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jlepore62&#39;s gravatar image" /><p>jlepore62<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jlepore62 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '15, 20:21</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43856" class="comments-container"><span id="43860"></span><div id="comment-43860" class="comment"><div id="post-43860-score" class="comment-score"></div><div class="comment-text"><p>Maybe this hepls you: <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div id="comment-43860-info" class="comment-info"><span class="comment-age">(04 Jul '15, 00:08)</span> Christian_R</div></div></div><div id="comment-tools-43856" class="comment-tools"></div><div class="clear"></div><div id="comment-43856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

