+++
type = "question"
title = "wireshark dissector profiling"
description = '''I want to write an SCTP dissector in C and in Lua, respectively, and record the time they need to dissect the protocol. Then, I can make a comparison. However, I do not know how to get the time of dissecting a packet. Is there any API or other ways to do this? Thanks a lot~'''
date = "2011-09-29T19:13:00Z"
lastmod = "2011-10-12T18:44:00Z"
weight = 6644
keywords = [ "lua", "dissector", "profiling" ]
aliases = [ "/questions/6644" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark dissector profiling](/questions/6644/wireshark-dissector-profiling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6644-score" class="post-score" title="current number of votes">1</div><span id="post-6644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to write an SCTP dissector in C and in Lua, respectively, and record the time they need to dissect the protocol. Then, I can make a comparison. However, I do not know how to get the time of dissecting a packet. Is there any API or other ways to do this? Thanks a lot~</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-profiling" rel="tag" title="see questions tagged &#39;profiling&#39;">profiling</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '11, 19:13</strong></p><img src="https://secure.gravatar.com/avatar/648f9031cad279f5c33963853e123493?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dingding0743&#39;s gravatar image" /><p><span>dingding0743</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dingding0743 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Sep '11, 20:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6644" class="comments-container"><span id="6805"></span><div id="comment-6805" class="comment"><div id="post-6805-score" class="comment-score"></div><div class="comment-text"><p>Great question. It's well known, that scipted language is slower. But it's worth to know how worse the performance can be. There is no API for profiling. This would be difficult to tell the time per dissector since one dissector calls the other. One approach could be a unit tester. I build such a thing running tshark with synthetic capture data. The problem is that invoking the tshark process makes a lot of time in comparision to the actual dissection.</p></div><div id="comment-6805-info" class="comment-info"><span class="comment-age">(08 Oct '11, 08:26)</span> <span class="comment-user userinfo">harper</span></div></div><span id="6875"></span><div id="comment-6875" class="comment"><div id="post-6875-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!</p></div><div id="comment-6875-info" class="comment-info"><span class="comment-age">(12 Oct '11, 18:44)</span> <span class="comment-user userinfo">dingding0743</span></div></div></div><div id="comment-tools-6644" class="comment-tools"></div><div class="clear"></div><div id="comment-6644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6645"></span>

<div id="answer-container-6645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6645-score" class="post-score" title="current number of votes">1</div><span id="post-6645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>All things being equal, the C dissector will always outperform the Lua one. This is generally true when comparing a program written in C (compiled) to an equivalent in a scripting language (interpreted).</p><p>That said, it could be interesting to see the difference in the context of Wireshark.</p><p>One quick-and-dirty (and non-exact) way is to create a large pcap of duplicate SCTP packets (e.g., 1000000 packets), and open the pcap with tshark using the C dissector alone (w/o the Lua equivalent) and then Lua alone. Use the Linux <a href="http://linux.die.net/man/1/time">time</a> command to get statistics about the run. For example:</p><pre><code>$ time tshark -r huge.pcap
[...]
real    0m0.###s
user    0m0.###s
sys 0m0.###s

$ time tshark -r huge.pcap -Xlua_script:sctp.lua
[...]
real    0m0.###s
user    0m0.###s
sys     0m0.###s</code></pre><p>You might also want to try <a href="http://www.cs.utah.edu/dept/old/texinfo/as/gprof.html">GNU gprof</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '11, 21:12</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-6645" class="comments-container"><span id="6874"></span><div id="comment-6874" class="comment"><div id="post-6874-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, I will try the tshark</p></div><div id="comment-6874-info" class="comment-info"><span class="comment-age">(12 Oct '11, 18:43)</span> <span class="comment-user userinfo">dingding0743</span></div></div></div><div id="comment-tools-6645" class="comment-tools"></div><div class="clear"></div><div id="comment-6645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

