+++
type = "question"
title = "I see only HTTP/1.1 200 OK response packets"
description = '''Suddenly my wireshark is only showing packets from Source IP to Destination IP only. e.g. My source IP is 10.10.23.234 and destination IP is 10.10.23.236. Then my wiereshark should show packets originating from Source and Destination IP but instead it is only showing one direction responses. It is n...'''
date = "2013-10-17T17:11:00Z"
lastmod = "2013-10-18T11:12:00Z"
weight = 26150
keywords = [ "http" ]
aliases = [ "/questions/26150" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I see only HTTP/1.1 200 OK response packets](/questions/26150/i-see-only-http11-200-ok-response-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26150-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Suddenly my wireshark is only showing packets from Source IP to Destination IP only. e.g. My source IP is 10.10.23.234 and destination IP is 10.10.23.236. Then my wiereshark should show packets originating from Source and Destination IP but instead it is only showing one direction responses. It is not showing request packets.</p><p>What went wrong with wireshark suddenly? Appreciate any help.</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '13, 17:11</strong></p><img src="https://secure.gravatar.com/avatar/460f1afbbe95c01ae8176f3c97289575?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdp&#39;s gravatar image" /><p>jdp<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdp has one accepted answer">100%</span></p></div></div><div id="comments-container-26150" class="comments-container"><span id="26154"></span><div id="comment-26154" class="comment"><div id="post-26154-score" class="comment-score"></div><div class="comment-text"><p>What OS are you running Wireshark on, and do you capture on a wireless or a wired connection?</p></div><div id="comment-26154-info" class="comment-info"><span class="comment-age">(17 Oct '13, 22:39)</span> Jasper ♦♦</div></div><span id="26155"></span><div id="comment-26155" class="comment"><div id="post-26155-score" class="comment-score"></div><div class="comment-text"><p>I am using Windows 7. I checked on Local area connection and Wireless as well. It still doesn't show the response packets.</p></div><div id="comment-26155-info" class="comment-info"><span class="comment-age">(17 Oct '13, 22:55)</span> jdp</div></div><span id="26157"></span><div id="comment-26157" class="comment"><div id="post-26157-score" class="comment-score"></div><div class="comment-text"><p>What AV/firewall/VPN software do you have installed on your capturing machine?</p></div><div id="comment-26157-info" class="comment-info"><span class="comment-age">(18 Oct '13, 01:00)</span> grahamb ♦</div></div></div><div id="comment-tools-26150" class="comment-tools"></div><div class="clear"></div><div id="comment-26150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26197"></span>

<div id="answer-container-26197" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26197-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found that recently some DNE Update (Deterministic Networks, Inc) was installed on my machine. I uninstalled it and now wireshark is working properly.</p><p>Thanks all for your time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/460f1afbbe95c01ae8176f3c97289575?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdp&#39;s gravatar image" /><p>jdp<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdp has one accepted answer">100%</span></p></div></div><div id="comments-container-26197" class="comments-container"></div><div id="comment-tools-26197" class="comment-tools"></div><div class="clear"></div><div id="comment-26197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

