+++
type = "question"
title = "How to see console messages in wireshark linux ?"
description = '''http://wiki.wireshark.org/Development/Tips Above link shows how can we use printf to debug in console. But i am not able to see console in linux. Please help.'''
date = "2013-03-12T23:42:00Z"
lastmod = "2013-03-13T00:05:00Z"
weight = 19420
keywords = [ "debugger", "wireshark" ]
aliases = [ "/questions/19420" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to see console messages in wireshark linux ?](/questions/19420/how-to-see-console-messages-in-wireshark-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19420-score" class="post-score" title="current number of votes">0</div><span id="post-19420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="http://wiki.wireshark.org/Development/Tips">http://wiki.wireshark.org/Development/Tips</a></p><p>Above link shows how can we use printf to debug in console. But i am not able to see console in linux. Please help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debugger" rel="tag" title="see questions tagged &#39;debugger&#39;">debugger</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p><span>yogeshg</span><br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-19420" class="comments-container"><span id="19421"></span><div id="comment-19421" class="comment"><div id="post-19421-score" class="comment-score"></div><div class="comment-text"><p>I mean , should proto_tree_add_debug_text display in gdb output ?</p></div><div id="comment-19421-info" class="comment-info"><span class="comment-age">(12 Mar '13, 23:50)</span> <span class="comment-user userinfo">yogeshg</span></div></div></div><div id="comment-tools-19420" class="comment-tools"></div><div class="clear"></div><div id="comment-19420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19423"></span>

<div id="answer-container-19423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19423-score" class="post-score" title="current number of votes">1</div><span id="post-19423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Open a console, launch Wireshark from it, see the console output. Try this on your fresh build:</p><pre><code>WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 WIRESHARK_DEBUG_MIBS=6 ./wireshark</code></pre><p>or with gdb:</p><pre><code>WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 WIRESHARK_DEBUG_MIBS=6 libtool --mode=execute gdb wireshark
(gdb) run</code></pre><p>These env vars only tweak Wireshark into knowing it runs from the build directory and spew a lot of MIB parsing output. No need for them other than to showcase the console output.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19423" class="comments-container"></div><div id="comment-tools-19423" class="comment-tools"></div><div class="clear"></div><div id="comment-19423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

