+++
type = "question"
title = "How can I capture traffic in Android and convert pcap file to a plain text file like Wireshark does ?"
description = '''I want to capture traffic in a Android phone using tcpdump in Terminal Emulator, and convert pcap file obtained to a plain text file. Does anyone know how can i do it. Thanks'''
date = "2015-07-24T07:17:00Z"
lastmod = "2015-07-24T11:50:00Z"
weight = 44431
keywords = [ "pcap", "android", "tcpdump", "plain-text" ]
aliases = [ "/questions/44431" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I capture traffic in Android and convert pcap file to a plain text file like Wireshark does ?](/questions/44431/how-can-i-capture-traffic-in-android-and-convert-pcap-file-to-a-plain-text-file-like-wireshark-does)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44431-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture traffic in a Android phone using tcpdump in Terminal Emulator, and convert pcap file obtained to a plain text file. Does anyone know how can i do it. Thanks</p></div><div id="question-tags" class="tags-container tags">pcap android tcpdump plain-text</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/3ff5f5b5b44acf16d015bcb42f0506cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miguel%20Freitas&#39;s gravatar image" /><p>Miguel Freitas<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miguel Freitas has no accepted answers">0%</span></p></div></div><div id="comments-container-44431" class="comments-container"></div><div id="comment-tools-44431" class="comment-tools"></div><div class="clear"></div><div id="comment-44431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44443"></span>

<div id="answer-container-44443" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44443-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Use tcpdump to read the pcap file, without <code>-w</code>; that will print it as a plain-text file in tcpdump's print format.</li><li>Get TShark ported to Android, and read the file with it and the appropriate command-line arguments, such as <code>-V</code>.</li><li>Write your own program to duplicate what tcpdump or TShark does.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44443" class="comments-container"><span id="44450"></span><div id="comment-44450" class="comment"><div id="post-44450-score" class="comment-score"></div><div class="comment-text"><p>My goal is convert a given pcap file in a plain text file with details of all packet, using a Android phone. Do you know how can I install TShark on my Android phone?</p></div><div id="comment-44450-info" class="comment-info"><span class="comment-age">(24 Jul '15, 13:36)</span> Miguel Freitas</div></div><span id="44452"></span><div id="comment-44452" class="comment"><div id="post-44452-score" class="comment-score">1</div><div class="comment-text"><p>A quick Web search for "tshark android" didn't find anything. You might have to be the first person to port it, which would involve porting, at minimum, the GLib library (not glibc, this is a library used by GTK+ and also used by non-GUI programs such as TShark and the packet-dissection libraries it uses).</p></div><div id="comment-44452-info" class="comment-info"><span class="comment-age">(24 Jul '15, 14:28)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-44443" class="comment-tools"></div><div class="clear"></div><div id="comment-44443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

