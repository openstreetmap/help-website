+++
type = "question"
title = "tshark command to write payload to a file"
description = '''Hi, Can some tell me what are the arguments that we need to pass to tshark command to capture all the request and response(http xml) messages and write them to a file in txt format? I am aware of -W option, but the issue is that the file data is not readable; it can only be readable by a tool like w...'''
date = "2012-05-28T02:19:00Z"
lastmod = "2012-05-28T06:31:00Z"
weight = 11421
keywords = [ "tshark", "payload" ]
aliases = [ "/questions/11421" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark command to write payload to a file](/questions/11421/tshark-command-to-write-payload-to-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11421-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Can some tell me what are the arguments that we need to pass to tshark command to capture all the request and response(http xml) messages and write them to a file in txt format? I am aware of <code>-W</code> option, but the issue is that the file data is not readable; it can only be readable by a tool like wireshark. My plan is to read the payload messages from a java code after getting the data into a file by using tshark command.</p></div><div id="question-tags" class="tags-container tags">tshark payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '12, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/54dfb1796a8beedf9843a326d673eaae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vikram&#39;s gravatar image" /><p>vikram<br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vikram has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 May '12, 07:39</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-11421" class="comments-container"><span id="11424"></span><div id="comment-11424" class="comment"><div id="post-11424-score" class="comment-score"></div><div class="comment-text"><p>Hi, I am able to use the below command and able to see the payload...</p><p><code>tshark -r test2.log -R "http" -V</code></p><p>(I used <code>tshark -i eth1 -d tcp.port=8101,http -w test2.log</code> for capturing the traffic)</p><p>The problem now is along with the payload I see a lot of additional frame network related data. Can someone tell me any filter expression that I can use so that I will get only payload (http req/resp messages) or at least with minimal network related data?</p></div><div id="comment-11424-info" class="comment-info"><span class="comment-age">(28 May '12, 06:23)</span> vikram</div></div><span id="11425"></span><div id="comment-11425" class="comment"><div id="post-11425-score" class="comment-score"></div><div class="comment-text"><p>From the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark manual page</a>:</p><blockquote><p>NOTE: -w provides raw packet data, not text. If you want text output you need to redirect stdout (e.g. using '&gt;'), don't use the -w option for this.</p></blockquote></div><div id="comment-11425-info" class="comment-info"><span class="comment-age">(28 May '12, 06:28)</span> Jaap ♦</div></div></div><div id="comment-tools-11421" class="comment-tools"></div><div class="clear"></div><div id="comment-11421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11426"></span>

<div id="answer-container-11426" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11426-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark manual page</a>:</p><blockquote><p>-T pdml|psml|ps|text|fields</p><p>pdml Packet Details Markup Language, an XML-based format for the details of a decoded packet. This information is equivalent to the packet details printed with the -V flag.</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '12, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-11426" class="comments-container"><span id="11432"></span><div id="comment-11432" class="comment"><div id="post-11432-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap, Thanks a lot for your reply.I am intrested in reading only the actaul messge that is being sent(in my case it is a xml)..is there any way to filter out maxium data that is being captured and get only the payload.When i use the -T pdml even the frames related network information is also coming in the from of xml and the file is becoming too huge.</p></div><div id="comment-11432-info" class="comment-info"><span class="comment-age">(29 May '12, 00:24)</span> vikram</div></div><span id="11468"></span><div id="comment-11468" class="comment"><div id="post-11468-score" class="comment-score"></div><div class="comment-text"><p>tshark -i eth1 -R http -V &gt; <a href="http://test2.txt">test2.txt</a> when i use the above command,the data is coming in txt format..how ever some times the payload messge is only coming as hexadecimal format..is there any filter option to get the payload data as simple text</p></div><div id="comment-11468-info" class="comment-info"><span class="comment-age">(30 May '12, 02:07)</span> vikram</div></div></div><div id="comment-tools-11426" class="comment-tools"></div><div class="clear"></div><div id="comment-11426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

