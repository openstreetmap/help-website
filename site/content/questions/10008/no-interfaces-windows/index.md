+++
type = "question"
title = "No Interfaces - Windows"
description = '''I have recently installed WireShark and WinPCap. During the install, everything seemed to be fine. During my first launch, I got an error somewhere along the lines of &quot;Child dumpcap closed sync pipe prematurely.&quot; I read and read and read to finding no solution. I unistalled everything, re-downloaded...'''
date = "2012-04-07T01:58:00Z"
lastmod = "2016-11-29T07:59:00Z"
weight = 10008
keywords = [ "interface", "windows", "windows7", "winpcap" ]
aliases = [ "/questions/10008" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [No Interfaces - Windows](/questions/10008/no-interfaces-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10008-score" class="post-score" title="current number of votes">0</div><span id="post-10008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have recently installed WireShark and WinPCap. During the install, everything seemed to be fine. During my first launch, I got an error somewhere along the lines of "Child dumpcap closed sync pipe prematurely." I read and read and read to finding no solution. I unistalled everything, re-downloaded the 1.7.1 Developer version of WireShark and downloaded WinPCap version 4.1.2 directly from <a href="http://winpcap.org">winpcap.org</a>.</p><p>After installing both, I now get no errors, but also have no interfaces like before. When clicking Capture -&gt; Interfaces... I receive the following message, "There are no interfaces on which a capture can be done." I have tried as much as I could to try to get my NICs to appear, but to no avail again.</p><p>I tried using WinDump -D and it showed both of my adapters so I'm wondering where the issue lies.</p><p>I'm running Windows 7 Ultimate on a NetBook. I believe I have all of the latest updates for drivers and Windows.</p><p>Thank you for any information.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '12, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/d8e3b39729659bc0eb35a82a81adc8e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrplow123456&#39;s gravatar image" /><p><span>mrplow123456</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrplow123456 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Apr '12, 08:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10008" class="comments-container"></div><div id="comment-tools-10008" class="comment-tools"></div><div class="clear"></div><div id="comment-10008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10032"></span>

<div id="answer-container-10032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10032-score" class="post-score" title="current number of votes">0</div><span id="post-10032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As WinDump uses exactly the same capture mechanism as wireshark (and tshark etc.), that is WinPCap, it seems odd that WinDump can display interfaces but Wireshark can't.</p><p>There should be no difference between the version of WinPCap installed via the Wireshark installer and that directly from <a href="http://winpcap.org">winpcap.org</a>.</p><p>Have you tried <code>tshark -D</code>? Have you tried the Windows "standard repair" of rebooting the machine?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '12, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10032" class="comments-container"></div><div id="comment-tools-10032" class="comment-tools"></div><div class="clear"></div><div id="comment-10032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56907"></span>

<div id="answer-container-56907" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56907-score" class="post-score" title="current number of votes">0</div><span id="post-56907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>please download the latest version of wireshark which is 2.2.1 and winpcap 4.1.3.</p><p>if npf driver is not starting then also interfaces will not be started</p><p><strong>To start</strong> npf driver :</p><p>run cmd in administrator mode</p><p>enter code: net start npf. The service will be started and interfaces will be seen.</p><p>if not through this start wireshark also in administrator mode</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/26cfc77e3e3c34b6ea1453dc6b3ae62c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karan9537&#39;s gravatar image" /><p><span>karan9537</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karan9537 has no accepted answers">0%</span></p></div></div><div id="comments-container-56907" class="comments-container"><span id="56908"></span><div id="comment-56908" class="comment"><div id="post-56908-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the answer, but the OP is probably long gone in the 4 years since the question was asked.</p><p>Please also do <strong>not</strong> recommend that anyone run Wireshark with Administrator privileges, it's not necessary and can actually be dangerous for the host system.</p></div><div id="comment-56908-info" class="comment-info"><span class="comment-age">(01 Nov '16, 10:33)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57703"></span><div id="comment-57703" class="comment"><div id="post-57703-score" class="comment-score"></div><div class="comment-text"><p>I started having the exact same issue this morning on my Win10Pro PC. I uninstalled WinPCAP, and NPCAP, reinstalled Wireshark with WinPCAP 4.1.3 and still Wireshark shows no interfaces that can be captured on.</p><p>I see the NPF service running.</p><pre><code>SERVICE_NAME: npf
        TYPE               : 1  KERNEL_DRIVER
        STATE              : 4  RUNNING
                                (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0</code></pre><p>TSHARK -D yields...</p><p><code>"tshark: There are no interfaces on which a capture can be done"</code></p><p>DUMPCAP -D yields....</p><pre><code>c:\Program Files\Wireshark&gt;dumpcap -D
1. \Device\NPF_{1B4ACF91-D052-45F8-A690-C3019D84C27C} (Wireless Network Connection)
2. \Device\NPF_{8CE18B19-0F74-4CB1-87C7-C9A413898079} (Local Area Connection)
3. \Device\NPF_{913FCDC3-03F2-4C84-A390-44185F2A83A8} (Local Area Connection* 2)</code></pre></div><div id="comment-57703-info" class="comment-info"><span class="comment-age">(29 Nov '16, 06:58)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="57704"></span><div id="comment-57704" class="comment"><div id="post-57704-score" class="comment-score"></div><div class="comment-text"><p>Did you install any extcap utilities when re-installing Wireshark? If so, try uninstalling, rebooting and reinstalling without the extcap utilities. You might also consider uninstall usbpcap if that's installed.</p></div><div id="comment-57704-info" class="comment-info"><span class="comment-age">(29 Nov '16, 07:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57705"></span><div id="comment-57705" class="comment"><div id="post-57705-score" class="comment-score"></div><div class="comment-text"><p>I haven't, but will try that. In the meantime, I installed NPCAP 0.78, stopped the NPF driver, and now see all of the interfaces including the NPAP created loopback interface.</p></div><div id="comment-57705-info" class="comment-info"><span class="comment-age">(29 Nov '16, 07:20)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="57708"></span><div id="comment-57708" class="comment"><div id="post-57708-score" class="comment-score"></div><div class="comment-text"><p>Same results. Uninstalled Wireshark, WinPCAP, USBPCAP, NPCAP. Rebooted. Installed Wireshark, no extcap utilities, no USBPCAP. Queried NPF driver and running. Launch Wireshark, no capture interfaces found. Installed NPCAP, interfaces discovered.</p><p>Very frustrating, but will continue with NPCAP going forward.</p></div><div id="comment-57708-info" class="comment-info"><span class="comment-age">(29 Nov '16, 07:59)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-56907" class="comment-tools"></div><div class="clear"></div><div id="comment-56907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

