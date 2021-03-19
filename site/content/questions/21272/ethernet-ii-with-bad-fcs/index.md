+++
type = "question"
title = "Ethernet II with bad FCS"
description = '''Did somebody get this packet? If you did, could you give me pcap file?'''
date = "2013-05-19T13:02:00Z"
lastmod = "2013-05-20T13:09:00Z"
weight = 21272
keywords = [ "ethernet" ]
aliases = [ "/questions/21272" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ethernet II with bad FCS](/questions/21272/ethernet-ii-with-bad-fcs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21272-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Did somebody get this packet? If you did, could you give me pcap file?</p></div><div id="question-tags" class="tags-container tags">ethernet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '13, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/6ea9dee45098683ffc6bd92101d0cde5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DariaS&#39;s gravatar image" /><p>DariaS<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DariaS has no accepted answers">0%</span></p></div></div><div id="comments-container-21272" class="comments-container"><span id="21294"></span><div id="comment-21294" class="comment"><div id="post-21294-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, but what exactly is your question?</p></div><div id="comment-21294-info" class="comment-info"><span class="comment-age">(20 May '13, 03:36)</span> Kurt Knochner ♦</div></div><span id="21331"></span><div id="comment-21331" class="comment"><div id="post-21331-score" class="comment-score"></div><div class="comment-text"><p>I recon he/she is asking for a sample trace file containing a frame with a broken Ethernet FCS.</p></div><div id="comment-21331-info" class="comment-info"><span class="comment-age">(20 May '13, 12:56)</span> Jasper ♦♦</div></div></div><div id="comment-tools-21272" class="comment-tools"></div><div class="clear"></div><div id="comment-21272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21332"></span>

<div id="answer-container-21332" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21332-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I recon he/she is asking for a sample trace file containing a frame with a broken Ethernet FCS.</p></blockquote><p>if that is the case, here we go</p><ul><li>First some information about FCS capturing: <a href="http://www.wireshark.org/faq.html#q7.10">http://www.wireshark.org/faq.html#q7.10</a></li><li>Second a pcapng with a broken FCS (created via HEX editor), based on a <a href="http://wiki.wireshark.org/Development/PcapNg?action=AttachFile&amp;do=view&amp;target=icmp2.ntar">sample capture file</a></li></ul><p>Frame #1 in the following file:</p><blockquote><p><code>https://www.cloudshark.org/captures/e776a282ec02</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '13, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21332" class="comments-container"></div><div id="comment-tools-21332" class="comment-tools"></div><div class="clear"></div><div id="comment-21332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

