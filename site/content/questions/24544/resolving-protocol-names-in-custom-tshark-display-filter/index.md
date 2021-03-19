+++
type = "question"
title = "Resolving protocol names in custom tshark display filter"
description = '''I want to parse the standard header outputs of tshark. Since the default doesn&#x27;t work, I am using a custom field parser that does almost the same thing. What I am missing is the resolution of the name of the protocol. My command is: sudo tshark -b 256 -P -T fields -e frame.time_epoch -e ip.src -e ip...'''
date = "2013-09-10T21:54:00Z"
lastmod = "2014-06-19T17:00:00Z"
weight = 24544
keywords = [ "tshark", "linux" ]
aliases = [ "/questions/24544" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Resolving protocol names in custom tshark display filter](/questions/24544/resolving-protocol-names-in-custom-tshark-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24544-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to parse the standard header outputs of tshark. Since the default doesn't work, I am using a custom field parser that does <em>almost</em> the same thing. What I am missing is the resolution of the name of the protocol. My command is:</p><pre><code>sudo tshark -b 256 -P -T fields -e frame.time_epoch -e ip.src -e ip.dst -e ip.proto -e ip.len -e col.Info -E separator=&#39;;&#39; -b filesize:65535 -b files:10 -w tshark_tmp</code></pre><p>This almost works, what I get is (this example is capturing two pings):</p><pre><code>1378869929.862628000;192.168.78.252;192.168.78.53;1;84;Echo (ping) request  id=0x0abe, seq=65/16640, ttl=64
1378869929.863188000;192.168.78.53;192.168.78.252;1;84;Echo (ping) reply    id=0x0abe, seq=65/16640, ttl=64 (request in 1)</code></pre><p>The same two pings look like this in the normal, no custom field tshark:</p><pre><code>0.000000 192.168.78.252 -&gt; 192.168.78.53 ICMP 98 Echo (ping) request  id=0x0abe, seq=13/3328, ttl=64
0.000707 192.168.78.53 -&gt; 192.168.78.252 ICMP 98 Echo (ping) reply    id=0x0abe, seq=13/3328, ttl=64 (request in 1)</code></pre><p>The main difference that I need to solve is in mine I get <code>84</code> for the protocol, whereas tshark prints <code>ICMP 98</code>. I could implement my own lookup table, but there is a large number of protocols and tshark already knows how to decode them, I just need to figure out how to get that in my parsing.</p></div><div id="question-tags" class="tags-container tags">tshark linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '13, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/60416386b8cacdb203359bad9078b477?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdwiegman&#39;s gravatar image" /><p>jdwiegman<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdwiegman has 2 accepted answers">100%</span></p></div></div><div id="comments-container-24544" class="comments-container"></div><div id="comment-tools-24544" class="comment-tools"></div><div class="clear"></div><div id="comment-24544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24545"></span>

<div id="answer-container-24545" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24545-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://ask.wireshark.org/questions/23482/use-tshark-to-write-protocol-like-the-column-in-wireshark">Found the answer</a></p><p><code>-e col.Protocol</code></p><p>Like always happens, you work on a problem for days, post the question then find the answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '13, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/60416386b8cacdb203359bad9078b477?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdwiegman&#39;s gravatar image" /><p>jdwiegman<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdwiegman has 2 accepted answers">100%</span></p></div></div><div id="comments-container-24545" class="comments-container"></div><div id="comment-tools-24545" class="comment-tools"></div><div class="clear"></div><div id="comment-24545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33972"></span>

<div id="answer-container-33972" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33972-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As of the 1.11.x and 1.12 versions of tshark, the field names are "_ws.col.Protocol" and "_ws.col.Info", instead of "col.Protocol" and "col.Info".</p><p>Example:</p><p><code>tshark -T fields -e _ws.col.Protocol -e _ws.col.Info</code></p><p>Source: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10201">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10201</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '14, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/028a4be69999143f43a3ed2e97f42159?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CraigGarrett&#39;s gravatar image" /><p>CraigGarrett<br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CraigGarrett has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '14, 10:19</p></div></div><div id="comments-container-33972" class="comments-container"></div><div id="comment-tools-33972" class="comment-tools"></div><div class="clear"></div><div id="comment-33972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

