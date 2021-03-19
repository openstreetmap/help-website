+++
type = "question"
title = "Capture all packets in promiscuous mode ?"
description = '''What is the Golden Gate Bridge ? It&#x27;s a bridge. What does the check box &quot;Capture all packets in promiscuous mode&quot; do ? &quot;This checkbox allows you to specify that Wireshark should put all interfaces in promiscuous mode when capturing&quot;.   So, what is promiscuous mode ?'''
date = "2013-02-03T11:18:00Z"
lastmod = "2013-02-03T14:15:00Z"
weight = 18259
keywords = [ "bridge", "promiscuous-mode", "golden" ]
aliases = [ "/questions/18259" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture all packets in promiscuous mode ?](/questions/18259/capture-all-packets-in-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18259-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the Golden Gate Bridge ? It's a bridge.</p><p>What does the check box "Capture all packets in promiscuous mode" do ? "This checkbox allows you to specify that Wireshark should put all interfaces in promiscuous mode when capturing".<br />
</p><p>So, what is promiscuous mode ?</p></div><div id="question-tags" class="tags-container tags">bridge promiscuous-mode golden</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '13, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/a984f0c6c05cea1964d76fb123050a4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wstest&#39;s gravatar image" /><p>wstest<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wstest has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-18259" class="comments-container"></div><div id="comment-tools-18259" class="comment-tools"></div><div class="clear"></div><div id="comment-18259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18262"></span>

<div id="answer-container-18262" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18262-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Normally a network interface will only "receive" packets directly addressed to the interface. Promiscuous mode allows the interface to receive all packets that it sees whether they are addressed to the interface or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '13, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18262" class="comments-container"><span id="18268"></span><div id="comment-18268" class="comment"><div id="post-18268-score" class="comment-score"></div><div class="comment-text"><p>or, to be more specific: when a network card is in promiscuous mode it accepts all packets, even if the destination MAC of the frame does not match it's own MAC. Broadcasts are accepted anyway. Without promiscuous mode frames with MACs other than the one the interface has are ignored (apart from broadcasts, again).</p></div><div id="comment-18268-info" class="comment-info"><span class="comment-age">(03 Feb '13, 17:22)</span> Jasper ♦♦</div></div><span id="18275"></span><div id="comment-18275" class="comment"><div id="post-18275-score" class="comment-score"></div><div class="comment-text"><p>I could try to argue that broadcast packets are addressed to all interfaces, and thus fall within my woolly definition :-)</p></div><div id="comment-18275-info" class="comment-info"><span class="comment-age">(04 Feb '13, 03:44)</span> grahamb ♦</div></div></div><div id="comment-tools-18262" class="comment-tools"></div><div class="clear"></div><div id="comment-18262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

