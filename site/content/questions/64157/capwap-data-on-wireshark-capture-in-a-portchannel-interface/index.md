+++
type = "question"
title = "Capwap data on Wireshark capture in a portchannel interface"
description = '''hi, I am trying to capture the data on a port-channel connected to a wireless controller so I can see what traffic is going to and from the wireless controller from the access point and wifi client. I am not see this traffic and only seeing some of the other traffic, for instance, I see the RDP repl...'''
date = "2017-10-24T08:27:00Z"
lastmod = "2017-10-26T00:15:00Z"
weight = 64157
keywords = [ "wireless", "capwap", "port-channel" ]
aliases = [ "/questions/64157" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capwap data on Wireshark capture in a portchannel interface](/questions/64157/capwap-data-on-wireshark-capture-in-a-portchannel-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64157-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I am trying to capture the data on a port-channel connected to a wireless controller so I can see what traffic is going to and from the wireless controller from the access point and wifi client.</p><p>I am not see this traffic and only seeing some of the other traffic, for instance, I see the RDP replies\ack but not the data.</p><p>Any help would be great. I am running wireshark on a windows machine.</p><p>Mikey</p></div><div id="question-tags" class="tags-container tags">wireless capwap port-channel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '17, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/956eda944de640cab4fe8db272a63aac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikeyConway&#39;s gravatar image" /><p>MikeyConway<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikeyConway has no accepted answers">0%</span></p></div></div><div id="comments-container-64157" class="comments-container"><span id="64197"></span><div id="comment-64197" class="comment"><div id="post-64197-score" class="comment-score"></div><div class="comment-text"><p>Can you elaborate on your capture setup? Are you using port mirroring, a tap, what is the line speed of the port-channel and of your capturing card, ...</p></div><div id="comment-64197-info" class="comment-info"><span class="comment-age">(25 Oct '17, 11:05)</span> sindy</div></div></div><div id="comment-tools-64157" class="comment-tools"></div><div class="clear"></div><div id="comment-64157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64212"></span>

<div id="answer-container-64212" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64212-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I am spanning an 8-port port channel but I resolved the issue The issues is with the MacAfee HIPS services, once that was stopped the traffic was seen correctly.</p><p>Thanks for your response.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '17, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/956eda944de640cab4fe8db272a63aac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikeyConway&#39;s gravatar image" /><p>MikeyConway<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikeyConway has no accepted answers">0%</span></p></div></div><div id="comments-container-64212" class="comments-container"><span id="64213"></span><div id="comment-64213" class="comment"><div id="post-64213-score" class="comment-score"></div><div class="comment-text"><p>Glad to hear that, however even if it is just 8×FE, you'd need to capture 1.6 Gbit/s at peak, so it won't fit to a single SPAN port even if it would be a GE one. Leaving alone 8×GE where you'd need to deal with 16 Gbit/s at peak which no PC is likely to manage regardless what network card you'd plug in.</p></div><div id="comment-64213-info" class="comment-info"><span class="comment-age">(26 Oct '17, 00:22)</span> sindy</div></div></div><div id="comment-tools-64212" class="comment-tools"></div><div class="clear"></div><div id="comment-64212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

