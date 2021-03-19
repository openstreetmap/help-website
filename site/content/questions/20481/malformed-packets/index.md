+++
type = "question"
title = "Malformed Packets"
description = '''Hi There I am seeing a large amount of malformed packets on our network. The source hardware address is 00:00:00:00:00:00 and the destination is also 00:00:00:00:00:00. Does anyone have any idea how I can trace these packets? The packet length is 60 - the same as an arp request?? Any ideas? I&#x27;ve dra...'''
date = "2013-04-16T14:56:00Z"
lastmod = "2013-04-16T15:25:00Z"
weight = 20481
keywords = [ "packets", "malformed" ]
aliases = [ "/questions/20481" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed Packets](/questions/20481/malformed-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20481-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There</p><p>I am seeing a large amount of malformed packets on our network. The source hardware address is 00:00:00:00:00:00 and the destination is also 00:00:00:00:00:00. Does anyone have any idea how I can trace these packets? The packet length is 60 - the same as an arp request??</p><p>Any ideas? I've drawn a total blank on this one...</p><p>Many thanks Phill</p></div><div id="question-tags" class="tags-container tags">packets malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/86d71b8409d508a3790fcf4606ed4ff7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pippin_uk&#39;s gravatar image" /><p>Pippin_uk<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pippin_uk has no accepted answers">0%</span></p></div></div><div id="comments-container-20481" class="comments-container"></div><div id="comment-tools-20481" class="comment-tools"></div><div class="clear"></div><div id="comment-20481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20482"></span>

<div id="answer-container-20482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20482-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>there was a similar question some time ago:</p><blockquote><p><code>http://ask.wireshark.org/questions/12833/unknown-frame-malformed-packet</code><br />
</p></blockquote><p>Looks like you've got a broken network interface.</p><p>How to identify/find it? You could try to look at the <a href="http://en.wikipedia.org/wiki/CAM_Table">CAM table</a> of your switch and find the port where the mac address (0:0:0:0:0:0) is seen by the switch. If that does not work, you can only switch off the systems one after the other while monitoring the network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '13, 15:52</p></div></div><div id="comments-container-20482" class="comments-container"><span id="20484"></span><div id="comment-20484" class="comment"><div id="post-20484-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt</p><p>Thanks very much for your reply. I'll look into this and let you know how it goes.</p><p>Thanks again! Phill</p></div><div id="comment-20484-info" class="comment-info"><span class="comment-age">(16 Apr '13, 15:33)</span> Pippin_uk</div></div></div><div id="comment-tools-20482" class="comment-tools"></div><div class="clear"></div><div id="comment-20482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

