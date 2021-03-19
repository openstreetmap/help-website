+++
type = "question"
title = "measure the total transmitted byte in a time interval"
description = '''I want to measure the total transmitted byte in a time interval from my captured traffic. e.g from time 46.3901 to time 46.4329 how many byte was transmitted.  Or if i see the IO Graphic. I want to measure the burst in byte from 187,3s to 188,7s. How can i measure this? Thank you for your help.  '''
date = "2012-03-28T03:07:00Z"
lastmod = "2012-03-28T03:30:00Z"
weight = 9805
keywords = [ "total", "burst", "bytes", "measure" ]
aliases = [ "/questions/9805" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [measure the total transmitted byte in a time interval](/questions/9805/measure-the-total-transmitted-byte-in-a-time-interval)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9805-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to measure the total transmitted byte in a time interval from my captured traffic. e.g from time 46.3901 to time 46.4329 how many byte was transmitted.</p><p>Or if i see the IO Graphic. I want to measure the burst in byte from 187,3s to 188,7s.</p><p>How can i measure this?</p><p>Thank you for your help.</p><p><img src="http://dl.dropbox.com/u/19366365/Bildschirmfoto1.png" alt="Foto" /> <img src="http://dl.dropbox.com/u/19366365/I%20O%20graphic" alt="IO Graphic" /></p></div><div id="question-tags" class="tags-container tags">total burst bytes measure</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '12, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/215af508b35bb00077dd46976031691e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hanamichi&#39;s gravatar image" /><p>hanamichi<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hanamichi has no accepted answers">0%</span></p></img></div></div><div id="comments-container-9805" class="comments-container"></div><div id="comment-tools-9805" class="comment-tools"></div><div class="clear"></div><div id="comment-9805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9810"></span>

<div id="answer-container-9810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9810-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>use a display-filter such as (frame.time&gt;="Mar 28, 2012 15:58:18.730" &amp;&amp; frame.time&lt;"Mar 28, 2012 15:58:18.770")</p><p>and then goto statistics &gt;summary&gt; and you will get what your looking for...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '12, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/6cb6685f12bd537f0f2e1e86a591e940?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sangmeshp&#39;s gravatar image" /><p>sangmeshp<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sangmeshp has no accepted answers">0%</span></p></img></div></div><div id="comments-container-9810" class="comments-container"></div><div id="comment-tools-9810" class="comment-tools"></div><div class="clear"></div><div id="comment-9810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9807"></span>

<div id="answer-container-9807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9807-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go to the preferences, edit your column settings and add a colum with the field type of "Cummulative Bytes". Go back to your packet list, select the packet you want to start at, and use the popup menu to set a time reference. That way the cummulative byte counter will start at that packet. Then move to the last packet and simply read the amount of bytes from the cummulative byte column.</p><p>Hint: if you want to determine the cummulative bytes of a single connection you should filter on it first, because otherwise packet/bytes from other connections will increase that number, too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '12, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9807" class="comments-container"><span id="9816"></span><div id="comment-9816" class="comment"><div id="post-9816-score" class="comment-score"></div><div class="comment-text"><p>thanks for your quick answer.</p><p>@Jasper: I want to analysis the traffic from website youtube. How can I filter here only packet/bytes from a website youtube?</p><p>[converted to a comment]</p></div><div id="comment-9816-info" class="comment-info"><span class="comment-age">(28 Mar '12, 05:53)</span> hanamichi</div></div><span id="9817"></span><div id="comment-9817" class="comment"><div id="post-9817-score" class="comment-score">1</div><div class="comment-text"><p>Usually you'll have to find out which IPs at youtube you're talking to, for example by using nslookup to find the IPs, and then filter on them with <strong>ip.addr==a.b.c.d or ip.address=e.f.g.h...</strong>.</p><p>Or you could filter on GET requests that contain youtube with a filter like this: <strong>http.request.full_uri contains "youtube"</strong> and then use the packets that you see to filter on the single tcp communications.</p><p>By the way, if you like one of the answers please accept it (round checkmark button next to it)</p></div><div id="comment-9817-info" class="comment-info"><span class="comment-age">(28 Mar '12, 06:00)</span> Jasper ♦♦</div></div><span id="9837"></span><div id="comment-9837" class="comment"><div id="post-9837-score" class="comment-score"></div><div class="comment-text"><p>@Jasper: I have now a I/O Graph with many buste. Is es possible to measure or filter the time interval between these burst?</p><p><img src="http://dl.dropbox.com/u/19366365/burst%20io%20graph" alt="alt text" /></p></div><div id="comment-9837-info" class="comment-info"><span class="comment-age">(29 Mar '12, 04:33)</span> hanamichi</div></div><span id="9851"></span><div id="comment-9851" class="comment"><div id="post-9851-score" class="comment-score"></div><div class="comment-text"><p>Well, you can click into the graph just where a peak starts, which will jump to the according approximate packet in the packet list. Mark it, and then click on the I/O graph again to jump to the end of a peak. Mark that packet, too, and then you could start looking at the packet between the two markers.</p></div><div id="comment-9851-info" class="comment-info"><span class="comment-age">(29 Mar '12, 13:56)</span> Jasper ♦♦</div></div></div><div id="comment-tools-9807" class="comment-tools"></div><div class="clear"></div><div id="comment-9807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

