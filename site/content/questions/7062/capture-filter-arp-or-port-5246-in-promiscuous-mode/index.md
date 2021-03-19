+++
type = "question"
title = "capture filter: arp or port 5246, in Promiscuous mode"
description = '''I use wireshark 1.6.2 version. i switch Mirror port capature packet. I find capature fileter: arp . But no packet, in Promiscuoous mode.This is a error! Wireshark: Summary Time  First packet: 1970-01-01 08:00:00  Last packet: 1970-01-01 08:00:00  Elapse: 00:00:00 Capture  capture filter: arp Traffic...'''
date = "2011-10-25T08:42:00Z"
lastmod = "2011-10-26T02:22:00Z"
weight = 7062
keywords = [ "arp", "capture", "filter" ]
aliases = [ "/questions/7062" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter: arp or port 5246, in Promiscuous mode](/questions/7062/capture-filter-arp-or-port-5246-in-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7062-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use wireshark 1.6.2 version. i switch Mirror port capature packet. I find capature fileter: arp . But no packet, in Promiscuoous mode.This is a error!</p><p>Wireshark: Summary Time First packet: 1970-01-01 08:00:00 Last packet: 1970-01-01 08:00:00 Elapse: 00:00:00</p><p>Capture capture filter: arp</p><p>Traffice packets: 0</p></div><div id="question-tags" class="tags-container tags">arp capture filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Oct '11, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/5f3ece42e2e71f94aa9ac19bee296792?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhoutree&#39;s gravatar image" /><p>zhoutree<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhoutree has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Oct '11, 09:44</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7062" class="comments-container"><span id="7063"></span><div id="comment-7063" class="comment"><div id="post-7063-score" class="comment-score"></div><div class="comment-text"><p>我发现别的抓包程序都可以设置成 arp or port 5246捕获过滤。 但是wireshark 设置居然一个包都没有。 我是在交换机镜像端口抓包的。</p></div><div id="comment-7063-info" class="comment-info"><span class="comment-age">(25 Oct '11, 08:46)</span> zhoutree</div></div><span id="7064"></span><div id="comment-7064" class="comment"><div id="post-7064-score" class="comment-score"></div><div class="comment-text"><p>hope to modify it.<br />
can to capture arp</p></div><div id="comment-7064-info" class="comment-info"><span class="comment-age">(25 Oct '11, 08:47)</span> zhoutree</div></div><span id="7066"></span><div id="comment-7066" class="comment"><div id="post-7066-score" class="comment-score"></div><div class="comment-text"><p>Is there a VLAN on this network?</p><p>If so, try</p><pre><code>(arp or port 5246) or (vlan and (arp or port 5246))</code></pre></div><div id="comment-7066-info" class="comment-info"><span class="comment-age">(25 Oct '11, 09:43)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-7062" class="comment-tools"></div><div class="clear"></div><div id="comment-7062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7074"></span>

<div id="answer-container-7074" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7074-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>very thanks! Mirro port is VLAN network</p><p>vlan and (arp or port 5246) work very much. in Promiscuous mode!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '11, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/5f3ece42e2e71f94aa9ac19bee296792?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhoutree&#39;s gravatar image" /><p>zhoutree<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhoutree has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-7074" class="comments-container"></div><div id="comment-tools-7074" class="comment-tools"></div><div class="clear"></div><div id="comment-7074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

