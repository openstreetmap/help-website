+++
type = "question"
title = "how to convert .cap to .pcap"
description = '''Hi there I have over 300 cap files that some that had been generated. I&#x27;m looking to use network miner to analyse these files, the only trouble is network miner can only read pcap captures. I know you can re save a cap to pcap, but i dont want to do this 300 times. Is there a way to convert cap to p...'''
date = "2016-01-10T12:49:00Z"
lastmod = "2016-01-10T13:01:00Z"
weight = 49056
keywords = [ "to", "convert", "cap", "pcap" ]
aliases = [ "/questions/49056" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to convert .cap to .pcap](/questions/49056/how-to-convert-cap-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49056-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there I have over 300 cap files that some that had been generated. I'm looking to use network miner to analyse these files, the only trouble is network miner can only read pcap captures. I know you can re save a cap to pcap, but i dont want to do this 300 times. Is there a way to convert cap to pcap in a batch? or merge all 300 together in a batch then re save the unified batch to pcap??</p></div><div id="question-tags" class="tags-container tags">to convert cap pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '16, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/3fc6816112a0503d3e4c09fe134cf590?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kenny%20Kev&#39;s gravatar image" /><p>Kenny Kev<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kenny Kev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '16, 03:08</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-49056" class="comments-container"><span id="49070"></span><div id="comment-49070" class="comment"><div id="post-49070-score" class="comment-score"></div><div class="comment-text"><p>What is the intend of removing the question?</p></div><div id="comment-49070-info" class="comment-info"><span class="comment-age">(11 Jan '16, 02:06)</span> Jaap ♦</div></div><span id="49071"></span><div id="comment-49071" class="comment"><div id="post-49071-score" class="comment-score"></div><div class="comment-text"><p>I've reverted that change.</p></div><div id="comment-49071-info" class="comment-info"><span class="comment-age">(11 Jan '16, 03:08)</span> grahamb ♦</div></div><span id="49083"></span><div id="comment-49083" class="comment"><div id="post-49083-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What is the intend of removing the question?</p></blockquote><p>maybe, homework and the fear to get caught ?!?</p></div><div id="comment-49083-info" class="comment-info"><span class="comment-age">(11 Jan '16, 07:15)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-49056" class="comment-tools"></div><div class="clear"></div><div id="comment-49056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49057"></span>

<div id="answer-container-49057" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49057-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="https://www.wireshark.org/docs/man-pages/editcap.html">editcap</a> in a script.</p><blockquote><p>editcap -F pcap input.cap output.pcap</p></blockquote><p>If you <a href="http://stackoverflow.com/questions/138497/iterate-all-files-in-a-directory-using-a-for-loop">loop over the files in a script</a>, you can automatically convert all files.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '16, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jan '16, 13:08</p></div></div><div id="comments-container-49057" class="comments-container"><span id="49059"></span><div id="comment-49059" class="comment"><div id="post-49059-score" class="comment-score"></div><div class="comment-text"><p>see the link in my answer. (loop over files...).</p><p>Like:</p><blockquote><p>for /r %i in (*.cap) do editcap -F pcap %i %i.pcap</p></blockquote></div><div id="comment-49059-info" class="comment-info"><span class="comment-age">(10 Jan '16, 13:05)</span> Kurt Knochner ♦</div></div><span id="49064"></span><div id="comment-49064" class="comment"><div id="post-49064-score" class="comment-score"></div><div class="comment-text"><p>The examples are in my answer and my comment. What <strong>exactly</strong> does not work? Any error messages?</p><p>BTW: <strong>editcap</strong> is probably not in your PATH variable on Windows, so you'll have to start it with</p><blockquote><p>"c:\program files\wireshark\editcap"</p></blockquote><p>or</p><blockquote><p>"c:\program files (x86)\wireshark\editcap"</p></blockquote></div><div id="comment-49064-info" class="comment-info"><span class="comment-age">(10 Jan '16, 14:26)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-49057" class="comment-tools"></div><div class="clear"></div><div id="comment-49057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

