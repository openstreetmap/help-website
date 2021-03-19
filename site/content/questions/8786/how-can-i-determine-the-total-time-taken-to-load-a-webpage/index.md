+++
type = "question"
title = "How can I determine the total time taken to load a Webpage?"
description = '''I would like to know the Total content size and Total time taken to load a particular Webpage in Wireshark. The time parameter in Wireshark shows either time elapsed from first frame or previous frame. How can I obtain the above parameters using Wireshark?'''
date = "2012-02-02T11:17:00Z"
lastmod = "2012-02-06T04:55:00Z"
weight = 8786
keywords = [ "http", "time" ]
aliases = [ "/questions/8786" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I determine the total time taken to load a Webpage?](/questions/8786/how-can-i-determine-the-total-time-taken-to-load-a-webpage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8786-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know the Total content size and Total time taken to load a particular Webpage in Wireshark. The time parameter in Wireshark shows either time elapsed from first frame or previous frame. How can I obtain the above parameters using Wireshark?</p></div><div id="question-tags" class="tags-container tags">http time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '12, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/84da5ede7d868490afe7e099e42aeed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rhiya&#39;s gravatar image" /><p>Rhiya<br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rhiya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Feb '12, 11:28</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8786" class="comments-container"></div><div id="comment-tools-8786" class="comment-tools"></div><div class="clear"></div><div id="comment-8786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8789"></span>

<div id="answer-container-8789" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8789-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would suggest using the Firebug plugin instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '12, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/e7d1d3994349a9ea0554a6430dbe2ec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naskop&#39;s gravatar image" /><p>naskop<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naskop has no accepted answers">0%</span></p></div></div><div id="comments-container-8789" class="comments-container"><span id="8790"></span><div id="comment-8790" class="comment"><div id="post-8790-score" class="comment-score"></div><div class="comment-text"><p>Would you mind updating your answer to explain how to use firebug to accomplish this?</p></div><div id="comment-8790-info" class="comment-info"><span class="comment-age">(02 Feb '12, 14:44)</span> multipleinte...</div></div><span id="8792"></span><div id="comment-8792" class="comment"><div id="post-8792-score" class="comment-score"></div><div class="comment-text"><p>In Firebug, simply open the Net tab and reload the page. It shows the load time of every object (css, js, html, etc.), and the total load time is shown at the bottom of the tab.</p><p>Chrome has a similar <a href="http://code.google.com/chrome/devtools/docs/network.html">tool</a> that's built-in. The total time is shown at the top in the timeline bar, farthest to the right.</p></div><div id="comment-8792-info" class="comment-info"><span class="comment-age">(02 Feb '12, 15:01)</span> helloworld</div></div><span id="8816"></span><div id="comment-8816" class="comment"><div id="post-8816-score" class="comment-score"></div><div class="comment-text"><p>Thank You , But I actually need to code a java program to find the Time from my saved Pcap file. Can you please let me know if it is possible with wireshark file.</p><p>Thank You :-)</p></div><div id="comment-8816-info" class="comment-info"><span class="comment-age">(03 Feb '12, 14:35)</span> Rhiya</div></div></div><div id="comment-tools-8789" class="comment-tools"></div><div class="clear"></div><div id="comment-8789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8842"></span>

<div id="answer-container-8842" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8842-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If there is only one TCP connection to the webserver I would filter for that and then either look at the summary statistic, which tells you all you need to know or if the connection is held alive for a longer idle time set a time reference on the SYN or the first GET request (your choice) and look at the relative time of the last data packet from the server arriving.</p><p>If there are multiple sessions to the webserver you can try to set the time reference on the first SYN packet and then filter for your IP and the servers IP and jump to the last data packet or your last ACK to the server and again look up the time it took at the relative time.</p><p>Regarding content size: Configuring cumulative bytes gives you a good hint on how much data (including per packet overhead) was transmitted in both directions. If you just want the downstream data, you'd have to filter on only webserver sourced packets with tcp.len greater zero and roughly substract the headers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '12, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Feb '12, 04:57</p></div></div><div id="comments-container-8842" class="comments-container"><span id="8940"></span><div id="comment-8940" class="comment"><div id="post-8940-score" class="comment-score"></div><div class="comment-text"><p>Thank You , I have followed a different approach meanwhile. Could you please tell me if this is correct?</p><p>Right Now I am filtering all Http packets and computing the summation of "Content-Length " field of Response packets based on URL ( i.e Http Host name). I am also calculating the time based on the difference between first GET and the Last Response received for that URL..Is that a correct way to do?</p><p>But the problem is, I am unable to identify the instance at which the Webpage would be refreshed.As in Start the capture -&gt; You hit www.google.com from your web browser -&gt;Hit www.facebook.com -&gt;www.google.com-&gt;Stop capturing. How can I get the packet which again requests for www.google.com for the second time, as it is not possible to tell just from Host name field of HTTp</p></div><div id="comment-8940-info" class="comment-info"><span class="comment-age">(09 Feb '12, 14:07)</span> Rhiya</div></div></div><div id="comment-tools-8842" class="comment-tools"></div><div class="clear"></div><div id="comment-8842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

