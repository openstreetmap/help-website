+++
type = "question"
title = "Create plugin on Windows and Linux platforms"
description = '''Hello, I need to add a new plugin dissector to Wireshark and create a version for windows an linux. Is the source code the same for Windows and Linux ? Can I develop and compil under Windows, then cross compil for linux (or i need to install source code, tools on linux OS, then compil) ? Edd'''
date = "2013-11-13T06:48:00Z"
lastmod = "2013-11-14T05:42:00Z"
weight = 26943
keywords = [ "windows", "plugin", "linux" ]
aliases = [ "/questions/26943" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Create plugin on Windows and Linux platforms](/questions/26943/create-plugin-on-windows-and-linux-platforms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26943-score" class="post-score" title="current number of votes">0</div><span id="post-26943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I need to add a new plugin dissector to Wireshark and create a version for windows an linux. Is the source code the same for Windows and Linux ? Can I develop and compil under Windows, then cross compil for linux (or i need to install source code, tools on linux OS, then compil) ?</p><p>Edd</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '13, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/d412cc145e61c1255a7667caec29d3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edd&#39;s gravatar image" /><p><span>Edd</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '13, 07:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-26943" class="comments-container"></div><div id="comment-tools-26943" class="comment-tools"></div><div class="clear"></div><div id="comment-26943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="26999"></span>

<div id="answer-container-26999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26999-score" class="post-score" title="current number of votes">1</div><span id="post-26999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can I develop and compil under Windows, then cross compil for linux (or i need to install source code, tools on linux OS, then compil) ?</p></blockquote><p>I suggest to build it on Linux for Linux, at least if you want to avoid trouble ;-)</p><p>Reasons:</p><ul><li><a href="http://wiki.wireshark.org/Development/CygwinGCC">http://wiki.wireshark.org/Development/CygwinGCC</a><br />
</li><li>my explanation below</li></ul><p>You can (somehow) build Wireshark on Windows with the Cygwin gcc toolchain, although even that is kind of a pain in the ... (see link above)</p><p>Now, <strong>if you really succeed</strong> to use the Cygwin gcc toolchain to build Wireshark on Windows (and I'm pretty sure the current release will <strong>not</strong> build without larger problems), then you <strong>may be able</strong> to also cross compile a binary for Linux. <strong>However</strong> that will <strong>cause even more trouble</strong>, as there is no (ready to use) support for cross compiling on Windows, even if you use Cygwin.</p><p>If you use the Microsoft compiler toolchain, there is <strong>no support at all</strong> for cross compiling a Linux binary, as you can imagine.</p><p><strong>So, to sum it up:</strong> You might be able to cross compile a Linux binary on Windows, by using the Cygwin gcc toolchain, but that will be much more trouble than installing a Linux distribution in a virtual machine and compile the Linux version there. It's pretty easy on Ubuntu and other Distributions and there are a lot of documents that describe how to do it.</p><p>My estimation:</p><ul><li>Install Linux in a VM and build the Linux Wireshark binary there: 1-2 hours (total)</li><li>Try to cross-compile a Linux Binary on Windows: 1-2 weeks, if it works at all</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 05:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '13, 05:50</strong> </span></p></div></div><div id="comments-container-26999" class="comments-container"></div><div id="comment-tools-26999" class="comment-tools"></div><div class="clear"></div><div id="comment-26999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26945"></span>

<div id="answer-container-26945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26945-score" class="post-score" title="current number of votes">0</div><span id="post-26945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In general, the source code is generally the same, however differences with platform headers etc. are covered by conditional #if def blocks. Certain other areas (generally GUI stuff and not often found in dissectors) has different code for the various platforms.</p><p>I don't know of anyone cross compiling on Windows and targeting Linux, you can certainly develop on Windows, then copy the source over to a Linux environment and build there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '13, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-26945" class="comments-container"></div><div id="comment-tools-26945" class="comment-tools"></div><div class="clear"></div><div id="comment-26945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26988"></span>

<div id="answer-container-26988" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26988-score" class="post-score" title="current number of votes">0</div><span id="post-26988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Edd,</p><p>I had the same problem and did not found a tool that create a linux version from windows. However you can copy the source of your plugin and build there like grahamb said.</p><p>For me the most important thing is to have the same version of Wireshark in both OSs</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p><span>Afrim</span><br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-26988" class="comments-container"><span id="26996"></span><div id="comment-26996" class="comment"><div id="post-26996-score" class="comment-score"></div><div class="comment-text"><p>Ok, fine I understand.</p><p>Thank you</p></div><div id="comment-26996-info" class="comment-info"><span class="comment-age">(14 Nov '13, 05:18)</span> <span class="comment-user userinfo">Edd</span></div></div></div><div id="comment-tools-26988" class="comment-tools"></div><div class="clear"></div><div id="comment-26988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

