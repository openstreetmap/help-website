+++
type = "question"
title = "Have packet capture, somethings wrong"
description = '''Hey all, I have a packet (dont know where I can attach it, but I have a link below) that has a t1 connection to the internet that is &quot;not working&quot; If anyone can help me as to why on line 94, destination host unreachable is displaying, that would be awesome. Thank you. Here is the packet link: https:...'''
date = "2013-11-04T15:09:00Z"
lastmod = "2013-11-04T15:46:00Z"
weight = 26667
keywords = [ "problem", "t1" ]
aliases = [ "/questions/26667" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Have packet capture, somethings wrong](/questions/26667/have-packet-capture-somethings-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26667-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey all, I have a packet (dont know where I can attach it, but I have a link below) that has a t1 connection to the internet that is "not working"</p><p>If anyone can help me as to why on line 94, destination host unreachable is displaying, that would be awesome. Thank you.</p><p>Here is the packet link:</p><p><a href="https://www.dropbox.com/s/5eqli7z84taa9au/jp-capture-tdc376.pcap">https://www.dropbox.com/s/5eqli7z84taa9au/jp-capture-tdc376.pcap</a></p></div><div id="question-tags" class="tags-container tags">problem t1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '13, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/b73344d4e74bac41e45c995e6b05b89d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="candyluls&#39;s gravatar image" /><p>candyluls<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="candyluls has no accepted answers">0%</span></p></div></div><div id="comments-container-26667" class="comments-container"></div><div id="comment-tools-26667" class="comment-tools"></div><div class="clear"></div><div id="comment-26667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26668"></span>

<div id="answer-container-26668" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26668-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In frame #93 there is an SNMP request from <code>140.192.39.96 -&gt; 140.192.40.56</code>. That request did not make it to the destination as some system on the way blocked the request. The ICMP message in frame #94 is the response for that.</p><pre><code>94  0.001756    140.192.34.95   140.192.39.96   ICMP    70      Destination unreachable (Communication administratively filtered)</code></pre><p><strong>Communication administratively filtered</strong> means that there is a kind of filter (router ACL or firewall), that prohibited the SNMP request of frame #93. The system that sent the ICMP packet (140.192.34.95) is a good candidate for the ACL or firewall.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '13, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '13, 15:48</p></div></div><div id="comments-container-26668" class="comments-container"><span id="26683"></span><div id="comment-26683" class="comment"><div id="post-26683-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much kurt!!</p></div><div id="comment-26683-info" class="comment-info"><span class="comment-age">(05 Nov '13, 11:25)</span> candyluls</div></div></div><div id="comment-tools-26668" class="comment-tools"></div><div class="clear"></div><div id="comment-26668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

