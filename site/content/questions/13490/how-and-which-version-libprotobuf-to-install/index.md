+++
type = "question"
title = "How and which version libprotobuf to install ?"
description = '''I intend to write protobuf dissector , for that i read in http://protobuf-wireshark.googlecode.com/files/README-runtime-v0.1.txt , that we have to install libprotobuf?   Step 2: Prepare Protocol Buffers We assume that libprotobuf is installed in a well-known location.   How to go about it ? Please h...'''
date = "2012-08-09T02:14:00Z"
lastmod = "2012-08-09T02:36:00Z"
weight = 13490
keywords = [ "google", "protobuf", "wireshark" ]
aliases = [ "/questions/13490" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How and which version libprotobuf to install ?](/questions/13490/how-and-which-version-libprotobuf-to-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13490-score" class="post-score" title="current number of votes">0</div><span id="post-13490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I intend to write protobuf dissector , for that i read in <a href="http://protobuf-wireshark.googlecode.com/files/README-runtime-v0.1.txt">http://protobuf-wireshark.googlecode.com/files/README-runtime-v0.1.txt</a> , that we have to install libprotobuf?</p><blockquote><blockquote><h1 id="step-2-prepare-protocol-buffers">Step 2: Prepare Protocol Buffers</h1><p>We assume that libprotobuf is installed in a well-known location.</p></blockquote></blockquote><p>How to go about it ? Please help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span> <span class="post-tag tag-link-protobuf" rel="tag" title="see questions tagged &#39;protobuf&#39;">protobuf</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '12, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p><span>yogeshg</span><br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Aug '12, 02:16</strong> </span></p></div></div><div id="comments-container-13490" class="comments-container"></div><div id="comment-tools-13490" class="comment-tools"></div><div class="clear"></div><div id="comment-13490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13495"></span>

<div id="answer-container-13495" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13495-score" class="post-score" title="current number of votes">0</div><span id="post-13495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not really anything to do with Wireshark as it's a separate project, but I guess you need to build <a href="http://code.google.com/p/protobuf/">protobuf</a>.</p><p>Slightly worrying that the protobuf dissector is based on Wireshark 1.0.2 which is really ancient. If you do get it to compile with a more recent version, please post back here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '12, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13495" class="comments-container"></div><div id="comment-tools-13495" class="comment-tools"></div><div class="clear"></div><div id="comment-13495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

