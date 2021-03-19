+++
type = "question"
title = "How to use (pre)-master-secret log file with tshark"
description = '''Hi!Is there the way to make tshark use (pre)-master-secret log file to decrypt ssl traffic as full version does ? '''
date = "2015-10-19T09:23:00Z"
lastmod = "2015-10-28T10:24:00Z"
weight = 46699
keywords = [ "ssl", "tshark" ]
aliases = [ "/questions/46699" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to use (pre)-master-secret log file with tshark](/questions/46699/how-to-use-pre-master-secret-log-file-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46699-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!Is there the way to make tshark use (pre)-master-secret log file to decrypt ssl traffic as full version does ?</p></div><div id="question-tags" class="tags-container tags">ssl tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/59ab875b84a6f1de9278386fd160f056?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ArkTaS&#39;s gravatar image" /><p>ArkTaS<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ArkTaS has no accepted answers">0%</span></p></div></div><div id="comments-container-46699" class="comments-container"></div><div id="comment-tools-46699" class="comment-tools"></div><div class="clear"></div><div id="comment-46699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47025"></span>

<div id="answer-container-47025" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47025-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The -o option should do the trick for <code>tshark</code> (this works for <code>wireshark</code> too!):</p><pre><code>tshark -nr input.pcap -o ssl.keylog_file:/path/to/your/SSLKEYLOGFILE</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/0142b62cc28b774da26cdd0daaccf816?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xixel&#39;s gravatar image" /><p>xixel<br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xixel has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Oct '15, 04:14</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-47025" class="comments-container"><span id="47057"></span><div id="comment-47057" class="comment"><div id="post-47057-score" class="comment-score"></div><div class="comment-text"><p>@xixel: I accepted your answer, as it correctly answers the question. And you're right. I overlooked the word tshark in the question title AND the questions itself ;-)</p></div><div id="comment-47057-info" class="comment-info"><span class="comment-age">(29 Oct '15, 04:13)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47025" class="comment-tools"></div><div class="clear"></div><div id="comment-47025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46728"></span>

<div id="answer-container-46728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46728-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please take a look at the following question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/29936/decrypting-ssl-traffic-in-wireshark-processed-by-sslsniff">https://ask.wireshark.org/questions/29936/decrypting-ssl-traffic-in-wireshark-processed-by-sslsniff</a><br />
</p></blockquote><p>or this online resource.</p><blockquote><p><a href="http://www.root9.net/2012/11/ssl-decryption-with-wireshark-private.html">http://www.root9.net/2012/11/ssl-decryption-with-wireshark-private.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-46728" class="comments-container"></div><div id="comment-tools-46728" class="comment-tools"></div><div class="clear"></div><div id="comment-46728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

