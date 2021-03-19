+++
type = "question"
title = "&quot;Browser emulation&quot; Is this possible/does this exist?"
description = '''Hey! I have two laptops set up on my network, and I have been using Wireshark to pick up the packets from one on the other. I&#x27;m wondering, is there any way to &quot;mirror&quot; the activity of the laptop being sniffed on the sniffing laptop? Like, I get one packet from laptop A and laptop B says &quot;Oh, I am go...'''
date = "2013-08-30T18:57:00Z"
lastmod = "2013-08-31T14:21:00Z"
weight = 24218
keywords = [ "mirroring", "forwarding", "emulation", "packet" ]
aliases = [ "/questions/24218" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ["Browser emulation" Is this possible/does this exist?](/questions/24218/browser-emulation-is-this-possibledoes-this-exist)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24218-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey!</p><p>I have two laptops set up on my network, and I have been using Wireshark to pick up the packets from one on the other. I'm wondering, is there any way to "mirror" the activity of the laptop being sniffed on the sniffing laptop? Like, I get one packet from laptop A and laptop B says "Oh, I am going to pretend this packet is for me!". In theory, wouldn't this allow laptop B to see pretty much what laptop A is seeing (minus dropped packets, inability to ACK, etc?) Even a somewhat decent emulation in a browser would be so much easier to sift through than looking through the packets manually. Thoughts?</p></div><div id="question-tags" class="tags-container tags">mirroring forwarding emulation packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 18:57</strong></p><img src="https://secure.gravatar.com/avatar/7826e9b5784b2c31ad45ceb5930cc3ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="orisqu&#39;s gravatar image" /><p>orisqu<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="orisqu has no accepted answers">0%</span></p></div></div><div id="comments-container-24218" class="comments-container"></div><div id="comment-tools-24218" class="comment-tools"></div><div class="clear"></div><div id="comment-24218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24240"></span>

<div id="answer-container-24240" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24240-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>In theory, wouldn't this allow laptop B to see pretty much what laptop A is seeing</p></blockquote><p>Yes, and in practice, that's what webspy (part of <a href="http://www.monkey.org/~dugsong/dsniff/">dsniff</a>) was designed for.</p><blockquote><p><a href="http://linux.die.net/man/8/webspy">http://linux.die.net/man/8/webspy</a></p></blockquote><p>However, that project/tool is abandoned now, and I have not tried webspy lately.</p><p>xplico has similar features.</p><blockquote><p><a href="http://www.xplico.org/">http://www.xplico.org/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24240" class="comments-container"></div><div id="comment-tools-24240" class="comment-tools"></div><div class="clear"></div><div id="comment-24240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

