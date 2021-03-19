+++
type = "question"
title = "How to change copyright info in Help&gt;About Wireshark&gt;Wireshark"
description = '''Hi, I built wireshark 2.2.4 in cent os using following command: make uninstall, ./autogen.sh, ./configure, make clean, make, make install, Now for some internal purpose I want to change copyright info in Help&amp;gt;About Wireshark&amp;gt;Wireshark. How to that? P.S: I went through code and found that get_c...'''
date = "2017-07-13T01:19:00Z"
lastmod = "2017-07-16T00:50:00Z"
weight = 62731
keywords = [ "link", "compilation", "source-code", "help", "copyright" ]
aliases = [ "/questions/62731" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to change copyright info in Help&gt;About Wireshark&gt;Wireshark](/questions/62731/how-to-change-copyright-info-in-helpabout-wiresharkwireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62731-score" class="post-score" title="current number of votes">0</div><span id="post-62731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I built wireshark 2.2.4 in cent os using following command: make uninstall, ./autogen.sh, ./configure, make clean, make, make install, Now for some internal purpose I want to change copyright info in Help&gt;About Wireshark&gt;Wireshark. How to that?</p><p>P.S: I went through code and found that get_copyright_info() in wsutil/copyright_info.c is the function to change. But it seems ws_version_info.c has dependency on copyright_info.c and ws_version_info.c has soft link with wiretap/ws_version_info.c. So if i change any of the ws_version_info.c it will throw compilation error.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-link" rel="tag" title="see questions tagged &#39;link&#39;">link</span> <span class="post-tag tag-link-compilation" rel="tag" title="see questions tagged &#39;compilation&#39;">compilation</span> <span class="post-tag tag-link-source-code" rel="tag" title="see questions tagged &#39;source-code&#39;">source-code</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-copyright" rel="tag" title="see questions tagged &#39;copyright&#39;">copyright</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '17, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p><span>Abhisek</span><br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div></div><div id="comments-container-62731" class="comments-container"><span id="62746"></span><div id="comment-62746" class="comment"><div id="post-62746-score" class="comment-score"></div><div class="comment-text"><p>I don't get it, if you change the text in get_copyright_info() and recompile it does not work?</p></div><div id="comment-62746-info" class="comment-info"><span class="comment-age">(13 Jul '17, 07:26)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="62773"></span><div id="comment-62773" class="comment"><div id="post-62773-score" class="comment-score"></div><div class="comment-text"><p>I am afraid of trying the change and re-compilation, because I had a bad experience with ws_version_info.c file change.If you even touch the file ws_version_info.c the whole wireshark code will not further compile any more time. Now I already modified many wireshark file as per my needs, so if in this moment if i try to change wsutil/copyright_info.c(which is a dependent of ws_version_info.c), it may push me to do a hell of lot rework. So my request/question is that anyone have any idea on changing wsutil/copyright_info.c and successfully recompilation after that OR any other way to change copyright information.</p></div><div id="comment-62773-info" class="comment-info"><span class="comment-age">(14 Jul '17, 00:46)</span> <span class="comment-user userinfo">Abhisek</span></div></div></div><div id="comment-tools-62731" class="comment-tools"></div><div class="clear"></div><div id="comment-62731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62818"></span>

<div id="answer-container-62818" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62818-score" class="post-score" title="current number of votes">0</div><span id="post-62818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Abhisek has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>P.S: I went through code and found that <code>get_copyright_info()</code> in <code>wsutil/copyright_info.c</code> is the function to change.</p></blockquote><p>Yes it is.</p><blockquote><p>But it seems <code>ws_version_info.c</code> has dependency on <code>copyright_info.c</code></p></blockquote><p><code>show_version()</code>, in <code>ws_version_info.c</code>, calls <code>get_copyright_info()</code>, so, yes, there is a link-time dependency.</p><blockquote><p><code>ws_version_info.c</code> has soft link with <code>wiretap/ws_version_info.c</code></p></blockquote><p>Yes, if you build with autotools, the build process makes <code>wiretap/ws_version_info.c</code> a symbolic link to <code>ws_version_info.c</code>.</p><blockquote><p>So if i change any of the ws_version_info.c it will throw compilation error.</p></blockquote><p>First of all, you don't need to change <code>ws_version_info.c</code> to change the copyright notice, you only have to change <code>wsutil/copyright_info.c</code>. (Yes, that is true, as I just created a version of Wireshark that credits "Roland the Headless Thomson Gunner" with the copyright, by editing <code>wsutil/copyright_info.c</code> to change the string in <code>get_copyright_info()</code>, without changing <code>ws_version_info.c</code>, and recompiling.)</p><p>Second, the only version of <code>ws_version_info.c</code> in the Wireshark source is the one in the top-level directory, so that's the only one you should change. And if you change it, it'll compile. (Yes, that is true, as I just created a version of Wireshark that not only gives Mr. Zevon's character credit for Wireshark, but appends "(Or so it is claimed.)" on the line after the copyright notice, by editing the top-level <code>ws_version_info.c</code> to add that message to the format string, and recompiling.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '17, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62818" class="comments-container"><span id="62819"></span><div id="comment-62819" class="comment"><div id="post-62819-score" class="comment-score"></div><div class="comment-text"><p>This is the answer I am waiting... Thanks a lot... One thing I want to share, though i changed only the top level ws_version_info.c, the compilation was failed by autotool... So any idea on that?</p></div><div id="comment-62819-info" class="comment-info"><span class="comment-age">(16 Jul '17, 00:03)</span> <span class="comment-user userinfo">Abhisek</span></div></div><span id="62820"></span><div id="comment-62820" class="comment"><div id="post-62820-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So any idea on that?</p></blockquote><p>You probably did something wrong. Nobody else has reported a problem when they edited the top-level <code>ws_version_info.c</code> and tried compiling. (And, again, if you just want to change the copyright message, <em>you don't need to change <code>ws_version_info.c</code></em>.)</p></div><div id="comment-62820-info" class="comment-info"><span class="comment-age">(16 Jul '17, 00:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-62818" class="comment-tools"></div><div class="clear"></div><div id="comment-62818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62774"></span>

<div id="answer-container-62774" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62774-score" class="post-score" title="current number of votes">0</div><span id="post-62774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If modifying the string returned by <code>get_copyright_info()</code> causes compilation errors you have a broken build environment.</p><p>How are you modifying the info, presumably you ARE just changing the string contents?</p><p>What ARE the build errors you get?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '17, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-62774" class="comments-container"></div><div id="comment-tools-62774" class="comment-tools"></div><div class="clear"></div><div id="comment-62774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

