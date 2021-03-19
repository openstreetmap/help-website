+++
type = "question"
title = "Capture filter greyed out in red"
description = '''I&#x27;m not sure what I&#x27;m doing wrong. I have my router configured to use rpcapd. I can connect using the remote interface dialogue box &amp;amp; see a list of interfaces on the router. Previously, I was able also to input a capture filter &quot;host 192.168.1.53 or host 192.168.1.65&quot; but now, whenever I enter t...'''
date = "2016-11-10T14:49:00Z"
lastmod = "2016-11-11T23:35:00Z"
weight = 57284
keywords = [ "capture-filter" ]
aliases = [ "/questions/57284" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter greyed out in red](/questions/57284/capture-filter-greyed-out-in-red)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57284-score" class="post-score" title="current number of votes">0</div><span id="post-57284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm not sure what I'm doing wrong. I have my router configured to use rpcapd. I can connect using the remote interface dialogue box &amp; see a list of interfaces on the router. Previously, I was able also to input a capture filter "host 192.168.1.53 or host 192.168.1.65" but now, whenever I enter this, or even a single "host 192.168.1.53", the capture filter portion gets greyed out in red as through the syntax is wrong &amp; the start button is de-activated.</p><p>I can't think what could have changed or what I'm doing wrong? Any suggestions? Apologies in advances for noob issues.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '16, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/ec61cefc1ea8753d96cfbdd7fdc72cad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madumi&#39;s gravatar image" /><p><span>Madumi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madumi has no accepted answers">0%</span></p></div></div><div id="comments-container-57284" class="comments-container"><span id="57285"></span><div id="comment-57285" class="comment"><div id="post-57285-score" class="comment-score"></div><div class="comment-text"><p>I don't dare yet to post this as an answer as I have never seen the remote interface dialogue box, but the new start page of Wireshark wants you to select one or more interfaces before starting to fill the capture filter form field. Each of the interfaces may have its own capture filter, but only the one for the selected interface is shown in the capture filter field.</p><p>Try that there in the remote interface dialogue box and let me know if it worked, if so, I'll make it an answer.</p></div><div id="comment-57285-info" class="comment-info"><span class="comment-age">(10 Nov '16, 14:54)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="57287"></span><div id="comment-57287" class="comment"><div id="post-57287-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply sindy.</p><p>Sadly that doesn't seem to help. Whether I try to write the capture filter in the remote capture dialogue box, or whether I try to write it in the main screen after selecting for eg. the br0 interface (see screen capture), the filter is greyed out in red.</p><p>What vexes me is that it worked the first few times I tried it. Now however, it doesn't seem to accept the filters I'm tying in.</p><p>Any ideas?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Clipboard01_9a5GLhI.jpg" width="395" height="154" /></p></div><div id="comment-57287-info" class="comment-info"><span class="comment-age">(10 Nov '16, 21:18)</span> <span class="comment-user userinfo">Madumi</span></div></div><span id="57290"></span><div id="comment-57290" class="comment"><div id="post-57290-score" class="comment-score"></div><div class="comment-text"><p>Wilde guess: did you previously capture (without filter) first and then added a filter for subsequent capture?</p></div><div id="comment-57290-info" class="comment-info"><span class="comment-age">(10 Nov '16, 22:19)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="57291"></span><div id="comment-57291" class="comment"><div id="post-57291-score" class="comment-score"></div><div class="comment-text"><p>Yes, I tried capturing without a filter first (it captures traffic from all the IP's without any problem)... I've tried starting it different ways, together with stopping rpcapd &amp; restarting...</p></div><div id="comment-57291-info" class="comment-info"><span class="comment-age">(10 Nov '16, 22:57)</span> <span class="comment-user userinfo">Madumi</span></div></div><span id="57302"></span><div id="comment-57302" class="comment"><div id="post-57302-score" class="comment-score"></div><div class="comment-text"><p>For what it's worth, I tried re-installing wireshark &amp; erasing preferences, but it still seems to be having the same problem. Is the syntax host 192.168.1.53 somehow wrong?</p></div><div id="comment-57302-info" class="comment-info"><span class="comment-age">(11 Nov '16, 03:42)</span> <span class="comment-user userinfo">Madumi</span></div></div></div><div id="comment-tools-57284" class="comment-tools"></div><div class="clear"></div><div id="comment-57284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57330"></span>

<div id="answer-container-57330" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57330-score" class="post-score" title="current number of votes">0</div><span id="post-57330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, this has got to sound weird...</p><p>I found a "fix" by:</p><ol><li>selecting only one interface (eg. br0)</li><li>exiting from the capture interfaces dialogue box,</li><li>turning caps lock on and off</li><li>capture filters now turned green...</li></ol><p>Not sure why this could have fixed the bad syntax block, but it's working. Hope it helps someone else :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '16, 23:35</strong></p><img src="https://secure.gravatar.com/avatar/ec61cefc1ea8753d96cfbdd7fdc72cad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madumi&#39;s gravatar image" /><p><span>Madumi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madumi has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '16, 09:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-57330" class="comments-container"></div><div id="comment-tools-57330" class="comment-tools"></div><div class="clear"></div><div id="comment-57330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

