+++
type = "question"
title = "Is there a way to save packet comment when saving file."
description = '''Hi, I&#x27;ve installed rc8.0. I&#x27;m highly interested in packet comment feature. When I add a comment to a packet and then save the file, packet comment is not saved in the file. This lack makes packet comment feature much less interesting to me. Is it planned to implement saving packet comment within fil...'''
date = "2012-06-07T00:17:00Z"
lastmod = "2012-06-07T01:49:00Z"
weight = 11730
keywords = [ "comment", "pkt_comment", "save", "rc8", "file" ]
aliases = [ "/questions/11730" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to save packet comment when saving file.](/questions/11730/is-there-a-way-to-save-packet-comment-when-saving-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11730-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've installed rc8.0. I'm highly interested in packet comment feature. When I add a comment to a packet and then save the file, packet comment is not saved in the file. This lack makes packet comment feature much less interesting to me.</p><p>Is it planned to implement saving packet comment within file?</p></div><div id="question-tags" class="tags-container tags">comment pkt_comment save rc8 file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '12, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/440d27c4988bedf7343769132b5de7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="C%20Pietquin&#39;s gravatar image" /><p>C Pietquin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="C Pietquin has no accepted answers">0%</span></p></div></div><div id="comments-container-11730" class="comments-container"></div><div id="comment-tools-11730" class="comment-tools"></div><div class="clear"></div><div id="comment-11730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11732"></span>

<div id="answer-container-11732" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11732-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, is it that you did not save it in the new pcap file format "<em>.pcapng", because the older</em> .pcap does not save comments..?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '12, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-11732" class="comments-container"><span id="11734"></span><div id="comment-11734" class="comment"><div id="post-11734-score" class="comment-score"></div><div class="comment-text"><p>You're right.</p><p>I've also changed Capture preference by activating "Capture packets in pcap-ng format". That makes pcap-ng the default file format.</p><p>Many thanks for your quick answer.</p></div><div id="comment-11734-info" class="comment-info"><span class="comment-age">(07 Jun '12, 02:06)</span> C Pietquin</div></div><span id="11736"></span><div id="comment-11736" class="comment"><div id="post-11736-score" class="comment-score">1</div><div class="comment-text"><p>I believe that the new version picked up on your existing preferences when you installed it. A clean install (or one where you opt to remove personal preferences when upgrading) will have pcap-ng as the default file format.</p></div><div id="comment-11736-info" class="comment-info"><span class="comment-age">(07 Jun '12, 04:28)</span> grahamb ♦</div></div><span id="11739"></span><div id="comment-11739" class="comment"><div id="post-11739-score" class="comment-score"></div><div class="comment-text"><p>The fix for <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7222">bug 7222</a> will also, once implemented, make it obvious to users if they are trying to save to a capture file format that doesn't support comments.</p></div><div id="comment-11739-info" class="comment-info"><span class="comment-age">(07 Jun '12, 06:50)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-11732" class="comment-tools"></div><div class="clear"></div><div id="comment-11732-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

