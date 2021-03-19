+++
type = "question"
title = "Upgrade 1.8.7 to 1.10.0: Wireshark leaves a permission mess"
description = '''Hi there, here I&#x27;m on Windows 7 x64 Professional. Wireshark 1.8.7 was installed and I just recently downloaded 1.10.0 (the checksums were correct). I started the setup which wanted to uninstall 1.8.7 first (just as usual when upgrading Wireshark). This seems to go fine, but as soon as the installer ...'''
date = "2013-06-10T09:54:00Z"
lastmod = "2013-06-11T04:42:00Z"
weight = 21885
keywords = [ "windows" ]
aliases = [ "/questions/21885" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Upgrade 1.8.7 to 1.10.0: Wireshark leaves a permission mess](/questions/21885/upgrade-187-to-1100-wireshark-leaves-a-permission-mess)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21885-score" class="post-score" title="current number of votes">0</div><span id="post-21885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>here I'm on Windows 7 x64 Professional. Wireshark 1.8.7 was installed and I just recently downloaded 1.10.0 (the checksums were correct). I started the setup which wanted to uninstall 1.8.7 first (just as usual when upgrading Wireshark). This seems to go fine, but as soon as the installer starts, it shows me this error:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_Error1.jpg" alt="Error opening file for writing" /></p><p>Well, the problem seems to be a complete permission fuckup of my folder C:\Program Files\Wireshark - now I don't have any rights to access this folder. I'm even unable to acquire ownership of this folder. I also tried it with SYSTEM rights - unsuccessful. So I suspect the uninstaller caused a problem with the folder permissions. What to do now?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '13, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/9cd96b7e36437e7a66ac577656ca3814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abachmann&#39;s gravatar image" /><p><span>abachmann</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abachmann has no accepted answers">0%</span></p></img></div></div><div id="comments-container-21885" class="comments-container"></div><div id="comment-tools-21885" class="comment-tools"></div><div class="clear"></div><div id="comment-21885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21887"></span>

<div id="answer-container-21887" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21887-score" class="post-score" title="current number of votes">0</div><span id="post-21887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jaap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Neither Wireshark's installer nor the uninstaller explicitly set permissions on any files or folders. Do you have any Wireshark, TShark, or dumpcap processes hanging around? Open handles can keep you from deleting a folder and <a href="http://serverfault.com/questions/32481/how-do-i-take-ownership-of-a-folder-when-access-is-denied-and-the-security-tab-i">apparently keep you from taking ownership as well</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '13, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-21887" class="comments-container"><span id="21896"></span><div id="comment-21896" class="comment"><div id="post-21896-score" class="comment-score"></div><div class="comment-text"><p>Wireshark wasn't started since the system got switched on. Tomorrow I will see if the problem is gone. I will be quite unlucky if nothing has changed - I'll keep you informed.</p></div><div id="comment-21896-info" class="comment-info"><span class="comment-age">(10 Jun '13, 12:09)</span> <span class="comment-user userinfo">abachmann</span></div></div><span id="21922"></span><div id="comment-21922" class="comment"><div id="post-21922-score" class="comment-score"></div><div class="comment-text"><p>Ok, after a Windows restart the folder was gone. Very weird...</p></div><div id="comment-21922-info" class="comment-info"><span class="comment-age">(11 Jun '13, 04:42)</span> <span class="comment-user userinfo">abachmann</span></div></div></div><div id="comment-tools-21887" class="comment-tools"></div><div class="clear"></div><div id="comment-21887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

