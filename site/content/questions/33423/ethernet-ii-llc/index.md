+++
type = "question"
title = "Ethernet II / LLC"
description = '''Hello, frame can have such a combination or maybe it&#x27;s a misinterpretation of the program.  I think this frame 802.3/802.2/SNAP can be wrong? best wishes'''
date = "2014-06-05T02:11:00Z"
lastmod = "2014-06-05T02:16:00Z"
weight = 33423
keywords = [ "ethernet" ]
aliases = [ "/questions/33423" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Ethernet II / LLC](/questions/33423/ethernet-ii-llc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33423-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>frame can have such a combination or maybe it's a misinterpretation of the program.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/w_2.jpg" alt="alt text" /></p><p>I think this frame 802.3/802.2/SNAP</p><p>can be wrong?</p><p>best wishes</p></div><div id="question-tags" class="tags-container tags">ethernet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '14, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/9cc3412566a366e4f0d721d801d86256?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sergun&#39;s gravatar image" /><p>sergun<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sergun has no accepted answers">0%</span></p></img></div></div><div id="comments-container-33423" class="comments-container"></div><div id="comment-tools-33423" class="comment-tools"></div><div class="clear"></div><div id="comment-33423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33424"></span>

<div id="answer-container-33424" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33424-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>0x8100 is the Ethertype for a VLAN tag following the Ethernet II header, so that seems to be correct. In that VLAN tag is a length value less than 1500 so the next part is LLC. Seems all fine to me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33424" class="comments-container"><span id="33426"></span><div id="comment-33426" class="comment"><div id="post-33426-score" class="comment-score"></div><div class="comment-text"><p>but in frame ethernet II can contain LLC</p></div><div id="comment-33426-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:28)</span> sergun</div></div><span id="33428"></span><div id="comment-33428" class="comment"><div id="post-33428-score" class="comment-score"></div><div class="comment-text"><p>There is a VLAN tag between the Ethernet II header. Think of it as two Ether types following each other. The first says "Ethernet II" and points to a VLAN tag, the seconds (VLAN tag) says "next is 802.3", so that's fine, too.</p></div><div id="comment-33428-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:31)</span> Jasper ♦♦</div></div><span id="33431"></span><div id="comment-33431" class="comment"><div id="post-33431-score" class="comment-score"></div><div class="comment-text"><p>great, thank you</p></div><div id="comment-33431-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:41)</span> sergun</div></div><span id="33434"></span><div id="comment-33434" class="comment"><div id="post-33434-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-33434-info" class="comment-info"><span class="comment-age">(05 Jun '14, 02:57)</span> grahamb ♦</div></div></div><div id="comment-tools-33424" class="comment-tools"></div><div class="clear"></div><div id="comment-33424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

