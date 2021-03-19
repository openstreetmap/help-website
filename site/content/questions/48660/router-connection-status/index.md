+++
type = "question"
title = "Router Connection Status"
description = '''Hello, What string am i supposed to use in the Capture Filter that i can only the network connection status for my router? I been looking in https://wiki.wireshark.org/CaptureFilters#Examples but dident find much usefull as i could see. (I haven&#x27;t been working much with Network before.)'''
date = "2015-12-21T07:12:00Z"
lastmod = "2015-12-21T07:31:00Z"
weight = 48660
keywords = [ "status", "router", "connection" ]
aliases = [ "/questions/48660" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Router Connection Status](/questions/48660/router-connection-status)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48660-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>What string am i supposed to use in the Capture Filter that i can only the network connection status for my router?</p><p>I been looking in <a href="https://wiki.wireshark.org/CaptureFilters#Examples">https://wiki.wireshark.org/CaptureFilters#Examples</a> but dident find much usefull as i could see. (I haven't been working much with Network before.)</p></div><div id="question-tags" class="tags-container tags">status router connection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '15, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/9d3bb02d7039c4fd42d81d5fa163b47b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yonose&#39;s gravatar image" /><p>Yonose<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yonose has no accepted answers">0%</span></p></div></div><div id="comments-container-48660" class="comments-container"></div><div id="comment-tools-48660" class="comment-tools"></div><div class="clear"></div><div id="comment-48660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48661"></span>

<div id="answer-container-48661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48661-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is not all that simple, and Wireshark may not be the right tool for your goal.</p><p>The network connection <strong>status</strong>, which the web management page of your router or the icon in your operating system's system tray indicate, is a result of active periodic testing of accessibility of some reference host(s) in the internet. While you can capture <strong>packets sent and received</strong> by the PC on which you run Wireshark, you cannot directly see packets which your router exchanges with the network without your PC's participation (unless your PC is between the router and the network, which I doubt is the case).</p><p>So to obtain a better answer, please be more specific about which network connection status you want to see (i.e. the router's one or your PC's one), and what is your network topology (how the PC, the router and the link to the ISP/internet are arranged).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '15, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48661" class="comments-container"></div><div id="comment-tools-48661" class="comment-tools"></div><div class="clear"></div><div id="comment-48661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

