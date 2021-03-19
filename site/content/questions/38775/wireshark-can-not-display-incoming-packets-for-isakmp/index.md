+++
type = "question"
title = "Wireshark can not display incoming packets for ISAKMP."
description = '''Hi all, I am using Shrew soft as VPN client to establish VPN tunnel. The tunnel up and work properly. But, i used Wireshark (version 1.12.2) to capture and filter (only ISAKMP)- i only see outgoing packets not see incoming packets. Could you please help to this? Sorry for my English, Thanks a lot,'''
date = "2014-12-30T01:58:00Z"
lastmod = "2015-01-08T00:25:00Z"
weight = 38775
keywords = [ "ipsec" ]
aliases = [ "/questions/38775" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark can not display incoming packets for ISAKMP.](/questions/38775/wireshark-can-not-display-incoming-packets-for-isakmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38775-score" class="post-score" title="current number of votes">0</div><span id="post-38775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am using Shrew soft as VPN client to establish VPN tunnel. The tunnel up and work properly. But, i used Wireshark (version 1.12.2) to capture and filter (only ISAKMP)- i only see outgoing packets not see incoming packets. Could you please help to this?</p><p>Sorry for my English, Thanks a lot,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipsec" rel="tag" title="see questions tagged &#39;ipsec&#39;">ipsec</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '14, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/737367970359573175a9e3cf21495321?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%E1%BA%A5u%20Con&#39;s gravatar image" /><p><span>Gấu Con</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gấu Con has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Dec '14, 02:01</strong> </span></p></div></div><div id="comments-container-38775" class="comments-container"><span id="38776"></span><div id="comment-38776" class="comment"><div id="post-38776-score" class="comment-score"></div><div class="comment-text"><p>I want to update:</p><p>OS: Windows 8 64bit Shrewsoft VPN client: 2.2.2 Wireshark: 1.12.2</p><p>Thanks a lot</p></div><div id="comment-38776-info" class="comment-info"><span class="comment-age">(30 Dec '14, 02:07)</span> <span class="comment-user userinfo">Gấu Con</span></div></div></div><div id="comment-tools-38775" class="comment-tools"></div><div class="clear"></div><div id="comment-38775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="38786"></span>

<div id="answer-container-38786" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38786-score" class="post-score" title="current number of votes">1</div><span id="post-38786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gấu Con has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark on Windows is using <a href="http://www.winpcap.org/">WinPcap</a>, which hooks itself into the windows networking stack to get frames. If the VPN client is "in front" of WinPcap, it will process the ISAKMP frames before WinPcap ever sees them. We have had reports about similar effects with all sort of security software (VPN clients, Endpoint Security, etc.) in the past. There isn't much you can do about it. If you need the ISAKMP traffic, you can</p><ul><li>capture in front of your windows client, on a switch mirror port</li><li>try to use Microsoft Network Monitor, as it uses a different way to get network frames than WinPcap.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38786" class="comments-container"><span id="38815"></span><div id="comment-38815" class="comment"><div id="post-38815-score" class="comment-score"></div><div class="comment-text"><p>Dear,</p><p>Thank you very much for your info.!</p></div><div id="comment-38815-info" class="comment-info"><span class="comment-age">(30 Dec '14, 18:14)</span> <span class="comment-user userinfo">Gấu Con</span></div></div></div><div id="comment-tools-38786" class="comment-tools"></div><div class="clear"></div><div id="comment-38786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38936"></span>

<div id="answer-container-38936" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38936-score" class="post-score" title="current number of votes">1</div><span id="post-38936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>You can generate directly pcap with Shrew : <a href="https://www.shrew.net/static/help-2.2.x/html/Shrew%20Soft%20VPN%20Client%20Administrators%20Guide.html">https://www.shrew.net/static/help-2.2.x/html/Shrew%20Soft%20VPN%20Client%20Administrators%20Guide.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '15, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/d62b869ec385c6bbc2c04dc7176e8ea8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexis%20La%20Goutte&#39;s gravatar image" /><p><span>Alexis La Go...</span><br />
<span class="score" title="110 reputation points">110</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexis La Goutte has one accepted answer">25%</span></p></div></div><div id="comments-container-38936" class="comments-container"></div><div id="comment-tools-38936" class="comment-tools"></div><div class="clear"></div><div id="comment-38936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38781"></span>

<div id="answer-container-38781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38781-score" class="post-score" title="current number of votes">0</div><span id="post-38781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">VPN client interference</a> is a known issue, outside the realm of Wireshark unfortunately.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '14, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-38781" class="comments-container"></div><div id="comment-tools-38781" class="comment-tools"></div><div class="clear"></div><div id="comment-38781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

