+++
type = "question"
title = "broadcasts"
description = '''Hi, I&#x27;m not familiar with Wireshark and how to interpret the output from it. I have output like this : Sender MAC: IETF-VRRP-VRID_64 (00:00:5e:00:01:64) Sender IP: 0.0.0.0 (0.0.0.0) Target MAC: Broadcast (ff:ff:ff:ff:ff:ff)  Target IP: 10.189.8.12 How can I stop the broadcast? I have Cisco N7K as co...'''
date = "2014-04-14T19:36:00Z"
lastmod = "2014-04-15T01:38:00Z"
weight = 31810
keywords = [ "broadcast" ]
aliases = [ "/questions/31810" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [broadcasts](/questions/31810/broadcasts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31810-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm not familiar with Wireshark and how to interpret the output from it. I have output like this :</p><p>Sender MAC: IETF-VRRP-VRID_64 (00:00:5e:00:01:64) Sender IP: 0.0.0.0 (0.0.0.0) Target MAC: Broadcast (ff:ff:ff:ff:ff:ff) Target IP: 10.189.8.12</p><p>How can I stop the broadcast? I have Cisco N7K as core switch. Sender is DHCP Server that is directly connected to N7K</p><p>Regards &amp; Thanks, Syafiq</p></div><div id="question-tags" class="tags-container tags">broadcast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '14, 19:36</strong></p><img src="https://secure.gravatar.com/avatar/9a6bba608748c25e1de67a9478a6d470?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="syafiqrahin&#39;s gravatar image" /><p>syafiqrahin<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="syafiqrahin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Apr '14, 19:41</p></div></div><div id="comments-container-31810" class="comments-container"></div><div id="comment-tools-31810" class="comment-tools"></div><div class="clear"></div><div id="comment-31810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31827"></span>

<div id="answer-container-31827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31827-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I stop the broadcast?</p></blockquote><p>You should <strong>not</strong> try to stop it, until you fully understand why it is happening. VRRP is a redundancy protocol used by network devices to build a cluster. If you <strong>stop</strong> those frames (in whatever way you manage to do so), you could break the cluster.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31827" class="comments-container"><span id="31829"></span><div id="comment-31829" class="comment"><div id="post-31829-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thank you.</p><p>Regards, Syafiq</p></div><div id="comment-31829-info" class="comment-info"><span class="comment-age">(15 Apr '14, 01:41)</span> syafiqrahin</div></div></div><div id="comment-tools-31827" class="comment-tools"></div><div class="clear"></div><div id="comment-31827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

