+++
type = "question"
title = "Can I specify a raw port number as a tshark command -e option"
description = '''Hi, I extract the tshark packet list fields into a CSV using: tshark -2 -q -ta -T fields -E separator=, -E quote=d -E header=y -e frame.number -e _ws.col.Time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e _ws.col.Info -r _file_name_  Rather than use tcp.srcport and tcp.dstport I&#x27;d like to inc...'''
date = "2017-04-15T15:00:00Z"
lastmod = "2017-04-15T16:45:00Z"
weight = 60850
keywords = [ "tshark" ]
aliases = [ "/questions/60850" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I specify a raw port number as a tshark command -e option](/questions/60850/can-i-specify-a-raw-port-number-as-a-tshark-command-e-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60850-score" class="post-score" title="current number of votes">0</div><span id="post-60850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I extract the tshark packet list fields into a CSV using:</p><pre><code>tshark -2 -q -ta -T fields -E separator=, -E quote=d -E header=y -e frame.number -e _ws.col.Time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e _ws.col.Info -r _file_name_</code></pre><p>Rather than use <code>tcp.srcport</code> and <code>tcp.dstport</code> I'd like to include the port number from any transport protocol. I can do this in Wireshark by defining columns with <code>Src port (unresolved)</code> and <code>Dest port (unresolved)</code>. Is there an equivalent for tshark command line parameters?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '17, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-60850" class="comments-container"></div><div id="comment-tools-60850" class="comment-tools"></div><div class="clear"></div><div id="comment-60850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60853"></span>

<div id="answer-container-60853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60853-score" class="post-score" title="current number of votes">0</div><span id="post-60853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not aware of a way to do this directly with Wireshark, but you might be able to write a Lua postdissector that utilizes field extractors of both the UDP and TCP source and destination ports and then add a new generic port number field which you can then specify on the <code>tshark</code> command-line, e.g., <code>-e transport.srcport -e transport.dstport</code>.</p><p>Another possible alternative might be to just specify the columns you want, but if you want them comma-separated in order to be able to export them to a CSV file, then that probably won't work for you. Here's what that might look like though:</p><pre><code>tshark.exe -o &quot;gui.column.format:\&quot;No.\&quot;,\&quot;%m\&quot;,\&quot;Time\&quot;,\&quot;%t\&quot;,\&quot;Source\&quot;,\&quot;%s\&quot;,\&quot;Destination\&quot;,\&quot;%d\&quot;,\&quot;Source Port\&quot;,\&quot;%S\&quot;,\&quot;Destination Port\&quot;,\&quot;%D\&quot;,\&quot;Info\&quot;,\&quot;%i\&quot;&quot; -r _file_name_</code></pre><p>Run <code>"tshark.exe -G column-formats"</code> for a list of all the column format specifiers and their meaning.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '17, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-60853" class="comments-container"></div><div id="comment-tools-60853" class="comment-tools"></div><div class="clear"></div><div id="comment-60853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

