+++
type = "question"
title = "process traffic with Lua"
description = '''Hi, I&#x27;m writing a program with Lua processing the captured data in real time. I need to process data collected at the end of each minute (I collect the data for a minute or any other suitable period and at the end of the period I will process the data collected withen this peroid only and start coll...'''
date = "2012-02-12T23:05:00Z"
lastmod = "2012-02-13T02:57:00Z"
weight = 8971
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/8971" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [process traffic with Lua](/questions/8971/process-traffic-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8971-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm writing a program with Lua processing the captured data in real time. I need to process data collected at the end of each minute (I collect the data for a minute or any other suitable period and at the end of the period I will process the data collected withen this peroid only and start collecting the data for the next period) I'm afraid of losing data in the time between processing data and starting collecting data again in the new period,is it possible to happen? is there any hint can be given to make sure that all data are captured and processed carefully?<br />
Also, I'm in need for a piece of code written in Lua that can check any octect in the IP address. Appreciating any help from everyone Regards</p></div><div id="question-tags" class="tags-container tags">lua tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '12, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p>Leena<br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-8971" class="comments-container"><span id="8987"></span><div id="comment-8987" class="comment"><div id="post-8987-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Also, I'm in need for a piece of code written in Lua that can check any octect in the IP address.</p></blockquote><p>I think you should ask that in a new question; not in this post.</p></div><div id="comment-8987-info" class="comment-info"><span class="comment-age">(13 Feb '12, 20:16)</span> helloworld</div></div><span id="8991"></span><div id="comment-8991" class="comment"><div id="post-8991-score" class="comment-score"></div><div class="comment-text"><p>Thanks SYNbit for your answer, but I need the time of collecting to start processing also, just a part of the process will be at the time end</p></div><div id="comment-8991-info" class="comment-info"><span class="comment-age">(14 Feb '12, 01:34)</span> Leena</div></div></div><div id="comment-tools-8971" class="comment-tools"></div><div class="clear"></div><div id="comment-8971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8973"></span>

<div id="answer-container-8973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8973-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you kind of post-process each minute any way, I would say your best bet would be to use dumpcap with a duration limit of 1 minute. That will create files of one-minute intervals which you can then process individually.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '12, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8973" class="comments-container"></div><div id="comment-tools-8973" class="comment-tools"></div><div class="clear"></div><div id="comment-8973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

