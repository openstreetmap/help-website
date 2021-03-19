+++
type = "question"
title = "Wireshark crashing when running a trace"
description = '''When leaving wireshark running a trace it crashes and in event viewer I get the error. Faulting application name: Wireshark.exe, version: 2.0.3.0, time stamp:0x571a5d95 Faulting module name: libwireshark.dll, version: 2.0.3.0, time stamp 0x571a5ca5 Exception code: 0x0000005 Fault offset: 0x000000000...'''
date = "2016-06-08T01:51:00Z"
lastmod = "2016-06-08T05:53:00Z"
weight = 53303
keywords = [ "wireshark", "crash", "error" ]
aliases = [ "/questions/53303" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashing when running a trace](/questions/53303/wireshark-crashing-when-running-a-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53303-score" class="post-score" title="current number of votes">0</div><span id="post-53303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When leaving wireshark running a trace it crashes and in event viewer I get the error.</p><pre><code>Faulting application name: Wireshark.exe, version: 2.0.3.0, time stamp:0x571a5d95
Faulting module name: libwireshark.dll, version: 2.0.3.0, time stamp 0x571a5ca5
Exception code: 0x0000005
Fault offset: 0x0000000000012527
Faulting process id:0x1308
Faulting application start time: x01d1bfc97d4ed270
Faulting application pat: C:\Program Files\Wireshark\Wireshark.exe
Faulting module path: C:\Program Files\Wireshark\libwireshark.dll
Report Id: *cbdb5a6-2c1c-11e6-8253-bb8e6fa7e1c0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '16, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/0bfabb44c662192bed32f1818643c715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattG&#39;s gravatar image" /><p><span>MattG</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattG has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jun '16, 02:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53303" class="comments-container"><span id="53304"></span><div id="comment-53304" class="comment"><div id="post-53304-score" class="comment-score"></div><div class="comment-text"><p>What were you doing with Wireshark when the crash occurred? If you've been running it for some time with reasonable amounts of traffic it's likely that Wireshark run out of memory, see <a href="https://wiki.wireshark.org/KnownBugs/OutOfMemory">this</a> Wiki page for more info.</p></div><div id="comment-53304-info" class="comment-info"><span class="comment-age">(08 Jun '16, 02:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53305"></span><div id="comment-53305" class="comment"><div id="post-53305-score" class="comment-score"></div><div class="comment-text"><p>The wireshark is being used to monitor traffic constantly out of a firewall</p></div><div id="comment-53305-info" class="comment-info"><span class="comment-age">(08 Jun '16, 02:37)</span> <span class="comment-user userinfo">MattG</span></div></div><span id="53306"></span><div id="comment-53306" class="comment"><div id="post-53306-score" class="comment-score"></div><div class="comment-text"><p>From your additional comment I'm pretty certain that it is an out of memory situation.</p><p>What is the purpose of running wireshark in this manner, as there may be better tools for you to use, e.g. dumpcap?</p></div><div id="comment-53306-info" class="comment-info"><span class="comment-age">(08 Jun '16, 02:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53307"></span><div id="comment-53307" class="comment"><div id="post-53307-score" class="comment-score"></div><div class="comment-text"><pre><code>The wireshark is being used to monitor traffic constantly out of a firewall</code></pre><p>That suggests that it would be prudent to use <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> to get your captures, and use Wireshark to selectively analyse them.</p></div><div id="comment-53307-info" class="comment-info"><span class="comment-age">(08 Jun '16, 02:48)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="53315"></span><div id="comment-53315" class="comment"><div id="post-53315-score" class="comment-score"></div><div class="comment-text"><p>Its for a customer they wanted wireshark running constantly , I will try just using the dumpcap to capture the traffic, thanks</p></div><div id="comment-53315-info" class="comment-info"><span class="comment-age">(08 Jun '16, 05:49)</span> <span class="comment-user userinfo">MattG</span></div></div><span id="53316"></span><div id="comment-53316" class="comment not_top_scorer"><div id="post-53316-score" class="comment-score"></div><div class="comment-text"><p>Check the ring buffer options allowing to write the output into a series of smaller files, as it is much more convenient to handle these files later (analysis &amp; eventual archiving).</p></div><div id="comment-53316-info" class="comment-info"><span class="comment-age">(08 Jun '16, 05:53)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-53303" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-53303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

