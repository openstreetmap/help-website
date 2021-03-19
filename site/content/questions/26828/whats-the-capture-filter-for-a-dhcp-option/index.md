+++
type = "question"
title = "What&#x27;s the capture filter for a DHCP option?"
description = '''What&#x27;s the capture filter equivalent to the display filter &quot;(bootp.option.type == 53)&quot; for DHCP?'''
date = "2013-11-10T18:25:00Z"
lastmod = "2013-11-11T07:55:00Z"
weight = 26828
keywords = [ "filter", "dhcp" ]
aliases = [ "/questions/26828" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What's the capture filter for a DHCP option?](/questions/26828/whats-the-capture-filter-for-a-dhcp-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26828-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What's the capture filter equivalent to the display filter "(bootp.option.type == 53)" for DHCP?</p></div><div id="question-tags" class="tags-container tags">filter dhcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '13, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p>metamatrix<br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Nov '13, 07:52</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-26828" class="comments-container"></div><div id="comment-tools-26828" class="comment-tools"></div><div class="clear"></div><div id="comment-26828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26843"></span>

<div id="answer-container-26843" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26843-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The order of option 53 in the frame, and with that the position, is unknown. As <strong><a href="http://wiki.wireshark.org/CaptureFilters">capture filters</a></strong> don't have any protocol intelligence, you can't define a <strong><a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a></strong> for a certain DHCP option.</p><p>The best thing you can do: Capture all DHCP/BOOTP frames and later use a <strong><a href="http://wiki.wireshark.org/DisplayFilters">display filter</a></strong> in Wireshark or tshark to filter only those frames with option 53.</p><p>Wireshark <a href="http://wiki.wireshark.org/DisplayFilters">display filter</a></p><blockquote><p>bootp.option.type == 53<br />
</p></blockquote><p>Alternatively, you can use tshark with a <strong><a href="http://wiki.wireshark.org/DisplayFilters">display filter</a></strong> while you are capturing. Downside: you can't write a capture file (-w not supported with display filters). But you can print whatever fields you may need.</p><blockquote><p>tshark -ni eth0 -Y "bootp.option.type == 53" -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e bootp.option.type -e bootp.ip.client -e xxxx</p></blockquote><p>Replace xxxx with whatever bootp protocol field you may need.</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/b/bootp.html">http://www.wireshark.org/docs/dfref/b/bootp.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '13, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26843" class="comments-container"><span id="26859"></span><div id="comment-26859" class="comment"><div id="post-26859-score" class="comment-score"></div><div class="comment-text"><p>Thank you,Kurt. If I just want to filter all the DHCP/bootp frames, then what's the appropriate capture filter？</p></div><div id="comment-26859-info" class="comment-info"><span class="comment-age">(11 Nov '13, 16:39)</span> metamatrix</div></div><span id="26876"></span><div id="comment-26876" class="comment"><div id="post-26876-score" class="comment-score"></div><div class="comment-text"><blockquote><p>udp port 68 or port 67</p></blockquote><p>should work.</p></div><div id="comment-26876-info" class="comment-info"><span class="comment-age">(12 Nov '13, 03:53)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26843" class="comment-tools"></div><div class="clear"></div><div id="comment-26843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

