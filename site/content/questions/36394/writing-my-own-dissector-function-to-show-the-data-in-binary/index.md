+++
type = "question"
title = "writing my own dissector - function to show the data in binary"
description = '''Hello, I am writing my own wireshark dissector and I have one short question: Is there any function in wireshark, which turns an array of bytes into a string, showing the bytes in binary? I know that there are functions, showing the data in hex format, but I cannot find anything analogical with bina...'''
date = "2014-09-17T01:17:00Z"
lastmod = "2014-10-22T08:53:00Z"
weight = 36394
keywords = [ "binary", "dissector", "string" ]
aliases = [ "/questions/36394" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [writing my own dissector - function to show the data in binary](/questions/36394/writing-my-own-dissector-function-to-show-the-data-in-binary)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36394-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am writing my own wireshark dissector and I have one short question:</p><p>Is there any function in wireshark, which turns an array of bytes into a string, showing the bytes in binary? I know that there are functions, showing the data in hex format, but I cannot find anything analogical with binary.</p></div><div id="question-tags" class="tags-container tags">binary dissector string</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '14, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/4cb7b7ac61efaded7749985daff28985?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magda%20Nowak-Trzos&#39;s gravatar image" /><p>Magda Nowak-...<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magda Nowak-Trzos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Sep '14, 01:34</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-36394" class="comments-container"><span id="36420"></span><div id="comment-36420" class="comment"><div id="post-36420-score" class="comment-score"></div><div class="comment-text"><p>I.e., you'd want to take a sequence of byte values such as 0xFE 0xED 0xFA 0xCE 0xDE 0xAD 0xBE 0xEF and turn it into a text string such as "FEEDFACEDEADBEEF" or "FE:ED:FA:CE:DE:AD:BE:EF"?</p></div><div id="comment-36420-info" class="comment-info"><span class="comment-age">(17 Sep '14, 12:52)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-36394" class="comment-tools"></div><div class="clear"></div><div id="comment-36394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37291"></span>

<div id="answer-container-37291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37291-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you mean to take an array of bytes like 0xFE 0xED and turning it into a text string like "1111111011101101". I'm virtually certain there's no function in Wireshark to do that today--not many people want to see that many bytes in binary.</p><p>Note that if you have a particular field (e.g., an FT_UINT32) and you provide a bitmask (in the hf definition) then Wireshark will show the bit values in the field decode; you can see this in the decode of the TCP Flags:</p><pre><code>.... 0000 0000 0010 = Flags: 0x002 (SYN)
    000. .... .... = Reserved: Not set
    ...0 .... .... = Nonce: Not set
    .... 0... .... = Congestion Window Reduced (CWR): Not set</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37291" class="comments-container"></div><div id="comment-tools-37291" class="comment-tools"></div><div class="clear"></div><div id="comment-37291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

