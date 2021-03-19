+++
type = "question"
title = "trouble shoot capture"
description = '''Hello, I am having an issue in running our in house developed application. This application access remotely setup SQL Server to establish connection. we were using the application since last 4 months. unfortunately on last friday i do not know what happened and just this location is not able to run ...'''
date = "2011-06-07T22:36:00Z"
lastmod = "2011-06-08T12:08:00Z"
weight = 4449
keywords = [ "capture", "troubleshooting", "analysis" ]
aliases = [ "/questions/4449" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [trouble shoot capture](/questions/4449/trouble-shoot-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4449-score" class="post-score" title="current number of votes">0</div><span id="post-4449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am having an issue in running our in house developed application. This application access remotely setup SQL Server to establish connection. we were using the application since last 4 months. unfortunately on last friday i do not know what happened and just this location is not able to run the application as it is not able to establish connection with SQL server. As trouble shooting i have replaced router, by pass whole network just connected my laptop and tried to run application but did not worked.</p><p>So i connected my pc directly to ISP modem ( Charter) and captured the data flow between my pc and server. I am a new person for networking and do not know how to read the captured packets. so i am attaching the captured packet log with this.</p><p>please if you can make out of this log and understand what it is saying please advise me.</p><p>Thanks for looking into my question.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '11, 22:36</strong></p><img src="https://secure.gravatar.com/avatar/72f763da37a74d5fe4d10620f2c66aa0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bharatp80&#39;s gravatar image" /><p><span>bharatp80</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bharatp80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>08 Jun '11, 19:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4449" class="comments-container"></div><div id="comment-tools-4449" class="comment-tools"></div><div class="clear"></div><div id="comment-4449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4456"></span>

<div id="answer-container-4456" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4456-score" class="post-score" title="current number of votes">0</div><span id="post-4456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>SQL typically connects via port 1433. Try using tcp.port == 1433 for a display filter when you try to connect to the server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '11, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4456" class="comments-container"></div><div id="comment-tools-4456" class="comment-tools"></div><div class="clear"></div><div id="comment-4456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

