+++
type = "question"
title = "WinPcap not receiving data"
description = '''I have an odd situation and will try to explain with detail what I am seeing and would really appreciate some help fixing this. On 2 pc&#x27;s my setup is Windows 7 Ultimate, Service Pack 1 and have WinPcap 4.1.2 and Windows 7 Professional, SP1 and WinPcap 4.1.2 on a third pc. The PC&#x27;s with Windows 7 Ult...'''
date = "2012-12-19T07:40:00Z"
lastmod = "2012-12-20T22:47:00Z"
weight = 17059
keywords = [ "winpcap", "windows7", "pcap_next_ex" ]
aliases = [ "/questions/17059" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [WinPcap not receiving data](/questions/17059/winpcap-not-receiving-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17059-score" class="post-score" title="current number of votes">0</div><span id="post-17059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an odd situation and will try to explain with detail what I am seeing and would really appreciate some help fixing this.</p><p>On 2 pc's my setup is Windows 7 Ultimate, Service Pack 1 and have WinPcap 4.1.2 and Windows 7 Professional, SP1 and WinPcap 4.1.2 on a third pc. The PC's with Windows 7 Ultimate, Service Pack have Symantec EndPoint Protection version 11.0.6005.562 and the Windows 7 Professional, SP1 pc has Symantec EndPoint Protection version 11.0.7000.975</p><p>Prior to several months ago all was working fine.<br />
But then on 2 of my 3 PC's (win7 Ultimate &amp; symantec 11.0.6005.562) I started having problems receiving data via the WinPcap API. In my applications (either written in C or SharpPcap) I can open a connection/handle to an interface and I can successfully transmit data over this interface but all attempts to read/receive data result in the application being blocked. However (this is the weird part) I can open Wireshark and successfully receive data on these same pc's and interfaces.</p><p>As I mentioned before these applications were working on all my pc's up until some months ago.<br />
I suspect our corporate IT department pushed (via the evil Altiris application) some security patch on my pc and then after rebooting these applications no longer worked in the aforementioned receive mode. So I upgraded one of the non-working pc's to the version of Symantec EndPoint Protection version 11.0.7000.975 on the pc that is working, but this had no affect so I presume the root cause is not due to the presence or version of Symantec. Symantec EndPoint Protection has the runtime option of disabling protection and I have tried this but there is no change in behavior.</p><p>Again I need to state that Wireshark can work fine.</p><p>I have tried all reasonable combinations of pcap_open, pcap_open_live and using the classis pcap_loop vs pcap_next_ex and nothing seems to open up the reception of data. I looked at the source code to wireshark (e.g. dumpcap.c) and I am using the same api calls.</p><p>I should note that this errant behavior seems to be independent of the network interface I use. I have 4 different NIC's in my setup (yes a lot) and all behave the same.</p><p>I am at a loss to explain or fix what is happening.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-pcap_next_ex" rel="tag" title="see questions tagged &#39;pcap_next_ex&#39;">pcap_next_ex</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '12, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/f247269fc030fb0907926c252bc8b84a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eckorsberg&#39;s gravatar image" /><p><span>eckorsberg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eckorsberg has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-17059" class="comments-container"></div><div id="comment-tools-17059" class="comment-tools"></div><div class="clear"></div><div id="comment-17059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17063"></span>

<div id="answer-container-17063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17063-score" class="post-score" title="current number of votes">0</div><span id="post-17063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>. So I upgraded one of the non-working pc's to the version of Symantec EndPoint Protection version 11.0.7000.975</p></blockquote><p>I suggest to uninstall Symantec EndPoint Protection and then see what happens. SEP has a bad history of interfering with network traffic.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '12, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-17063" class="comments-container"><span id="17069"></span><div id="comment-17069" class="comment"><div id="post-17069-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately our corporate IT setup prevents uninstalling Symantec EndPoint Protection. But again I have a pc running Symantec EndPoint Protection in which my application works fine so I know that in some configuration my application works alongside Symantec EndPoint Protection.</p></div><div id="comment-17069-info" class="comment-info"><span class="comment-age">(19 Dec '12, 09:40)</span> <span class="comment-user userinfo">eckorsberg</span></div></div><span id="17072"></span><div id="comment-17072" class="comment"><div id="post-17072-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But again I have a pc running Symantec EndPoint Protection in which my application works fine so I know that in some configuration</p></blockquote><p>It might work in <strong>some</strong> configuration. But do you know it is the <strong>same</strong> configuration? I still recommend to uninstall SEP, as I'm pretty convinced that is SEP causing the problems.</p></div><div id="comment-17072-info" class="comment-info"><span class="comment-age">(19 Dec '12, 11:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17076"></span><div id="comment-17076" class="comment"><div id="post-17076-score" class="comment-score"></div><div class="comment-text"><p>BTW: Are you sure that the WinPcap service is started while your own application is running? If it is not started, you will have problems getting any data.</p><p>Please run this command before you start your own application:</p><blockquote><p><code>sc query npf</code><br />
</p></blockquote><p>You should see:</p><blockquote><p><code>STATE              : 4  RUNNING</code><br />
</p></blockquote><p>If it is not running, start it from an elevated DOS box.</p><blockquote><p><code>sc start npf</code></p></blockquote></div><div id="comment-17076-info" class="comment-info"><span class="comment-age">(19 Dec '12, 12:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17113"></span><div id="comment-17113" class="comment"><div id="post-17113-score" class="comment-score"></div><div class="comment-text"><p>Yes this is what I see SERVICE_NAME: npf TYPE : 1 KERNEL_DRIVER STATE : 4 RUNNING (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN) WIN32_EXIT_CODE : 0 (0x0) SERVICE_EXIT_CODE : 0 (0x0) CHECKPOINT : 0x0 WAIT_HINT : 0x0</p></div><div id="comment-17113-info" class="comment-info"><span class="comment-age">(20 Dec '12, 20:02)</span> <span class="comment-user userinfo">eckorsberg</span></div></div><span id="17116"></span><div id="comment-17116" class="comment"><div id="post-17116-score" class="comment-score"></div><div class="comment-text"><p>O.K. then back to SEP. Did you talk to your IT department about uninstalling SEP, just for a test?</p></div><div id="comment-17116-info" class="comment-info"><span class="comment-age">(20 Dec '12, 22:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17063" class="comment-tools"></div><div class="clear"></div><div id="comment-17063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17066"></span>

<div id="answer-container-17066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17066-score" class="post-score" title="current number of votes">0</div><span id="post-17066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Wireshark is also using WinPcap and does indeed see packets, might your user rights have changed in a way that your own application does not have enough rights anymore to do the capturing?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '12, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-17066" class="comments-container"><span id="17068"></span><div id="comment-17068" class="comment"><div id="post-17068-score" class="comment-score"></div><div class="comment-text"><p>I have my UAC set to minimal setting and this has not changed. When running Wireshark, does that process execute with different rights than my own application? Is there a way to manually 'upgrade' or alter the explicit rights to my .exe application file?</p></div><div id="comment-17068-info" class="comment-info"><span class="comment-age">(19 Dec '12, 09:38)</span> <span class="comment-user userinfo">eckorsberg</span></div></div></div><div id="comment-tools-17066" class="comment-tools"></div><div class="clear"></div><div id="comment-17066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

