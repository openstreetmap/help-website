+++
type = "question"
title = "download timed out"
description = '''2 of my servers are trying to download a virus signature file from McAfee site and it just kept timing out. I plugged my PC directly to the switch and I was able to download the file without any problem. I am using Wireshark to see what is going on with my servers. I saw [tcp dup ack 674#2] and [tcp...'''
date = "2013-07-15T10:51:00Z"
lastmod = "2013-07-15T11:00:00Z"
weight = 22975
keywords = [ "download", "times", "out", "server" ]
aliases = [ "/questions/22975" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [download timed out](/questions/22975/download-timed-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22975-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>2 of my servers are trying to download a virus signature file from McAfee site and it just kept timing out. I plugged my PC directly to the switch and I was able to download the file without any problem.</p><p>I am using Wireshark to see what is going on with my servers. I saw [tcp dup ack 674#2] and [tcp zerowindow], and [tcp out-of-order]. I am not familiar with those errors. May be you can tell me the meaning of those errors.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">download times out server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '13, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/4bf9a4681570406f873b404a912f2a7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="character9&#39;s gravatar image" /><p>character9<br />
<span class="score" title="16 reputation points">16</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="character9 has no accepted answers">0%</span></p></div></div><div id="comments-container-22975" class="comments-container"><span id="22995"></span><div id="comment-22995" class="comment"><div id="post-22995-score" class="comment-score"></div><div class="comment-text"><p>is it possible to post the capture files somewhere (google docs, dropbox, etc.)?</p></div><div id="comment-22995-info" class="comment-info"><span class="comment-age">(16 Jul '13, 02:36)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22975" class="comment-tools"></div><div class="clear"></div><div id="comment-22975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22976"></span>

<div id="answer-container-22976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22976-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>TCP Duplicate acknowledgement is an error recovery behavior w.r.t TCP protocol.TCP Duplicate acknowledgement(from receiver) notifies (to sender) that one or more segments lost during transmission.After this notification sender realizes that there is a loss and tries to retransmit the lost segment.</p><p>TCP Zero-window indicates that the receiver buffer filled up and doesn't have any space to process the data from sender.This indicates the sender to stall the data transmission until receiver indicates that it got some free buffer to process.</p><p>TCP Out of Order: Check out the link below <a href="http://ask.wireshark.org/questions/1698/tcp-out-of-order-what-does-it-means">http://ask.wireshark.org/questions/1698/tcp-out-of-order-what-does-it-means</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '13, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '13, 11:01</p></div></div><div id="comments-container-22976" class="comments-container"><span id="22984"></span><div id="comment-22984" class="comment"><div id="post-22984-score" class="comment-score"></div><div class="comment-text"><p>So is it valid to say that the time out issue is due to the TCP zero-window as the source does not have space to process the downloaded data? Is there any feature or techniques in Wireshark that I can use to pinpoint the issue. Thank you.</p></div><div id="comment-22984-info" class="comment-info"><span class="comment-age">(15 Jul '13, 17:42)</span> character9</div></div></div><div id="comment-tools-22976" class="comment-tools"></div><div class="clear"></div><div id="comment-22976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

