+++
type = "question"
title = "I just installed Wireshark on Win7 on a Thinkpad.  Why is the wireless interface not listed?"
description = '''I just installed Wireshark on Win7 on a Thinkpad. Why is the wireless interface not listed?'''
date = "2012-07-11T08:51:00Z"
lastmod = "2012-07-12T00:36:00Z"
weight = 12635
keywords = [ "wireless", "interface" ]
aliases = [ "/questions/12635" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I just installed Wireshark on Win7 on a Thinkpad. Why is the wireless interface not listed?](/questions/12635/i-just-installed-wireshark-on-win7-on-a-thinkpad-why-is-the-wireless-interface-not-listed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12635-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just installed Wireshark on Win7 on a Thinkpad. Why is the wireless interface not listed?</p></div><div id="question-tags" class="tags-container tags">wireless interface</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '12, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/b075b05cebb5f0d5d3b6feb514e21c9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daveap&#39;s gravatar image" /><p>daveap<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daveap has no accepted answers">0%</span></p></div></div><div id="comments-container-12635" class="comments-container"></div><div id="comment-tools-12635" class="comment-tools"></div><div class="clear"></div><div id="comment-12635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12647"></span>

<div id="answer-container-12647" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12647-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Windows, Wireless adaptes show up as "Microsoft". Please check the IP address of the adapter to identify it.</p><p>Wireshark 1.8</p><blockquote><p><code>Capture -&gt; Interfaces -&gt; "Column IP"</code><br />
</p></blockquote><p>You can also click the <strong><code>Details</code></strong> Button. It will show interface parameters. The <strong><code>Link Speed</code></strong> will be 54 Mbit/s or any other speed specific to wifi, but not 10,100,1000 MBit/s.</p><p>Dumpcap will also show the IP address.</p><blockquote><p><code>dumpcap -D -M</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '12, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12647" class="comments-container"></div><div id="comment-tools-12647" class="comment-tools"></div><div class="clear"></div><div id="comment-12647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

