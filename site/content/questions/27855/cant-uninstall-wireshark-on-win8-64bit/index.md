+++
type = "question"
title = "Can&#x27;t uninstall wireshark on win8 64bit"
description = '''Hi, I installed wireshark on windows 8 64bit. Everytime I try to run it, it crashes. So I tried to uninstall it, but doesn&#x27;t allow it as some resources are in use. From processes I see there is 2 instances running even though I just powered computer on; wireshark.exe and dumpcap.exe. I can&#x27;t taskkil...'''
date = "2013-12-06T02:48:00Z"
lastmod = "2013-12-14T00:26:00Z"
weight = 27855
keywords = [ "windows", "8", "uninstall", "killtask" ]
aliases = [ "/questions/27855" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can't uninstall wireshark on win8 64bit](/questions/27855/cant-uninstall-wireshark-on-win8-64bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27855-score" class="post-score" title="current number of votes">1</div><span id="post-27855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I installed wireshark on windows 8 64bit. Everytime I try to run it, it crashes. So I tried to uninstall it, but doesn't allow it as some resources are in use.</p><p>From processes I see there is 2 instances running even though I just powered computer on; wireshark.exe and dumpcap.exe.</p><p>I can't taskkill them even with administrator rights. There is something weird going with the taskkill command in windows 8 64bit (I can't kill anything that isn't running all right - if that makes any sense).</p><p>Really frustrating.</p><p>Regards, Tom the Wombat</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-8" rel="tag" title="see questions tagged &#39;8&#39;">8</span> <span class="post-tag tag-link-uninstall" rel="tag" title="see questions tagged &#39;uninstall&#39;">uninstall</span> <span class="post-tag tag-link-killtask" rel="tag" title="see questions tagged &#39;killtask&#39;">killtask</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '13, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/18f72ddc7cf53910e6a83bebb66e99fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom%20the%20Wombat&#39;s gravatar image" /><p><span>Tom the Wombat</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tom the Wombat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '17, 06:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-27855" class="comments-container"></div><div id="comment-tools-27855" class="comment-tools"></div><div class="clear"></div><div id="comment-27855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="27856"></span>

<div id="answer-container-27856" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27856-score" class="post-score" title="current number of votes">0</div><span id="post-27856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think it's a windows issue.</p><p>Maybe check your permission, seems like you losed your admin permission.</p><p>Another solution is to not start wireshark and dumpcap at windows start. I know you can do that in win7 but not sure for win8.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '13, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p><span>Afrim</span><br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '13, 03:30</strong> </span></p></div></div><div id="comments-container-27856" class="comments-container"><span id="27885"></span><div id="comment-27885" class="comment"><div id="post-27885-score" class="comment-score"></div><div class="comment-text"><p>How can I lose admin permission when I'm running it as administrator, and if I did lose it, where I can check it back on?</p></div><div id="comment-27885-info" class="comment-info"><span class="comment-age">(07 Dec '13, 03:35)</span> <span class="comment-user userinfo">Tom the Wombat</span></div></div><span id="27911"></span><div id="comment-27911" class="comment"><div id="post-27911-score" class="comment-score"></div><div class="comment-text"><p>I removed dumpcap from starting on boot up, but still refuses to uninstall. Still claiming it is in use, even thou it is in stopped state in services. Wireshark seems to work like malware...double v t f, mate? Do I need to start to fiddle with regitery keys to get rid of wireshark?</p></div><div id="comment-27911-info" class="comment-info"><span class="comment-age">(08 Dec '13, 00:12)</span> <span class="comment-user userinfo">Tom the Wombat</span></div></div></div><div id="comment-tools-27856" class="comment-tools"></div><div class="clear"></div><div id="comment-27856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27913"></span>

<div id="answer-container-27913" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27913-score" class="post-score" title="current number of votes">0</div><span id="post-27913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Why is dumpcap installed as an autostarting service? The standard Wireshark install definitely doesn't do that. Where did you get your Wireshark install from?</p><p>Can you install <a href="http://technet.microsoft.com/en-gb/sysinternals/bb896653.aspx">Process Explorer</a>, run that as an Administrator, and then examine the Wireshark.exe and dumpcap.exe processes. With the processes displayed in the default "tree" order, dumpcap should be a child of Wireshark. Right click on each of the processes and select "Properties", and on the resulting dialog "Image" tab, the program name should be displayed along with "(Verified) Wireshark Foundation". Report back your findings as comment, not an "answer".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '13, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27913" class="comments-container"></div><div id="comment-tools-27913" class="comment-tools"></div><div class="clear"></div><div id="comment-27913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28100"></span>

<div id="answer-container-28100" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28100-score" class="post-score" title="current number of votes">0</div><span id="post-28100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello. It seems that the problem was my firewall (Zonealarm), dont ask why, but after I uninstalled zonealarm, I could remove wireshark. I had problem with the firewall so I was removing it anyways, and tried to remove wireshar after that and it worked nicely.</p><p>No more Zonealarms for me.</p><p>Thanks from your help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '13, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/18f72ddc7cf53910e6a83bebb66e99fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom%20the%20Wombat&#39;s gravatar image" /><p><span>Tom the Wombat</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tom the Wombat has no accepted answers">0%</span></p></div></div><div id="comments-container-28100" class="comments-container"></div><div id="comment-tools-28100" class="comment-tools"></div><div class="clear"></div><div id="comment-28100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

