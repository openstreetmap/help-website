+++
type = "question"
title = "SMB Expression for Close Request Time..."
description = '''Hello, So I&#x27;m troubleshooting some SMB issues where files on a NAS are taking a long time to close. So I have a filter for &quot;smb2.cmd == 6&quot; which is the SMB command issued for closing a file. I can run a different filter &quot;tcp.ack == 1510 or tcp.seq == 1510&quot; which will give me the request and the ackn...'''
date = "2015-12-10T17:22:00Z"
lastmod = "2015-12-11T05:59:00Z"
weight = 48438
keywords = [ "smb2", "troubleshooting" ]
aliases = [ "/questions/48438" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [SMB Expression for Close Request Time...](/questions/48438/smb-expression-for-close-request-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48438-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>So I'm troubleshooting some SMB issues where files on a NAS are taking a long time to close. So I have a filter for "smb2.cmd == 6" which is the SMB command issued for closing a file. I can run a different filter "tcp.ack == 1510 or tcp.seq == 1510" which will give me the request and the acknowledgement.</p><p>But what really want to be able to create an expression that will allow me to filter on the close and any close function that is greater than let's say 20ms.</p><p>So I would assume using the "smb2.cmd == 6" along with something else would get me there. Can someone help me with that expression and/or filter? So maybe even a filter that gives me the close command, acknowledgement and only those with a time difference greater then a number a choose.</p><p>I'm being told closing files is taking 10-30 seconds so I would really want to search within that time frame.</p></div><div id="question-tags" class="tags-container tags">smb2 troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '15, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/4136f47fd762c7ca82d7455c7d5b6ee6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ew0506&#39;s gravatar image" /><p>ew0506<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ew0506 has no accepted answers">0%</span></p></div></div><div id="comments-container-48438" class="comments-container"><span id="48439"></span><div id="comment-48439" class="comment"><div id="post-48439-score" class="comment-score"></div><div class="comment-text"><p>The filter I was thinking was something to this degree, but I'm missing something cause it's still red (invalid).</p><p>smb2.cmd == 6 &amp;&amp; tcp.ack == &amp;&amp; or tcp.seq == &amp;&amp; time &gt; 1</p></div><div id="comment-48439-info" class="comment-info"><span class="comment-age">(10 Dec '15, 17:53)</span> ew0506</div></div></div><div id="comment-tools-48438" class="comment-tools"></div><div class="clear"></div><div id="comment-48438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48445"></span>

<div id="answer-container-48445" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48445-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Leaving aside the syntax errors in your suggestion of the filter, there may be an issue with the notion of time.</p><p><code>smb.time</code> is "time from samba request" (in seconds) and it is only calculated for responses to that request, and "command" and "request" may not mean the same. But try</p><p><code>smb2.cmd == 6 and smb2.time &gt; 0.02</code></p><p>If it is the solution, please accept it by clicking the checkmark. If it is not, send a <em>comment</em> to this answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '15, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Dec '15, 05:58</p></div></div><div id="comments-container-48445" class="comments-container"></div><div id="comment-tools-48445" class="comment-tools"></div><div class="clear"></div><div id="comment-48445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48447"></span>

<div id="answer-container-48447" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48447-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Filters can't be used to compare things between packets, they are a yes\no match on each packet in turn.</p><p>However, if the packet in question has a field, such as <code>smb2.time</code> which shows the time between the request and response, then that could be used in a filter.</p><p>A filter of <code>(smb2.cmd == 6) and smb2.time</code> will show all SMB2 close responses, the latter part of the filter can be modified to compare against a specific time value, e.g. <code>(smb2.time &gt; 0.1)</code> to display all responses that took greater than 100 mS from the request.</p><p>What that filter doesn't show is the associated request, and it's not possible to do that with a filter as there is no <code>smb2.time</code> field in the request.</p><p>The Wireshark <a href="https://wiki.wireshark.org/Mate">MATE</a> system may be able to help here, as that allows associations between packets to be built.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '15, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48447" class="comments-container"><span id="48456"></span><div id="comment-48456" class="comment"><div id="post-48456-score" class="comment-score"></div><div class="comment-text"><p>Thanks to both you, Graham and Sindy - your answers helped a tremendous amount. So it makes it that mush easier to widdle down a 288,000+ packet trace and and then follow only particular threads from there.</p><p>Much appreciated!</p></div><div id="comment-48456-info" class="comment-info"><span class="comment-age">(11 Dec '15, 09:15)</span> ew0506</div></div><span id="48507"></span><div id="comment-48507" class="comment"><div id="post-48507-score" class="comment-score"></div><div class="comment-text"><p>You can use TRANSUM to add SMB2 response times to request packet decodes. It will show as APDU Resp Time which you can then Apply as a column.</p></div><div id="comment-48507-info" class="comment-info"><span class="comment-age">(14 Dec '15, 06:32)</span> PaulOfford</div></div></div><div id="comment-tools-48447" class="comment-tools"></div><div class="clear"></div><div id="comment-48447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

