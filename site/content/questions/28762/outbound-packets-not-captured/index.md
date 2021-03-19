+++
type = "question"
title = "Outbound Packets not captured"
description = '''I know this question has been asked here many times but I found no convincing answer as to the root cause of it. When capturing, outbound packets are not captured when the NIC has DNE LightWeight Filter enabled. DNE is required for my SonicWALL VPN client. My question is 1) What is the reason for th...'''
date = "2014-01-10T00:14:00Z"
lastmod = "2014-01-15T09:58:00Z"
weight = 28762
keywords = [ "dne", "outgoing", "outbound" ]
aliases = [ "/questions/28762" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Outbound Packets not captured](/questions/28762/outbound-packets-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28762-score" class="post-score" title="current number of votes">0</div><span id="post-28762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know this question has been asked here many times but I found no convincing answer as to the root cause of it. When capturing, outbound packets are not captured when the NIC has DNE LightWeight Filter enabled. DNE is required for my SonicWALL VPN client. My question is 1) What is the reason for this 2) Is there a workaround to capture outbound packets without disabling DNE LightWeight Filter. Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dne" rel="tag" title="see questions tagged &#39;dne&#39;">dne</span> <span class="post-tag tag-link-outgoing" rel="tag" title="see questions tagged &#39;outgoing&#39;">outgoing</span> <span class="post-tag tag-link-outbound" rel="tag" title="see questions tagged &#39;outbound&#39;">outbound</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '14, 00:14</strong></p><img src="https://secure.gravatar.com/avatar/ee4540808f9394e0e5c711619b6e8b07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Budao&#39;s gravatar image" /><p><span>Budao</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Budao has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jan '14, 07:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-28762" class="comments-container"></div><div id="comment-tools-28762" class="comment-tools"></div><div class="clear"></div><div id="comment-28762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28787"></span>

<div id="answer-container-28787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28787-score" class="post-score" title="current number of votes">0</div><span id="post-28787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try the following</p><ul><li>uninstall Wireshark, <strong>including</strong> WinPcap (the later is actually more important)</li><li>uninstall the VPN client</li><li>Reboot</li><li>re-install Wireshark + WinPcap</li><li>then re-install the VPN client</li></ul><p>the order of installation is important. WinPcap first, then the VPN client including DNE.</p><p>Please report back if it works on your system.</p><p>If not, your options are:</p><ul><li>disable DNE</li><li>Boot the system with a Linux CD and run Wireshark there</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '14, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28787" class="comments-container"><span id="28926"></span><div id="comment-28926" class="comment"><div id="post-28926-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for taking time to answer my question. I followed your instructions but the issue remains. Disabling DNE is difficult because I use the SonicWALL VPN Client all the time. As for the second option, I use Wireshark extensively and I don't think that's a better option. Any more ideas?</p></div><div id="comment-28926-info" class="comment-info"><span class="comment-age">(15 Jan '14, 09:14)</span> <span class="comment-user userinfo">Budao</span></div></div><span id="28928"></span><div id="comment-28928" class="comment"><div id="post-28928-score" class="comment-score"></div><div class="comment-text"><p>You could try to capture the traffic with Microsoft Network Monitor (maybe that's compatible with DNE), or it's successor MessageAnalyzer and use Wireshark only to analyze the frames.</p></div><div id="comment-28928-info" class="comment-info"><span class="comment-age">(15 Jan '14, 09:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28787" class="comment-tools"></div><div class="clear"></div><div id="comment-28787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

