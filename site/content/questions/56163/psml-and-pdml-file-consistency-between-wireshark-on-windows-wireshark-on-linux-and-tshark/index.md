+++
type = "question"
title = "PSML and PDML file consistency between Wireshark on Windows, WireShark on Linux, and Tshark"
description = '''Hello, I am writing an application which parses PDML and PSML XML files (then using their content). These files could be created on Windows or Linux, with Wireshark or Tshark. Will PDML and PSML files created with Wireshark on Linux, Wireshark on Windows and Tshark on Linux all be exactly the same, ...'''
date = "2016-10-05T07:54:00Z"
lastmod = "2016-10-13T08:36:00Z"
weight = 56163
keywords = [ "pdml", "psml", "tshark", "wireshark" ]
aliases = [ "/questions/56163" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PSML and PDML file consistency between Wireshark on Windows, WireShark on Linux, and Tshark](/questions/56163/psml-and-pdml-file-consistency-between-wireshark-on-windows-wireshark-on-linux-and-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56163-score" class="post-score" title="current number of votes">0</div><span id="post-56163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am writing an application which parses PDML and PSML XML files (then using their content). These files could be created on Windows or Linux, with Wireshark or Tshark. Will PDML and PSML files created with Wireshark on Linux, Wireshark on Windows and Tshark on Linux all be exactly the same, or will there be <strong>any</strong> differences between them? I am using regular expressions on the content so it is vital to my application that there are no differences.</p><p>Many thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pdml" rel="tag" title="see questions tagged &#39;pdml&#39;">pdml</span> <span class="post-tag tag-link-psml" rel="tag" title="see questions tagged &#39;psml&#39;">psml</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '16, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/05aa98a3a949c17526355a407a7c506e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lobster&#39;s gravatar image" /><p><span>Lobster</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lobster has no accepted answers">0%</span></p></div></div><div id="comments-container-56163" class="comments-container"></div><div id="comment-tools-56163" class="comment-tools"></div><div class="clear"></div><div id="comment-56163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56172"></span>

<div id="answer-container-56172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56172-score" class="post-score" title="current number of votes">1</div><span id="post-56172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The only measure of stability guaranteed is PDML / PSML schema compliance, so a more flexible parser would be more future proof. Other than that the programs use the same routines to output these files, so you should be good.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '16, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56172" class="comments-container"><span id="56336"></span><div id="comment-56336" class="comment"><div id="post-56336-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer :)</p><p>What do you mean by 'a more flexible parser would be more future proof'?</p><p>And will there be any differences due to character encoding on different platforms?</p></div><div id="comment-56336-info" class="comment-info"><span class="comment-age">(13 Oct '16, 08:36)</span> <span class="comment-user userinfo">Lobster</span></div></div></div><div id="comment-tools-56172" class="comment-tools"></div><div class="clear"></div><div id="comment-56172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

