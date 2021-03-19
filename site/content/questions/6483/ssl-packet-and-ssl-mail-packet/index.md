+++
type = "question"
title = "ssl packet and ssl mail packet"
description = '''Hi, is there any way to tell the difference between normal ssl packet and ssl mail packet?'''
date = "2011-09-21T15:44:00Z"
lastmod = "2011-11-08T00:56:00Z"
weight = 6483
keywords = [ "ssl", "mail" ]
aliases = [ "/questions/6483" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ssl packet and ssl mail packet](/questions/6483/ssl-packet-and-ssl-mail-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6483-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, is there any way to tell the difference between normal ssl packet and ssl mail packet?</p></div><div id="question-tags" class="tags-container tags">ssl mail</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '11, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/61c771620f5b1da1a7fa027cb558f0b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timho1985&#39;s gravatar image" /><p>timho1985<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timho1985 has no accepted answers">0%</span></p></div></div><div id="comments-container-6483" class="comments-container"><span id="6484"></span><div id="comment-6484" class="comment"><div id="post-6484-score" class="comment-score"></div><div class="comment-text"><p>What's 'ssl mail' ?</p></div><div id="comment-6484-info" class="comment-info"><span class="comment-age">(21 Sep '11, 22:29)</span> Jaap ♦</div></div></div><div id="comment-tools-6483" class="comment-tools"></div><div class="clear"></div><div id="comment-6483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6496"></span>

<div id="answer-container-6496" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6496-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If by "ssl mail" you mean SMTP-over-TLS or POP-over-TLS or something such as that, then an "ssl mail packet" <em>IS</em> a normal SSL/TLS packet; there's nothing about HTTP-over-TLS that makes it more "normal" than anything else over SSL/TLS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '11, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-6496" class="comments-container"><span id="7042"></span><div id="comment-7042" class="comment"><div id="post-7042-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I was looking for a pattern to distinguish the packet of POP-over-TLS and HTTP-over-TLS . I guess there isn't then.</p></div><div id="comment-7042-info" class="comment-info"><span class="comment-age">(22 Oct '11, 19:25)</span> timho1985</div></div></div><div id="comment-tools-6496" class="comment-tools"></div><div class="clear"></div><div id="comment-6496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7270"></span>

<div id="answer-container-7270" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7270-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Under normal circumstances, HTTP-over-SSL will use tcp port 443 and POP-over-TLS will use tcp port 995. Of course people can use different ports in which case the ports will not give away it's upper layer protocol (even on the default ports, people can use another protocol, for example use HTTP-over-SSL on port 995).</p><p>One other thing that might help you is to look at the CommonName in the Certificate (look for the Certificate PDU and expand it), this usually has the fully qualified domain name in it. So if it has something like www.example.com, you might assume it's HTTP-over-SSL and if it is pop.example.com, you might assume it is POP-over-TLS. Of course, this can also be forged to be misleading.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7270" class="comments-container"></div><div id="comment-tools-7270" class="comment-tools"></div><div class="clear"></div><div id="comment-7270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

