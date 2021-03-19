+++
type = "question"
title = "filters applied to saved capture files"
description = '''Very comfortable with Wireshark and understand filters, etc... It seems that a lot of people ask this question and the answers always involve saving a massive .pcap file and doing some post processing on it to isolate only what&#x27;s needed. Trouble is I need to run Wireshark for many hours and capture ...'''
date = "2015-12-15T06:36:00Z"
lastmod = "2015-12-15T19:39:00Z"
weight = 48531
keywords = [ "filteredsave" ]
aliases = [ "/questions/48531" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [filters applied to saved capture files](/questions/48531/filters-applied-to-saved-capture-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48531-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Very comfortable with Wireshark and understand filters, etc... It seems that a lot of people ask this question and the answers always involve saving a massive .pcap file and doing some post processing on it to isolate only what's needed. Trouble is I need to run Wireshark for many hours and capture activity only to a specific port. I set the filter to isolate the port activity in the display window but can't watch the screen for 8 hours.</p><p>The basic question is how can I simply write only the filtered result to a file. What I see in the display need to be saved in a file for later review.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">filteredsave</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/94233e7919c318b82ec99ae9ebcbe296?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="King%20Of%20Crab&#39;s gravatar image" /><p>King Of Crab<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="King Of Crab has no accepted answers">0%</span></p></div></div><div id="comments-container-48531" class="comments-container"></div><div id="comment-tools-48531" class="comment-tools"></div><div class="clear"></div><div id="comment-48531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48534"></span>

<div id="answer-container-48534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48534-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The simple answer is "use <code>File -&gt; Export specified packets</code>" while a display filter is applied, assuming that capture(-time) filter is not narrow enough for your purpose and you needed to apply display(-time) filter to choose by protocol fields which the capture filter cannot access.</p><p>Or you may want to use command-line tshark instead of the GUI Wireshark and use <code>-Y</code> or <code>-R</code> to specify "display filter" during capture and -w to write the result (see further details and syntax <a href="https://www.wireshark.org/docs/man-pages/tshark.html">here</a>).</p><p>A hint which I haven't found at the wiki: if you need to specify more complex display filter conditions, use "" to delimit the condition, and use \" where you need to use " as part of the filter.</p><p>Example: <code>-Y "usb.iso.status == 0 and usb.src == \"3.6.2\""</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '15, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48534" class="comments-container"><span id="48536"></span><div id="comment-48536" class="comment"><div id="post-48536-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy. I ran tshark with a few filter options and got what's needed on the screen output but didn't have the same filter option for writing to a file. Just redirected stdio to a file did the trick. Yay for me. Thanks again</p></div><div id="comment-48536-info" class="comment-info"><span class="comment-age">(15 Dec '15, 08:12)</span> King Of Crab</div></div></div><div id="comment-tools-48534" class="comment-tools"></div><div class="clear"></div><div id="comment-48534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48556"></span>

<div id="answer-container-48556" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48556-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Trouble is I need to run Wireshark for many hours and capture activity only to a specific port.</p></blockquote><p>If <em>all</em> you want is activity to a specific TCP or UDP port, and will never have <em>any</em> interest in anything else (as in "you won't, after reading the traffic, realize that you really need to see something other than traffic to that port"), you can use a capture filter such as <code>tcp dst port XXX</code> or <code>udp dst port XXX</code>; with a capture filter such as that, the only packets written to the file will be packets to the port in question.</p><p>If you want packets both to <em>and</em> from that port, remove the <code>dst</code> from those filters.</p><p>Capture filters are handled by a <em>much</em> simpler engine (in the libpcap/WinPcap library and in the OS kernel), won't handle arbitrary forms of tunneling/encapsulation of IP traffic, and require extra care if you're using VLANs (the filter expression in question won't handle VLAN traffic; you'd need something like</p><pre><code>tcp dst port XXX or (vlan and tcp dst port XXX)</code></pre><p>(with <code>dst</code> removed if you want traffic to and from the port).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '15, 19:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-48556" class="comments-container"></div><div id="comment-tools-48556" class="comment-tools"></div><div class="clear"></div><div id="comment-48556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

