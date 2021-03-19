+++
type = "question"
title = "Encapsulation type : Ethernet (1)"
description = '''I am new to Wireshark and wanted to ask some questions, firstly, when looking at &quot;Encapsulation type : Ethernet (1)&quot; what does the &quot;(1)&quot; mean? I have also seen &quot;Per-packet Information Header (97)&quot;, what is the &quot;(97)&quot;?  So many questions.... so little knowledge...'''
date = "2016-02-15T13:49:00Z"
lastmod = "2016-02-15T17:13:00Z"
weight = 50216
keywords = [ "encapsulation", "type" ]
aliases = [ "/questions/50216" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Encapsulation type : Ethernet (1)](/questions/50216/encapsulation-type-ethernet-1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50216-score" class="post-score" title="current number of votes">0</div><span id="post-50216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to Wireshark and wanted to ask some questions, firstly, when looking at "Encapsulation type : Ethernet (1)" what does the "(1)" mean? I have also seen "Per-packet Information Header (97)", what is the "(97)"?</p><p>So many questions.... so little knowledge...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encapsulation" rel="tag" title="see questions tagged &#39;encapsulation&#39;">encapsulation</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '16, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/805be7967456f8118bc3afc85d4711f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JimmyM&#39;s gravatar image" /><p><span>JimmyM</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JimmyM has no accepted answers">0%</span></p></div></div><div id="comments-container-50216" class="comments-container"></div><div id="comment-tools-50216" class="comment-tools"></div><div class="clear"></div><div id="comment-50216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50219"></span>

<div id="answer-container-50219" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50219-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50219-score" class="post-score" title="current number of votes">1</div><span id="post-50219-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's a Wireshark-internal value that represents the particular link-layer header type for the packet in question - and the numerical values are subject to change from release to release, so perhaps we shouldn't be displaying it.</p><p>Wireshark's capture-file-reading code maps the link-layer header type or types in the file - which have values that may be different for different file types - into the internal value so that the Wireshark dissection code doesn't need to know <a href="http://www.tcpdump.org/linktypes.html">the particular values used in pcap/pcapng files</a> or the ones used in Microsoft Network Monitor files or the ones used in {Ether,Token,Airo,Omini}Peek files or....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '16, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50219" class="comments-container"><span id="50224"></span><div id="comment-50224" class="comment"><div id="post-50224-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for that! If I don't need to know, then I am happier</p></div><div id="comment-50224-info" class="comment-info"><span class="comment-age">(15 Feb '16, 17:13)</span> <span class="comment-user userinfo">JimmyM</span></div></div></div><div id="comment-tools-50219" class="comment-tools"></div><div class="clear"></div><div id="comment-50219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

