+++
type = "question"
title = "LUA: How can I read protocol pref tcp.desegment_tcp_streams?"
description = '''Hi, I&#x27;m adding some code to a LUA Wireshark postdissector script and I need to check if &quot;Allow subdissector to reassemble TCP streams&quot; is enabled in Preferences -&amp;gt; Protocols -&amp;gt; TCP I have other areas of code where I create and later read preference values for my subdissector protocol, e.g. tra...'''
date = "2014-09-06T02:36:00Z"
lastmod = "2014-09-08T08:16:00Z"
weight = 36040
keywords = [ "lua" ]
aliases = [ "/questions/36040" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA: How can I read protocol pref tcp.desegment\_tcp\_streams?](/questions/36040/lua-how-can-i-read-protocol-pref-tcpdesegment_tcp_streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36040-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm adding some code to a LUA Wireshark postdissector script and I need to check if "Allow subdissector to reassemble TCP streams" is enabled in Preferences -&gt; Protocols -&gt; TCP</p><p>I have other areas of code where I create and later read preference values for my subdissector protocol, e.g.</p><pre><code>transum.prefs.client_side = Pref.bool( &quot;Client side trace&quot;, true, &quot;Uncheck this if the trace was captured adjacent to the service&quot; )
.
.
if transum.prefs.client_side and retran and stream_dir[s] == 0 then</code></pre><p>This all works fine. I just can't figure out how to read compiled dissector preferences.</p><p>How can I read <code>tcp.desegment_tcp_streams</code>?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '14, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-36040" class="comments-container"></div><div id="comment-tools-36040" class="comment-tools"></div><div class="clear"></div><div id="comment-36040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36076"></span>

<div id="answer-container-36076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36076-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There does not appear to be a way to read another dissector's preference from Lua.</p><p>But why do you want to? No other dissector reads this preference.</p><p>If you really want it, you could always <a href="https://bugs.wireshark.org">submit an enhancement request</a> (with a use case).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '14, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36076" class="comments-container"><span id="36080"></span><div id="comment-36080" class="comment"><div id="post-36080-score" class="comment-score"></div><div class="comment-text"><p>Yeah, I also don't think there's a way to read a pre-existing preference currently.</p></div><div id="comment-36080-info" class="comment-info"><span class="comment-age">(08 Sep '14, 08:23)</span> Hadriel</div></div><span id="36307"></span><div id="comment-36307" class="comment"><div id="post-36307-score" class="comment-score"></div><div class="comment-text"><p>Thanks. That's a shame. The reason I need to read it is because I need different program logic if TCP subdissector reassembly is disabled.</p><p>Best regards...Paul</p></div><div id="comment-36307-info" class="comment-info"><span class="comment-age">(14 Sep '14, 01:34)</span> PaulOfford</div></div><span id="45948"></span><div id="comment-45948" class="comment"><div id="post-45948-score" class="comment-score"></div><div class="comment-text"><p>It looks like someone opened a bug report for this. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11479">bug 11479</a>.</p></div><div id="comment-45948-info" class="comment-info"><span class="comment-age">(18 Sep '15, 09:32)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-36076" class="comment-tools"></div><div class="clear"></div><div id="comment-36076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

