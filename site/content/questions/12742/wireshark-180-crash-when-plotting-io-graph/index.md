+++
type = "question"
title = "Wireshark 1.8.0 crash when plotting IO graph"
description = '''Hi all, My wireshark crashes since I&#x27;ve upgraded to the latest version 1.8.0 when i am trying to plot the retransmission count over time in the IO graph. I got the same error message when trying to plot duplicate ack count over time in the IO graph as well. When i use the earlier stable version (1.6...'''
date = "2012-07-16T03:14:00Z"
lastmod = "2012-07-23T06:52:00Z"
weight = 12742
keywords = [ "crash" ]
aliases = [ "/questions/12742" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 1.8.0 crash when plotting IO graph](/questions/12742/wireshark-180-crash-when-plotting-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12742-score" class="post-score" title="current number of votes">0</div><span id="post-12742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>My wireshark crashes since I've upgraded to the latest version 1.8.0 when i am trying to plot the retransmission count over time in the IO graph. I got the same error message when trying to plot duplicate ack count over time in the IO graph as well. When i use the earlier stable version (1.6.8), I have no problem. Here is my setup:</p><ul><li>Windows 7 Enterprise 64bit</li><li>WinPcap 4.1.2</li><li>Multiple version of Wireshark (installed) - 1.8.0 (64bit), 1.6.8(64bit), 1.6.5(64bit), 1.4.10(64bit)</li><li>Some custom profiles that I was using from the earlier Wireshark version in my own personal profile folder</li></ul><p>Here is some of the troubleshooting that i've done.</p><ul><li>Tried removed the custom profile, uninstalled wireshark 1.8.0, uninstalled winpcap and then reinstall back wireshark 1.8.0 with winpcap with the default profile &gt; Same error;</li><li>Tried installing wireshark 1.8.0 (64bit) on a fresh machine (Windows 7 Enterprise 64bit version) &gt; Same error;</li><li>Tried installing wireshark 1.8.0 (32bit) on my windows 2003 R2 SP2 server &gt; Same error;</li></ul><p>Please find the screenshot of the error message that i am seeing and the graph that I am trying to plot.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/crash_error.png" alt="alt text" /></p><p>Is it just me having this issue or something has changed that I might not know about? Any advice is very much appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/2cb4221f1e51fa51dde3b0684402d9af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thhoong&#39;s gravatar image" /><p><span>thhoong</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thhoong has no accepted answers">0%</span></p></img></div></div><div id="comments-container-12742" class="comments-container"></div><div id="comment-tools-12742" class="comment-tools"></div><div class="clear"></div><div id="comment-12742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12744"></span>

<div id="answer-container-12744" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12744-score" class="post-score" title="current number of votes">0</div><span id="post-12744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="thhoong has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like a bug.</p><p>Please file a bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a> so that it can be tracked and etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-12744" class="comments-container"><span id="12758"></span><div id="comment-12758" class="comment"><div id="post-12758-score" class="comment-score"></div><div class="comment-text"><p>Just to update everyone on this matter.. Where I submitted this bug, there is already a bug reported. If you are interested to follow the status of this issue, please find it in the link below,</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7441">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7441</a></p></div><div id="comment-12758-info" class="comment-info"><span class="comment-age">(16 Jul '12, 05:58)</span> <span class="comment-user userinfo">thhoong</span></div></div><span id="12914"></span><div id="comment-12914" class="comment"><div id="post-12914-score" class="comment-score"></div><div class="comment-text"><p>Since the answer is that it's a bug, I converted Bill's comment to an Answer.</p></div><div id="comment-12914-info" class="comment-info"><span class="comment-age">(23 Jul '12, 06:52)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-12744" class="comment-tools"></div><div class="clear"></div><div id="comment-12744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

