+++
type = "question"
title = "Dissecting ASCII-encoded hex"
description = '''Hello, I am trying to dissect a data format that consists of an ASCII-encoded hexadecimal sting. As an example, some data I might receive is 30 30 31 32, which corresponds to the ASCII string 0012. Does Wireshark have any way for me to perform dissection operations on the ASCII data (0012)? Thanks!'''
date = "2014-06-02T07:47:00Z"
lastmod = "2014-06-04T06:55:00Z"
weight = 33282
keywords = [ "hex", "dissector", "ascii" ]
aliases = [ "/questions/33282" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting ASCII-encoded hex](/questions/33282/dissecting-ascii-encoded-hex)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33282-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to dissect a data format that consists of an ASCII-encoded hexadecimal sting. As an example, some data I might receive is <code>30 30 31 32</code>, which corresponds to the ASCII string <code>0012</code>. Does Wireshark have any way for me to perform dissection operations on the ASCII data (<code>0012</code>)?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">hex dissector ascii</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '14, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/2973b6be28bed95434b4ee70047a5735?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burwell&#39;s gravatar image" /><p>burwell<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burwell has one accepted answer">100%</span></p></div></div><div id="comments-container-33282" class="comments-container"></div><div id="comment-tools-33282" class="comment-tools"></div><div class="clear"></div><div id="comment-33282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33376"></span>

<div id="answer-container-33376" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33376-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Figured it out. I wrote a function that converts the ASCII characters to hex and used this array to create a new <code>tvbuff_t</code>. Added the new <code>tvbuff_t</code> as a data source and used it for dissection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/2973b6be28bed95434b4ee70047a5735?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burwell&#39;s gravatar image" /><p>burwell<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burwell has one accepted answer">100%</span></p></div></div><div id="comments-container-33376" class="comments-container"></div><div id="comment-tools-33376" class="comment-tools"></div><div class="clear"></div><div id="comment-33376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33293"></span>

<div id="answer-container-33293" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33293-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure what you mean by "perform dissection operations", but in the "Packet Bytes" pane, the ASCII characters are shown in the column to the right of the HEX data.</p><p>If you are looking for a display filter to only show packets with 0012, then you can do the "contains" display filter.</p><p>For example: frame contains "0012"</p><p>or, if it is specifically in TCP data: tcp contains "0012"</p><p>Hope this helps.</p><p>Travis</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '14, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-33293" class="comments-container"></div><div id="comment-tools-33293" class="comment-tools"></div><div class="clear"></div><div id="comment-33293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

