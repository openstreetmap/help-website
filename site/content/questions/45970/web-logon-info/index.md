+++
type = "question"
title = "Web logon info"
description = '''Can I use WireShark to see the handshake data exchange between my router/modem and my ISP&#x27;s server at first logon?'''
date = "2015-09-20T05:27:00Z"
lastmod = "2015-09-20T13:08:00Z"
weight = 45970
keywords = [ "noobquestion" ]
aliases = [ "/questions/45970" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Web logon info](/questions/45970/web-logon-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45970-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I use WireShark to see the handshake data exchange between my router/modem and my ISP's server at first logon?</p></div><div id="question-tags" class="tags-container tags">noobquestion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '15, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/4751dd93a2c9f2bf710d2d05418cca31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonnyc&#39;s gravatar image" /><p>Jonnyc<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonnyc has no accepted answers">0%</span></p></div></div><div id="comments-container-45970" class="comments-container"></div><div id="comment-tools-45970" class="comment-tools"></div><div class="clear"></div><div id="comment-45970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45975"></span>

<div id="answer-container-45975" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45975-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't because the link between your router and your ISP is (most certainly) not Ethernet. I guess it's either a DSL link or a cable link (DOCSIS). For both, you would need (very expensive) hardware protocol analyzers.</p><p>But maybe I'm misunderstanding your question. In that case, please add more details what you expect to see in that first few packets between your router and the ISP.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '15, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45975" class="comments-container"><span id="45982"></span><div id="comment-45982" class="comment"><div id="post-45982-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt. Thanks for your answer to my dumb question! What I'm trying to do is to configure a modem/router to be a standby for the ISP's box. We get a lot of thunderstorms here in Central France, and when the last one took out the box I was without I/net and phone for the week it took them to replace it. PITA! I called and asked them for some required parameters (VPI/VCI, Registrar address Etc.) but they refused to give them. So I'm looking for a way to read this information at first logon. I'm hoping maybe someone has already done this and save me "re-discovering the wheel"! I'm completely new to this so ANY help would much appreciated. TNX.</p><p>JC</p></div><div id="comment-45982-info" class="comment-info"><span class="comment-age">(20 Sep '15, 17:49)</span> Jonnyc</div></div><span id="45984"></span><div id="comment-45984" class="comment"><div id="post-45984-score" class="comment-score"></div><div class="comment-text"><p>P.S. How do I "cast my vote"?</p><p>JC</p></div><div id="comment-45984-info" class="comment-info"><span class="comment-age">(20 Sep '15, 17:54)</span> Jonnyc</div></div><span id="46007"></span><div id="comment-46007" class="comment"><div id="post-46007-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p><p>To upvote (or downvote) an answer or comment click the thumbs up or down icon next to the answer or comment.</p></div><div id="comment-46007-info" class="comment-info"><span class="comment-age">(21 Sep '15, 05:28)</span> grahamb ♦</div></div><span id="46026"></span><div id="comment-46026" class="comment"><div id="post-46026-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So I'm looking for a way to read this information at first logon.<br />
I called and asked them for some required parameters (VPI/VCI,</p></blockquote><p><strong>VPI/VCI</strong> sounds like it's a DSL modem/router. In that case, you can't capture that traffic with Wireshark, as I have explained. The protocol <strong>between</strong> the modem/router and and your ISP is not ethernet. It's not even anything close to anything you can capture with Wireshark. So, I'm sorry for you! Unless you are able to capture that information <strong>IN</strong> the modem/router, you'll have to rely on the ISP to hand over that information. Alternatively you could (politely) ask them to send you a second pre-configured box as a "cold standby" device. Other than that I don't see a solution for you.</p><p>You might be able to find some information on the internet how to open the modem/router and how to access the internal JTAG interface. Sometimes it's possible to "root" a modem/router via that way, but that's certainly beyond the scope of this site!</p><p>Some general hints, <strong>NOT</strong> related to your modem/router, as you did not mention the brand/model!!</p><blockquote><p><a href="http://wiki.openwrt.org/doc/hardware/port.jtag">http://wiki.openwrt.org/doc/hardware/port.jtag</a><br />
<a href="http://wiki.openwrt.org/doc/howto/generic.debrick">http://wiki.openwrt.org/doc/howto/generic.debrick</a><br />
<a href="http://www.dd-wrt.com/wiki/index.php/Serial_Recovery">http://www.dd-wrt.com/wiki/index.php/Serial_Recovery</a></p></blockquote></div><div id="comment-46026-info" class="comment-info"><span class="comment-age">(21 Sep '15, 09:56)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-45975" class="comment-tools"></div><div class="clear"></div><div id="comment-45975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

