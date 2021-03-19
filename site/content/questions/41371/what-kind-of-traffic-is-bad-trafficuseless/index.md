+++
type = "question"
title = "What kind of traffic is bad traffic(Useless)?"
description = '''If I wanted to minimize senseless or useless traffic on my network what kind of traffic would I look for and what are some good wireshark filters to find this traffic? Basically I would like to make the ethernet pipes clean for all the good traffic flowing through. I realize this seems pretty genera...'''
date = "2015-04-10T20:13:00Z"
lastmod = "2015-04-11T05:23:00Z"
weight = 41371
keywords = [ "quality", "traffic", "network", "filters", "wireshark" ]
aliases = [ "/questions/41371" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What kind of traffic is bad traffic(Useless)?](/questions/41371/what-kind-of-traffic-is-bad-trafficuseless)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41371-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I wanted to minimize senseless or useless traffic on my network what kind of traffic would I look for and what are some good wireshark filters to find this traffic? Basically I would like to make the ethernet pipes clean for all the good traffic flowing through. I realize this seems pretty general, as with varying types of networks types of traffic may be deemed good or bad. Just trying to get a general idea of what others look for. Any help or offered experience would be helpful, thanks</p></div><div id="question-tags" class="tags-container tags">quality traffic network filters wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '15, 20:13</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p>zer0day<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div></div><div id="comments-container-41371" class="comments-container"></div><div id="comment-tools-41371" class="comment-tools"></div><div class="clear"></div><div id="comment-41371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41377"></span>

<div id="answer-container-41377" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41377-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is probably no easy answer for this. One thing could be do get rid of all obsolete protocols, like AppleTalk, IPX, etc, but this is not what I'd call network performance tuning. It's just annoying to see those.</p><p>Other protocols could be STP, SSDP and others which you may not need, but again, they aren't really stealing bandwidth - plus, you need to know what their purpose is and if you need them or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '15, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41377" class="comments-container"></div><div id="comment-tools-41377" class="comment-tools"></div><div class="clear"></div><div id="comment-41377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41379"></span>

<div id="answer-container-41379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41379-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to make the ethernet pipes clean for all the good traffic flowing through.</p></blockquote><p>As @Jasper said: not easy to answer. Here is my attempt.</p><p>I don't believe that there is a general need to <strong>keep the pipe clean</strong>, unless you are experiencing network problems. However, as a "network problem" could be caused by a lot of things (overload, dns problems, duplicate addresses, physical problems, etc.), there is nothing one can do in advance to "keep the pipes clean".</p><p>Furthermore, I don't believe that any traffic is useless per se, as there is usually a reason why that traffic is on the line. Some kind of traffic might be "less usefull" in certain environments, and then you should try to figure out who (system, software) is generating that traffic and then decide if and how you are going to stop it.</p><p>So, to answer your question: There is no "good" traffic I can recommend to look for, as that's totally dependent on your own behavior and there is no "bad" traffic I can recommend to look for either, for the same reason.</p><p><strong>What you can do:</strong></p><p>Capture the traffic at a mirror port in front of your internet router and let it run for a few minutes while you are NOT surfing the web (close all browser instances). Then look at the Conversations (Statistics -&gt; Conversations) and try to identify TCP connections that look "strange" (whatever that means in your environment) or connections that consume bandwidth they should not. You can also try to find "unusual" UDP connections in the same view and/or other protocols.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '15, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '15, 05:39</p></div></div><div id="comments-container-41379" class="comments-container"></div><div id="comment-tools-41379" class="comment-tools"></div><div class="clear"></div><div id="comment-41379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

