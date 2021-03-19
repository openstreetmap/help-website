+++
type = "question"
title = "Wireshark isn&#x27;t detecting my 3G modem"
description = '''My Huawei 3G USB modem is not listed on the interface list. I am using Wireshark(1.8.7) on Windows8-64bit. My device is Huawei E1550(model).. This device used to work with Wireshark(1.6.8) on windows7-32bit....'''
date = "2013-05-30T22:11:00Z"
lastmod = "2013-06-05T23:23:00Z"
weight = 21633
keywords = [ "huawei", "modem", "3g" ]
aliases = [ "/questions/21633" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark isn't detecting my 3G modem](/questions/21633/wireshark-isnt-detecting-my-3g-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21633-score" class="post-score" title="current number of votes">0</div><span id="post-21633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My Huawei 3G USB modem is not listed on the interface list. I am using Wireshark(1.8.7) on Windows8-64bit. My device is Huawei E1550(model)..</p><p>This device used to work with Wireshark(1.6.8) on windows7-32bit....</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-huawei" rel="tag" title="see questions tagged &#39;huawei&#39;">huawei</span> <span class="post-tag tag-link-modem" rel="tag" title="see questions tagged &#39;modem&#39;">modem</span> <span class="post-tag tag-link-3g" rel="tag" title="see questions tagged &#39;3g&#39;">3g</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '13, 22:11</strong></p><img src="https://secure.gravatar.com/avatar/363cb255b97d9cdd63c7ac2ba836a3c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ska00sh&#39;s gravatar image" /><p><span>ska00sh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ska00sh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '13, 11:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-21633" class="comments-container"></div><div id="comment-tools-21633" class="comment-tools"></div><div class="clear"></div><div id="comment-21633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21646"></span>

<div id="answer-container-21646" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21646-score" class="post-score" title="current number of votes">0</div><span id="post-21646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you restart the WinPcap NPF driver <strong>after</strong> you inserted the USB stick? If no, please try this:</p><ul><li>Insert the USB stick</li><li>Start a DOS box <strong>as administrator</strong></li><li>run: <strong>sc stop npf</strong></li><li>run: <strong>sc start npf</strong></li><li>check if the interface is now listed: <strong>dumpcap -D -M</strong></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '13, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '13, 02:45</strong> </span></p></div></div><div id="comments-container-21646" class="comments-container"></div><div id="comment-tools-21646" class="comment-tools"></div><div class="clear"></div><div id="comment-21646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21680"></span>

<div id="answer-container-21680" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21680-score" class="post-score" title="current number of votes">0</div><span id="post-21680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>3G USB modem ... windows7</p></blockquote><p><a href="http://www.winpcap.org/misc/faq.htm#Q-5">WinPcap doesn't support PPP interfaces on Windows 7</a>, and mobile phone network "modems" run PPP over the modem phone connection, and Wireshark uses WinPcap for packet capture, so those devices are not supported in Wireshark on Windows Vista, 7, and 8.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '13, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21680" class="comments-container"><span id="21683"></span><div id="comment-21683" class="comment"><div id="post-21683-score" class="comment-score"></div><div class="comment-text"><p>Just a comment Guy, lose the scare quotes. :)</p><p>There's nothing inaccurate about the term "modem" here, as they literally are performing QAM modulation/demodulation. Also it's not a "phone connection". HSPA data service does not touch a telephone switch, rather the line of path is from the device to the radio network to a GPRS Core (SGSN/GGSN nodes, effectively IP routers for the purpose of user IP packets) to an ISP. In older architectures it wasn't quite the case and carrier telephone switches actually carried IP payload, but from GPRS onwards it's really a packet-switched core infrastructure for all data service. In fact it's come full circle from LTE/EPC and beyond, as the telephone side has all gone to SIP/RTP over a fully IP network model.</p><p>You're correct on the point about PPP support on Windows 7 though. I found this out for myself as well.</p></div><div id="comment-21683-info" class="comment-info"><span class="comment-age">(31 May '13, 19:41)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="21788"></span><div id="comment-21788" class="comment"><div id="post-21788-score" class="comment-score"></div><div class="comment-text"><p>That's disappointing....</p></div><div id="comment-21788-info" class="comment-info"><span class="comment-age">(05 Jun '13, 23:23)</span> <span class="comment-user userinfo">ska00sh</span></div></div></div><div id="comment-tools-21680" class="comment-tools"></div><div class="clear"></div><div id="comment-21680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

