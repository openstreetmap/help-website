+++
type = "question"
title = "tshark two-pass NFSv4 skips valid operations"
description = '''Individual NFSv4 opcodes are contained within a COMPOUND NFSv4 procedure. If one runs tshark -r a.pcap -q -z rpc,srt,100003,4  to print the RTT of NFSv4 opcodes, you only get results for the COMPOUND procedure and not individual ops. We have a script which parses the output of the nfs.main_opcode wi...'''
date = "2015-11-16T16:26:00Z"
lastmod = "2015-11-16T17:10:00Z"
weight = 47649
keywords = [ "two-pass", "nfsv4", "nfs", "tshark", "opcode" ]
aliases = [ "/questions/47649" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark two-pass NFSv4 skips valid operations](/questions/47649/tshark-two-pass-nfsv4-skips-valid-operations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47649-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Individual NFSv4 opcodes are contained within a COMPOUND NFSv4 procedure. If one runs</p><pre><code>tshark -r a.pcap -q -z rpc,srt,100003,4</code></pre><p>to print the RTT of NFSv4 opcodes, you only get results for the COMPOUND procedure and not individual ops.</p><p>We have a script which parses the output of the <code>nfs.main_opcode</code> with a command like:</p><pre><code>tshark -r a.pcap -2 -R &quot;nfs.procedure_v4 and rpc.time&quot; -T fields -e nfs.main_opcode -e rpc.time</code></pre><p>This uses two-pass mode. However, when running this in single-pass mode like:</p><pre><code>tshark -r a.pcap -Y &quot;nfs.procedure_v4 and rpc.time&quot; -T fields -e nfs.main_opcode -e rpc.time</code></pre><p>We see a difference in the number of operations the two commands report.</p><p>Sometimes two-pass will either not print the opcode, or not even consider the operation in its analysis. Hand-counting operations shows that two-pass is inaccurate and single-pass is accurate.</p><p>Is this some behaviour of the NFSv4 dissector which we don't understand, or is this likely a bug in the NFSv4 two-pass dissector?</p><p>(note: most of our analysis so far has been done on packet captures where tcpdump has dropped at least some traffic due to buffer overrun during receive. We've yet to test this on a "perfect" packet capture)</p></div><div id="question-tags" class="tags-container tags">two-pass nfsv4 nfs tshark opcode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '15, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/1cadd3b79b540cd9f93ef00bdc3980da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="superjamie&#39;s gravatar image" /><p>superjamie<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="superjamie has no accepted answers">0%</span></p></div></div><div id="comments-container-47649" class="comments-container"></div><div id="comment-tools-47649" class="comment-tools"></div><div class="clear"></div><div id="comment-47649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47650"></span>

<div id="answer-container-47650" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47650-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Hand-counting operations shows that two-pass is inaccurate and single-pass is accurate.</p></blockquote><p>...</p><blockquote><p>Is this some behaviour of the NFSv4 dissector which we don't understand, or is this likely a bug in the NFSv4 two-pass dissector?</p></blockquote><p>I'd say "two-pass is inaccurate and single-pass is accurate" indicates that there's a bug somewhere.</p><p>There's no such thing as "the NFSv4 two-pass dissector"; there's only one dissector, the NFSv4 dissector. This is almost certainly a bug in that dissector; please file a bug on it at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '15, 17:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-47650" class="comments-container"><span id="47651"></span><div id="comment-47651" class="comment"><div id="post-47651-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy, have done: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11720">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11720</a></p></div><div id="comment-47651-info" class="comment-info"><span class="comment-age">(16 Nov '15, 17:58)</span> superjamie</div></div></div><div id="comment-tools-47650" class="comment-tools"></div><div class="clear"></div><div id="comment-47650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

