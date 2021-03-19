+++
type = "question"
title = "Struggling to get correct answer..... IP Range"
description = '''Hi, Think I have googled just about everything but cannot find he answer I am looking for. I want Wireshark to monitor a range of ip address, ie: 192.168.2.10 - 192.168.2.30 Have tried all sorts of options with AND OR &amp;lt;&amp;gt; and dont seem to get anywhere. I am guessing its a simple one and I am ju...'''
date = "2016-07-10T11:09:00Z"
lastmod = "2016-07-10T12:38:00Z"
weight = 53965
keywords = [ "d95gas" ]
aliases = [ "/questions/53965" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Struggling to get correct answer..... IP Range](/questions/53965/struggling-to-get-correct-answer-ip-range)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53965-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Think I have googled just about everything but cannot find he answer I am looking for.</p><p>I want Wireshark to monitor a range of ip address, ie: 192.168.2.10 - 192.168.2.30</p><p>Have tried all sorts of options with AND OR &lt;&gt; and dont seem to get anywhere. I am guessing its a simple one and I am just not seeing it.</p><p>Any help would be appreicated.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">d95gas</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '16, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/9c57c5eea9c6a4ad0f6eeabe99d5516d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d95gas&#39;s gravatar image" /><p>d95gas<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="d95gas has no accepted answers">0%</span></p></div></div><div id="comments-container-53965" class="comments-container"></div><div id="comment-tools-53965" class="comment-tools"></div><div class="clear"></div><div id="comment-53965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53966"></span>

<div id="answer-container-53966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53966-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no direct way to define an ip range in a <em>capture</em> filter syntax. The maximum you can do is to use a combination of <code>net</code> and <code>host</code> expressions, like <code>(net 192.168.2.8/29 and not host 192.168.2.8 and not host 192.168.2.9) or (net 192.168.2.16/28 and not host 192.168.2.31)</code> for your particular case, to make the condition shorter than a plain list of <code>host x.x.x.x</code> expressions.</p><p>For a <em>display</em> filter, <code>ip.addr &gt;= 192.168.2.10 and ip.addr &lt;= 192.168.2.30</code> does what you want, and for tshark with <code>-w</code> option, a display filter has the same effect on the output capture file like a capture filter (there are differences but in this case I think you can neglect them).</p><p>Depending on your use case, for Wireshark use, it might make sense to use a wider capture filter (like <code>net 192.168.2.0/27</code>) to reduce the amount of captured packets, then apply the display filter above to show only the ones you really wanted, and then use <code>File -&gt; Export Selected Packets -&gt; Displayed</code> to save only the shown ones to a new file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '16, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '16, 12:44</p></div></div><div id="comments-container-53966" class="comments-container"></div><div id="comment-tools-53966" class="comment-tools"></div><div class="clear"></div><div id="comment-53966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

