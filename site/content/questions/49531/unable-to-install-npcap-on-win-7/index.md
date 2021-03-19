+++
type = "question"
title = "Unable to install npcap on win 7"
description = '''Hello. I am using W7 X64 with SP1, and have the driver installation issue as in this question. If I try installing with the command line, I have that message: c:&#92;Program Files&#92;Npcap&amp;gt;NPFInstall.exe -i Npcap LWF driver has failed the installation.  I tried to install the W7 update posted by Pascal ...'''
date = "2016-01-27T02:28:00Z"
lastmod = "2016-02-03T06:51:00Z"
weight = 49531
keywords = [ "win7", "npcap" ]
aliases = [ "/questions/49531" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to install npcap on win 7](/questions/49531/unable-to-install-npcap-on-win-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49531-score" class="post-score" title="current number of votes">0</div><span id="post-49531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I am using W7 X64 with SP1, and have the driver installation issue as in <a href="https://ask.wireshark.org/questions/45894/driver-signing-error-trying-to-install-npcap">this</a> question. If I try installing with the command line, I have that message:</p><pre><code>c:\Program Files\Npcap&gt;NPFInstall.exe -i
Npcap LWF driver has failed the installation.</code></pre><p>I tried to install the W7 <a href="https://technet.microsoft.com/en-us/library/security/3033929">update</a> posted by Pascal Quantin, but Windows tells me it's already installed.</p><p>Any clues?</p><p>Best regards,</p><p>Nelson.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-win7" rel="tag" title="see questions tagged &#39;win7&#39;">win7</span> <span class="post-tag tag-link-npcap" rel="tag" title="see questions tagged &#39;npcap&#39;">npcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '16, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/0a05d85a7ffd058fe66b977932ff7b6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NelsonB&#39;s gravatar image" /><p><span>NelsonB</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NelsonB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>27 Jan '16, 03:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-49531" class="comments-container"><span id="49534"></span><div id="comment-49534" class="comment"><div id="post-49534-score" class="comment-score"></div><div class="comment-text"><p>Please don't create a new question as an "answer" to an existing one, this is a Q&amp;A site not a forum. Please see the FAQ for more information.</p></div><div id="comment-49534-info" class="comment-info"><span class="comment-age">(27 Jan '16, 03:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-49531" class="comment-tools"></div><div class="clear"></div><div id="comment-49531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49627"></span>

<div id="answer-container-49627" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49627-score" class="post-score" title="current number of votes">0</div><span id="post-49627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Solution:</strong></p><p>For Vista x64 and Win7 x64 users:</p><p>If you still get the pop-up window that said Windows requires a digitally signed driver (or get error 577 when executing net start npf), please try these steps:</p><p>1) Install Microsoft's KB3033929 patch successfully (it should requires reboot).</p><p>2) Install latest Npcap 0.05-r8.</p><p>3) If step 2) still fails running the driver, then reinstall an alternate version of Npcap you NEVER installed on the machine before (like 0.05-r7, if you unfortunately tried 0.05-r7 before step1), then try 0.05-r6.) to "flush" the driver cache. You should use the same option of Install Npcap in WinPcap API-compatible Mode as you did in step 2). This installation of 0.05-r7 should work.</p><p>4) Reinstall back the latest Npcap 0.05-r8. This second-time installation should succeed.</p><hr /><p><strong>UPDATE</strong>:</p><p>Solution:</p><p>You should install the lastest Npcap 0.05 R14, all signing issues should have gone.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '16, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p><span>Yang Luo</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '16, 19:10</strong> </span></p></div></div><div id="comments-container-49627" class="comments-container"><span id="49723"></span><div id="comment-49723" class="comment"><div id="post-49723-score" class="comment-score"></div><div class="comment-text"><p>Hi Yang, I appreciate your efforts on this driver and the given support. I followed all your steps, it still not working.</p></div><div id="comment-49723-info" class="comment-info"><span class="comment-age">(02 Feb '16, 07:03)</span> <span class="comment-user userinfo">NelsonB</span></div></div><span id="49726"></span><div id="comment-49726" class="comment"><div id="post-49726-score" class="comment-score"></div><div class="comment-text"><p>You probably have the experience of installing 0.05-r7 before following these steps, right? The "alternate version" of 3) should be a Npcap version you never installed before, maybe 0.05-r6 or 0.05-r5 (one that you didn't install on that machine)</p></div><div id="comment-49726-info" class="comment-info"><span class="comment-age">(02 Feb '16, 07:25)</span> <span class="comment-user userinfo">Yang Luo</span></div></div><span id="49758"></span><div id="comment-49758" class="comment"><div id="post-49758-score" class="comment-score"></div><div class="comment-text"><p>My first experience with the Npcap driver was with r5. Then I tried with r8. Following your comments, I installed r7 then r8 again. Is there any possibilities to use the signing method used on the winpcap npf driver? I never went through a driver signing process, so I cannot give more help than test your package and give you feedback on it.</p></div><div id="comment-49758-info" class="comment-info"><span class="comment-age">(03 Feb '16, 01:28)</span> <span class="comment-user userinfo">NelsonB</span></div></div><span id="49772"></span><div id="comment-49772" class="comment"><div id="post-49772-score" class="comment-score"></div><div class="comment-text"><p>OK. Then currently, I think the most workable solution for you would be disable the driver signing enforcement for your system. This is absolutely usable I think.</p></div><div id="comment-49772-info" class="comment-info"><span class="comment-age">(03 Feb '16, 06:51)</span> <span class="comment-user userinfo">Yang Luo</span></div></div></div><div id="comment-tools-49627" class="comment-tools"></div><div class="clear"></div><div id="comment-49627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

