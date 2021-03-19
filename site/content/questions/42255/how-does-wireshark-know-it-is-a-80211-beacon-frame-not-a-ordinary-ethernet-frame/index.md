+++
type = "question"
title = "How does wireshark know it is a 802.11 beacon frame, not  a ordinary ethernet frame"
description = '''I downloaded a simple 802.11 beacon frames from link, the first few bytes in the frame/packet are 8000 0000 ffff ffff ffff 0013 460b 22ba 0013 460b 22ba 8054. The question is, how does wireshark know it&#x27;s not a ordinary ethernet frame? Does the first two bytes &quot;80 00&quot; give wireshark a clue?  Thanks.'''
date = "2015-05-09T07:48:00Z"
lastmod = "2015-05-09T07:52:00Z"
weight = 42255
keywords = [ "wireshark" ]
aliases = [ "/questions/42255" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does wireshark know it is a 802.11 beacon frame, not a ordinary ethernet frame](/questions/42255/how-does-wireshark-know-it-is-a-80211-beacon-frame-not-a-ordinary-ethernet-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42255-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded a simple 802.11 beacon frames from <a href="http://chrissanders.org/packet-captures/">link</a>, the first few bytes in the frame/packet are 8000 0000 ffff ffff ffff 0013 460b 22ba 0013 460b 22ba 8054. The question is, how does wireshark know it's not a ordinary ethernet frame? Does the first two bytes "80 00" give wireshark a clue?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '15, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-42255" class="comments-container"></div><div id="comment-tools-42255" class="comment-tools"></div><div class="clear"></div><div id="comment-42255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42256"></span>

<div id="answer-container-42256" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42256-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just found that pcap file header (24) has a field for data-link-type, this value will give wireshark a clue on how to decode the packet.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '15, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span> </br></p></div></div><div id="comments-container-42256" class="comments-container"></div><div id="comment-tools-42256" class="comment-tools"></div><div class="clear"></div><div id="comment-42256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

