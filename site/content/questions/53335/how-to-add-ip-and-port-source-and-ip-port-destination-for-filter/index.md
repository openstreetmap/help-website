+++
type = "question"
title = "how to add ip and port source and ip port destination for filter?"
description = '''how to add ip and port source and ip port destination for filter? How to monitoring sorce Ip and port /destination ip and port for filter in wireshark?'''
date = "2016-06-09T07:50:00Z"
lastmod = "2016-06-09T08:16:00Z"
weight = 53335
keywords = [ "ip", "add", "destination", "port", "source" ]
aliases = [ "/questions/53335" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to add ip and port source and ip port destination for filter?](/questions/53335/how-to-add-ip-and-port-source-and-ip-port-destination-for-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53335-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to add ip and port source and ip port destination for filter?</p><p>How to monitoring sorce Ip and port /destination ip and port for filter in wireshark?</p></div><div id="question-tags" class="tags-container tags">ip add destination port source</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '16, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/d819e9d5f0dacd450723f691878ff035?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anderson_araujo&#39;s gravatar image" /><p>anderson_araujo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anderson_araujo has no accepted answers">0%</span></p></div></div><div id="comments-container-53335" class="comments-container"><span id="53336"></span><div id="comment-53336" class="comment"><div id="post-53336-score" class="comment-score"></div><div class="comment-text"><p>Is this for a <a href="https://wiki.wireshark.org/CaptureFilters">capture filter</a> or a <a href="https://wiki.wireshark.org/DisplayFilters">display filter</a>?</p><p>Have you looked at the user guide sections on <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html">filtering when capturing</a> and <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkDisplayFilterSection.html">filtering when viewing</a>?</p><p>What have you tried?</p></div><div id="comment-53336-info" class="comment-info"><span class="comment-age">(09 Jun '16, 08:11)</span> grahamb ♦</div></div><span id="53338"></span><div id="comment-53338" class="comment"><div id="post-53338-score" class="comment-score"></div><div class="comment-text"><p>I need to monitor the response time of several communications from a server. Requests from other applications on other servers And requests within the own server</p><p>How do I add the monitoring processes?</p><p>Localhost = server1</p><p>localhost for server2 and port localhost for server3 and port</p><p>localhost port 9443 for localhost port 9444 localhost port 9444 for localhost port 9443</p></div><div id="comment-53338-info" class="comment-info"><span class="comment-age">(09 Jun '16, 08:25)</span> anderson_araujo</div></div></div><div id="comment-tools-53335" class="comment-tools"></div><div class="clear"></div><div id="comment-53335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53337"></span>

<div id="answer-container-53337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53337-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you'll have some reading to do:</p><ul><li><a href="https://wiki.wireshark.org/DisplayFilters">Display filters, wiki article</a></li><li><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">Display filters, Users Guide</a></li><li><a href="https://wiki.wireshark.org/CaptureFilters">Caapture filters, wiki article</a></li></ul><p>What you're looking at is creating (display) filter expressions with <code>ip.src</code> and <code>ip.dst</code>, and <code>tcp.srcport</code> and <code>tcp.dstport</code> or <code>udp.srcport</code> and <code>udp.dstport</code>.</p><p>When you want to filter during capture the BPF expression elements are <code>ip src</code> and <code>ip dst</code>, and <code>port</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '16, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53337" class="comments-container"><span id="53346"></span><div id="comment-53346" class="comment"><div id="post-53346-score" class="comment-score"></div><div class="comment-text"><p>...and maybe you also need to adjust your understanding of how Wireshark works:</p><blockquote><p>How do I add the monitoring processes?</p></blockquote><p>You do not set up individual monitoring processes, one per socket pair, in Wireshark; you use a single process to monitor all the traffic on one or more interfaces, and you may optionally use a capture filter to control which frames will be stored to the capture file. When you analyse the capture later, you may use a display filter to further restrict the number of packets shown.</p></div><div id="comment-53346-info" class="comment-info"><span class="comment-age">(10 Jun '16, 03:25)</span> sindy</div></div></div><div id="comment-tools-53337" class="comment-tools"></div><div class="clear"></div><div id="comment-53337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

