+++
type = "question"
title = "Interface list is incomplete"
description = '''I am using windows server 2003 SR2, there are two HP NC373i Multifunction Gigabit Network adapters. One is disabled and #2 is enabled. When I bring up the Wireshark I only see &quot;Adapter for generic dialup and VPN capture&quot;. This was showing the network adapter last week and I was able to capture. Choo...'''
date = "2011-05-11T10:28:00Z"
lastmod = "2011-05-13T15:07:00Z"
weight = 4042
keywords = [ "interface", "winpcap", "adapter", "npf", "missing" ]
aliases = [ "/questions/4042" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Interface list is incomplete](/questions/4042/interface-list-is-incomplete)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4042-score" class="post-score" title="current number of votes">0</div><span id="post-4042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using windows server 2003 SR2, there are two HP NC373i Multifunction Gigabit Network adapters. One is disabled and #2 is enabled.</p><p>When I bring up the Wireshark I only see "Adapter for generic dialup and VPN capture".</p><p>This was showing the network adapter last week and I was able to capture. Choosing the "Adapter for generic dialup and VPN capture" doesn't capture any packets (as you would expect).</p><p>I have since upgraded wireshark to version 1.4.6 and WinPCap to version 4.1.2 but this doesn't help at all.</p><p>The installs and the login were done with administrator privileges.</p><p>Tony</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-adapter" rel="tag" title="see questions tagged &#39;adapter&#39;">adapter</span> <span class="post-tag tag-link-npf" rel="tag" title="see questions tagged &#39;npf&#39;">npf</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '11, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/ef6961cc22dcedf6d60c4b5e58dff2c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tony&#39;s gravatar image" /><p><span>Tony</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tony has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 May '11, 13:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4042" class="comments-container"><span id="4043"></span><div id="comment-4043" class="comment"><div id="post-4043-score" class="comment-score"></div><div class="comment-text"><p>What do you get if you run "<code>tshark.exe -D</code>"? How about if you run <code>"WinDump.exe -D</code>"? You can download WinDump from <a href="http://www.winpcap.org/windump/install/default.htm">http://www.winpcap.org/windump/install/default.htm</a>.</p></div><div id="comment-4043-info" class="comment-info"><span class="comment-age">(11 May '11, 12:12)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="4044"></span><div id="comment-4044" class="comment"><div id="post-4044-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply</p><p>I tried your suggestions. Both tshark.exe -D and WinDump.exe -D come back with DeviceNPF_GenericDialupAdapter ...</p></div><div id="comment-4044-info" class="comment-info"><span class="comment-age">(11 May '11, 12:30)</span> <span class="comment-user userinfo">Tony</span></div></div></div><div id="comment-tools-4042" class="comment-tools"></div><div class="clear"></div><div id="comment-4042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4045"></span>

<div id="answer-container-4045" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4045-score" class="post-score" title="current number of votes">1</div><span id="post-4045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://www.winpcap.org/misc/faq.htm#Q-4">http://www.winpcap.org/misc/faq.htm#Q-4</a>. Since <code>WinDump -D</code> doesn't show the interfaces, this isn't a Wireshark problem, but likely a WinPcap problem.</p><p>You might check to see if the npf driver is running. See <a href="http://www.winpcap.org/misc/faq.htm#Q-3">http://www.winpcap.org/misc/faq.htm#Q-3</a>.</p><p>See also this related question here at ask: <a href="http://ask.wireshark.org/questions/1281/npf-driver-problem-in-windows-7">http://ask.wireshark.org/questions/1281/npf-driver-problem-in-windows-7</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '11, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4045" class="comments-container"><span id="4046"></span><div id="comment-4046" class="comment"><div id="post-4046-score" class="comment-score"></div><div class="comment-text"><p>Another place to look at it is on the Wireshark wiki: <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a></p></div><div id="comment-4046-info" class="comment-info"><span class="comment-age">(11 May '11, 13:07)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="4047"></span><div id="comment-4047" class="comment"><div id="post-4047-score" class="comment-score"></div><div class="comment-text"><p>NPF is running and I have checked, it is running as administrator.</p></div><div id="comment-4047-info" class="comment-info"><span class="comment-age">(11 May '11, 13:28)</span> <span class="comment-user userinfo">Tony</span></div></div><span id="4081"></span><div id="comment-4081" class="comment"><div id="post-4081-score" class="comment-score">1</div><div class="comment-text"><p>Your problem is solved already, but anyway...<br />
Here is another way to check the status or to start the NPF driver:<br />
Go to Start -&gt; Computer -&gt; right-click -&gt; Manage<br />
Select Device Manager<br />
or<br />
Go to Run -&gt; compmgmt.msc<br />
<br />
Next you select View -&gt; Show Hidden Devices<br />
Double-click Non-Plug and Play Drivers in the list of devices<br />
Right-click on NetGroup Packet Filter Driver and select Properties.<br />
On the Driver tab you can change the start settings to <a href="http://technet.microsoft.com/en-us/library/cc725630%28WS.10%29.aspx">"Automatic" or "System"</a>.</p></div><div id="comment-4081-info" class="comment-info"><span class="comment-age">(13 May '11, 15:07)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-4045" class="comment-tools"></div><div class="clear"></div><div id="comment-4045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4048"></span>

<div id="answer-container-4048" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4048-score" class="post-score" title="current number of votes">1</div><span id="post-4048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using the 64bit version of Win2K3? If so, are you using the 64bit version of Wireshark? I have heard some people say the 32bit version does not see interfaces on Win7-64 bit.</p><p>You state that one of the NICs is disabled. Did you try enabling that NIC to see if both NICs then become visible? As you say the 1st NIC is disabled, I wonder whether that is blocking WinPcap from accessing the second NIC (with the same driver). But this is just a hunch :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '11, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-4048" class="comments-container"><span id="4060"></span><div id="comment-4060" class="comment"><div id="post-4060-score" class="comment-score"></div><div class="comment-text"><p>I am useing windows 32 bit version. I thought I was but I wanted to check some more. It is MS Windows Server 2003, Standard Edition, 5.2.3790 Service Pack 2. This is 32 bit. The 64 bit version specifically says 64 bit.</p><p>I did try to enable the first driver but that didn't help. I also rebooted the server after I did that and the driver came back disabled.</p></div><div id="comment-4060-info" class="comment-info"><span class="comment-age">(12 May '11, 12:47)</span> <span class="comment-user userinfo">Tony</span></div></div></div><div id="comment-tools-4048" class="comment-tools"></div><div class="clear"></div><div id="comment-4048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4074"></span>

<div id="answer-container-4074" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4074-score" class="post-score" title="current number of votes">1</div><span id="post-4074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I am not sure that this is the complete answer to this issue. The issue was solved up upgrading to the latest HP NIC driver.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '11, 13:28</strong></p><img src="https://secure.gravatar.com/avatar/ef6961cc22dcedf6d60c4b5e58dff2c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tony&#39;s gravatar image" /><p><span>Tony</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tony has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-4074" class="comments-container"></div><div id="comment-tools-4074" class="comment-tools"></div><div class="clear"></div><div id="comment-4074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

