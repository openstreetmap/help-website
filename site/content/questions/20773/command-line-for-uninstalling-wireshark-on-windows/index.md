+++
type = "question"
title = "Command line for uninstalling Wireshark on Windows"
description = '''I have some old servers that have old versions of WireShark installed. I need a command line to uninstall Wireshark. I&#x27;m going to use SCCM to push this command to a group of servers. Is there a msiexec command that I could run? I need to uninstall any version.'''
date = "2013-04-24T10:35:00Z"
lastmod = "2013-05-13T12:56:00Z"
weight = 20773
keywords = [ "windows", "uninstall", "wireshark" ]
aliases = [ "/questions/20773" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Command line for uninstalling Wireshark on Windows](/questions/20773/command-line-for-uninstalling-wireshark-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20773-score" class="post-score" title="current number of votes">0</div><span id="post-20773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some old servers that have old versions of WireShark installed.</p><p>I need a command line to uninstall Wireshark. I'm going to use SCCM to push this command to a group of servers. Is there a msiexec command that I could run? I need to uninstall any version.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-uninstall" rel="tag" title="see questions tagged &#39;uninstall&#39;">uninstall</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '13, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/af6e8e78d1b30c9b104ff675b55a0d00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="claudiup&#39;s gravatar image" /><p><span>claudiup</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="claudiup has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '13, 11:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-20773" class="comments-container"></div><div id="comment-tools-20773" class="comment-tools"></div><div class="clear"></div><div id="comment-20773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20775"></span>

<div id="answer-container-20775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20775-score" class="post-score" title="current number of votes">0</div><span id="post-20775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There should be an uninstaller named <code>uninistall.exe</code> in Wireshark's installation directory. Its complete path should be in</p><pre><code>\HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\Wireshark\UninstallString</code></pre><p>More recent versions provide a quiet uninstall path, but this is simply the uninstaller with a "/S" argument</p><pre><code>\HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall\Wireshark\QuietUninstallString</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '13, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-20775" class="comments-container"><span id="21115"></span><div id="comment-21115" class="comment"><div id="post-21115-score" class="comment-score"></div><div class="comment-text"><p>Thanks Gerald,</p><p>So what would the msiexec command look like if I needed to uninstall Wireshark with the "Silent" and "no reboot" options based on that registry entry?</p></div><div id="comment-21115-info" class="comment-info"><span class="comment-age">(13 May '13, 09:37)</span> <span class="comment-user userinfo">claudiup</span></div></div><span id="21116"></span><div id="comment-21116" class="comment"><div id="post-21116-score" class="comment-score"></div><div class="comment-text"><p>you can't use <strong>msiexec</strong> as there is no MSI package. Please run this command to find the silent uninstaller string</p><blockquote><p>`reg query HKLM\Software /v QuietUninstallString /s | find "Wireshark"</p></blockquote><p>Usually, this will resolve to something like this:</p><blockquote><p><code>%ProgramFiles%\Wiresahrk\unistaller.exe /S</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-21116-info" class="comment-info"><span class="comment-age">(13 May '13, 12:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20775" class="comment-tools"></div><div class="clear"></div><div id="comment-20775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

