+++
type = "question"
title = "Decoding IP(IPv4/IPv6) packets with LLC SNAP header"
description = '''I see that for IPv4/IPv6 packets which have a LLC SNAP header, wireshark does not decode the L3 and L4 layers.Only for ENET II type(DIX) it decodes L3 and L4 layers.'''
date = "2017-04-05T03:56:00Z"
lastmod = "2017-04-06T17:46:00Z"
weight = 60584
keywords = [ "llc", "snap" ]
aliases = [ "/questions/60584" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding IP(IPv4/IPv6) packets with LLC SNAP header](/questions/60584/decoding-ipipv4ipv6-packets-with-llc-snap-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60584-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see that for IPv4/IPv6 packets which have a LLC SNAP header, wireshark does not decode the L3 and L4 layers.Only for ENET II type(DIX) it decodes L3 and L4 layers.</p></div><div id="question-tags" class="tags-container tags">llc snap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '17, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/9dc974714033e7709b1c6e3e7d073ac0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pkn&#39;s gravatar image" /><p>pkn<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pkn has no accepted answers">0%</span></p></div></div><div id="comments-container-60584" class="comments-container"><span id="60589"></span><div id="comment-60589" class="comment"><div id="post-60589-score" class="comment-score"></div><div class="comment-text"><p>There's no question here. In general this looks like it should be turned into a bug report instead. Go to <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and enter a complete bug description. Don't forget screenshots and/or pcaps, so the developers can understand what the problem is.</p></div><div id="comment-60589-info" class="comment-info"><span class="comment-age">(05 Apr '17, 08:29)</span> Jasper ♦♦</div></div><span id="60590"></span><div id="comment-60590" class="comment"><div id="post-60590-score" class="comment-score">1</div><div class="comment-text"><p>More info on bug reporting available on the wiki <a href="https://wiki.wireshark.org/ReportingBugs">ReportingBugs</a> page.</p></div><div id="comment-60590-info" class="comment-info"><span class="comment-age">(05 Apr '17, 08:58)</span> grahamb ♦</div></div><span id="60600"></span><div id="comment-60600" class="comment"><div id="post-60600-score" class="comment-score">2</div><div class="comment-text"><blockquote><p>Don't forget screenshots and/or pcaps</p></blockquote><p>...with capture files <strong><em>very strongly</em></strong> preferred over screenshots! With a capture file, we can test Wireshark/TShark with the file, and test any fixes with the file as well.</p></div><div id="comment-60600-info" class="comment-info"><span class="comment-age">(06 Apr '17, 00:03)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-60584" class="comment-tools"></div><div class="clear"></div><div id="comment-60584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60627"></span>

<div id="answer-container-60627" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60627-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If an IPv4/IPv6 packet has a <strong><em>CORRECT</em></strong> LLC SNAP header, with an OUI of 00:00:00 and a PID of 0x0800 for IPv4 or 0x86dd for IPv6, wireshark <em>does</em> decode them.</p><p>If, however, it has a packet with some <em>other</em> OUI and a PID of 0x0800 or 0x86dd, the only reason why it should decode them as IPv4 or IPv6, respectively, would be if the organization to whom that OUI belongs decided to use 0x0800 as a PID for IPv4 or use 0x86dd as a PID for IPv6.</p><p>In a SNAP header, <strong><em>the OUI matters</em></strong>!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '17, 17:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-60627" class="comments-container"><span id="60628"></span><div id="comment-60628" class="comment"><div id="post-60628-score" class="comment-score"></div><div class="comment-text"><p>Thanks Harris for the clarification!</p></div><div id="comment-60628-info" class="comment-info"><span class="comment-age">(06 Apr '17, 21:06)</span> pkn</div></div></div><div id="comment-tools-60627" class="comment-tools"></div><div class="clear"></div><div id="comment-60627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

