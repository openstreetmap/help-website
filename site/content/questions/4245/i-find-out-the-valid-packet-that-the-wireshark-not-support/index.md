+++
type = "question"
title = "I find out the valid packet that the wireshark not support."
description = '''When the DHCPv6 relay agent add the interface id(option 18) and the remote id(option 37) to relay forward packet, we can not find out the parsing content by wireshark after remote id. The valid DHCPv6 relay forward packet is bellow: &amp;lt;interface id=&quot;&quot;&amp;gt; &amp;lt;remote id=&quot;&quot;&amp;gt; &amp;lt;msg relay=&quot;&quot; optio...'''
date = "2011-05-26T19:27:00Z"
lastmod = "2011-05-26T22:22:00Z"
weight = 4245
keywords = [ "dhcp" ]
aliases = [ "/questions/4245" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I find out the valid packet that the wireshark not support.](/questions/4245/i-find-out-the-valid-packet-that-the-wireshark-not-support)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4245-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When the DHCPv6 relay agent add the interface id(option 18) and the remote id(option 37) to relay forward packet, we can not find out the parsing content by wireshark after remote id. The valid DHCPv6 relay forward packet is bellow: &lt;interface id=""&gt; &lt;remote id=""&gt; &lt;msg relay="" option=""&gt;</p><p>The wireshark parsing is bellow: &lt;interface id=""&gt; &lt;remote id=""&gt; XXXXXXX(can not parse)</p></div><div id="question-tags" class="tags-container tags">dhcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '11, 19:27</strong></p><img src="https://secure.gravatar.com/avatar/a5b8dfb0fc1b7375e70917cc521b86d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shih527&#39;s gravatar image" /><p>shih527<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shih527 has no accepted answers">0%</span></p></div></div><div id="comments-container-4245" class="comments-container"><span id="34151"></span><div id="comment-34151" class="comment"><div id="post-34151-score" class="comment-score"></div><div class="comment-text"><p>Hi, Can you please let me know the DHCPv6 server that you have used with option18 and option37 enabled. Also let me know the configuration of same.</p><p>Thanks, Ranjith</p></div><div id="comment-34151-info" class="comment-info"><span class="comment-age">(25 Jun '14, 01:32)</span> Rans</div></div></div><div id="comment-tools-4245" class="comment-tools"></div><div class="clear"></div><div id="comment-4245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4246"></span>

<div id="answer-container-4246" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4246-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you think Wireshark is in error, you should file a bug report at <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a>. Include all relevant information and be prepared to attach a sample capture file showing the problem. This way the developers can track down the bug, and test the repair before releasing a new version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '11, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4246" class="comments-container"></div><div id="comment-tools-4246" class="comment-tools"></div><div class="clear"></div><div id="comment-4246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

