+++
type = "question"
title = "Log analyzer or traffic analyzer"
description = '''Hi.   I have to export the logs captured with wireshark and make a report of the traffic. There is some program that can i use to help me with this?. Sorry for my English.  Thanks. '''
date = "2015-10-26T07:14:00Z"
lastmod = "2015-10-26T07:54:00Z"
weight = 46934
keywords = [ "analyze", "traffic", "log" ]
aliases = [ "/questions/46934" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Log analyzer or traffic analyzer](/questions/46934/log-analyzer-or-traffic-analyzer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46934-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I have to export the logs captured with wireshark and make a report of the traffic. There is some program that can i use to help me with this?.</p><p>Sorry for my English.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">analyze traffic log</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '15, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/22190e87da4221754fd631ce34fced2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buddhaa11&#39;s gravatar image" /><p>buddhaa11<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buddhaa11 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '15, 09:50</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-46934" class="comments-container"></div><div id="comment-tools-46934" class="comment-tools"></div><div class="clear"></div><div id="comment-46934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46938"></span>

<div id="answer-container-46938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46938-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has some inbuilt reporting</p><blockquote><p>Statistics -&gt; Summary<br />
Statistics -&gt; Conversations<br />
Statistics -&gt; Protocol Hiearachy<br />
Statistics -&gt; IO Graphs &lt;=== maybe the most usefull one for you !?!</p></blockquote><p>So, if that is not sufficient, what kind of reporting are you looking for?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '15, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-46938" class="comments-container"><span id="46942"></span><div id="comment-46942" class="comment"><div id="post-46942-score" class="comment-score"></div><div class="comment-text"><p>That's useful but i need manipulate the extracted data to make graphics. i'm looking for some way to extract a plane text o .CSV, that i can open with excel.</p></div><div id="comment-46942-info" class="comment-info"><span class="comment-age">(26 Oct '15, 08:11)</span> buddhaa11</div></div><span id="46943"></span><div id="comment-46943" class="comment"><div id="post-46943-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/like_this.jpg" alt="i have to do something like this" /></p></div><div id="comment-46943-info" class="comment-info"><span class="comment-age">(26 Oct '15, 09:12)</span> buddhaa11</div></div><span id="46945"></span><div id="comment-46945" class="comment"><div id="post-46945-score" class="comment-score"></div><div class="comment-text"><p>Then you can use tshark to export informations from the capture file in a "text format", readable by a spreadsheet software.</p><p>What kind of information do you need?</p><p>BTW: Please follow-up with a comment, instead on an answer, as that's how this site works. See the FAQ.</p></div><div id="comment-46945-info" class="comment-info"><span class="comment-age">(26 Oct '15, 09:49)</span> Kurt Knochner ♦</div></div><span id="46947"></span><div id="comment-46947" class="comment"><div id="post-46947-score" class="comment-score"></div><div class="comment-text"><p>Oh sorry for that.</p><p>i need, ip Source, ip dest, bytes, protocol, service.</p></div><div id="comment-46947-info" class="comment-info"><span class="comment-age">(26 Oct '15, 09:58)</span> buddhaa11</div></div><span id="46953"></span><div id="comment-46953" class="comment"><div id="post-46953-score" class="comment-score"></div><div class="comment-text"><p>Hm.. I'm unsure what you mean by "bytes", "protocol" and "service". Can you please post an example?</p></div><div id="comment-46953-info" class="comment-info"><span class="comment-age">(26 Oct '15, 13:02)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46938" class="comment-tools"></div><div class="clear"></div><div id="comment-46938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

