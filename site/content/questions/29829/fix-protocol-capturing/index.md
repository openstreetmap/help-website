+++
type = "question"
title = "FIX protocol capturing"
description = '''Hello, Is it possible to capture in tshark the dump which:  contains FIX protocol packets only capturing without decoding  If yes, which capture-filter needs to be applied?  Thanks in advance!'''
date = "2014-02-13T05:51:00Z"
lastmod = "2014-02-13T12:15:00Z"
weight = 29829
keywords = [ "fix", "capture-filter", "tshark" ]
aliases = [ "/questions/29829" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [FIX protocol capturing](/questions/29829/fix-protocol-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29829-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is it possible to capture in tshark the dump which:</p><ul><li>contains FIX protocol packets only</li><li>capturing without decoding</li></ul><p>If yes, which capture-filter needs to be applied?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">fix capture-filter tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '14, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/00fc9b7ddbee4ec657351cff07ace3ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrav&#39;s gravatar image" /><p>mrav<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrav has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '14, 06:10</p></div></div><div id="comments-container-29829" class="comments-container"></div><div id="comment-tools-29829" class="comment-tools"></div><div class="clear"></div><div id="comment-29829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29837"></span>

<div id="answer-container-29837" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29837-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Every FIX message starts with the string '8=FIX', followed by a version number. So, you need to filter for that string.</p><p>This can be done with a simple <strong>capture filter</strong>, like the following:</p><blockquote><p>tcpdump -ni eth0 'host 1.2.3.4 and tcp[20:4]=0x383D4649 and tcp[24:1]=0x58' -w fix.pcap<br />
dumpcap -ni eth0 'host 1.2.3.4 and tcp[20:4]=0x383D4649 and tcp[24:1]=0x58' -w fix.pcap<br />
</p></blockquote><p><strong>HOWEVER</strong>: That will only work, if there are not TCP options. If there are options, you must adjust the offest [20:4], according to the bytes consumed by the TCP header options. <strong>And</strong> if some implementation does not adhere fully to the standard, and uses lower case letters (8=fix), the capture filter won't work, as it only matches upper case letters.</p><p>As that's kind of odd, there is a better/simpler way.</p><p><strong>ngrep:</strong></p><blockquote><p>ngrep -d eth0 -i '8=FIX' 'host 1.2.3.4 and tcp' -O fix.pcap</p></blockquote><p>Ngrep will search for the string '8=FIX' (-i is ignore case) in any tcp frame from/to 1.2.3.4 (replace that with the IP address in your environment). Every matching frame will be written to fix.pcap.</p><p>Regards<br />
Kurt<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '14, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '14, 02:21</p></div></div><div id="comments-container-29837" class="comments-container"></div><div id="comment-tools-29837" class="comment-tools"></div><div class="clear"></div><div id="comment-29837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

