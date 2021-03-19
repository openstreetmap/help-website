+++
type = "question"
title = "no outgoing packets"
description = '''Hello. I have fresh install of Windows 7 x64 with Wireshark 1.8.4 and last time I noticed that outgoing packets aren&#x27;t displayed at all no matter which network interface I choose (wired, wireless, VPN). I also have Cisco VPN Client and SonicWALL Global VPN Client installed which may cause problems b...'''
date = "2013-01-12T06:03:00Z"
lastmod = "2014-04-09T03:30:00Z"
weight = 17638
keywords = [ "packets", "outgoing", "outbound" ]
aliases = [ "/questions/17638" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [no outgoing packets](/questions/17638/no-outgoing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17638-score" class="post-score" title="current number of votes">0</div><span id="post-17638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I have fresh install of Windows 7 x64 with Wireshark 1.8.4 and last time I noticed that outgoing packets aren't displayed at all no matter which network interface I choose (wired, wireless, VPN). I also have Cisco VPN Client and SonicWALL Global VPN Client installed which may cause problems but it used to work previously. Did anybody have similar problem? What can I do to display outgoing packets again? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-outgoing" rel="tag" title="see questions tagged &#39;outgoing&#39;">outgoing</span> <span class="post-tag tag-link-outbound" rel="tag" title="see questions tagged &#39;outbound&#39;">outbound</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '13, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/f30d95ef874326d64af2058c54ebbeb9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pitfall&#39;s gravatar image" /><p><span>pitfall</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pitfall has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jan '14, 07:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-17638" class="comments-container"><span id="19971"></span><div id="comment-19971" class="comment"><div id="post-19971-score" class="comment-score"></div><div class="comment-text"><p>I have the same issue but on W7 Ultimate 32-bit: Intel 3945ABG wireless and Broadcom 440x 10/100 Ethernet in a Dell Laptop. I see all incoming packets but no outgoing packets. I also have Sonicwall GVC installed. I am about to uninstall that to see if it helps and will post back if it does.... Any assistance will be gratefully received. Thanks</p></div><div id="comment-19971-info" class="comment-info"><span class="comment-age">(31 Mar '13, 07:38)</span> <span class="comment-user userinfo">Andy M</span></div></div><span id="19972"></span><div id="comment-19972" class="comment"><div id="post-19972-score" class="comment-score"></div><div class="comment-text"><p>Regret no luck with uninstalling GVC. Still only seeing incoming packets both on wireless and with wired. Using Windows Firewall and Windows Security Essentials. No other firewall or AV installed.</p></div><div id="comment-19972-info" class="comment-info"><span class="comment-age">(31 Mar '13, 08:01)</span> <span class="comment-user userinfo">Andy M</span></div></div></div><div id="comment-tools-17638" class="comment-tools"></div><div class="clear"></div><div id="comment-17638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20217"></span>

<div id="answer-container-20217" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20217-score" class="post-score" title="current number of votes">0</div><span id="post-20217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure there is no <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> (AV, Firewall, Endpoint Security, VPN Client, etc.) installed?</p><p>You could boot the system with a bootable Linux CD (BackTrack, Ubuntu, Knoppix) and see if it then works. If it still does not work, I would assume a strange hardware problem. If it works, it must be some software problem on windows, like the mentioned <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> or a driver setting (TCP/IP offloading, chimney, etc.).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20217" class="comments-container"></div><div id="comment-tools-20217" class="comment-tools"></div><div class="clear"></div><div id="comment-20217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20235"></span>

<div id="answer-container-20235" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20235-score" class="post-score" title="current number of votes">0</div><span id="post-20235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Uncheck DNE LightWeight Filter in the adapter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '13, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/ee4540808f9394e0e5c711619b6e8b07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Budao&#39;s gravatar image" /><p><span>Budao</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Budao has no accepted answers">0%</span></p></div></div><div id="comments-container-20235" class="comments-container"><span id="31666"></span><div id="comment-31666" class="comment"><div id="post-31666-score" class="comment-score"></div><div class="comment-text"><p>For Trend Micro Deep Secure users: uncheck "Trend Micro LightWeight Filter Driver"</p></div><div id="comment-31666-info" class="comment-info"><span class="comment-age">(09 Apr '14, 03:30)</span> <span class="comment-user userinfo">kaj</span></div></div></div><div id="comment-tools-20235" class="comment-tools"></div><div class="clear"></div><div id="comment-20235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

