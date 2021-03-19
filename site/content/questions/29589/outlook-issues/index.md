+++
type = "question"
title = "outlook issues"
description = '''https://www.cloudshark.org/captures/5c7260923ba4 I have some users at a remote site connection to an exchange server, the users are complaining that Outlooks locks up at times requiring them to reboot and it takes and it takes a very long time to open. In the trace, I am seeing very long Delta time ...'''
date = "2014-02-09T14:22:00Z"
lastmod = "2014-02-10T06:30:00Z"
weight = 29589
keywords = [ "outlook_issues" ]
aliases = [ "/questions/29589" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [outlook issues](/questions/29589/outlook-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29589-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="https://www.cloudshark.org/captures/5c7260923ba4">https://www.cloudshark.org/captures/5c7260923ba4</a> I have some users at a remote site connection to an exchange server, the users are complaining that Outlooks locks up at times requiring them to reboot and it takes and it takes a very long time to open.</p><p>In the trace, I am seeing very long Delta time between the server and the client as they attempt to communicate with each, I am not sure if it is the server responding or the Client, can someone who know much more the me about packet analysis review this trace an let me know what could be the issue Please</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">outlook_issues</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '14, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/530b55f3fcb17b760aabdf113d9318aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejohnson7&#39;s gravatar image" /><p>ejohnson7<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejohnson7 has no accepted answers">0%</span></p></div></div><div id="comments-container-29589" class="comments-container"></div><div id="comment-tools-29589" class="comment-tools"></div><div class="clear"></div><div id="comment-29589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29628"></span>

<div id="answer-container-29628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29628-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The analysis of the capture file does not show any real network problems (only a few DUP ACK, etc.).</p><p>However, there are some RPC calls that take pretty long.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/outlook_screenshot.png" alt="alt text" /></p><p><strong>But</strong>, after (and during) those RPC calls, the communication continues with pretty good response times, so those long lasting RPC calls are (probably) not a good explanation for <strong>a complete lock up</strong> of Outlook.</p><p>I conclude:</p><ul><li>there is either a local problem on the client that causes the lock up, like interfering software (AV, Firewall, Endpoint Security, Malware) or attempted (and failed) network connections you did not capture.</li><li>or, there is really a problem in the communication between client and server, but you did not capture that traffic and/or the moment when it took place</li><li>or, there is a problem with the server (like not answering the client at all) but you did not capture that either</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 10 Feb '14, 06:52</p></div></div><div id="comments-container-29628" class="comments-container"><span id="29816"></span><div id="comment-29816" class="comment"><div id="post-29816-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much there is a lot of security on these laptops AV, DLP etc and that is causing many problems</p></div><div id="comment-29816-info" class="comment-info"><span class="comment-age">(12 Feb '14, 22:03)</span> ejohnson7</div></div><span id="30256"></span><div id="comment-30256" class="comment"><div id="post-30256-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much my friend</p></div><div id="comment-30256-info" class="comment-info"><span class="comment-age">(27 Feb '14, 20:24)</span> ejohnson7</div></div><span id="30258"></span><div id="comment-30258" class="comment"><div id="post-30258-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-30258-info" class="comment-info"><span class="comment-age">(27 Feb '14, 23:09)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29628" class="comment-tools"></div><div class="clear"></div><div id="comment-29628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

