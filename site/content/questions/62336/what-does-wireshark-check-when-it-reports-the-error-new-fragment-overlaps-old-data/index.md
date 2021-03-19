+++
type = "question"
title = "what does wireshark check when it reports the error &quot; new fragment overlaps old data&quot;"
description = '''what does wireshark check when it reports the error &quot; new fragment overlaps old data&quot;? i mean what kind of analysis does wireshark does when it reports this error in TCP ?'''
date = "2017-06-27T07:05:00Z"
lastmod = "2017-06-27T07:51:00Z"
weight = 62336
keywords = [ "tcp", "error" ]
aliases = [ "/questions/62336" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what does wireshark check when it reports the error " new fragment overlaps old data"](/questions/62336/what-does-wireshark-check-when-it-reports-the-error-new-fragment-overlaps-old-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62336-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what does wireshark check when it reports the error " new fragment overlaps old data"? i mean what kind of analysis does wireshark does when it reports this error in TCP ?</p></div><div id="question-tags" class="tags-container tags">tcp error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '17, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/5c77cb959500e29e3fb5e2c971c4e3d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="soumya033&#39;s gravatar image" /><p>soumya033<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="soumya033 has no accepted answers">0%</span></p></div></div><div id="comments-container-62336" class="comments-container"></div><div id="comment-tools-62336" class="comment-tools"></div><div class="clear"></div><div id="comment-62336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62338"></span>

<div id="answer-container-62338" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62338-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Lower layer packets (IP) should contain each fragment of the higher layer packet (TCP) only once. If a lower layer packet contains fragment data which is also found in another lower layer packet, this gets reported.</p><pre><code>              +-----------+
              |bytes 1..37|
              +-----------+
          Higher layer packet

+-----------+ +------------+ +------------+
|bytes 1..20| |bytes 21..30| |bytes 27..37|
+-----------+ +------------+ +------------+
   packet 1       packet 2       packet 3</code></pre><p>This is an example of three fragments which overlap bytes 27, 28, 29 and 30, which are found in lower layer packet 2 and 3.</p><pre><code>              +-----------+
              |bytes 1..37|
              +-----------+
          Higher layer packet

+-----------+ +------------+ +------------+
|bytes 1..20| |bytes 21..37| |bytes 21..37|
+-----------+ +------------+ +------------+
   packet 1       packet 2       packet 3</code></pre><p>This is an example of three fragments where packet 3 is a retransmission of the fragment already seen in packet 2. This is a common cause of overlapping fragment data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '17, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62338" class="comments-container"><span id="62399"></span><div id="comment-62399" class="comment"><div id="post-62399-score" class="comment-score"></div><div class="comment-text"><p>TCP should not bother about this right , it is up to the application to do what it wants with it ? So why wireshark analysis classifies it with TCP error . It TCP really has to see it as error then there should be overlapping sequence numbers , because each byte is numbered in TCP in form of sequence numbers .</p><p>The capture which i have have all sequence number perfect there is no overlap of TCP sequence numbers , so the above explanation is not answering my question .</p></div><div id="comment-62399-info" class="comment-info"><span class="comment-age">(29 Jun '17, 05:28)</span> soumya033</div></div><span id="62400"></span><div id="comment-62400" class="comment"><div id="post-62400-score" class="comment-score"></div><div class="comment-text"><p>TCP should bother about this, it is its main purpose: to provide a reliable stream service. Try replacing it with UDP and watch what happens to your application in adverse network conditions.</p></div><div id="comment-62400-info" class="comment-info"><span class="comment-age">(29 Jun '17, 05:57)</span> Jaap ♦</div></div></div><div id="comment-tools-62338" class="comment-tools"></div><div class="clear"></div><div id="comment-62338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

