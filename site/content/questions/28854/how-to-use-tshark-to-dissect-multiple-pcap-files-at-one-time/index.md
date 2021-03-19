+++
type = "question"
title = "How to use tshark to dissect multiple pcap files at one time"
description = '''There&#x27;re multiple pcap files, I want to use tshark to dissect them at one time, how to config the input parameters?'''
date = "2014-01-13T21:46:00Z"
lastmod = "2014-01-14T06:56:00Z"
weight = 28854
keywords = [ "files", "dissect", "multiple", "tshark" ]
aliases = [ "/questions/28854" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to use tshark to dissect multiple pcap files at one time](/questions/28854/how-to-use-tshark-to-dissect-multiple-pcap-files-at-one-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28854-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>There're multiple pcap files, I want to use tshark to dissect them at one time, how to config the input parameters?</p></div><div id="question-tags" class="tags-container tags">files dissect multiple tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '14, 21:46</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p>metamatrix<br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div></div><div id="comments-container-28854" class="comments-container"></div><div id="comment-tools-28854" class="comment-tools"></div><div class="clear"></div><div id="comment-28854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28855"></span>

<div id="answer-container-28855" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28855-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't see how with tshark alone this can be achieved but you could run a mergecap before and then process the resulting file.</p><pre><code>mergecap -w merged.pcapng  trace* 
tshark -r merged.pcapng &quot;tcp.analysis.flags&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '14, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28855" class="comments-container"><span id="28893"></span><div id="comment-28893" class="comment"><div id="post-28893-score" class="comment-score"></div><div class="comment-text"><p>Thank you, mrEEde. I think mergecap is what I need, I just want a single output file with multiple input.</p></div><div id="comment-28893-info" class="comment-info"><span class="comment-age">(14 Jan '14, 18:34)</span> metamatrix</div></div></div><div id="comment-tools-28855" class="comment-tools"></div><div class="clear"></div><div id="comment-28855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28860"></span>

<div id="answer-container-28860" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28860-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>see the answers to the following questions for a scripted solution</p><p><strong>Linux</strong> (and other Unix like systems)</p><blockquote><p><a href="http://ask.wireshark.org/questions/28542/converting-multiple-pcap-files-to-csv">http://ask.wireshark.org/questions/28542/converting-multiple-pcap-files-to-csv</a></p></blockquote><p><strong>Windows</strong></p><blockquote><p><a href="http://ask.wireshark.org/questions/12799/how-to-convert-multiple-pcap-files-to-csv">http://ask.wireshark.org/questions/12799/how-to-convert-multiple-pcap-files-to-csv</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '14, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jan '14, 07:07</p></div></div><div id="comments-container-28860" class="comments-container"></div><div id="comment-tools-28860" class="comment-tools"></div><div class="clear"></div><div id="comment-28860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

