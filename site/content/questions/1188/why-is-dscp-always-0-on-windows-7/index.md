+++
type = "question"
title = "Why is DSCP always 0 on Windows 7?"
description = '''Hi! I know this is not specifically Wireshark problem, but people here are more likely done this themselves. All packets shows DSCP values being 0x00 (default), how can I get DSCP configurations to work in Windows 7 (x64 pro)? I have configured them like this:  I&#x27;ve been defining QoS policy settings...'''
date = "2010-12-01T03:19:00Z"
lastmod = "2011-01-06T05:40:00Z"
weight = 1188
keywords = [ "windows7", "qos" ]
aliases = [ "/questions/1188" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why is DSCP always 0 on Windows 7?](/questions/1188/why-is-dscp-always-0-on-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1188-score" class="post-score" title="current number of votes">0</div><span id="post-1188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I know this is not specifically Wireshark problem, but people here are more likely done this themselves.</p><p>All packets shows DSCP values being 0x00 (default), how can I get DSCP configurations to work in Windows 7 (x64 pro)?</p><p>I have configured them like this:</p><ol><li>I've been defining QoS policy settings from Group Policy Editor: Computer Configuration -&gt; Windows Settings -&gt; Policy-based QoS (<a href="http://4.bp.blogspot.com/_G-OW5TgcJUY/TQTWR62nLsI/AAAAAAAAAHI/iHbjMiqxs1A/s1600/ssh_group_policy.jpg">Screenshot</a>)</li><li>From "Advanced QoS settings" I have ticked the "Control DSCP marking requests from applications and services" with "Ignored: Only QoS policies can specify DSCP value".</li><li>I have QoS Packet Scheduler in Network Card settings turned on.</li></ol><p>Stuff I've tried, without help:</p><ul><li><a href="http://www.wireshark.org/lists/wireshark-users/200809/msg00129.html">Mailing list post about similar problem</a></li><li><a href="http://goo.gl/AlLQf">Registry editing HKEY_LOCAL_MACHINESYSTEMCurrentControlSetservicesTcpipParametersDisableUserTOSSetting</a> (Windows 7 does not have this key and creating one manually did not help)</li><li><a href="http://itexpertvoice.com/home/getting-the-most-out-of-your-windows-7-internet-connection/">qostraffic.exe as suggested by lchappell</a> which can be downloaded from <a href="http://connect.microsoft.com/WNDP/Downloads">Microsoft Connect WNDP</a></li><li>I tried to <em>"Join a Domain"</em> (can be found in Windows 7 <em>Start Menu</em> search) as suggested by <em>packethunter</em>.</li></ul><p><strong>Update:</strong> I found out that using <code>qostraffic.exe -source -tcp -dest 192.168.1.1,80 -throttle 1000 -tc 40,4</code> I can mark the packets if I run it as administrator! But all packets Windows creates "normally" are not marked.</p><p><strong>Update:</strong> This is probably a bug in Windows 7, other people seem to have a same problem in <a href="http://goo.gl/F4faz">QoS Policy MSDN thread</a>.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '10, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/7e497922b6a3060aa8fedd117b0eb7ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ciantic&#39;s gravatar image" /><p><span>Ciantic</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ciantic has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '10, 07:40</strong> </span></p></div></div><div id="comments-container-1188" class="comments-container"><span id="1202"></span><div id="comment-1202" class="comment"><div id="post-1202-score" class="comment-score"></div><div class="comment-text"><p>Have you seen this... http://itexpertvoice.com/home/getting-the-most-out-of-your-windows-7-internet-connection/ It's an interesting article and something to try. Caveat - haven't done myself.</p></div><div id="comment-1202-info" class="comment-info"><span class="comment-age">(02 Dec '10, 00:15)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div><span id="1208"></span><div id="comment-1208" class="comment"><div id="post-1208-score" class="comment-score"></div><div class="comment-text"><p>@lchapell: Thanks, I read it, though did not fix the problem. New thing in the article was the tool <code>qostraffic.exe</code> that creates QoS traffic, and it also unfortunately cannot set the DSCP field in IP header. But should be helpful for debugging further.</p></div><div id="comment-1208-info" class="comment-info"><span class="comment-age">(02 Dec '10, 02:23)</span> <span class="comment-user userinfo">Ciantic</span></div></div></div><div id="comment-tools-1188" class="comment-tools"></div><div class="clear"></div><div id="comment-1188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1648"></span>

<div id="answer-container-1648" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1648-score" class="post-score" title="current number of votes">1</div><span id="post-1648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ciantic has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found an answer, thanks goes to <a href="http://forums.speedguide.net/showthread.php?274421-Windows-7-resets-DiffServ-(DSCP)-to-0x00&amp;p=2378071&amp;viewfull=1#post2378071"><em>xedoc</em> in speedguide.net</a></p><p>Use following registry file to circumvent Domain Joined limitation of Win7:</p><pre><code>Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Tcpip\QoS]
&quot;Do not use NLA&quot;=&quot;1&quot;</code></pre><p>That is, create <em>REG_SZ</em> "<code>Do not use NLA</code>" and set it to "<code>1</code>" and create key "<code>QoS</code>" if it does not exist.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '11, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/7e497922b6a3060aa8fedd117b0eb7ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ciantic&#39;s gravatar image" /><p><span>Ciantic</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ciantic has one accepted answer">100%</span></p></div></div><div id="comments-container-1648" class="comments-container"></div><div id="comment-tools-1648" class="comment-tools"></div><div class="clear"></div><div id="comment-1648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1275"></span>

<div id="answer-container-1275" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1275-score" class="post-score" title="current number of votes">2</div><span id="post-1275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is your computer part of a domain?</p><p>Check out the Microsoft QoS Blog at http://blogs.msdn.com/b/wndp/archive/2009/01/28/qos-in-windows-7.aspx</p><p>The discussion includes a statement from the QoS program manager: "I forgot to point out in my response to Aibulat that a client computer (running Win7 client SKU) has to be domain-joined in order for the local QoS policies to be effective."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '10, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-1275" class="comments-container"><span id="1315"></span><div id="comment-1315" class="comment"><div id="post-1315-score" class="comment-score"></div><div class="comment-text"><p>Very interesting. I tried the <em>"Join a Domain"</em> entry in Start Menu, but all it does it allows me to specify the <em>workgroup</em> again, I did retry specifying it and restarted, did not help. But if that workgroup thing is "joining a domain", I had joined a domain already since I can see other computers in my LAN.</p></div><div id="comment-1315-info" class="comment-info"><span class="comment-age">(11 Dec '10, 07:29)</span> <span class="comment-user userinfo">Ciantic</span></div></div><span id="1323"></span><div id="comment-1323" class="comment"><div id="post-1323-score" class="comment-score"></div><div class="comment-text"><p>Joining a domain requires a workstation with Windows 7 Professional, Ultimate or Enterprise. You need at least one dedicated server configured as domain controller.</p></div><div id="comment-1323-info" class="comment-info"><span class="comment-age">(12 Dec '10, 13:09)</span> <span class="comment-user userinfo">packethunter</span></div></div></div><div id="comment-tools-1275" class="comment-tools"></div><div class="clear"></div><div id="comment-1275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

