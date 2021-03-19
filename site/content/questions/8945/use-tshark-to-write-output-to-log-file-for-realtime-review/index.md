+++
type = "question"
title = "use tshark to write output to .log file for realtime review"
description = '''Folks, I am trying to leverage tshark to write output in plain text to a log file (.log), so I can review with a log viewer from another machine. My wireshark machine does not have a GUI, which is no big deal since I can use tshark. I have already learned how to limit pcap output by time and filesiz...'''
date = "2012-02-10T07:31:00Z"
lastmod = "2012-02-10T09:22:00Z"
weight = 8945
keywords = [ "log", "tshark" ]
aliases = [ "/questions/8945" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [use tshark to write output to .log file for realtime review](/questions/8945/use-tshark-to-write-output-to-log-file-for-realtime-review)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8945-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Folks, I am trying to leverage tshark to write output in plain text to a log file (.log), so I can review with a log viewer from another machine. My wireshark machine does not have a GUI, which is no big deal since I can use tshark.</p><p>I have already learned how to limit pcap output by time and filesize, but I need something that will write until stopped. I need the default data that is shown in a normal GUI dump, but I need to track via the .log file for a extended period of time.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">log tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '12, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/ae897e20625df9db38d37f98126bf90e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaz0nj4ckal&#39;s gravatar image" /><p>jaz0nj4ckal<br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaz0nj4ckal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 10 Feb '12, 09:24</p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span></p></div></div><div id="comments-container-8945" class="comments-container"></div><div id="comment-tools-8945" class="comment-tools"></div><div class="clear"></div><div id="comment-8945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8946"></span>

<div id="answer-container-8946" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8946-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Although I don't recommend doing this for long captures (it's inefficient and you'll quickly run out of disk space in this case), you can use the <code>-V</code> flag with file redirection:</p><pre><code>tshark {options} -V &gt; text.log</code></pre><p>A more suitable alternative (esp for long captures) is to use <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html"><code>dumpcap</code></a> to capture to a <code>pcap</code> file, and then later use <a href="http://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> to view the <code>pcap</code> (and you can still redirect <code>tshark</code>'s output to a log file as indicated above).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-8946" class="comments-container"><span id="8952"></span><div id="comment-8952" class="comment"><div id="post-8952-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much!!!</p></div><div id="comment-8952-info" class="comment-info"><span class="comment-age">(10 Feb '12, 11:02)</span> jaz0nj4ckal</div></div></div><div id="comment-tools-8946" class="comment-tools"></div><div class="clear"></div><div id="comment-8946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

