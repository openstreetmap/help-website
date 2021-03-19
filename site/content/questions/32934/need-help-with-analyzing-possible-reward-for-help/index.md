+++
type = "question"
title = "Need help with analyzing. Possible reward for help."
description = '''In a few weeks I&#x27;ll have the chance to gather a massive amount of data from my schools network and I would like to do a bunch of statistics on what I collect (think bar graphs and so on). Some of the stuff I would like to do is:  Find the most visited websites (statistics -&amp;gt; http -&amp;gt; Load distr...'''
date = "2014-05-20T13:11:00Z"
lastmod = "2014-05-20T15:11:00Z"
weight = 32934
keywords = [ "graph", "statistics", "analysis" ]
aliases = [ "/questions/32934" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need help with analyzing. Possible reward for help.](/questions/32934/need-help-with-analyzing-possible-reward-for-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32934-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a few weeks I'll have the chance to gather a massive amount of data from my schools network and I would like to do a bunch of statistics on what I collect (think bar graphs and so on). Some of the stuff I would like to do is:</p><ul><li>Find the most visited websites (statistics -&gt; http -&gt; Load distribution isn't very accurate)</li><li>Who's using the most bandwidth.</li><li>What kind of traffic is going through (games, video streaming, websites and so on)</li><li>Can't think of anything else, but let me know if you have ideas.</li></ul><p>Somee of these things I know how to do, but not very well. If anyone could link me to guides or maybe even write something for me, on all of the topics I would be very very thankful. If I can get it to work just how I want, there might just be some kind of money reward, though I am just a poor student :)</p><p><strong>Edit:</strong> Basically I need some way to extract all this data automatically, as I'll probably capture a good few hundred gigabytes of data.</p></div><div id="question-tags" class="tags-container tags">graph statistics analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '14, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/bf0f3416dbd4075272c8c58e206cc20e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TumbaBit&#39;s gravatar image" /><p>TumbaBit<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TumbaBit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 May '14, 13:14</p></div></div><div id="comments-container-32934" class="comments-container"></div><div id="comment-tools-32934" class="comment-tools"></div><div class="clear"></div><div id="comment-32934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32939"></span>

<div id="answer-container-32939" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32939-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>think <strong>bar graphs</strong> and so on).<br />
<strong>What kind of traffic</strong> is going through (games, video streaming, websites and so on)<br />
as I'll probably <strong>capture a good few hundred gigabytes</strong> of data.</p></blockquote><p>With those requirements my answer is: Wireshark is the wrong tool for you.</p><p>Wireshark was designed and built as a network troubleshooting tool to look at network packets in order to analyze network problems. Although it offers some statistics, and with tshark, some scripting capabilities, it's not the best product out there for <strong>network monitoring</strong> and "accounting".</p><p>So, while you might be able to do parts of what you mentioned with Wireshark/tshark, you should have a look at other products that are able to classify network traffic (games, video streaming, etc.) and do some nice graphs on bandwidth usage per user/network/ip.</p><p>The bad news for you: There is no ready-to-use open source tool I know of that can do it for you. There are some commercial products available, but they are all targeted to the enterprise market, which means enterprise features and <strong>enterprise price</strong>. So, nothing for a poor student.</p><p>You can try to find an open source solution by searching for "network bandwidth monitoring software open source". You should also check out l7-Filter for traffic classification (and some monitoring).</p><blockquote><p><a href="http://l7-filter.clearfoundation.com/">http://l7-filter.clearfoundation.com/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '14, 15:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-32939" class="comments-container"><span id="32943"></span><div id="comment-32943" class="comment"><div id="post-32943-score" class="comment-score"></div><div class="comment-text"><p>Oh, thanks! I had asked on another forum if Wireshark was a good tool for what I wanted and all I got was a few people saying yes, but I guess you're right. Thank you for the help!</p></div><div id="comment-32943-info" class="comment-info"><span class="comment-age">(20 May '14, 21:10)</span> TumbaBit</div></div><span id="32957"></span><div id="comment-32957" class="comment"><div id="post-32957-score" class="comment-score"></div><div class="comment-text"><p>Here are some free options for you as a student</p><p>You could try Trisul (trisul.org). Trisul is free if you are only interested in keeping a rolling 3-day recent window of data. From your description, sounds like a fit.</p><p>Another alternative is ntop-ng, <a href="http://www.ntop.org/products/ntop/">http://www.ntop.org/products/ntop/</a> - although it is not very good at historical reporting.</p><p>If you dont mind a bit of a learning curve, Argus is quite a powerful tool <a href="http://qosient.com/argus/">http://qosient.com/argus/</a></p></div><div id="comment-32957-info" class="comment-info"><span class="comment-age">(21 May '14, 11:37)</span> VIVEKRJG</div></div></div><div id="comment-tools-32939" class="comment-tools"></div><div class="clear"></div><div id="comment-32939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

