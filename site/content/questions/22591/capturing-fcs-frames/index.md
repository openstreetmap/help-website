+++
type = "question"
title = "capturing fcs frames"
description = '''Trying to capture fcs for Ethernet frame. what be the best bet to capture it would that be netBSD. Any clues folks who have tried it before.'''
date = "2013-07-03T02:28:00Z"
lastmod = "2013-07-08T18:21:00Z"
weight = 22591
keywords = [ "ethernet", "fcs" ]
aliases = [ "/questions/22591" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capturing fcs frames](/questions/22591/capturing-fcs-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22591-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to capture fcs for Ethernet frame. what be the best bet to capture it would that be netBSD. Any clues folks who have tried it before.</p></div><div id="question-tags" class="tags-container tags">ethernet fcs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '13, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/e0e2dc23842e8a3a3b6437eafa10cdfd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dees&#39;s gravatar image" /><p>Dees<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dees has no accepted answers">0%</span></p></div></div><div id="comments-container-22591" class="comments-container"></div><div id="comment-tools-22591" class="comment-tools"></div><div class="clear"></div><div id="comment-22591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22594"></span>

<div id="answer-container-22594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22594-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please see my answer to a similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/21272/ethernet-ii-with-bad-fcs">http://ask.wireshark.org/questions/21272/ethernet-ii-with-bad-fcs</a></p></blockquote><p>If that does not help, please add some details to your question.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '13, 03:59</p></div></div><div id="comments-container-22594" class="comments-container"><span id="22738"></span><div id="comment-22738" class="comment"><div id="post-22738-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt.</p><p>We are trying to debug some packet with incorrect FCS and to compare this with what application is reporting was looking to capture some wired traces with FCS.</p><p>Could somebody guide me which interface card or OS is suitable to capture FCS on the Ethernet frame?</p></div><div id="comment-22738-info" class="comment-info"><span class="comment-age">(08 Jul '13, 14:30)</span> Dees</div></div><span id="22743"></span><div id="comment-22743" class="comment"><div id="post-22743-score" class="comment-score"></div><div class="comment-text"><p>Well, I know that my Network General S6000 devices can capture FCS and even duplex negotionation link pulses, but they are very special capture solutions. I guess most of the expensive commercial network recording solutions should be able to do the same.</p></div><div id="comment-22743-info" class="comment-info"><span class="comment-age">(08 Jul '13, 19:08)</span> Jasper ♦♦</div></div></div><div id="comment-tools-22594" class="comment-tools"></div><div class="clear"></div><div id="comment-22594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22742"></span>

<div id="answer-container-22742" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22742-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I know of no definitive list of adapters that supply an Ethernet FCS; however, <a href="http://ask.wireshark.org/users/79/guy-harris">Guy Harris</a> has apparently had some luck with at least one and has also mentioned some hardware capable of supplying the Ethernet FCS in his answer to <a href="http://serverfault.com/questions/521443/can-wireshark-capture-an-entire-ethernet-frame-including-preamble-crc-and-inter">"Can Wireshark capture an entire Ethernet frame including preamble, CRC and Interframe spacing?"</a> over on serverfault.com.</p><p>You might also want to research network taps. There are many vendors/manufacturers that supply such taps, so many in fact that I hesitate to mention any by name, for a few reasons.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '13, 18:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-22742" class="comments-container"></div><div id="comment-tools-22742" class="comment-tools"></div><div class="clear"></div><div id="comment-22742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

