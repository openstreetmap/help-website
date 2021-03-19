+++
type = "question"
title = "tshark option -M (together with -D)"
description = '''Hi, is there a reason why tshark does not offer the option -M (together with -D), comparable to dumpcap? dumpcap -D -M dumps the IP address of the interface, which is quite usefull to identify the right NIC, if there are several similar (or identical) ones in a machine. BTW: tshark does not complain...'''
date = "2012-05-07T05:50:00Z"
lastmod = "2012-05-07T15:56:00Z"
weight = 10726
keywords = [ "interfacelist", "tshark" ]
aliases = [ "/questions/10726" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark option -M (together with -D)](/questions/10726/tshark-option-m-together-with-d)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10726-score" class="post-score" title="current number of votes">0</div><span id="post-10726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>is there a reason why tshark does not offer the option -M (together with -D), comparable to dumpcap? dumpcap -D -M dumps the IP address of the interface, which is quite usefull to identify the right NIC, if there are several similar (or identical) ones in a machine. BTW: tshark does not complain about any unknown option (e.g. -M), if used after -D.</p><p><strong>tshark 1.7.1 Windows</strong></p><blockquote><p><code>C:\tshark.exe -v</code><br />
<code>TShark 1.7.1 (SVN Rev 41970 from /trunk)</code></p><p><code>C:\dumpcap.exe -D</code><br />
<code>1. \Device\NPF_{9A6C7DD4-7E39-4309-8B15-C5FAD27E5878} (Intel(R) 82567LM Gigabit Network Connection)</code></p><p><code>C:\dumpcap.exe -D -M</code><br />
<code>1. \Device\NPF_{9A6C7DD4-7E39-4309-8B15-C5FAD27E5878}   Intel(R) 82567LM Gigabit Network Connection     fe80::351f:fe35:b686:7c36,192.168.90.51 network</code></p><p><code>C:\tshark.exe -D -M</code><br />
<code>1. \Device\NPF_{9A6C7DD4-7E39-4309-8B15-C5FAD27E5878} (Intel(R) 82567LM Gigabit Network Connection)</code></p></blockquote><p><strong>tshark 1.6.2 Linux</strong></p><blockquote><p><code>[email protected]:~# tshark -v</code><br />
<code>TShark 1.6.2</code></p><p><code>[email protected]:~# dumpcap -D</code><br />
<code>1. eth0</code><br />
<code>2. lo</code><br />
</p><p><code>[email protected]:~# dumpcap -D -M</code><br />
<code>1. eth0       192.168.30.151,fe80::20c:29ff:fed5:4585 network</code><br />
<code>2. lo     127.0.0.1,::1   loopback</code><br />
</p><p><code>[email protected]:~# tshark -D -M</code><br />
<code>1. eth0</code><br />
<code>2. lo</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interfacelist" rel="tag" title="see questions tagged &#39;interfacelist&#39;">interfacelist</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '12, 16:13</strong> </span></p></div></div><div id="comments-container-10726" class="comments-container"></div><div id="comment-tools-10726" class="comment-tools"></div><div class="clear"></div><div id="comment-10726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10746"></span>

<div id="answer-container-10746" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10746-score" class="post-score" title="current number of votes">0</div><span id="post-10746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kurt Knochner has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The option doesn't do anything in TShark and Wireshark as no-one has coded it yet.</p><p>Please raise an enhancement request on <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-10746" class="comments-container"><span id="10753"></span><div id="comment-10753" class="comment"><div id="post-10753-score" class="comment-score"></div><div class="comment-text"><p>I just wanted to know if there is any special reason for that, before I raise an enhancement request.</p><p>Regards<br />
Kurt</p></div><div id="comment-10753-info" class="comment-info"><span class="comment-age">(07 May '12, 15:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10755"></span><div id="comment-10755" class="comment"><div id="post-10755-score" class="comment-score"></div><div class="comment-text"><p>Personally I don't really need it as dumpcap is always available (tshark will just call dumpcap anyways). But I can see the wish for uniformity...</p></div><div id="comment-10755-info" class="comment-info"><span class="comment-age">(07 May '12, 15:56)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-10746" class="comment-tools"></div><div class="clear"></div><div id="comment-10746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

