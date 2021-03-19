+++
type = "question"
title = "header checksum error"
description = '''HELLO We are running into a lot of server timeout when sending mails, I download wireshark to check the probelm on running the program i got this error Internet protcol,src 10.200.4.2 Dsy 195.92.231.55  header checksum 0x0000 [incorrect,should be 0x3cf4 , what does this mean? we are behind a check p...'''
date = "2011-02-07T08:34:00Z"
lastmod = "2011-02-07T09:00:00Z"
weight = 2195
keywords = [ "checksum" ]
aliases = [ "/questions/2195" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [header checksum error](/questions/2195/header-checksum-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2195-score" class="post-score" title="current number of votes">1</div><span id="post-2195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HELLO</p><p>We are running into a lot of server timeout when sending mails, I download wireshark to check the probelm on running the program i got this error</p><p>Internet protcol,src 10.200.4.2 Dsy 195.92.231.55 header checksum 0x0000 [incorrect,should be 0x3cf4 , what does this mean? we are behind a check point firewall and a cisco asa5510 firewall</p><p>Cheers</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '11, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/865d67a4db31dad8430573ac4ee9f5b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwc1972&#39;s gravatar image" /><p><span>jwc1972</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwc1972 has no accepted answers">0%</span></p></div></div><div id="comments-container-2195" class="comments-container"></div><div id="comment-tools-2195" class="comment-tools"></div><div class="clear"></div><div id="comment-2195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2197"></span>

<div id="answer-container-2197" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2197-score" class="post-score" title="current number of votes">6</div><span id="post-2197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It means that you probably used Wireshark to capture your own traffic on your local machine. Outgoing packets will most likely show incorrect checksums due to checksum offloading, especially since yours is 0x0000. See <a href="http://wiki.wireshark.org/TCP_Checksum_Verification">http://wiki.wireshark.org/TCP_Checksum_Verification</a>.</p><p>Meaning: what you found is not a problem, it's a result of your capture setup and not an error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '11, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2197" class="comments-container"></div><div id="comment-tools-2197" class="comment-tools"></div><div class="clear"></div><div id="comment-2197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

