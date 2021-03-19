+++
type = "question"
title = "plain text automatic save"
description = '''is there a possibility &quot;plain text objects&quot; automatically export and in real time? I need the data in real time as individual files. thx'''
date = "2013-10-20T10:41:00Z"
lastmod = "2013-10-21T03:05:00Z"
weight = 26224
keywords = [ "real", "plain", "save", "time", "text" ]
aliases = [ "/questions/26224" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [plain text automatic save](/questions/26224/plain-text-automatic-save)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26224-score" class="post-score" title="current number of votes">0</div><span id="post-26224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>is there a possibility "plain text objects" automatically export and in real time? I need the data in real time as individual files.</p><p>thx</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-real" rel="tag" title="see questions tagged &#39;real&#39;">real</span> <span class="post-tag tag-link-plain" rel="tag" title="see questions tagged &#39;plain&#39;">plain</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span> <span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '13, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/0ca9044dc9c341761095139a07b00a6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sub2k&#39;s gravatar image" /><p><span>sub2k</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sub2k has no accepted answers">0%</span></p></div></div><div id="comments-container-26224" class="comments-container"></div><div id="comment-tools-26224" class="comment-tools"></div><div class="clear"></div><div id="comment-26224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26230"></span>

<div id="answer-container-26230" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26230-score" class="post-score" title="current number of votes">0</div><span id="post-26230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I need the data in real time as individual files.</p></blockquote><p>Unfortunately that's not possible with tshark/Wireshark. You can extract the TCP payload with tshark, however <strong>not</strong> in real time and <strong>not automatically</strong> as separate files.</p><p>See the following similar questions:</p><blockquote><p><a href="http://ask.wireshark.org/questions/11331/tshark-t-fields-question">http://ask.wireshark.org/questions/11331/tshark-t-fields-question</a><br />
<a href="http://ask.wireshark.org/questions/25371/how-to-extract-hex-data-from-ssl">http://ask.wireshark.org/questions/25371/how-to-extract-hex-data-from-ssl</a><br />
<a href="http://ask.wireshark.org/questions/23827/get-tcp-and-udp-payloads-with-tshark">http://ask.wireshark.org/questions/23827/get-tcp-and-udp-payloads-with-tshark</a><br />
<a href="http://ask.wireshark.org/questions/16268/how-do-i-extract-all-the-data-sections">http://ask.wireshark.org/questions/16268/how-do-i-extract-all-the-data-sections</a><br />
<a href="http://ask.wireshark.org/questions/16592/tcp-stream-output-in-pdml-format">http://ask.wireshark.org/questions/16592/tcp-stream-output-in-pdml-format</a></p></blockquote><p>What you need is kind of a forensic network tool. Please check one of the following tools</p><blockquote><p><a href="http://www.forensicswiki.org/wiki/Tcpflow">http://www.forensicswiki.org/wiki/Tcpflow</a><br />
<a href="http://ngrep.sourceforge.net/">http://ngrep.sourceforge.net/</a><br />
<a href="http://www.xplico.org/">http://www.xplico.org/</a><br />
<a href="http://www.cockos.com/assniffer/">http://www.cockos.com/assniffer/</a></p></blockquote><p>Or maybe another tool listed here</p><blockquote><p><a href="http://wiki.wireshark.org/Tools">http://wiki.wireshark.org/Tools</a><br />
<a href="http://www.winpcap.org/misc/links.htm">http://www.winpcap.org/misc/links.htm</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26230" class="comments-container"></div><div id="comment-tools-26230" class="comment-tools"></div><div class="clear"></div><div id="comment-26230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

