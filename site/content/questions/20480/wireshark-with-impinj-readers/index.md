+++
type = "question"
title = "Wireshark with Impinj readers"
description = '''How would Wireshark be used to capture RFID tag data from the Impinj Speedway Revolution R420 or R220 in order to write it out to a database or send it to the cloud?'''
date = "2013-04-16T14:29:00Z"
lastmod = "2013-04-16T15:50:00Z"
weight = 20480
keywords = [ "capture", "data", "impinj", "output" ]
aliases = [ "/questions/20480" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with Impinj readers](/questions/20480/wireshark-with-impinj-readers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20480-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How would Wireshark be used to capture RFID tag data from the Impinj Speedway Revolution R420 or R220 in order to write it out to a database or send it to the cloud?</p></div><div id="question-tags" class="tags-container tags">capture data impinj output</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/c908b5ecb708fa712f900858aaf7a2c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vimpinj&#39;s gravatar image" /><p>vimpinj<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vimpinj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '13, 14:47</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20480" class="comments-container"></div><div id="comment-tools-20480" class="comment-tools"></div><div class="clear"></div><div id="comment-20480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20485"></span>

<div id="answer-container-20485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20485-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is able to decode the <a href="http://rfidwikipedia.org/index.php/Low_Level_Reader_Protocol_%28LLRP%29">LLRP protocol</a>. So, if you have a client that talks to the RFID reader via LLRP, you would be able to capture and analyze that traffic with Wireshark (<a href="http://wiki.wireshark.org/LLRP">http://wiki.wireshark.org/LLRP</a> ). If the client does <strong>not</strong> use LLRP, there is no way to capture that communication with Wireshark.</p><p>With tshark, you can also export the RFID tag (EPC code) from the LLRP messages:</p><blockquote><p><code>tshark -nr llrp.cap -R "llrp.param.epc" -T fields -e llrp.param.epc</code><br />
</p></blockquote><p>Sample output:</p><pre><code>00:00:00:00:00:00:00:00:00:00:00:f1,e2:00:34:11:b8:02:01:14:12:25:32:71,00:00:90:00:b8:02:01:14:12:25:32:76,e2:00:34:11:b8:02:01:14:12:25:32
:42,30:34:12:5b:b0:24:c3:41:23:45:67:89,e2:00:90:00:17:10:02:39:17:80:5f:1f,00:00:90:00:b8:02:01:14:12:25:32:76,00:00:00:00:00:00:00:00:00:0
0:00:f1,e2:00:34:11:b8:02:01:14:12:25:32:71,30:34:12:5b:b0:24:c3:41:23:45:67:89,e2:00:90:00:17:10:02:39:17:80:5f:1f</code></pre><p>The tags are separated by a comma (,).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '13, 16:06</p></div></div><div id="comments-container-20485" class="comments-container"></div><div id="comment-tools-20485" class="comment-tools"></div><div class="clear"></div><div id="comment-20485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

