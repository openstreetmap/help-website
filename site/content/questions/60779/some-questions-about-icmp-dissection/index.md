+++
type = "question"
title = "Some questions about ICMP dissection"
description = '''Version 2.2.5 (v2.2.5-0-g440fd4d) icmp.ident Identifier (BE) Unsigned integer, 2 bytes 1.0.0 to 2.2.5 icmp.seq Sequence number (BE) Unsigned integer, 2 bytes 1.0.0 to 2.2.5 icmp.seq_le Sequence number (LE) Unsigned integer, 2 bytes 1.4.0 to 2.2.5   When added as a column: icmp.seq and icmp.seq_le di...'''
date = "2017-04-12T13:11:00Z"
lastmod = "2017-04-15T17:45:00Z"
weight = 60779
keywords = [ "icmp" ]
aliases = [ "/questions/60779" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Some questions about ICMP dissection](/questions/60779/some-questions-about-icmp-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60779-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Version 2.2.5 (v2.2.5-0-g440fd4d)<br />
icmp.ident Identifier (BE) Unsigned integer, 2 bytes 1.0.0 to 2.2.5<br />
icmp.seq Sequence number (BE) Unsigned integer, 2 bytes 1.0.0 to 2.2.5<br />
icmp.seq_le Sequence number (LE) Unsigned integer, 2 bytes 1.4.0 to 2.2.5</p><ol><li>When added as a column: icmp.seq and icmp.seq_le display two bytes and only one copy (be/le) which is properly formatted. icmp.ident displays both be and le in the same column</li><li>None of them seem to sort properly when column header clicked in 2.2.5</li><li>Is the ICMP dissector in a dll/binary or is there an ASCII file with its config?</li></ol></div><div id="question-tags" class="tags-container tags">icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '17, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/7294965538dc8dedd784550d9cb4f1a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bubbasnmp&#39;s gravatar image" /><p>bubbasnmp<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bubbasnmp has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Apr '17, 15:24</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></br></p></div></div><div id="comments-container-60779" class="comments-container"><span id="60780"></span><div id="comment-60780" class="comment"><div id="post-60780-score" class="comment-score"></div><div class="comment-text"><p>This isn't really an answer but a related question.</p></div><div id="comment-60780-info" class="comment-info"><span class="comment-age">(12 Apr '17, 13:12)</span> bubbasnmp</div></div><span id="60851"></span><div id="comment-60851" class="comment"><div id="post-60851-score" class="comment-score"></div><div class="comment-text"><p>And, therefore, it was converted into a question. This is a Q&amp;A site, so each question should be a separate item; questions, whether related or not, should be asked separately.</p></div><div id="comment-60851-info" class="comment-info"><span class="comment-age">(15 Apr '17, 15:25)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-60779" class="comment-tools"></div><div class="clear"></div><div id="comment-60779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60854"></span>

<div id="answer-container-60854" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60854-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-icmp.c;h=7f59b9917b8d568f791624a2bb23a8232339c42b;hb=HEAD">This</a> is the source code for the ICMP dissector. When compiled, it is part of libwireshark.dll.</p><p>Regarding the ICMP sequence number fields, since some OS's use use big-endian and others use little-endian for the ICMP multi-byte fields, two different filters exist, <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-icmp.c;h=7f59b9917b8d568f791624a2bb23a8232339c42b;hb=HEAD#l1647"><code>icmp.seq</code></a> in case it's big-endian and <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-icmp.c;h=7f59b9917b8d568f791624a2bb23a8232339c42b;hb=HEAD#l1652"><code>icmp.seq_le</code></a> in case it's little-endian. There is no reliable way to know which format the field is in, so both filters are available, and it's left up to the user to determine which one is correct. Both fields are declared as <code>BASE_DEC_HEX</code>, so they're displayed in both decimal and hexadecimal formats. I'm honestly not entirely sure how useful it is to display these fields in hexadecimal, but that's the way the dissector is currently written.</p><p>The situation is similar for <code>icmp.ident</code>; however, there appears to be a bug in the source code because both <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-icmp.c;h=7f59b9917b8d568f791624a2bb23a8232339c42b;hb=HEAD#l1637"><code>hf_icmp_ident</code></a> and <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-icmp.c;h=7f59b9917b8d568f791624a2bb23a8232339c42b;hb=HEAD#l1642"><code>hf_icmp_ident_le</code></a> use the same <code>icmp.ident</code> filter. This is the reason why the <code>icmp.ident</code> column displays both of them in the same column. I would suggest opening a <a href="https://bugs.wireshark.org/bugzilla/">Wireshark bug</a> to report this inconsistency and ask for <code>hf_icmp_ident_le</code> to use a separate <code>icmp.ident_le</code> filter, just like <code>icmp.seq_le</code> is used for <code>hf_icmp_seq_num_le</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '17, 17:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-60854" class="comments-container"><span id="64345"></span><div id="comment-64345" class="comment"><div id="post-64345-score" class="comment-score"></div><div class="comment-text"><p>Fixed: <a href="https://gitlab.com/wireshark/wireshark/-/merge_requests/1082">https://gitlab.com/wireshark/wireshark/-/merge_requests/1082</a></p><p>Notes: <a href="https://gitlab.com/wireshark/wireshark/-/issues/17045">https://gitlab.com/wireshark/wireshark/-/issues/17045</a></p></div><div id="comment-64345-info" class="comment-info"><span class="comment-age">(30 Nov '20, 13:21)</span> bubbasnmp</div></div></div><div id="comment-tools-60854" class="comment-tools"></div><div class="clear"></div><div id="comment-60854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

