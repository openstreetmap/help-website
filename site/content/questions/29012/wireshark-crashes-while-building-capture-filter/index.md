+++
type = "question"
title = "Wireshark crashes while building Capture Filter"
description = '''Every time I try to build this Capture Filter Wireshark crashes with this error from Windows 7: The Filter is:&quot; not ether host xx.xx.xx.xx.xx.xx &quot; where the x&#x27;s are my ipv6 address. The crash always happens when I reach this point: &quot;not ether host xxxx::&quot; entering the second colon. The error I get f...'''
date = "2014-01-19T08:41:00Z"
lastmod = "2014-01-19T15:15:00Z"
weight = 29012
keywords = [ "crashes", "wireshark" ]
aliases = [ "/questions/29012" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes while building Capture Filter](/questions/29012/wireshark-crashes-while-building-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29012-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Every time I try to build this Capture Filter Wireshark crashes with this error from Windows 7: The Filter is:" not ether host xx.xx.xx.xx.xx.xx " where the x's are my ipv6 address. The crash always happens when I reach this point: "not ether host xxxx::" entering the second colon. The error I get from Windows 7 64bit is:"Runtime Error Program:C:\Progam Files\Wireshark\Wireshark.exe. This program has requested the Runtime to terminate in an unusual way." Any information on what I may be doing wrong would be appreciated. Thanks</p></div><div id="question-tags" class="tags-container tags">crashes wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '14, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/4f506da607cd03ce1e8e9d9a432047b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Strydr&#39;s gravatar image" /><p>Strydr<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Strydr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jan '14, 08:43</p></div></div><div id="comments-container-29012" class="comments-container"></div><div id="comment-tools-29012" class="comment-tools"></div><div class="clear"></div><div id="comment-29012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="29013"></span>

<div id="answer-container-29013" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29013-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>not ether host</code> needs to be followed by an address in <strong>ethernet</strong> format <code>nn:nn:nn:nn:nn:nn</code></p><p>To capture all traffic other than to a specific IPV6 host you need to use</p><pre><code>not host nnnn::...</code></pre><p>In any case, <code>not ether host nnnn::</code> should not cause a crash.</p><p>It would be appreciated if you could file a bug at bugs.wireshark.org (Thanks)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '14, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jan '14, 09:28</p></div></div><div id="comments-container-29013" class="comments-container"><span id="29021"></span><div id="comment-29021" class="comment"><div id="post-29021-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick answer I'll file a report as soon as possible.</p></div><div id="comment-29021-info" class="comment-info"><span class="comment-age">(19 Jan '14, 16:16)</span> Strydr</div></div></div><div id="comment-tools-29013" class="comment-tools"></div><div class="clear"></div><div id="comment-29013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29017"></span>

<div id="answer-container-29017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29017-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a libpcap bug, fixed in <a href="https://github.com/the-tcpdump-group/libpcap/commit/c513a4781f33985be01fa6999a9ad21e1e7a0f1b">this commit</a>; it's fixed in libpcap 1.5.1 and later, but, unfortunately, there's no version of WinPcap based on that version of libpcap.</p><p>The workaround is to specify MAC addresses as xx:xx:xx:xx:xx:xx, not as IPv6 addresses; the fix means that you will get an <em>error</em> if you specify them as IPv6 addresses, so you <em>still</em> won't be able to do that, it just means that programs using libpcap/WinPcap will tell you "that doesn't work" rather than just crashing.</p><p>So don't say "not ether host xxxx:: ...".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '14, 15:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29017" class="comments-container"><span id="29022"></span><div id="comment-29022" class="comment"><div id="post-29022-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the great answer. It's good to know the why's of a problem, plus a work around. So if I don't want this problem and I want to use the Filter with my syntax I should be in a Linux distro.</p></div><div id="comment-29022-info" class="comment-info"><span class="comment-age">(19 Jan '14, 16:40)</span> Strydr</div></div><span id="29023"></span><div id="comment-29023" class="comment"><div id="post-29023-score" class="comment-score"></div><div class="comment-text"><p>No.</p><p>If you are using a UN*X (Linux distribution, *BSD, OS X, whatever) with a libpcap prior to 1.5.1, you'll get a crash if you use "not ether host xxxx::...", just as you do on Windows.</p><p>If you are using a UN*X (Linux distribution, *BSD, OS X, whatever) with libpcap 1.5.1 or later, you'll get an error message if you use "not ether host xxxx::...".</p><p>If you want to filter out a given MAC address, use "not ether host xx:xx:xx:xx:xx:xx", where "xx:xx:xx:xx:xx:xx" is the MAC address you want to filter out.</p><p>If you want to filter out a given <em>IPv6</em> address, use "not host xxxx::..." or "not ip6 host xxxx::...", where "xxxx:..." is the IPv6 address you want to filter out.</p></div><div id="comment-29023-info" class="comment-info"><span class="comment-age">(19 Jan '14, 16:47)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-29017" class="comment-tools"></div><div class="clear"></div><div id="comment-29017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29014"></span>

<div id="answer-container-29014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29014-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filter <code>ether host ...</code> is for mac address filtering. For IP address filtering use <code>host ...</code>.</p><p>Admittedly it would be handy if Wireshark didn't crash when an incorrect filter is entered. Please raise a bug for this on the Wireshark <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '14, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29014" class="comments-container"><span id="29020"></span><div id="comment-29020" class="comment"><div id="post-29020-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick answer. I must say that is the quickest I have ever received an answer in any Forum. I'll try using that syntax and see what happens.</p></div><div id="comment-29020-info" class="comment-info"><span class="comment-age">(19 Jan '14, 16:00)</span> Strydr</div></div></div><div id="comment-tools-29014" class="comment-tools"></div><div class="clear"></div><div id="comment-29014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

