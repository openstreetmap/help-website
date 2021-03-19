+++
type = "question"
title = "How do I determine a TCP segment&#x27;s length"
description = '''How do I determine a TCP segment&#x27;s length - Header length + No. Bytes in flight?'''
date = "2011-05-22T20:49:00Z"
lastmod = "2014-09-04T02:46:00Z"
weight = 4178
keywords = [ "segment", "tcp" ]
aliases = [ "/questions/4178" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I determine a TCP segment's length](/questions/4178/how-do-i-determine-a-tcp-segments-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4178-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I determine a TCP segment's length - Header length + No. Bytes in flight?</p></div><div id="question-tags" class="tags-container tags">segment tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '11, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/cc48a4a27244cd1ec37ccee4c7187e27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaden&#39;s gravatar image" /><p>jaden<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaden has no accepted answers">0%</span></p></div></div><div id="comments-container-4178" class="comments-container"></div><div id="comment-tools-4178" class="comment-tools"></div><div class="clear"></div><div id="comment-4178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4183"></span>

<div id="answer-container-4183" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4183-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP payload size is calculated by taking the "Total Length" from the IP header (ip.len) and then substract the "IP header length" (ip.hdr_len) and the "TCP header length" (tcp.hdr_len).</p><p>The "Bytes in Flight" field shows the amount of data that has been sent, but not yet ACKed (seen from the perspective of the point of capture).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '11, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4183" class="comments-container"></div><div id="comment-tools-4183" class="comment-tools"></div><div class="clear"></div><div id="comment-4183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4180"></span>

<div id="answer-container-4180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4180-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can add columns by right-clicking the fields in the Packet Details pane and select "Apply as Column" from the context menu:<br />
tcp.len<br />
tcp.hdr_len<br />
tcp.analysis.bytes_in_flight<br />
</p><p><a href="http://www.lovemytool.com/blog/2011/05/wireshark-151-add-and-customize-columns-by-joke-snelders.html">Here</a> you can read more about adding and customizing columns.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '11, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '11, 21:16</p></div></div><div id="comments-container-4180" class="comments-container"></div><div id="comment-tools-4180" class="comment-tools"></div><div class="clear"></div><div id="comment-4180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35997"></span>

<div id="answer-container-35997" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35997-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>tcp.len <a href="https://www.wireshark.org/docs/dfref/t/tcp.html">https://www.wireshark.org/docs/dfref/t/tcp.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '14, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/11ec440092c588bc95d4618e6e889f01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jayjair&#39;s gravatar image" /><p>jayjair<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jayjair has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-35997" class="comments-container"></div><div id="comment-tools-35997" class="comment-tools"></div><div class="clear"></div><div id="comment-35997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

