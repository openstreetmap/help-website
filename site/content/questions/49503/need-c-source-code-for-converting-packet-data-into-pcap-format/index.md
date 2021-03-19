+++
type = "question"
title = "Need &quot;C&quot; source code for converting packet data into PCAP format."
description = '''Hi, I&#x27;m working for CISCO, we would like to convert the packet capture made in cisco routers into PCAP format, for that I would like to understand the PCAP format. Please suggest how to convert the raw packet data into pcap format? Thx Amby'''
date = "2016-01-25T06:38:00Z"
lastmod = "2016-01-25T13:27:00Z"
weight = 49503
keywords = [ "pcap" ]
aliases = [ "/questions/49503" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Need "C" source code for converting packet data into PCAP format.](/questions/49503/need-c-source-code-for-converting-packet-data-into-pcap-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49503-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm working for CISCO, we would like to convert the packet capture made in cisco routers into PCAP format, for that I would like to understand the PCAP format.</p><p>Please suggest how to convert the raw packet data into pcap format?</p><p>Thx Amby</p></div><div id="question-tags" class="tags-container tags">pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '16, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/fd4daa385f074922057bfc60973d9503?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ambalavanan&#39;s gravatar image" /><p>Ambalavanan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ambalavanan has no accepted answers">0%</span></p></div></div><div id="comments-container-49503" class="comments-container"></div><div id="comment-tools-49503" class="comment-tools"></div><div class="clear"></div><div id="comment-49503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="49504"></span>

<div id="answer-container-49504" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49504-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would strongly recommend to use <a href="https://github.com/pcapng/pcapng">pcapng</a>, as it</p><ul><li><p>provides more space for additional information about the captured frames,</p></li><li><p>allows for multiple frame encapsulation types in a single file (so you can e.g. save frames from an HDLC channel and from an Ethernet interface),</p></li><li><p>etc.</p></li></ul><p>If you insist, the traditional pcap is described <a href="https://wiki.wireshark.org/Development/LibpcapFileFormat">here</a>.</p><p>In both cases, the raw packet data need no <em>conversion</em>, they just need to be augmented with additional information and, in some cases, an appropriate encapsulation header.</p><p>(edit: updated the link to pcapng description with Jaap's up-to-date one, kept the advice to use pcapng).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '16, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jan '16, 07:58</p></div></div><div id="comments-container-49504" class="comments-container"></div><div id="comment-tools-49504" class="comment-tools"></div><div class="clear"></div><div id="comment-49504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49507"></span>

<div id="answer-container-49507" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49507-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If using pcapng please use <a href="https://github.com/pcapng/pcapng">the current draft</a>.</p><p>If going 'old school', use <a href="https://wiki.wireshark.org/Development/LibpcapFileFormat">this specification</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '16, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jan '16, 08:07</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-49507" class="comments-container"></div><div id="comment-tools-49507" class="comment-tools"></div><div class="clear"></div><div id="comment-49507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49512"></span>

<div id="answer-container-49512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Also, I think there's some router company some of whose equipment <a href="http://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-embedded-packet-capture/116045-productconfig-epc-00.html">can export captures in pcap format</a>; you might want to see if you can talk to the people responsible for that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '16, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49512" class="comments-container"></div><div id="comment-tools-49512" class="comment-tools"></div><div class="clear"></div><div id="comment-49512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

