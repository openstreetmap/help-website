+++
type = "question"
title = "Cannot access &quot;pinfo&quot; in gdb"
description = '''I am using wireshark version 1.12.6. I want to debug a specific packet in a capture file. I followed the development tips from https://wiki.wireshark.org/Development/Tips. But when i set a condition on the breakpoint in GDB, i get following message. (gdb) condition 1 pinfo-&amp;gt;fd-&amp;gt;num == 132 No s...'''
date = "2015-07-19T21:55:00Z"
lastmod = "2015-07-20T11:24:00Z"
weight = 44306
keywords = [ "pinfo", "gdb", "packets", "debugger" ]
aliases = [ "/questions/44306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot access "pinfo" in gdb](/questions/44306/cannot-access-pinfo-in-gdb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44306-score" class="post-score" title="current number of votes">0</div><span id="post-44306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark version 1.12.6. I want to debug a specific packet in a capture file. I followed the development tips from <a href="https://wiki.wireshark.org/Development/Tips.">https://wiki.wireshark.org/Development/Tips.</a> But when i set a condition on the breakpoint in GDB, i get following message.</p><pre><code>(gdb) condition 1 pinfo-&gt;fd-&gt;num == 132
No symbol &quot;pinfo&quot; in current context.</code></pre><p>How do I access "pinfo"?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pinfo" rel="tag" title="see questions tagged &#39;pinfo&#39;">pinfo</span> <span class="post-tag tag-link-gdb" rel="tag" title="see questions tagged &#39;gdb&#39;">gdb</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-debugger" rel="tag" title="see questions tagged &#39;debugger&#39;">debugger</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '15, 21:55</strong></p><img src="https://secure.gravatar.com/avatar/9a82a72e98beb5613defc6c452c2b0c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PratikYeole&#39;s gravatar image" /><p><span>PratikYeole</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PratikYeole has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jul '15, 10:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-44306" class="comments-container"></div><div id="comment-tools-44306" class="comment-tools"></div><div class="clear"></div><div id="comment-44306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44312"></span>

<div id="answer-container-44312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44312-score" class="post-score" title="current number of votes">1</div><span id="post-44312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As indicated in the wiki, this breakpoint the will only work if pinfo structure is given as parameter to the function you are interested in (pinfo structure is not global but is a local variable).</p><p>If your function does not have access to pinfo (as the error you get suggest) either modify the source code to pass it as a parameter or put the breakpoint in whatever parent function which has access to pinfo structure. Or use another condition than the frame number ;)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '15, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-44312" class="comments-container"></div><div id="comment-tools-44312" class="comment-tools"></div><div class="clear"></div><div id="comment-44312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

