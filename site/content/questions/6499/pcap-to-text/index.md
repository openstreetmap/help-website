+++
type = "question"
title = "pcap to text"
description = '''I want to know how to convert a file .pcap to a plain text, i&#x27;ve tried using: tcpdump -r input.pcap &amp;gt; output.txt and it works, but the text inside the file isn&#x27;t the same data in the pcap file when I open the pcap in wireshark I want to export to text without using wireshark interface, I want to ...'''
date = "2011-09-22T20:35:00Z"
lastmod = "2011-09-23T00:55:00Z"
weight = 6499
keywords = [ "text", "pcap", "pcaptotext", "tcpdump" ]
aliases = [ "/questions/6499" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [pcap to text](/questions/6499/pcap-to-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6499-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know how to convert a file .pcap to a plain text, i've tried using:</p><p>tcpdump -r input.pcap &gt; output.txt</p><p>and it works, but the text inside the file isn't the same data in the pcap file when I open the pcap in wireshark</p><p>I want to export to text without using wireshark interface, I want to do it through the terminal in Linux.</p></div><div id="question-tags" class="tags-container tags">text pcap pcaptotext tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '11, 20:35</strong></p><img src="https://secure.gravatar.com/avatar/78867f35e2a419cd375a296ae681d3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="julle&#39;s gravatar image" /><p>julle<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="julle has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '11, 21:05</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-6499" class="comments-container"></div><div id="comment-tools-6499" class="comment-tools"></div><div class="clear"></div><div id="comment-6499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6500"></span>

<div id="answer-container-6500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6500-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're looking for help with tcpdump, you're at the wrong place. See the <a href="http://www.tcpdump.org/tcpdump_man.html">tcpdump man page</a> or post your question to the <a href="http://www.tcpdump.org/#mailing-lists">tcpdump mailing list</a>.</p><p>On the other hand, if you meant to type tshark, then you should refer to the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>, as there are many options to control the output, depending on your needs. You can also get help by running <code>tshark -h</code>.</p><p>One quick example, just to get you started, is: <code>tshark -V -r input.pcap &gt; output.txt</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '11, 21:05</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6500" class="comments-container"></div><div id="comment-tools-6500" class="comment-tools"></div><div class="clear"></div><div id="comment-6500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6502"></span>

<div id="answer-container-6502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6502-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>tcpdump dissects packets differently from Wireshark, so <code>tcpdump -r input.pcap &gt; output.txt</code> won't produce a dissection like that of Wireshark.</p><p>As Chris Maynard noted, you need to use a program that dissects packets the <em>same</em> way Wireshark does; TShark uses the same dissector code that Wireshark does, so it's the program to use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '11, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6502" class="comments-container"></div><div id="comment-tools-6502" class="comment-tools"></div><div class="clear"></div><div id="comment-6502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

