+++
type = "question"
title = "How to save only http packets in a pcap file ?"
description = '''Using wireshark, can I save just the http packets to a pcap file. My capture stream consists of a large number of packets, out which only 10% are http packets. I want to save only HTTP packets to the pcap file by applying some sort of filter before saving the file.'''
date = "2015-06-18T14:32:00Z"
lastmod = "2015-06-18T14:39:00Z"
weight = 43346
keywords = [ "pcap", "wireshark" ]
aliases = [ "/questions/43346" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to save only http packets in a pcap file ?](/questions/43346/how-to-save-only-http-packets-in-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43346-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using wireshark, can I save just the http packets to a pcap file. My capture stream consists of a large number of packets, out which only 10% are http packets. I want to save only HTTP packets to the pcap file by applying some sort of filter before saving the file.</p></div><div id="question-tags" class="tags-container tags">pcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '15, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/4541634d61685ddb3a8aa77299713c7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Backspace&#39;s gravatar image" /><p>Backspace<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Backspace has no accepted answers">0%</span></p></div></div><div id="comments-container-43346" class="comments-container"></div><div id="comment-tools-43346" class="comment-tools"></div><div class="clear"></div><div id="comment-43346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43347"></span>

<div id="answer-container-43347" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43347-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>you could filter on "http" to get all packets that Wireshark considers to be HTTP, and then use "Export specified packets" to save only the currently displayed packets to a new file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '15, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-43347" class="comments-container"></div><div id="comment-tools-43347" class="comment-tools"></div><div class="clear"></div><div id="comment-43347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

