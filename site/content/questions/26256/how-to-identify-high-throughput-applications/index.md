+++
type = "question"
title = "How to identify high throughput applications"
description = '''Yep, I’m a Newbie and I don’t even have a clue. System: Windows 7 64bit Wireshark is a fantastic program with very powerful features and I like it a lot; but, because of its extensive capabilities it does seem to have a steep learning curve and that’s OK I just need time to learn it.  However, I hav...'''
date = "2013-10-21T09:49:00Z"
lastmod = "2013-11-28T18:13:00Z"
weight = 26256
keywords = [ "application", "bandwidth" ]
aliases = [ "/questions/26256" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to identify high throughput applications](/questions/26256/how-to-identify-high-throughput-applications)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26256-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Yep, I’m a Newbie and I don’t even have a clue.</p><p>System: Windows 7 64bit</p><p>Wireshark is a fantastic program with very powerful features and I like it a lot; but, because of its extensive capabilities it does seem to have a steep learning curve and that’s OK I just need time to learn it.<br />
</p><p>However, I have a pressing issue with some unknown application that is consuming huge quantities of bandwidth (4GB, 2 days, 40% of monthly allotment). I have identified and blocked a range of offending IPs but other good programs also use some IPs out of that range. What I wish to do is identify the offending program and modify or delete it from the system. The problem is identifying that program.</p><p>QUESTION: How do I identify a host application that causes high bandwidth traffic?</p></div><div id="question-tags" class="tags-container tags">application bandwidth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '13, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/febf61b1019bc7e5c7e234c6283a491c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bluestar&#39;s gravatar image" /><p>Bluestar<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bluestar has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-26256" class="comments-container"><span id="26257"></span><div id="comment-26257" class="comment"><div id="post-26257-score" class="comment-score"></div><div class="comment-text"><p>Is that <strong>incoming</strong> traffic to your web server or <strong>outgoing</strong> traffic form your clients?</p></div><div id="comment-26257-info" class="comment-info"><span class="comment-age">(21 Oct '13, 11:06)</span> Kurt Knochner ♦</div></div><span id="26293"></span><div id="comment-26293" class="comment"><div id="post-26293-score" class="comment-score"></div><div class="comment-text"><p>you wouldn't not be able to identify the offending program using wireshark. on a windows pc executing netstat -a -b as admin will give you a list of exes along with the ports they are using.</p></div><div id="comment-26293-info" class="comment-info"><span class="comment-age">(22 Oct '13, 14:04)</span> net_tech</div></div><span id="27536"></span><div id="comment-27536" class="comment"><div id="post-27536-score" class="comment-score"></div><div class="comment-text"><p>I may get kicked out from this forum for promoting Microsoft Netmon, but netmon 3.4 will show you what ports are being utilized by what executables.</p><p><a href="http://blogs.technet.com/b/netmon/">http://blogs.technet.com/b/netmon/</a></p></div><div id="comment-27536-info" class="comment-info"><span class="comment-age">(28 Nov '13, 08:11)</span> net_tech</div></div><span id="27538"></span><div id="comment-27538" class="comment"><div id="post-27538-score" class="comment-score"></div><div class="comment-text"><p>@net_tech, no problem with mentioning Net Mon. Note it has now been replaced by <a href="http://www.microsoft.com/en-us/download/details.aspx?id=40308">Message Analyzer</a>.</p></div><div id="comment-27538-info" class="comment-info"><span class="comment-age">(28 Nov '13, 09:10)</span> grahamb ♦</div></div></div><div id="comment-tools-26256" class="comment-tools"></div><div class="clear"></div><div id="comment-26256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27543"></span>

<div id="answer-container-27543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27543-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use process explorer by MS, add network columns sends and receives, sort by sends or receives to see which process is using the most bandwidth.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '13, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/b7cb3cdffa3d69b446038a1f44db1423?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tushar&#39;s gravatar image" /><p>tushar<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tushar has no accepted answers">0%</span></p></div></div><div id="comments-container-27543" class="comments-container"></div><div id="comment-tools-27543" class="comment-tools"></div><div class="clear"></div><div id="comment-27543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27544"></span>

<div id="answer-container-27544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27544-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>get a trace file -&gt; open it with Wireshark -&gt; Statistics -&gt; check IPv4 tab -&gt; identify the top talker -&gt; go to other upper layer protocol tab, like tcp, udp,etc. to identify a potential top talker</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '13, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p>SteveZhou<br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-27544" class="comments-container"></div><div id="comment-tools-27544" class="comment-tools"></div><div class="clear"></div><div id="comment-27544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

