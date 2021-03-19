+++
type = "question"
title = "6lowpan/IPv6 RFC4944 data on 802.15.4 frames"
description = '''I can capture 802.15.4 frames containing IPv6 packets in RFC4944 format using TIs CC2531 hardware and their SmartRF sniffer. I&#x27;ve been able to convert them to PCAP format such that wireshark can decode the 802.15.4 headers, but I&#x27;m not able to get it to decode the IPv6 packet contents.  I know that ...'''
date = "2013-04-28T00:17:00Z"
lastmod = "2016-09-16T04:40:00Z"
weight = 20827
keywords = [ "802.15.4", "4944", "6lowpan", "ipv6" ]
aliases = [ "/questions/20827" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [6lowpan/IPv6 RFC4944 data on 802.15.4 frames](/questions/20827/6lowpanipv6-rfc4944-data-on-802154-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20827-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can capture 802.15.4 frames containing IPv6 packets in RFC4944 format using TIs CC2531 hardware and their SmartRF sniffer. I've been able to convert them to PCAP format such that wireshark can decode the 802.15.4 headers, but I'm not able to get it to decode the IPv6 packet contents.</p><p>I know that Wireshark supports RFC4944. I see it work fine with the example captures on <a href="http://wiki.wireshark.org/IEEE_802.15.4.">http://wiki.wireshark.org/IEEE_802.15.4.</a></p><p>Does my PCAP need something 'special' to get wireshark to recognize it as IPv6 data? Could it be because of the "Bad FCS"? (The sniffer unfortunately ruins the FCS)</p><p>The capture file is here: <a href="http://www.cloudshark.org/captures/65a478336de3">http://www.cloudshark.org/captures/65a478336de3</a></p></div><div id="question-tags" class="tags-container tags">802.15.4 4944 6lowpan ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '13, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/2f95a6e31db1bed7944d9e68d826b094?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hideo&#39;s gravatar image" /><p>hideo<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hideo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Apr '13, 00:24</p></div></div><div id="comments-container-20827" class="comments-container"></div><div id="comment-tools-20827" class="comment-tools"></div><div class="clear"></div><div id="comment-20827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37798"></span>

<div id="answer-container-37798" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37798-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I could get Wireshark to decode it a little further by changing the <a href="http://www.tcpdump.org/linktypes.html">data link type</a> in the PCAP <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">global header</a>, from 0xC3 (195) to 0xE6 (230). I do not really understand what is happening though.</p><p>Here is the modified file: <a href="https://www.cloudshark.org/captures/46a9a369e6a9">https://www.cloudshark.org/captures/46a9a369e6a9</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '14, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/c9be23553f5fae97efcdeb0f888190bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bbc&#39;s gravatar image" /><p>bbc<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bbc has no accepted answers">0%</span></p></div></div><div id="comments-container-37798" class="comments-container"></div><div id="comment-tools-37798" class="comment-tools"></div><div class="clear"></div><div id="comment-37798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55591"></span>

<div id="answer-container-55591" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55591-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What should I do to change the data link type in PCP global header?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '16, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/cb52b7b4b3aefda06953d48de6f9f296?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ketan&#39;s gravatar image" /><p>ketan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ketan has no accepted answers">0%</span></p></div></div><div id="comments-container-55591" class="comments-container"></div><div id="comment-tools-55591" class="comment-tools"></div><div class="clear"></div><div id="comment-55591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

