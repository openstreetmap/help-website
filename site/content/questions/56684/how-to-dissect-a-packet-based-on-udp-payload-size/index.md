+++
type = "question"
title = "how to Dissect a packet based on UDP payload size"
description = '''Hi  I am writing a dissector for a protocol which runs on top of UDP. 2 kinds of packets i can expect  1) with payload length 64Bytes  2) with payload length 16Bytes. I want to identify packet based on this. How can i do this? any example code is appreciated. regards sandeep'''
date = "2016-10-26T05:08:00Z"
lastmod = "2016-10-26T23:24:00Z"
weight = 56684
keywords = [ "on", "length", "dissection", "based", "payload" ]
aliases = [ "/questions/56684" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to Dissect a packet based on UDP payload size](/questions/56684/how-to-dissect-a-packet-based-on-udp-payload-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56684-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am writing a dissector for a protocol which runs on top of UDP.</p><p>2 kinds of packets i can expect 1) with payload length 64Bytes 2) with payload length 16Bytes.</p><p>I want to identify packet based on this.</p><p>How can i do this? any example code is appreciated.</p><p>regards sandeep</p></div><div id="question-tags" class="tags-container tags">on length dissection based payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '16, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/41e40bb12df6d7a84466fd7dcbf6cd26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sandyp&#39;s gravatar image" /><p>sandyp<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sandyp has no accepted answers">0%</span></p></div></div><div id="comments-container-56684" class="comments-container"><span id="56686"></span><div id="comment-56686" class="comment"><div id="post-56686-score" class="comment-score"></div><div class="comment-text"><p>What are you using for your dissector, C or Lua or something else? Are there any header bytes in your protocol that would allow you to differentiate on values rather than length?</p></div><div id="comment-56686-info" class="comment-info"><span class="comment-age">(26 Oct '16, 05:32)</span> grahamb ♦</div></div><span id="56723"></span><div id="comment-56723" class="comment"><div id="post-56723-score" class="comment-score"></div><div class="comment-text"><p>@grahamb I am using C. There is no such thing in my protocol header that tells the size. But it is known that the server always sends 16byte message and client always sends 64byte message.... If we can parse source and destination address of UDP packet, that also should be fine.</p></div><div id="comment-56723-info" class="comment-info"><span class="comment-age">(26 Oct '16, 22:22)</span> sandyp</div></div><span id="56724"></span><div id="comment-56724" class="comment"><div id="post-56724-score" class="comment-score"></div><div class="comment-text"><p>@sandyp Maybe you can register your dissector in the udp table to do a "decode-as" and then use tvb_captured_length() and use that check the length of the packet in order to process it some way?</p></div><div id="comment-56724-info" class="comment-info"><span class="comment-age">(26 Oct '16, 22:48)</span> koundi</div></div></div><div id="comment-tools-56684" class="comment-tools"></div><div class="clear"></div><div id="comment-56684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56727"></span>

<div id="answer-container-56727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56727-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should use <code>tvb_reported_length()</code>, that will be the original packet size on the wire regardless of whether the capture sliced the packet.</p><p>You can get access to the source and destination addresses via the pinfo parameter to your dissection function. See <code>epan/packet_info.h</code> for all the members of pinfo.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '16, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56727" class="comments-container"><span id="56732"></span><div id="comment-56732" class="comment"><div id="post-56732-score" class="comment-score"></div><div class="comment-text"><p>hi @grahamb wont using tvb_reported_length be a riskier move. If the packet is not complete then the dissector might run into exception if not very careful correct? Can you please tell us which is safer captured_length vs reported_length?</p></div><div id="comment-56732-info" class="comment-info"><span class="comment-age">(27 Oct '16, 02:51)</span> koundi</div></div><span id="56734"></span><div id="comment-56734" class="comment"><div id="post-56734-score" class="comment-score">1</div><div class="comment-text"><p>That's kind of the whole point of tvb's, they are a testable virtual buffer that safely handle attempts to access beyond their actual length.</p><p>In general, dissectors should use reported length, and if they do run off the end of the tvb, it will be correctly reported as a malformed packet.</p></div><div id="comment-56734-info" class="comment-info"><span class="comment-age">(27 Oct '16, 03:46)</span> grahamb ♦</div></div><span id="56736"></span><div id="comment-56736" class="comment"><div id="post-56736-score" class="comment-score">1</div><div class="comment-text"><p>You should use tvb_reported_length() to distinguish the two packet types, and may use tvb_captured_length to prevent trying to access data beyond the available buffer (which in itself isn't harmful, as the TVB access functions guard for that).</p></div><div id="comment-56736-info" class="comment-info"><span class="comment-age">(27 Oct '16, 05:15)</span> Jaap ♦</div></div></div><div id="comment-tools-56727" class="comment-tools"></div><div class="clear"></div><div id="comment-56727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

