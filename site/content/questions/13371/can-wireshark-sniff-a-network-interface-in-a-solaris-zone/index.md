+++
type = "question"
title = "Can Wireshark sniff a network interface in a Solaris Zone?"
description = '''Need to sniff packets in a Solaris Zone. Thanks in advance.'''
date = "2012-08-05T12:16:00Z"
lastmod = "2012-08-06T14:49:00Z"
weight = 13371
keywords = [ "solaris", "zone" ]
aliases = [ "/questions/13371" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark sniff a network interface in a Solaris Zone?](/questions/13371/can-wireshark-sniff-a-network-interface-in-a-solaris-zone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13371-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Need to sniff packets in a Solaris Zone.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">solaris zone</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '12, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/8e30973efcb57fe5f065850e28bb5f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joe98765432s1&#39;s gravatar image" /><p>Joe98765432s1<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joe98765432s1 has no accepted answers">0%</span></p></div></div><div id="comments-container-13371" class="comments-container"></div><div id="comment-tools-13371" class="comment-tools"></div><div class="clear"></div><div id="comment-13371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13393"></span>

<div id="answer-container-13393" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13393-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I haven't tried it (and I don't have a zone'd system to try it on), but I don't see why it would not work. I'd suggest giving it a try. (If it doesn't work, try Solaris' snoop command.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '12, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-13393" class="comments-container"></div><div id="comment-tools-13393" class="comment-tools"></div><div class="clear"></div><div id="comment-13393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13405"></span>

<div id="answer-container-13405" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13405-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Within a non-global zone, you cannot switch interfaces in promiscuous mode (per default). Thus you cannot capture all packets in a non-global zone. To be able to capture, the zone needs the privilege <strong>net_rawaccess</strong>.</p><p>Example:</p><blockquote><p><code>https://blogs.oracle.com/gbrunett/entry/i_see_you_snoop_1m</code><br />
</p></blockquote><p>However, if you sniff the interface (shared or exclusive) of non-global zones within the global zone, you should be able to see traffic of all zones that use this interface (use == have it mapped).</p><p>It does not matter if you sniff with Wireshark or snoop. If you want to sniff within a zone, you must install Wireshark in that zone. If you want to sniff in the global zone, you must install Wireshark there.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '12, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13405" class="comments-container"></div><div id="comment-tools-13405" class="comment-tools"></div><div class="clear"></div><div id="comment-13405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

