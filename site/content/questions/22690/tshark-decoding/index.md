+++
type = "question"
title = "Tshark decoding"
description = '''I&#x27;m using the command tshark to have a txt file with a dump of some packets. It works but I&#x27;ve got a problem. I&#x27;ve got UDP packets with proprietary protocol and in some cases wireshark decodes them as wrong protocol and I can see them as malformed packets. Actually they aren&#x27;t malformed because of t...'''
date = "2013-07-05T08:12:00Z"
lastmod = "2013-07-05T09:10:00Z"
weight = 22690
keywords = [ "tshark" ]
aliases = [ "/questions/22690" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark decoding](/questions/22690/tshark-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22690-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using the command tshark to have a txt file with a dump of some packets. It works but I've got a problem. I've got UDP packets with proprietary protocol and in some cases wireshark decodes them as wrong protocol and I can see them as malformed packets. Actually they aren't malformed because of the proprietary protocol. When I dump the packets I can see only the packets not recognized by wireshark and empty data for "malformed packets". Is there a way to say "not decode as" in tshark? I found only the option -d to say "decode as" but not "not decode as".</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '13, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/dc421f75bf3cba166762bd83797a4b51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marco&#39;s gravatar image" /><p>Marco<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marco has no accepted answers">0%</span></p></div></div><div id="comments-container-22690" class="comments-container"></div><div id="comment-tools-22690" class="comment-tools"></div><div class="clear"></div><div id="comment-22690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22691"></span>

<div id="answer-container-22691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22691-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're just looking to disable protocol decoding in tshark, this was answered in the below thread by SYN-bit previously: <a href="http://ask.wireshark.org/questions/9544/how-to-disable-dissectors-in-tshark">http://ask.wireshark.org/questions/9544/how-to-disable-dissectors-in-tshark</a></p><p>Basically just add the protocol to the disabled_protocols file in a profile, and use -C to specify that profile to use by tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '13, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-22691" class="comments-container"></div><div id="comment-tools-22691" class="comment-tools"></div><div class="clear"></div><div id="comment-22691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

