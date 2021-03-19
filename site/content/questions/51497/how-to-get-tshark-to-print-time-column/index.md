+++
type = "question"
title = "How to get tshark to print Time column"
description = '''I&#x27;m trying to use the following command: tshark -n -i eth0 -T fields -e _ws.col.Time -e ip.src -e ip.dst ... But the output does not display the Time. The ip.src column is moved over by a tab, compared to when _ws.col.Time is not specified. But the space is blank. What gives?  Version: TShark 1.10.6...'''
date = "2016-04-07T14:42:00Z"
lastmod = "2016-04-07T22:35:00Z"
weight = 51497
keywords = [ "timestamp", "tshark" ]
aliases = [ "/questions/51497" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get tshark to print Time column](/questions/51497/how-to-get-tshark-to-print-time-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51497-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to use the following command:</p><p>tshark -n -i eth0 -T fields -e _ws.col.Time -e ip.src -e ip.dst ...</p><p>But the output does not display the Time. The ip.src column is moved over by a tab, compared to when _ws.col.Time is not specified. But the space is blank.</p><p>What gives?<br />
</p><p>Version: TShark 1.10.6 (v1.10.6 from master-1.10)</p><p>THX</p></div><div id="question-tags" class="tags-container tags">timestamp tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '16, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/b8609fd95460c405523743577b0f788e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfox&#39;s gravatar image" /><p>mfox<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfox has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-51497" class="comments-container"></div><div id="comment-tools-51497" class="comment-tools"></div><div class="clear"></div><div id="comment-51497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51498"></span>

<div id="answer-container-51498" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51498-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It turns out that frame.time works. But _ws.col.Time does not -- at least for me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '16, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/b8609fd95460c405523743577b0f788e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfox&#39;s gravatar image" /><p>mfox<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfox has no accepted answers">0%</span></p></div></div><div id="comments-container-51498" class="comments-container"><span id="51508"></span><div id="comment-51508" class="comment"><div id="post-51508-score" class="comment-score"></div><div class="comment-text"><p>Column names for use with <code>-e</code> used to be prefixed with <code>col.</code> but got changed to use <code>_ws.col.</code>. I'm not sure which version this occurred in, but if you check the output of <code>tshark -h</code> for the description of <code>-e</code> it will show <code>col.Info</code> or <code>_ws.col.Info</code> indicating which to use in that version.</p></div><div id="comment-51508-info" class="comment-info"><span class="comment-age">(08 Apr '16, 06:15)</span> grahamb ♦</div></div><span id="51513"></span><div id="comment-51513" class="comment"><div id="post-51513-score" class="comment-score"></div><div class="comment-text"><p>The <code>_ws.</code> prefix was introduced starting with the 1.11.0 development release, which was announced on October 13, 2013. See the news article here: <a href="https://www.wireshark.org/news/20131015.html">https://www.wireshark.org/news/20131015.html</a>. The first stable release that introduced the <code>_ws.</code> prefix was 1.12.0, announced on July 31, 2014. Here's that news article: <a href="https://www.wireshark.org/news/20140731.html">https://www.wireshark.org/news/20140731.html</a>.</p></div><div id="comment-51513-info" class="comment-info"><span class="comment-age">(08 Apr '16, 07:29)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-51498" class="comment-tools"></div><div class="clear"></div><div id="comment-51498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

