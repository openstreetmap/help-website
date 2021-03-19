+++
type = "question"
title = "Protocol Statistics and TCP Dissector Reassembly - Possible Bug?"
description = '''Hallo, I was just examining some traffic and I noticed that whether or not the TCP Dissector Reassembles packets, the TCP packets of a HTTP Conversation do not show up as HTTP Traffic. I kinda remembered from WNA Study Guide that this should not be the case so I went back and looked (Chapter 8: Iden...'''
date = "2014-11-12T01:21:00Z"
lastmod = "2014-11-12T05:05:00Z"
weight = 37777
keywords = [ "reassembly", "statistics" ]
aliases = [ "/questions/37777" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Protocol Statistics and TCP Dissector Reassembly - Possible Bug?](/questions/37777/protocol-statistics-and-tcp-dissector-reassembly-possible-bug)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37777-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hallo,</p><p>I was just examining some traffic and I noticed that whether or not the TCP Dissector Reassembles packets, the TCP packets of a HTTP Conversation do not show up as HTTP Traffic. I kinda remembered from WNA Study Guide that this should not be the case so I went back and looked (Chapter 8: Identify Network Protocols and Applications) Even though they are seen as HTTP when disabling the reassembly Setting, they are not listed as HTTP under the Statistics. I am PRETTY (not 100% though) sure that when I went through this with a previous version of Wireshark it worked according to the Study Guide? Can anyone else confirm this? I even loaded the File from the guide that also only shows a maximum of 16% http, not 95% as shown in the book..</p><p>Darren</p></div><div id="question-tags" class="tags-container tags">reassembly statistics</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '14, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-37777" class="comments-container"></div><div id="comment-tools-37777" class="comment-tools"></div><div class="clear"></div><div id="comment-37777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37787"></span>

<div id="answer-container-37787" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37787-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using version 1.12.0 or 1.12.1? Those versions have problems with the HTTP dissector and do not always properly identify HTTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '14, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-37787" class="comments-container"><span id="37808"></span><div id="comment-37808" class="comment"><div id="post-37808-score" class="comment-score"></div><div class="comment-text"><p>I Just updated to 1.12.2, It's working again now? Will mark as answered</p></div><div id="comment-37808-info" class="comment-info"><span class="comment-age">(13 Nov '14, 01:49)</span> DarrenWright</div></div><span id="37940"></span><div id="comment-37940" class="comment"><div id="post-37940-score" class="comment-score"></div><div class="comment-text"><p>Just noticed I marked the worng answer..</p></div><div id="comment-37940-info" class="comment-info"><span class="comment-age">(18 Nov '14, 02:31)</span> DarrenWright</div></div><span id="37944"></span><div id="comment-37944" class="comment"><div id="post-37944-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-37944-info" class="comment-info"><span class="comment-age">(18 Nov '14, 03:35)</span> grahamb ♦</div></div></div><div id="comment-tools-37787" class="comment-tools"></div><div class="clear"></div><div id="comment-37787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

