+++
type = "question"
title = "How to run wireshark?"
description = '''I&#x27;ve installed version &quot;Windows Installer (64-bit)&quot; suggested on https://www.wireshark.org/download.html I know, under Linux, it is enough to type &quot;wireshark&quot; in the console. But how to run it under windows? The installation folder is D:&#92;Program Files&#92;Wireshark. I see executable files: mergecap.exe,...'''
date = "2014-12-07T07:29:00Z"
lastmod = "2014-12-07T08:29:00Z"
weight = 38412
keywords = [ "run" ]
aliases = [ "/questions/38412" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to run wireshark?](/questions/38412/how-to-run-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38412-score" class="post-score" title="current number of votes">0</div><span id="post-38412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've installed version "Windows Installer (64-bit)" suggested on <a href="https://www.wireshark.org/download.html">https://www.wireshark.org/download.html</a> I know, under Linux, it is enough to type "wireshark" in the console. But how to run it under windows? The installation folder is D:\Program Files\Wireshark. I see executable files: mergecap.exe, rawshark.exe, reordercap.exe, text2pcap.exe, tshark.exe, uninstall.exe Which of them I should run to wireshark main window be appeared?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-run" rel="tag" title="see questions tagged &#39;run&#39;">run</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '14, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/7b3ae694809893bed813efcdee22ffe9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kirill&#39;s gravatar image" /><p><span>Kirill</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kirill has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Dec '14, 07:30</strong> </span></p></div></div><div id="comments-container-38412" class="comments-container"></div><div id="comment-tools-38412" class="comment-tools"></div><div class="clear"></div><div id="comment-38412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38414"></span>

<div id="answer-container-38414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38414-score" class="post-score" title="current number of votes">0</div><span id="post-38414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unless you've altered the installation options there should be a shortcut in the start menu, the exact location varies with the particular version of Windows.</p><p>Somewhat unsurprisingly, the main Wireshark executable is called Wireshark.exe. Those other executables are for the companion programs in the Wireshark suite. If there is no Wireshark.exe then you have modified the installation options to not install it, on the Components page of the installer dialog ensure all components are selected.</p><p>To run the other applications in the Wireshark suite you'll need to use some form of command line prompt, with Cmd, or PowerShell and provide the path to the executable (with quotes as you have spaces in the path), e.g. <code>"D:\Program Files\Wireshark\tshark.exe"</code> and provide suitable parameters. See the manual pages for each application for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '14, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38414" class="comments-container"><span id="38416"></span><div id="comment-38416" class="comment"><div id="post-38416-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Somewhat unsurprisingly, the main Wireshark executable is called Wireshark.exe.</p></blockquote><p>Good news )) Then something wrong with my Wireshark installation. I've downloaded portable version of the program and it works fine.</p></div><div id="comment-38416-info" class="comment-info"><span class="comment-age">(07 Dec '14, 08:29)</span> <span class="comment-user userinfo">Kirill</span></div></div></div><div id="comment-tools-38414" class="comment-tools"></div><div class="clear"></div><div id="comment-38414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

