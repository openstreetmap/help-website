+++
type = "question"
title = "Trying to Capture TCP packets using a USB satellite Phone"
description = '''Hello, I am trying to capture TCP traffic using wire shark. I am using a Satellite phone connected via USB . Any help is greatly appreciated. Thanks'''
date = "2017-07-15T08:52:00Z"
lastmod = "2017-07-15T08:52:00Z"
weight = 62804
keywords = [ "phone", "tcppackets", "usb", "sat" ]
aliases = [ "/questions/62804" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to Capture TCP packets using a USB satellite Phone](/questions/62804/trying-to-capture-tcp-packets-using-a-usb-satellite-phone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62804-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to capture TCP traffic using wire shark. I am using a Satellite phone connected via USB . Any help is greatly appreciated.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">phone tcppackets usb sat</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '17, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/aaf9e4e4d3f212f56f4f67a28aa9d42a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="errabolu&#39;s gravatar image" /><p>errabolu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="errabolu has no accepted answers">0%</span></p></div></div><div id="comments-container-62804" class="comments-container"><span id="62810"></span><div id="comment-62810" class="comment"><div id="post-62810-score" class="comment-score"></div><div class="comment-text"><p>The information about your environment is insufficient.</p><p>Some wireless USB modems, regardless what wireless network they use, emulate serial ports, which means that IP connection uses ppp over serial, while others emulate ethernet ports so the IP connection is either direct or PPPoE.</p><p>Depending on this, you may be able to capture at the "ethernet" interface if the driver supports that (some Windows drivers don't), or you may have to capture the serial-over-USB packets (I'm not sure whether linux supports capturing at ppp interfaces, Windows do not AFAIK).</p><p>Ability to capture USB depends on kernel version on linux or OS X, and you need USBPcap on Windows.</p><p>And I'm afraid that dissection of ppp over serial over USB would require heavy post-processing of the capture.</p></div><div id="comment-62810-info" class="comment-info"><span class="comment-age">(15 Jul '17, 11:43)</span> sindy</div></div><span id="62812"></span><div id="comment-62812" class="comment"><div id="post-62812-score" class="comment-score"></div><div class="comment-text"><p>Microsoft's Message Analyzer (formerly Network Monitor) can capture over PPP.</p></div><div id="comment-62812-info" class="comment-info"><span class="comment-age">(15 Jul '17, 12:11)</span> grahamb ♦</div></div><span id="62817"></span><div id="comment-62817" class="comment"><div id="post-62817-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm not sure whether linux supports capturing at ppp interfaces</p></blockquote><p>It does.</p><blockquote><p>Windows do not AFAIK</p></blockquote><p>Windows with WinPcap doesn't; Windows with NPcap might.</p><blockquote><p>Ability to capture USB depends on kernel version on linux or OS X</p></blockquote><p>I think any reasonably recent kernel should support it on Linux; for macOS, you'll need High Sierra, I think (the upcoming <em>High</em> Sierra, not just the current Sierra).</p><blockquote><p>Microsoft's Message Analyzer (formerly Network Monitor) can capture over PPP.</p></blockquote><p>The Network Monitor driver probably plugs into the networking stack in a different place from where the WinPcap driver plugs; NPcap <em>might</em> plug in at the same point (although, at one point, I think there was have been a special hack in Windows that looked for the NetMon driver and treated it specially).</p><p>I think Message Analyzer may plug into the networking stack in yet another place, although I'm not certain.</p></div><div id="comment-62817-info" class="comment-info"><span class="comment-age">(15 Jul '17, 22:17)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-62804" class="comment-tools"></div><div class="clear"></div><div id="comment-62804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

