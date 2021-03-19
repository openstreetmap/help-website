+++
type = "question"
title = "Wireshark can&#x27;t capture packets after a DDOS attack"
description = '''The OS is windows 2003 SP2 The version of wireshark is 1.0.7 and the winpcap is the default one which follows with wireshark. The problem is that wireshark will not work after a ddos attack(larger thant 1Gb/s 100,000packets/s). When I click the capture button a error form shows: &quot;The capture session...'''
date = "2011-06-05T07:04:00Z"
lastmod = "2011-06-07T05:59:00Z"
weight = 4384
keywords = [ "ddos" ]
aliases = [ "/questions/4384" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark can't capture packets after a DDOS attack](/questions/4384/wireshark-cant-capture-packets-after-a-ddos-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4384-score" class="post-score" title="current number of votes">0</div><span id="post-4384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The OS is windows 2003 SP2 The version of wireshark is 1.0.7 and the winpcap is the default one which follows with wireshark.</p><p>The problem is that wireshark will not work after a ddos attack(larger thant 1Gb/s 100,000packets/s). When I click the capture button a error form shows: "The capture session could not be initiated (driver error: not enough memory to allocate the kernel buffer)." I must restart the OS to let it work correctly again.</p><p>I want to know which cause this phenomenon and if there is a way to resolve this problem whiout restarting the system. Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ddos" rel="tag" title="see questions tagged &#39;ddos&#39;">ddos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '11, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/a2a155d18db302c05a267b61b28859d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wangxr1985&#39;s gravatar image" /><p><span>wangxr1985</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wangxr1985 has no accepted answers">0%</span></p></div></div><div id="comments-container-4384" class="comments-container"><span id="4391"></span><div id="comment-4391" class="comment"><div id="post-4391-score" class="comment-score"></div><div class="comment-text"><p>Thank you. But both reinstalling wireshark/winpcap and reloading NPF driver have no effect.Wireshark still shows the same error message when I click the capture button.</p></div><div id="comment-4391-info" class="comment-info"><span class="comment-age">(05 Jun '11, 21:49)</span> <span class="comment-user userinfo">wangxr1985</span></div></div><span id="4417"></span><div id="comment-4417" class="comment"><div id="post-4417-score" class="comment-score"></div><div class="comment-text"><p>Disabling and re-enabling the network card needs to restart the server. I try to do that by a batch file: (devcon disable XXX &amp;&amp; devcon enable XXX). But it let me reboot the system: "Not all of 1 device(s) disabled, at least one requires reboot to complete the operation." Changing the swap file need a rebooting,too.</p><p>So I can't confirm whether these methods will resolve my problem,because the phenomenon will also disappear after rebooting even if I do nothing about it.</p><p>So can anyone give me a method which don't need to reboot the system?</p></div><div id="comment-4417-info" class="comment-info"><span class="comment-age">(06 Jun '11, 18:40)</span> <span class="comment-user userinfo">wangxr1985</span></div></div></div><div id="comment-tools-4384" class="comment-tools"></div><div class="clear"></div><div id="comment-4384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="4386"></span>

<div id="answer-container-4386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4386-score" class="post-score" title="current number of votes">1</div><span id="post-4386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might try <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges#Windows">reloading the NPF driver</a> using <code>net stop npf</code> followed by <code>net start npf</code>, although it sounds like you may not have enough available kernel memory to start a capture.</p><p><strong>Edit:</strong> Someone more knowledgeable than I suggested disabling and re-enabling your network card(s).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '11, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jun '11, 08:55</strong> </span></p></div></div><div id="comments-container-4386" class="comments-container"></div><div id="comment-tools-4386" class="comment-tools"></div><div class="clear"></div><div id="comment-4386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4418"></span>

<div id="answer-container-4418" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4418-score" class="post-score" title="current number of votes">1</div><span id="post-4418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Now I have Disabled and re-enabled the network card by using command "netsh" , but the problem is still there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '11, 21:39</strong></p><img src="https://secure.gravatar.com/avatar/a2a155d18db302c05a267b61b28859d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wangxr1985&#39;s gravatar image" /><p><span>wangxr1985</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wangxr1985 has no accepted answers">0%</span></p></div></div><div id="comments-container-4418" class="comments-container"></div><div id="comment-tools-4418" class="comment-tools"></div><div class="clear"></div><div id="comment-4418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4385"></span>

<div id="answer-container-4385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4385-score" class="post-score" title="current number of votes">0</div><span id="post-4385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would uninstall wireshark and winpcap, and reinstall them. Also, I would delete any temporary internet files. You can do these things without rebooting.<br />
To gain more memory I would increase the swap file size, but this will require a reboot. I would check the event logs for any additional information about the problem also. DDoS attacks are difficult by nature to avoid. However, I've read recently Cisco has released RTBH, Remotely Triggered Black Holing, as a method of managing those kinds of attacks.</p><p>Best of luck, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '11, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4385" class="comments-container"></div><div id="comment-tools-4385" class="comment-tools"></div><div class="clear"></div><div id="comment-4385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4397"></span>

<div id="answer-container-4397" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4397-score" class="post-score" title="current number of votes">0</div><span id="post-4397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds as though the DDoS flooded your memory, which then overflowed to the.swap file, and may have corrupted it. If you have a 2nd hard drive installed or another partition on the existing hard drive you can add another swapfile. Http://support.microsoft.com/kb/307886</p><p>This will require a reboot to become effective, but only once.</p><p>Also, you could run ccleaner to cleanup the system and check/correct the registry, just be sure to let it back your registry up first. This does not require a reboot. Ccleaner is a free download.</p><p>Hope this helps John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '11, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4397" class="comments-container"></div><div id="comment-tools-4397" class="comment-tools"></div><div class="clear"></div><div id="comment-4397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4422"></span>

<div id="answer-container-4422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4422-score" class="post-score" title="current number of votes">0</div><span id="post-4422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can also try upgrading your nic driver to the latest one from the nic manufacturer. Your nic will rebind during the update and this will not require a reboot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '11, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4422" class="comments-container"></div><div id="comment-tools-4422" class="comment-tools"></div><div class="clear"></div><div id="comment-4422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

