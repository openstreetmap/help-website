+++
type = "question"
title = "exclude remote desktop connection packets"
description = '''Hi, I&#x27;m doing some network test, capturing packets in my PC and a the same time in a server which I connect to via Remote Desktop Connection (windows 7), this generates a lot of traffic, how can I set a filter to exclude the traffic due to the remote destkop connection?'''
date = "2015-10-29T06:45:00Z"
lastmod = "2015-10-29T07:08:00Z"
weight = 47062
keywords = [ "remote-desktop" ]
aliases = [ "/questions/47062" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [exclude remote desktop connection packets](/questions/47062/exclude-remote-desktop-connection-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47062-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm doing some network test, capturing packets in my PC and a the same time in a server which I connect to via Remote Desktop Connection (windows 7), this generates a lot of traffic, how can I set a filter to exclude the traffic due to the remote destkop connection?</p></div><div id="question-tags" class="tags-container tags">remote-desktop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '15, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/065a787c1564a0f77c10c927f7f080b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rok&#39;s gravatar image" /><p>rok<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rok has no accepted answers">0%</span></p></div></div><div id="comments-container-47062" class="comments-container"></div><div id="comment-tools-47062" class="comment-tools"></div><div class="clear"></div><div id="comment-47062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47063"></span>

<div id="answer-container-47063" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47063-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filter: "not tcp port 3389", assuming you're running RDP on the standard port.</p><p>If you connect to the server via RDP and then run Wireshark on the server, Wireshark should automatically apply that capture filter for you on the server. See the section titled "Default Capture Filters" on <a href="https://wiki.wireshark.org/CaptureFilters">this page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '15, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-47063" class="comments-container"></div><div id="comment-tools-47063" class="comment-tools"></div><div class="clear"></div><div id="comment-47063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

