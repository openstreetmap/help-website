+++
type = "question"
title = "Offset into ethernet packets"
description = '''Hi, I have a capture of ethernet traffic. Now, I want to sift thru and display the packets and find those that have a certain keyword as well as a specific character (in hex) in say the 14th position of the ethernet packet(s). The keyword I am looking for can be found by the frame contains clause - ...'''
date = "2010-09-21T13:45:00Z"
lastmod = "2010-09-21T16:24:00Z"
weight = 253
keywords = [ "ethernet", "into", "packets", "offset" ]
aliases = [ "/questions/253" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Offset into ethernet packets](/questions/253/offset-into-ethernet-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-253-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a capture of ethernet traffic. Now, I want to sift thru and display the packets and find those that have a certain keyword as well as a specific character (in hex) in say the 14th position of the ethernet packet(s). The keyword I am looking for can be found by the frame contains clause - how do I find the offset into the ethernet packet at the 14th position ?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">ethernet into packets offset</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '10, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/052cea1a33dd51db67919582594e448b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="codie9002&#39;s gravatar image" /><p>codie9002<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="codie9002 has no accepted answers">0%</span></p></div></div><div id="comments-container-253" class="comments-container"><span id="452"></span><div id="comment-452" class="comment"><div id="post-452-score" class="comment-score">1</div><div class="comment-text"><p>By "14th position" do you mean "the last byte of the Ethernet <em>header</em>", e.g.:</p><p>Ethernet destination: 00:01:02:03:04:05 = the 1st through the 6th position; Ethernet source: 05:04:03:02:01:00 = the 7th through the 12th position; Ethernet type/length: 08:00 = the 13th and the 14th position;</p><p>in which case see Laura's answer, or do you mean "the first byte of the Ethernet <em>payload</em>", i.e., that, in the example there, the Ethernet destination is the 0th through the 5th position, etc. (i.e., zero-origin), in which case it'd be "frame[14:1] = 00"?</p></div><div id="comment-452-info" class="comment-info"><span class="comment-age">(06 Oct '10, 16:36)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-253" class="comment-tools"></div><div class="clear"></div><div id="comment-253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="254"></span>

<div id="answer-container-254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-254-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>frame[13:1] == 00</p><p>Count into the frame starting at zero (so "13" means you are interested in the 14th byte) and look for a single byte equal to 0x00 (in this exacmple).</p><p>That's kinda weird to be looking at the 14th byte as it will likely be either 0x00 or 0x06 (as in 0x0800 or 0x0806 for IP and ARP respectively). Just a note there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '10, 16:24</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-254" class="comments-container"></div><div id="comment-tools-254" class="comment-tools"></div><div class="clear"></div><div id="comment-254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

