+++
type = "question"
title = "How to find upload values from two Ip Addresses"
description = '''Hi, I am using statistics ---&amp;gt; Conversations option in the Wireshark. Aim to to find how much upload is being done in-between two IP Addresses. Source IP is 10.99.18.20 and the destination is 10.99.18.86, I took exactly 5 minutes of capture and then stopped it. Form Conversation it showed me ~ 21...'''
date = "2013-03-21T06:32:00Z"
lastmod = "2013-03-21T07:01:00Z"
weight = 19706
keywords = [ "wireshark" ]
aliases = [ "/questions/19706" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to find upload values from two Ip Addresses](/questions/19706/how-to-find-upload-values-from-two-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19706-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using statistics ---&gt; Conversations option in the Wireshark. Aim to to find how much upload is being done in-between two IP Addresses.</p><p>Source IP is 10.99.18.20 and the destination is 10.99.18.86, I took exactly 5 minutes of capture and then stopped it.</p><p>Form Conversation it showed me ~ 218111 Bytes of data. But I am not sure how to calculate the Upload value and how much bandwidth is consumed from this number.</p><p>I used the Bit calculator and it showed 1704 kilobits. But I guess this is huge value. Can any body assist me on this please ?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/2fd4419ad615504ce0ad00bcbc0a0cd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kaasi&#39;s gravatar image" /><p>Kaasi<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kaasi has no accepted answers">0%</span></p></div></div><div id="comments-container-19706" class="comments-container"></div><div id="comment-tools-19706" class="comment-tools"></div><div class="clear"></div><div id="comment-19706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19708"></span>

<div id="answer-container-19708" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19708-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The conversation statistics already has a column for throughput on the right (labeled "bps A-&gt;B" or "bps A&lt;-B", it's a little confusing because you have to see which way the arrow points). Have you seen that, or do you need something else?</p><p>You can also filter on the conversation you want and open the Summary Statistics. Look at the "Displayed" Column at the bottom to see throughput etc for the connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19708" class="comments-container"><span id="19829"></span><div id="comment-19829" class="comment"><div id="post-19829-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thank you for your reply.</p><p>I tried what you've mentioned. I have a filter like the ones below:</p><p>ip.src == 10.99.18.20 and ip.dst == 10.99.18.86 and then I went to</p><p>Statistics--&gt; Clicked on Summary. It showed a value.</p><p>I have another doubt, The problem is, this is not matching up with data shown on Statistics----&gt; IO Graphs.</p><p>The Summary showed Average Bytes/Sec as - 43835 But the I/O graph showed as 6000 Bytes. Any idea why ?</p></div><div id="comment-19829-info" class="comment-info"><span class="comment-age">(26 Mar '13, 00:19)</span> Kaasi</div></div><span id="19840"></span><div id="comment-19840" class="comment"><div id="post-19840-score" class="comment-score"></div><div class="comment-text"><p>Did you set the I/O Graph to tick as byte and tick interval to 1 second? If so, the graph should closely match the summary on averaging the graph. It is often a little hard to compare the two because the I/O graph plots over time while the summary just averages values for the whole trace.</p></div><div id="comment-19840-info" class="comment-info"><span class="comment-age">(26 Mar '13, 07:31)</span> Jasper ♦♦</div></div></div><div id="comment-tools-19708" class="comment-tools"></div><div class="clear"></div><div id="comment-19708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

