+++
type = "question"
title = "Capture retaining only conversation data"
description = '''I have a need to set up a capture for 24 hours and what I am interested in keeping is just the information in the Statistics | Conversations | TCP or UDP tabs, just interested in what IPs are talking to each other and what ports were used. There will be a lot of data if I try to keep all of the pack...'''
date = "2013-03-21T11:56:00Z"
lastmod = "2013-03-21T13:05:00Z"
weight = 19727
keywords = [ "conversationcapture" ]
aliases = [ "/questions/19727" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture retaining only conversation data](/questions/19727/capture-retaining-only-conversation-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19727-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a need to set up a capture for 24 hours and what I am interested in keeping is just the information in the Statistics | Conversations | TCP or UDP tabs, just interested in what IPs are talking to each other and what ports were used. There will be a lot of data if I try to keep all of the packets, is there a way to just have the capture running, retain the conversation information, and not save the data?</p></div><div id="question-tags" class="tags-container tags">conversationcapture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '13, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/02cc767ba6fd207c6c6b35f42b8a45e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richter&#39;s gravatar image" /><p>Richter<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richter has no accepted answers">0%</span></p></div></div><div id="comments-container-19727" class="comments-container"></div><div id="comment-tools-19727" class="comment-tools"></div><div class="clear"></div><div id="comment-19727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19731"></span>

<div id="answer-container-19731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19731-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark and tshark keep state information in memory and are not the best tools for monitoring long-term. Especially if you are only interested in conversation statistics.</p><p>Have a look at <a href="http://www.ntop.org/">ntop</a>, which exactly does what you want :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19731" class="comments-container"></div><div id="comment-tools-19731" class="comment-tools"></div><div class="clear"></div><div id="comment-19731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19728"></span>

<div id="answer-container-19728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Tshark[a command line equivalent of wireshark] might be one of the solutions. With that You can give the duration of the capture.You can set the capture filter for tcp || udp.You can retrieve the fields you want at the end by using -Tfileds option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '13, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Mar '13, 12:07</p></div></div><div id="comments-container-19728" class="comments-container"></div><div id="comment-tools-19728" class="comment-tools"></div><div class="clear"></div><div id="comment-19728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

