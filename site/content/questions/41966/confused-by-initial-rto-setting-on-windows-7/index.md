+++
type = "question"
title = "Confused by Initial RTO setting on Windows 7"
description = '''Hi I am developing software for an embedded device, running on a TI DSP. For test purposes I can communicate to this device over a TCP connection from a Windows 7 PC. So I have a Windows 7 PC connected to the device using a private subnet (crossover cable).  When I send a small message to the DSP fr...'''
date = "2015-04-30T06:16:00Z"
lastmod = "2015-04-30T12:44:00Z"
weight = 41966
keywords = [ "retransmissions", "tcp" ]
aliases = [ "/questions/41966" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Confused by Initial RTO setting on Windows 7](/questions/41966/confused-by-initial-rto-setting-on-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41966-score" class="post-score" title="current number of votes">0</div><span id="post-41966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am developing software for an embedded device, running on a TI DSP. For test purposes I can communicate to this device over a TCP connection from a Windows 7 PC.</p><p>So I have a Windows 7 PC connected to the device using a private subnet (crossover cable).</p><p>When I send a small message to the DSP from Windows (200 octets), I see that Windows performs a retransmission at about 900ms after the initial transmission. Using netsh I can see that Windows 'Initial RTO' is set to 3000ms. So I don't understand why Windows is retransmitting at 900ms.</p><p>Please can anyone explain why the retransmission is happening so early?</p><p>(I could paste in the TCP flow captured by Wireshark in text form, but it doesn't display well. Is there a good way of doing this?)</p><p>Best regards</p><p>David</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '15, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/cfb0228285e3c9494d763ba825e7a76c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA_2015&#39;s gravatar image" /><p><span>DavidA_2015</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA_2015 has one accepted answer">50%</span></p></div></div><div id="comments-container-41966" class="comments-container"><span id="41967"></span><div id="comment-41967" class="comment"><div id="post-41967-score" class="comment-score"></div><div class="comment-text"><p>Upload the capture to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and paste the link here.</p></div><div id="comment-41967-info" class="comment-info"><span class="comment-age">(30 Apr '15, 06:17)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="41968"></span><div id="comment-41968" class="comment"><div id="post-41968-score" class="comment-score"></div><div class="comment-text"><p>Here is the capture:</p><p><a href="https://www.cloudshark.org/captures/f660d96bdc85">https://www.cloudshark.org/captures/f660d96bdc85</a></p></div><div id="comment-41968-info" class="comment-info"><span class="comment-age">(30 Apr '15, 06:28)</span> <span class="comment-user userinfo">DavidA_2015</span></div></div></div><div id="comment-tools-41966" class="comment-tools"></div><div class="clear"></div><div id="comment-41966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41970"></span>

<div id="answer-container-41970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41970-score" class="post-score" title="current number of votes">0</div><span id="post-41970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is that this is because of the Push flag being set - this may be a reason why the Win7 PC is impatient and disregards RTO, but I haven't found anything more specific.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '15, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41970" class="comments-container"><span id="41980"></span><div id="comment-41980" class="comment"><div id="post-41980-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your comments.</p><p>I wonder if the initial timeout is affected by the RTT value, which I believe is 300ms for Windows?</p></div><div id="comment-41980-info" class="comment-info"><span class="comment-age">(30 Apr '15, 08:42)</span> <span class="comment-user userinfo">DavidA_2015</span></div></div></div><div id="comment-tools-41970" class="comment-tools"></div><div class="clear"></div><div id="comment-41970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41988"></span>

<div id="answer-container-41988" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41988-score" class="post-score" title="current number of votes">0</div><span id="post-41988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>3000 ms (3 seconds) is the <em>initial</em> receive time out timer value. However, the TCP stack will tune the RTO value during the communication and it should eventually end up being about twice the round-trip time, although <a href="https://tools.ietf.org/html/rfc6298">RFC 6298</a> states that if the calculated RTO is less than one second, than an RTO value of one second should be used.</p><p>There is no reason to wait three full seconds before retransmitting a packet under normal network conditions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '15, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-41988" class="comments-container"><span id="41992"></span><div id="comment-41992" class="comment"><div id="post-41992-score" class="comment-score"></div><div class="comment-text"><p>There is a hotfix out there that allows to reduce the minRTO value in Window: <a href="http://support.microsoft.com/kb/2472264">http://support.microsoft.com/kb/2472264</a></p></div><div id="comment-41992-info" class="comment-info"><span class="comment-age">(30 Apr '15, 12:44)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-41988" class="comment-tools"></div><div class="clear"></div><div id="comment-41988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

