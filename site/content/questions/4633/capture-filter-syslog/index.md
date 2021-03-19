+++
type = "question"
title = "capture filter syslog"
description = '''Hi All, How can i filter packets using &quot;capture filter&quot; to filter syslog packets ? Thanks'''
date = "2011-06-20T02:52:00Z"
lastmod = "2011-06-20T11:35:00Z"
weight = 4633
keywords = [ "syslog" ]
aliases = [ "/questions/4633" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter syslog](/questions/4633/capture-filter-syslog)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4633-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>How can i filter packets using "capture filter" to filter syslog packets ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">syslog</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '11, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/e95e9ca9a85b787c4085529c2eabe2b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nirh&#39;s gravatar image" /><p>nirh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nirh has no accepted answers">0%</span></p></div></div><div id="comments-container-4633" class="comments-container"></div><div id="comment-tools-4633" class="comment-tools"></div><div class="clear"></div><div id="comment-4633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4638"></span>

<div id="answer-container-4638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4638-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>$ egrep -i syslog /etc/services
syslog          514/udp #</code></pre><p>so try "udp port 514" or "udp port syslog".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '11, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4638" class="comments-container"><span id="4664"></span><div id="comment-4664" class="comment"><div id="post-4664-score" class="comment-score"></div><div class="comment-text"><p><code>[[email protected]:Active] / # grep syslog /etc/services</code></p><p><code>syslog     514/udp</code></p><p><code>syslog-conn    601/tcp             # Reliable Syslog Service</code></p><p><code>syslog-conn    601/udp             # Reliable Syslog Service</code></p><p><code>[[email protected]:Active] / #</code></p><p>So you might want to use the filter "udp port 514 or port 601"</p></div><div id="comment-4664-info" class="comment-info"><span class="comment-age">(22 Jun '11, 04:12)</span> SYN-bit ♦♦</div></div><span id="4701"></span><div id="comment-4701" class="comment"><div id="post-4701-score" class="comment-score">1</div><div class="comment-text"><p>Note that the Reliable Syslog Service, as specified by <a href="http://tools.ietf.org/html/rfc3195">RFC 3195</a>, is <em>very</em> different from traditional syslog; it runs over <a href="http://beepcore.org/">BEEP</a>, which runs over TCP.</p><p>While Wireshark has a BEEP dissector, it doesn't specifically know about the Reliable Syslog Service, so it might not dissect that as desired.</p></div><div id="comment-4701-info" class="comment-info"><span class="comment-age">(23 Jun '11, 10:32)</span> Guy Harris ♦♦</div></div><span id="4707"></span><div id="comment-4707" class="comment"><div id="post-4707-score" class="comment-score"></div><div class="comment-text"><p>OK, learned something today, I did not know there was the BEEP protocol in between, actually, I did not know the reliable syslog service was more than just syslog over TCP.</p><p>On my NetScreen I can use syslog over TCP, but by default that uses port 514 as it turns out. I did not check the port before on my NetScreen, so I just grepped in my virtual F5 box (on which I was logged in anyways) and assumed 601 was for syslog over TCP.</p><p>So all-in-all one might want to capture with "port 514 or tcp port 601" :-)</p></div><div id="comment-4707-info" class="comment-info"><span class="comment-age">(23 Jun '11, 12:19)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-4638" class="comment-tools"></div><div class="clear"></div><div id="comment-4638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

