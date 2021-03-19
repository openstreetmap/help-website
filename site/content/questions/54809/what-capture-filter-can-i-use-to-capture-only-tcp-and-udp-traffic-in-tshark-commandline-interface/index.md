+++
type = "question"
title = "What capture filter can I use to capture only TCP and UDP traffic in tshark commandline interface?"
description = '''HTTP uses port 80. I found this on the internet and used -f &quot;tcp port 80&quot; as the capture filter for capturing only HTTP traffic: tshark -i Ethernet -f &quot;tcp port 80&quot;  But since I am a newbie, searching for port used by TCP and that used by UDP has confused me, since they both appear to have so so man...'''
date = "2016-08-15T00:55:00Z"
lastmod = "2016-08-15T01:01:00Z"
weight = 54809
keywords = [ "udp", "capture-filter", "http", "tshark", "tcp" ]
aliases = [ "/questions/54809" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What capture filter can I use to capture only TCP and UDP traffic in tshark commandline interface?](/questions/54809/what-capture-filter-can-i-use-to-capture-only-tcp-and-udp-traffic-in-tshark-commandline-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54809-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HTTP uses port 80. I found this on the internet and used <code>-f "tcp port 80"</code> as the capture filter for capturing only HTTP traffic:</p><pre><code>tshark -i Ethernet -f &quot;tcp port 80&quot;</code></pre><p>But since I am a newbie, searching for port used by TCP and that used by UDP has confused me, since they both appear to have so so many ports.</p><p>So what capture filter do I use to capture only TCP and UDP traffic.</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">udp capture-filter http tshark tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '16, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p>Jesss<br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div></div><div id="comments-container-54809" class="comments-container"></div><div id="comment-tools-54809" class="comment-tools"></div><div class="clear"></div><div id="comment-54809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54810"></span>

<div id="answer-container-54810" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54810-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The manual with examples is <a href="https://wiki.wireshark.org/CaptureFilters">here</a>. For your case, it would be <code>-f "tcp or udp"</code>. Check the difference between "capture filter" and "display filter" as each of them has a different syntax and purpose (while the difference in purpose is clearly visible in Wireshark but much less clearly in tshark).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '16, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54810" class="comments-container"><span id="54811"></span><div id="comment-54811" class="comment"><div id="post-54811-score" class="comment-score"></div><div class="comment-text"><p><code>-f "tcp or udp"</code> is a display filter, not a capture filter. I need a capture filter.</p></div><div id="comment-54811-info" class="comment-info"><span class="comment-age">(15 Aug '16, 02:10)</span> Jesss</div></div><span id="54812"></span><div id="comment-54812" class="comment"><div id="post-54812-score" class="comment-score"></div><div class="comment-text"><p>I checked the manual. What I learnt from it is that for a capture filter based on protocol, I need to know the port number the protocol uses.</p></div><div id="comment-54812-info" class="comment-info"><span class="comment-age">(15 Aug '16, 02:14)</span> Jesss</div></div><span id="54813"></span><div id="comment-54813" class="comment"><div id="post-54813-score" class="comment-score">1</div><div class="comment-text"><p><code>-f</code> specifies a capture filter, <code>-Y</code> specifies a display filter. <code>tcp or udp</code> is a legal syntax in both. <code>tcp</code> is an abbreviation of <code>proto tcp</code> in capture filter syntax.</p><p>There are several protocol layers. UDP and TCP are transport protocols above IP so they are identified by a field in the IP header. HTTP or Telnet are application protocols using TCP as transport, and there the distinction based on TCP port number makes sense.</p></div><div id="comment-54813-info" class="comment-info"><span class="comment-age">(15 Aug '16, 02:17)</span> sindy</div></div></div><div id="comment-tools-54810" class="comment-tools"></div><div class="clear"></div><div id="comment-54810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

