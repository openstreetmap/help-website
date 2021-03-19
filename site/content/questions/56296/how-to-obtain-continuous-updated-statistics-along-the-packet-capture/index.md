+++
type = "question"
title = "How to obtain continuous updated statistics along the packet capture"
description = '''How can I have the ouput of  tshark -Y usb -z endpoints,ip ================================================================================ IPv4 Endpoints Filter:&amp;lt;No Filter&amp;gt; Packets | | Bytes | | Tx Packets | | Tx Bytes | | Rx Packets |  172.217.18.110 5314 5425872 3504 5305056 1810  192.168.1...'''
date = "2016-10-11T09:16:00Z"
lastmod = "2016-10-11T10:24:00Z"
weight = 56296
keywords = [ "statistics", "tshark" ]
aliases = [ "/questions/56296" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to obtain continuous updated statistics along the packet capture](/questions/56296/how-to-obtain-continuous-updated-statistics-along-the-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56296-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I have the ouput of</p><pre><code>tshark -Y usb -z endpoints,ip
================================================================================
IPv4 Endpoints
Filter:&lt;No Filter&gt;
Packets  | |  Bytes  | | Tx Packets | | Tx Bytes | | Rx Packets |  
172.217.18.110               5314       5425872       3504         5305056        1810         
192.168.1.55                5314       5425872       1810          120816        3504           
192.168.1.9                  1           272          1             272           0                
================================================================================</code></pre><p>in a dynamical fashion. This table should be displayed continuously on my terminal and have it updated along the packet capture.</p></div><div id="question-tags" class="tags-container tags">statistics tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '16, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/1d0a5c898c23c1ae1a7b009804920031?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user31415&#39;s gravatar image" /><p>user31415<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user31415 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Oct '16, 09:16</p></div></div><div id="comments-container-56296" class="comments-container"><span id="56297"></span><div id="comment-56297" class="comment"><div id="post-56297-score" class="comment-score"></div><div class="comment-text"><p>Can you imagine dynamic updates of a list of 10000+ IP addresses? I mean, this is not something you would implement as a generic feature, not only because it would generate a lot of load on the text output subsystem but mainly because the output would be totally impossible to deal with for the human observing it. So if you need such functionality for your particular scenario with less IP addresses on the wire than lines in your terminal window, I'd recommend to pipe the normal output of tshark <code>-T fields -e ip.src -e ip.dst</code> to stdin of your own piece of code (a perl script is enough) which would then do what you want.</p></div><div id="comment-56297-info" class="comment-info"><span class="comment-age">(11 Oct '16, 10:13)</span> sindy</div></div></div><div id="comment-tools-56296" class="comment-tools"></div><div class="clear"></div><div id="comment-56296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56298"></span>

<div id="answer-container-56298" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56298-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could maybe use a tool designed for the job, e.g. <a href="https://en.wikipedia.org/wiki/Ntop">ntop</a> or <a href="https://github.com/ntop/ntopng">ntopng</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '16, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56298" class="comments-container"></div><div id="comment-tools-56298" class="comment-tools"></div><div class="clear"></div><div id="comment-56298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

