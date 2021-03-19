+++
type = "question"
title = "Meaning of values for results of &quot;-e frame.len&quot; - Tshark"
description = '''I am currently using this... tshark -r &quot;C:&#92;Users&#92;admin&#92;Desktop&#92;test&#92;capture.cap&quot; -o ip.use_geoip:TRUE -T fields -e frame.len -e ip.src -e ip.dst -e ip.geoip.dst_asnum My result... 12469 60 192.168.3.98 208.117.253.29 AS43515 YOUTUBE What values does the &quot;12469&quot; and &quot;60&quot; represent(I know frame length...'''
date = "2016-05-16T10:41:00Z"
lastmod = "2016-05-16T12:14:00Z"
weight = 52630
keywords = [ "line", "command", "length", "frame", "tshark" ]
aliases = [ "/questions/52630" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Meaning of values for results of "-e frame.len" - Tshark](/questions/52630/meaning-of-values-for-results-of-e-framelen-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52630-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently using this...</p><p><em>tshark -r "C:\Users\admin\Desktop\test\capture.cap" -o ip.use_geoip:TRUE -T fields -e frame.len -e ip.src -e ip.dst -e ip.geoip.dst_asnum</em></p><p>My result...</p><p><em>12469 60 192.168.3.98 208.117.253.29 AS43515 YOUTUBE</em></p><p>What values does the "12469" and "60" represent(I know frame length), but is the "12469" bytes and the "60" the number of packets?</p></div><div id="question-tags" class="tags-container tags">line command length frame tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '16, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p>zer0day<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '16, 10:42</p></div></div><div id="comments-container-52630" class="comments-container"></div><div id="comment-tools-52630" class="comment-tools"></div><div class="clear"></div><div id="comment-52630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52639"></span>

<div id="answer-container-52639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is that you're using an old version of Wireshark and it's incorrectly displaying the capture count (12469 in this case). What version of Wireshark are you using? You could try upgrading your version of Wireshark to see if it resolves your problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '16, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-52639" class="comments-container"><span id="52641"></span><div id="comment-52641" class="comment"><div id="post-52641-score" class="comment-score"></div><div class="comment-text"><p>I am using tshark version 1.12.8, less than 6 months old. This is a capture reflecting 40+ users on our network, so if you think it's incorrect cause it is a large number, just letting you know that it could be correct.</p></div><div id="comment-52641-info" class="comment-info"><span class="comment-age">(16 May '16, 12:33)</span> zer0day</div></div><span id="52643"></span><div id="comment-52643" class="comment"><div id="post-52643-score" class="comment-score"></div><div class="comment-text"><p>In that case, I'm not sure why the first number is being printed. I tried this on my system with both 1.12.0 and 1.12.11 and neither one print the first erroneously displayed number. Maybe it's data-dependent? Can you post the capture file somewhere?</p></div><div id="comment-52643-info" class="comment-info"><span class="comment-age">(16 May '16, 12:39)</span> cmaynard ♦♦</div></div><span id="52644"></span><div id="comment-52644" class="comment"><div id="post-52644-score" class="comment-score"></div><div class="comment-text"><p>My bad, the "12469" value is a count of how many frames were seen between the 192.168.x.x source and the destination, it's a line in my script that preforms this operation. So then , what does the "60" represent? 60b, 60kb, 60mb?</p></div><div id="comment-52644-info" class="comment-info"><span class="comment-age">(16 May '16, 12:47)</span> zer0day</div></div><span id="52646"></span><div id="comment-52646" class="comment"><div id="post-52646-score" class="comment-score">1</div><div class="comment-text"><p>The unit for frame length is bytes.</p></div><div id="comment-52646-info" class="comment-info"><span class="comment-age">(16 May '16, 13:10)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-52639" class="comment-tools"></div><div class="clear"></div><div id="comment-52639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

