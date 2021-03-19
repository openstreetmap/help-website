+++
type = "question"
title = "Disable Capturing Capacity or Just to read the pcap files but no capture option"
description = '''Hi Is there any way to disable the capturimg feature on wire shark so that user can read only prevoiusly captured files but can not capture the packets on the network'''
date = "2011-05-14T16:12:00Z"
lastmod = "2011-05-17T00:19:00Z"
weight = 4090
keywords = [ "read", "only", "pcap" ]
aliases = [ "/questions/4090" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Disable Capturing Capacity or Just to read the pcap files but no capture option](/questions/4090/disable-capturing-capacity-or-just-to-read-the-pcap-files-but-no-capture-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4090-score" class="post-score" title="current number of votes">0</div><span id="post-4090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Is there any way to disable the capturimg feature on wire shark so that user can read only prevoiusly captured files but can not capture the packets on the network</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-read" rel="tag" title="see questions tagged &#39;read&#39;">read</span> <span class="post-tag tag-link-only" rel="tag" title="see questions tagged &#39;only&#39;">only</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '11, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/b727fa96a71573e88fa4fa6d6dde8749?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jignesh%20Furia&#39;s gravatar image" /><p><span>Jignesh Furia</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jignesh Furia has no accepted answers">0%</span></p></div></div><div id="comments-container-4090" class="comments-container"><span id="4091"></span><div id="comment-4091" class="comment"><div id="post-4091-score" class="comment-score"></div><div class="comment-text"><p>Yes you can, but it depends on the OS the user is on how to do it. Please enlighten us with the OS used :-)</p></div><div id="comment-4091-info" class="comment-info"><span class="comment-age">(14 May '11, 16:17)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="4100"></span><div id="comment-4100" class="comment"><div id="post-4100-score" class="comment-score"></div><div class="comment-text"><p>Note that you'd also have to prevent users from installing Wireshark (or, in the case of Windows, WinPcap) themselves, or prevent them from running with sufficient privilege to capture packets. How you'd do that is also dependent on the OS the machine is running.</p></div><div id="comment-4100-info" class="comment-info"><span class="comment-age">(17 May '11, 00:19)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4090" class="comment-tools"></div><div class="clear"></div><div id="comment-4090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4092"></span>

<div id="answer-container-4092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4092-score" class="post-score" title="current number of votes">0</div><span id="post-4092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way would be to compile it without libpcap (or WinPcap if it's Windows).</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '11, 18:37</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Mar '12, 07:02</strong> </span></p></div></div><div id="comments-container-4092" class="comments-container"><span id="4093"></span><div id="comment-4093" class="comment"><div id="post-4093-score" class="comment-score"></div><div class="comment-text"><p>Windows:<br />
uninstall or just don't install WinPcap.<br />
When you run the setup, you will get the question: Install WinPcap?<br />
WinPcap is required to capture live network data.</p></div><div id="comment-4093-info" class="comment-info"><span class="comment-age">(15 May '11, 02:10)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-4092" class="comment-tools"></div><div class="clear"></div><div id="comment-4092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

