+++
type = "question"
title = "Capturing the packets of two (not all) interfaces // tshark"
description = '''Hello! tshark -D 1. eth0 2. eth2 3. eth3 4. any (Pseudo-device that captures on all interfaces) 5. lo  Capturing the packets of eth2 and eth3 only is needed with the aid tshark. How I can make it?'''
date = "2013-07-30T21:31:00Z"
lastmod = "2013-07-31T01:30:00Z"
weight = 23456
keywords = [ "two_interfaces", "tshark", "capturing" ]
aliases = [ "/questions/23456" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing the packets of two (not all) interfaces // tshark](/questions/23456/capturing-the-packets-of-two-not-all-interfaces-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23456-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><pre><code>tshark -D
1. eth0
2. eth2
3. eth3
4. any (Pseudo-device that captures on all interfaces)
5. lo</code></pre><p>Capturing the packets of eth2 and eth3 only is needed with the aid tshark. How I can make it?</p></div><div id="question-tags" class="tags-container tags">two_interfaces tshark capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '13, 21:31</strong></p><img src="https://secure.gravatar.com/avatar/d7ebdfa64a88154cd163c7cc781e4315?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="factorial&#39;s gravatar image" /><p>factorial<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="factorial has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Jul '13, 01:20</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23456" class="comments-container"></div><div id="comment-tools-23456" class="comment-tools"></div><div class="clear"></div><div id="comment-23456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23461"></span>

<div id="answer-container-23461" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23461-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Install Wireshark 1.8 or later if Wireshark isn't installed or if an earlier version of Wireshark is installed, and then do</p><pre><code>tshark -i eth2 -i eth3 {other tshark command-line arguments}</code></pre><p>If you want to specify a capture filter for all interfaces, specify <code>-f {filter}</code> before all the <code>-i</code> arguments. If you want to specify a capture filter or filters for some but not all interfaces, specify <code>-f {filter}</code> after the <code>-i</code> argument for the interface on which the capture filter <code>{filter}</code> should be used.</p><p>NOTE: "Install Wireshark 1.8 or later if Wireshark isn't installed or if an earlier version of Wireshark is installed" is an important step; multiple <code>-i</code> arguments, and capturing on multiple interfaces at once, is <em>NOT</em> supported in Wireshark 1.6.x or earlier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '13, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23461" class="comments-container"><span id="23466"></span><div id="comment-23466" class="comment"><div id="post-23466-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I tried twice -i:</p><pre><code>  tshark -v 
  TShark 1.2.11
  tshark -i eth2 -i eth3 -w test.pcap
  Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
  Capturing on eth3...
  ...</code></pre><p>The capturing implemented just interface eth3.</p></div><div id="comment-23466-info" class="comment-info"><span class="comment-age">(31 Jul '13, 01:44)</span> factorial</div></div><span id="23468"></span><div id="comment-23468" class="comment"><div id="post-23468-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a "comment", please see the FAQ.</p><p>Guy's disclaimer:</p><blockquote><p>NOTE: "Install Wireshark 1.8 or later if Wireshark isn't installed or if an earlier version of Wireshark is installed" is an important step; multiple -i arguments, and capturing on multiple interfaces at once, is NOT supported in Wireshark 1.6.x or earlier.</p></blockquote><p>Your version:</p><blockquote><p>TShark 1.2.11</p></blockquote><p>Please upgrade your Wireshark installation (Tshark is part of Wireshark and uses the same version numbering)</p></div><div id="comment-23468-info" class="comment-info"><span class="comment-age">(31 Jul '13, 01:49)</span> SYN-bit ♦♦</div></div><span id="23469"></span><div id="comment-23469" class="comment"><div id="post-23469-score" class="comment-score"></div><div class="comment-text"><p>Ok! Thanks once more!</p></div><div id="comment-23469-info" class="comment-info"><span class="comment-age">(31 Jul '13, 01:54)</span> factorial</div></div></div><div id="comment-tools-23461" class="comment-tools"></div><div class="clear"></div><div id="comment-23461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

