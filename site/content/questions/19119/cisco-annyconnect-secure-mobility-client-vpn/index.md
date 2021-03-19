+++
type = "question"
title = "Cisco AnnyConnect Secure mobility client VPN"
description = '''Hi, Windows 8 64b, Wireshark 1.8.5  instalation OK  Cisco AnnyConnect Secure mobility client VPN  - not visible adapter -&amp;gt; nothing captured in this VPN Can you help me? Or can some new version of Wireshark, compatible with win8, help me? Pavel'''
date = "2013-03-04T04:57:00Z"
lastmod = "2013-03-11T03:14:00Z"
weight = 19119
keywords = [ "cisco", "annyconnect" ]
aliases = [ "/questions/19119" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Cisco AnnyConnect Secure mobility client VPN](/questions/19119/cisco-annyconnect-secure-mobility-client-vpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19119-score" class="post-score" title="current number of votes">0</div><span id="post-19119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Windows 8 64b, Wireshark 1.8.5</p><ul><li>instalation OK</li></ul><p>Cisco AnnyConnect Secure mobility client VPN - not visible adapter -&gt; nothing captured in this VPN</p><p>Can you help me? Or can some new version of Wireshark, compatible with win8, help me?</p><p>Pavel</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-annyconnect" rel="tag" title="see questions tagged &#39;annyconnect&#39;">annyconnect</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '13, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/5d07dbd8e18feaefc30b96b8682505c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kailer&#39;s gravatar image" /><p><span>kailer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kailer has no accepted answers">0%</span></p></div></div><div id="comments-container-19119" class="comments-container"></div><div id="comment-tools-19119" class="comment-tools"></div><div class="clear"></div><div id="comment-19119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19120"></span>

<div id="answer-container-19120" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19120-score" class="post-score" title="current number of votes">2</div><span id="post-19120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kailer has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>More a WinPCap issue than Wireshark. I haven't any experience with this VPN client but it's likely that WinPCap can't use this interface, especially as you say it doesn't show up.</p><p>Try Network Monitor (NM) from Microsoft, Wireshark can read captures made by NM.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '13, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19120" class="comments-container"><span id="19351"></span><div id="comment-19351" class="comment"><div id="post-19351-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. You are right.</p><p>The best solution is the new WinPCap 4.1.3 now. It is compatible with Windows 8 and work fine with Cisco client.</p><p>bye</p></div><div id="comment-19351-info" class="comment-info"><span class="comment-age">(11 Mar '13, 03:14)</span> <span class="comment-user userinfo">kailer</span></div></div></div><div id="comment-tools-19120" class="comment-tools"></div><div class="clear"></div><div id="comment-19120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19166"></span>

<div id="answer-container-19166" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19166-score" class="post-score" title="current number of votes">1</div><span id="post-19166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The 'problem' with the AnyConnect virtual adapter is, that it is disabled until you established a vpn tunnel. I <strong>guess</strong> that WinPcap is unable to see the adapter as it was disabled when the WinPcap NPF service was started, at least some tests let me assume this. So here is what you can try:</p><ul><li>establish a VPN tunnel</li><li>stop Wireshark</li><li>stop WinPcap NPF service: sc stop npf (in an elevated DOS box - run DOS box as Administrator!!)</li><li>start WinPcap NPF service: sc start npf</li><li>start Wireshark</li></ul><p>If you don't see the AnyConnect adapter now, WinPcap does not support that type of virtual interfaces and you are out of luck. Please use Microsoft Network Monitor, as <span>@grahamb</span> suggested.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-19166" class="comments-container"></div><div id="comment-tools-19166" class="comment-tools"></div><div class="clear"></div><div id="comment-19166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

