+++
type = "question"
title = "simulate low-bandwidth or high-latency"
description = '''How can I generate network traffic and measure the performance of the network? What tools/addons are recommended for Wireshark? Also, how to simulate low-bandwidth or high-latency?'''
date = "2013-02-09T04:16:00Z"
lastmod = "2013-02-12T12:08:00Z"
weight = 18467
keywords = [ "latency", "measurements", "tools", "performance" ]
aliases = [ "/questions/18467" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [simulate low-bandwidth or high-latency](/questions/18467/simulate-low-bandwidth-or-high-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18467-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I generate network traffic and measure the performance of the network? What tools/addons are recommended for Wireshark? Also, how to simulate low-bandwidth or high-latency?</p></div><div id="question-tags" class="tags-container tags">latency measurements tools performance</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '13, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/e9b234d20ab54e78235be0b566679210?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JDB&#39;s gravatar image" /><p>JDB<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JDB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Feb '13, 07:25</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-18467" class="comments-container"></div><div id="comment-tools-18467" class="comment-tools"></div><div class="clear"></div><div id="comment-18467-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="18468"></span>

<div id="answer-container-18468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18468-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a network protocol analyser and cannot generate traffic nor simulate network issues. Maybe there are items on the <a href="http://wiki.wireshark.org/Tools">Tools</a> page on the Wiki that can help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '13, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18468" class="comments-container"></div><div id="comment-tools-18468" class="comment-tools"></div><div class="clear"></div><div id="comment-18468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18471"></span>

<div id="answer-container-18471" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18471-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How I can I generate network traffic and measure the peformance of the network - what tools are recommend</p></blockquote><p>I can recommend <a href="http://code.google.com/p/xjperf/">jperf</a>. Nice and easy tool for simple performance tests.</p><blockquote><p>also how to simulate low-bandwidth or high-latency ?</p></blockquote><p>I can recommend either <a href="http://wanem.sourceforge.net/">wanem</a> or <a href="http://www.trafficsqueezer.org/">trafficsqueeszer</a> (in WAN simulator mode).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '13, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Feb '13, 14:00</p></div></div><div id="comments-container-18471" class="comments-container"></div><div id="comment-tools-18471" class="comment-tools"></div><div class="clear"></div><div id="comment-18471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18485"></span>

<div id="answer-container-18485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18485-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>"also how to simulate low-bandwidth or high-latency ?"</em></p><p>I haven't used it myself, but you might also want to look into <a href="http://www.linuxfoundation.org/collaborate/workgroups/networking/netem">netem</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '13, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-18485" class="comments-container"></div><div id="comment-tools-18485" class="comment-tools"></div><div class="clear"></div><div id="comment-18485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18563"></span>

<div id="answer-container-18563" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18563-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've had very good experience with FreeBSD's <a href="http://www.freebsd.org/cgi/man.cgi?query=dummynet&amp;apropos=0&amp;sektion=4&amp;manpath=FreeBSD+9.1-RELEASE&amp;arch=default&amp;format=html">dummynet</a> (part of their firewall).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-18563" class="comments-container"></div><div id="comment-tools-18563" class="comment-tools"></div><div class="clear"></div><div id="comment-18563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

