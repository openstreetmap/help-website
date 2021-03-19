+++
type = "question"
title = "custom hardware"
description = '''Hi I want to be able to &quot;on the fly&quot; remotely capture data. I want to have 24 TAPS where they are connected to a custom PC that has 8*3 NIC PCI express cards. The Motherboard NIC would be the RDP connection. When an issue happens I can RDP and start a capture on one or more of the 24 interfaces that...'''
date = "2011-10-17T16:56:00Z"
lastmod = "2011-10-26T02:19:00Z"
weight = 6937
keywords = [ "hardware", "build" ]
aliases = [ "/questions/6937" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [custom hardware](/questions/6937/custom-hardware)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6937-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I want to be able to "on the fly" remotely capture data.</p><p>I want to have 24 TAPS where they are connected to a custom PC that has 8*3 NIC PCI express cards. The Motherboard NIC would be the RDP connection.</p><p>When an issue happens I can RDP and start a capture on one or more of the 24 interfaces that I choose.</p><ol><li>Will Wireshark handle 24 interfaces.</li><li>Other than a powerful 64bit lots a RAM computer, anything special?</li><li>Those 8*3 PCI NICS, do they have to specifically be able to run in premiscious mode?</li></ol><p>Thanks s</p></div><div id="question-tags" class="tags-container tags">hardware build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '11, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/fd7e2cff0486ad1aa41922b783e07fba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goldbank&#39;s gravatar image" /><p>goldbank<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goldbank has no accepted answers">0%</span></p></div></div><div id="comments-container-6937" class="comments-container"></div><div id="comment-tools-6937" class="comment-tools"></div><div class="clear"></div><div id="comment-6937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6943"></span>

<div id="answer-container-6943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6943-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess if the OS can handle 24 NICs I don't see why Wireshark couldn't, but maybe there are additional technical reasons I am not aware of (maybe some enumeration issue).</p><p>I don't think lots of RAM is the most important thing (while it helps of course), the most important thing is a really really fast (and large) disk storage array. Unless you have data rates that do not require those of course. As soon as you're talking Gigabit you should plan for really fast storage.</p><p>And yes, for captures to make sense you need promiscuous mode on any card you want to capture on; otherwise it will only accept frames for it's own MAC (plus broadcast/multicast).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '11, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6943" class="comments-container"></div><div id="comment-tools-6943" class="comment-tools"></div><div class="clear"></div><div id="comment-6943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7073"></span>

<div id="answer-container-7073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7073-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>24 taps almost feels like a wrong approach to the problem there's probably a better way to do it maybe 24 port switch with a mirror port ?</p><p>I also think you'll have problems with interrupts handling if you plug 24 NICs into a singe PC. And if you are talking about gigabit speeds you'd see huge packet loss.</p><p>If I was doing the setup like your's I'd buy 6 fairly cheap PCS with relatively small disks. I'd Install linux on them. Then install and setup gulp <a href="http://staff.washington.edu/corey/gulp/">http://staff.washington.edu/corey/gulp/</a> to capture traffic without loss and escape the limitation of the disk.</p><p>Then on periodic basis I'd upload traces to 7th PC(windows maybe) with terrabyte storage for investigation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '11, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-7073" class="comments-container"></div><div id="comment-tools-7073" class="comment-tools"></div><div class="clear"></div><div id="comment-7073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

