+++
type = "question"
title = "How to print packet summary lines to a file in plain text format using WireShark2 ?"
description = '''How can I print packet summary lines to a file in plain text format using WireShark2.0.3 ? ( I need this functionality because I have some scripts to reformat plain text format print result )'''
date = "2016-05-28T02:59:00Z"
lastmod = "2016-05-28T07:37:00Z"
weight = 53024
keywords = [ "print", "wireshark2" ]
aliases = [ "/questions/53024" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to print packet summary lines to a file in plain text format using WireShark2 ?](/questions/53024/how-to-print-packet-summary-lines-to-a-file-in-plain-text-format-using-wireshark2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53024-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I print packet summary lines to a file in plain text format using WireShark2.0.3 ? ( I need this functionality because I have some scripts to reformat plain text format print result )</p></div><div id="question-tags" class="tags-container tags">print wireshark2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '16, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/a576f16d8362054cdef3246ee28a4d18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maimai&#39;s gravatar image" /><p>maimai<br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maimai has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 May '16, 03:08</p></div></div><div id="comments-container-53024" class="comments-container"><span id="53025"></span><div id="comment-53025" class="comment"><div id="post-53025-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "summary line". Please add an example of output your would like.</p><p>Have you looked at <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark</a>, the command line version of Wireshark that produces text output by default?</p></div><div id="comment-53025-info" class="comment-info"><span class="comment-age">(28 May '16, 03:38)</span> grahamb ♦</div></div><span id="53030"></span><div id="comment-53030" class="comment"><div id="post-53030-score" class="comment-score"></div><div class="comment-text"><p>"Packet summary line" means a contents of packet list pane (as displayed), and I use this term because WireShark1.12's print dialog use this term. Though I know tshark can print text output , WireShark is suitable for interactive packet selection , so I prefer WireShark to tshark. (If I use tshark only for printing interesting packet , I should write filter expression twice when I want to keep Frame.Number unchanged)</p></div><div id="comment-53030-info" class="comment-info"><span class="comment-age">(28 May '16, 18:01)</span> maimai</div></div></div><div id="comment-tools-53024" class="comment-tools"></div><div class="clear"></div><div id="comment-53024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53027"></span>

<div id="answer-container-53027" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53027-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the GUI I think you're looking for the "File-&gt;Export Specified Dissections" menu item. Once there select "As Plain Text...". Then, under "Packet Format" make sure only "Summary line" is selected (this basically means de-selecting "Packet Details").</p><p>Of course, as Graham points out, tshark would be more amenable to scripting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '16, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-53027" class="comments-container"><span id="53029"></span><div id="comment-53029" class="comment"><div id="post-53029-score" class="comment-score"></div><div class="comment-text"><p>Thanks. This is what I was looking for. I was not aware of "File-&gt;Export Packet Dissections" can be used for my purpose since WireShark1.12. In WireShark1.12 , "File-&gt;Print" shows a dialog with "Printer 'as plain text' and Output to file" and I used to use this GUI. (I guess very old WireShark does not has "File-&gt;Export Packet Dissections" GUI)</p></div><div id="comment-53029-info" class="comment-info"><span class="comment-age">(28 May '16, 17:49)</span> maimai</div></div><span id="53031"></span><div id="comment-53031" class="comment"><div id="post-53031-score" class="comment-score"></div><div class="comment-text"><p>Cool, glad that helped. (A bunch of functions were moved around in Wireshark 2 to, well, make more sense. But sometimes it's hard to find them.)</p><p>BTW since this appears to have answered your question please "accept" the answer by clicking on the checkbox next to the answer--that way your question won't show up in the list of unanswered questions, for example.</p></div><div id="comment-53031-info" class="comment-info"><span class="comment-age">(28 May '16, 18:10)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-53027" class="comment-tools"></div><div class="clear"></div><div id="comment-53027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

