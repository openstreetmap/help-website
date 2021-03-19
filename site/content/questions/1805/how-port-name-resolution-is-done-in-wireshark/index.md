+++
type = "question"
title = "How port name resolution is done in Wireshark ?"
description = '''i want to know about how port name resolution is done in wireshark? Directly using well known port numbers to match with the names or is there any other methods used for this purpose while decoding the port numbers ? thanks'''
date = "2011-01-18T23:05:00Z"
lastmod = "2011-01-18T23:46:00Z"
weight = 1805
keywords = [ "decoding", "port", "wireshark" ]
aliases = [ "/questions/1805" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How port name resolution is done in Wireshark ?](/questions/1805/how-port-name-resolution-is-done-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1805-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to know about how port name resolution is done in wireshark? Directly using well known port numbers to match with the names or is there any other methods used for this purpose while decoding the port numbers ?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">decoding port wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '11, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/bde1409a68745702a5dd0f41c6a544e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="berkey&#39;s gravatar image" /><p>berkey<br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="berkey has no accepted answers">0%</span></p></div></div><div id="comments-container-1805" class="comments-container"></div><div id="comment-tools-1805" class="comment-tools"></div><div class="clear"></div><div id="comment-1805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1806"></span>

<div id="answer-container-1806" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1806-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the file 'services' in your Wireshark installation.</p><pre><code># This is a local copy of the IANA port-numbers file.
#
# $Id: services 34645 2010-10-25 18:24:59Z morriss $
#
# Wireshark uses it to resolve port numbers into human readable
# service names, e.g. TCP port 80 -&gt; http.
#
# It is subject to copyright and being used with IANA&#39;s permission:
# http://www.wireshark.org/lists/wireshark-dev/200708/msg00160.html
#
# The original file can be found at:
# http://www.iana.org/assignments/port-numbers
#</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '11, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1806" class="comments-container"><span id="1862"></span><div id="comment-1862" class="comment"><div id="post-1862-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, thanks for the answer +1, Do you have any idea how the source and destination is identified if the there is no syn seen, we can say if my traces includes partial ones...</p></div><div id="comment-1862-info" class="comment-info"><span class="comment-age">(21 Jan '11, 13:39)</span> berkey</div></div><span id="1871"></span><div id="comment-1871" class="comment"><div id="post-1871-score" class="comment-score"></div><div class="comment-text"><p>Ports, hence port number name resolution aren't direction related. The concept of source and destination comes from their place in the protocol messages. For TCP, which you are referring to, it's the source port (tcp.srcport) and destination port (tcp.dstport).</p></div><div id="comment-1871-info" class="comment-info"><span class="comment-age">(22 Jan '11, 01:27)</span> Jaap ♦</div></div></div><div id="comment-tools-1806" class="comment-tools"></div><div class="clear"></div><div id="comment-1806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

