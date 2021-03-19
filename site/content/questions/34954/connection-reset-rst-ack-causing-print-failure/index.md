+++
type = "question"
title = "Connection reset (RST, ACK) causing print failure"
description = '''Hi all! I have an Epson 9600 wide format printer, we&#x27;re experiencing issues where the print job fails, always at the end. I&#x27;ve noticed that every time the job fails, the PC is sending standard ACK packets Every time the job succeeds, the last two ACK packets have the PSH flag set too. Output from a ...'''
date = "2014-07-28T22:37:00Z"
lastmod = "2015-04-17T14:19:00Z"
weight = 34954
keywords = [ "reset", "connection", "printer", "tcp" ]
aliases = [ "/questions/34954" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Connection reset (RST, ACK) causing print failure](/questions/34954/connection-reset-rst-ack-causing-print-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34954-score" class="post-score" title="current number of votes">0</div><span id="post-34954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all!</p><p>I have an Epson 9600 wide format printer, we're experiencing issues where the print job fails, <em>always</em> at the end.</p><p>I've noticed that every time the job fails, the PC is sending standard ACK packets<br />
Every time the job succeeds, the last two ACK packets have the PSH flag set too.</p><p>Output from a successful job: <a href="https://www.cloudshark.org/captures/47c1282d852d">https://www.cloudshark.org/captures/47c1282d852d</a></p><p>Output from a failed job: <a href="https://www.cloudshark.org/captures/d54ab50636c1">https://www.cloudshark.org/captures/d54ab50636c1</a></p><p>I'm stumped, to be perfectly honest I'm shooting in the dark. Tried LPR vs RAW printing, tried different machines etc, still failing. Any help would be greatly appreciated!</p><p>edit: bit of extra info, printing from a mac works fine every time. o.O different TCP/IP versions/settings/something?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reset" rel="tag" title="see questions tagged &#39;reset&#39;">reset</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-printer" rel="tag" title="see questions tagged &#39;printer&#39;">printer</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '14, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/02162838d19da496e64134e336f99d0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikeAnthony&#39;s gravatar image" /><p><span>MikeAnthony</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikeAnthony has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jul '14, 00:58</strong> </span></p></div></div><div id="comments-container-34954" class="comments-container"><span id="34958"></span><div id="comment-34958" class="comment"><div id="post-34958-score" class="comment-score">1</div><div class="comment-text"><p>both traces have the same source 192.168.1.91, is it a intermittent issue?</p><p>I saw packets going through without issue initially until the source issued RST all of a sudden. Looks like we should understand when and why TCP would send out RST proactively. Weird...</p></div><div id="comment-34958-info" class="comment-info"><span class="comment-age">(29 Jul '14, 01:10)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="34961"></span><div id="comment-34961" class="comment"><div id="post-34961-score" class="comment-score"></div><div class="comment-text"><p>Yep, issue is intermittent. It seems I can completely power cycle the printer (power cord out, turn on to drain residual charge, power back in) and it will successfully print a job (barring issues with the PDF).<br />
Subsequent jobs will then fail until I power cycle the printer again.</p></div><div id="comment-34961-info" class="comment-info"><span class="comment-age">(29 Jul '14, 01:15)</span> <span class="comment-user userinfo">MikeAnthony</span></div></div><span id="41532"></span><div id="comment-41532" class="comment"><div id="post-41532-score" class="comment-score"></div><div class="comment-text"><p>First I have a question. Are printing the same job or are they different?</p></div><div id="comment-41532-info" class="comment-info"><span class="comment-age">(17 Apr '15, 04:01)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="41538"></span><div id="comment-41538" class="comment"><div id="post-41538-score" class="comment-score">1</div><div class="comment-text"><p>Average RTT time in failed pcap is 2 ms,before sending RST 1.91 waits for almost 20 ms for an ack to come but it didnt receive.so in failure cases you can see that if this pattern is repeating,if yes than there could be some setting on device or system which is causing this.Other thing to find out is why 1.38 didnt sent an ack.</p></div><div id="comment-41538-info" class="comment-info"><span class="comment-age">(17 Apr '15, 06:28)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-34954" class="comment-tools"></div><div class="clear"></div><div id="comment-34954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41551"></span>

<div id="answer-container-41551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41551-score" class="post-score" title="current number of votes">0</div><span id="post-41551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A lot of important information is defined at the session start, which we can´t see here. So maybe we need it some day. The main difference between the traces as we can see is the termination of the session. In the successfull trace we can the a normal 4 way session closing (FIN-ACK)</p><p>In the failure trace we see an anormal session termination indicated by the RST-Bit. In the most cases I analyzed was the root cause a problem above Layer 4.</p><p>Maybe it is a driver problem at the 192.168.1.91 because this machine sends the RST apparently more or less unmotivated.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '15, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span> </br></br></p></div></div><div id="comments-container-41551" class="comments-container"></div><div id="comment-tools-41551" class="comment-tools"></div><div class="clear"></div><div id="comment-41551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

