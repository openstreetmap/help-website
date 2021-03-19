+++
type = "question"
title = "Capture of leaving packets doesn&#x27;t work on Windows"
description = '''Hi at all, using Wireshark 2.0.4 and 2.0.5 I am still have a problem. If I start a capture i could see all packets without packets leaving my own interface. e.g. if I do a ping, i am only able to capture the echo replays to me. Any ideas? Could this be a driver issue?'''
date = "2016-08-31T06:30:00Z"
lastmod = "2016-08-31T06:30:00Z"
weight = 55235
keywords = [ "windows", "capture", "problem", "outgoing" ]
aliases = [ "/questions/55235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture of leaving packets doesn't work on Windows](/questions/55235/capture-of-leaving-packets-doesnt-work-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi at all, using Wireshark 2.0.4 and 2.0.5 I am still have a problem. If I start a capture i could see all packets without packets leaving my own interface.</p><p>e.g. if I do a ping, i am only able to capture the echo replays to me.</p><p>Any ideas? Could this be a driver issue?</p></div><div id="question-tags" class="tags-container tags">windows capture problem outgoing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/192d47e303094398720ef0d9e0bc9292?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="magroll&#39;s gravatar image" /><p>magroll<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="magroll has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '16, 07:52</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-55235" class="comments-container"><span id="55236"></span><div id="comment-55236" class="comment"><div id="post-55236-score" class="comment-score"></div><div class="comment-text"><p>What OS are you using?</p></div><div id="comment-55236-info" class="comment-info"><span class="comment-age">(31 Aug '16, 06:31)</span> grahamb ♦</div></div><span id="55238"></span><div id="comment-55238" class="comment"><div id="post-55238-score" class="comment-score"></div><div class="comment-text"><p>I am using Windows 7SP1 Professionall - 64 bit</p></div><div id="comment-55238-info" class="comment-info"><span class="comment-age">(31 Aug '16, 06:50)</span> magroll</div></div><span id="55239"></span><div id="comment-55239" class="comment"><div id="post-55239-score" class="comment-score"></div><div class="comment-text"><p>Any VPN, firewall, and/or anti-virus software other than Windows firewall? There is a couple of Questions dealing with the same issue around here, with a common explanation that low-level drivers of such software interfere with WinPcap operation. You may try NPcap instead of WinPcap to avoid the issue, as the former binds into the networking stack at a different place than the latter, but if that does not help, you'll have to choose between ability to capture and use of the interfering software.</p><p>For testing, disabling the interfering software is often not enough as its network drivers remain plugged in. You would have to disable them manually (they are system services) or uninstall them.</p></div><div id="comment-55239-info" class="comment-info"><span class="comment-age">(31 Aug '16, 07:21)</span> sindy</div></div><span id="55241"></span><div id="comment-55241" class="comment"><div id="post-55241-score" class="comment-score"></div><div class="comment-text"><p>Use the tag "outgoing" that I've added to your question to find the similar questions alluded to by @sindy.</p></div><div id="comment-55241-info" class="comment-info"><span class="comment-age">(31 Aug '16, 07:50)</span> grahamb ♦</div></div></div><div id="comment-tools-55235" class="comment-tools"></div><div class="clear"></div><div id="comment-55235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

