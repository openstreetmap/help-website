+++
type = "question"
title = "Trace outgoing system account"
description = '''Hi We have an application (IBM Notes) which communicates with several other systems (servers), but we don&#x27;t know which, although we do know that it uses its system account to communicate.  Is it possible in Wireshark to trace which servers the account communicates with? I&#x27;ve tried to look in Convers...'''
date = "2012-09-22T14:37:00Z"
lastmod = "2012-09-23T04:54:00Z"
weight = 14449
keywords = [ "user", "trace" ]
aliases = [ "/questions/14449" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Trace outgoing system account](/questions/14449/trace-outgoing-system-account)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14449-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi We have an application (IBM Notes) which communicates with several other systems (servers), but we don't know which, although we do know that it uses its system account to communicate.</p><p>Is it possible in Wireshark to trace which servers the account communicates with? I've tried to look in Conversations and Endpoint but with no luck.</p><p>Thanks</p><p>//hp</p></div><div id="question-tags" class="tags-container tags">user trace</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '12, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/95d9c7d1628b89ec478e1b8ba35246cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c0zzman&#39;s gravatar image" /><p>c0zzman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c0zzman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '12, 18:09</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-14449" class="comments-container"></div><div id="comment-tools-14449" class="comment-tools"></div><div class="clear"></div><div id="comment-14449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14450"></span>

<div id="answer-container-14450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14450-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If all you need is "which other server does it communicate with?" then the answer is yes. However, it will not let you see "which system or user account" it's using to setup the communication.</p><p>Also, in all likelihood, your Notes server will use encrypted communication. Therefore, you'll only know which servers are involved in the communication. But you won't be able to tell anything about the communication.</p><p>I don't understand the "Conversations/Endpoints...but no luck" comment. Was there nothing in the trace or do you mean you don't know how to read the chart?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '12, 16:47</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '12, 18:10</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-14450" class="comments-container"><span id="14453"></span><div id="comment-14453" class="comment"><div id="post-14453-score" class="comment-score"></div><div class="comment-text"><p>Hi Thanks for the answer. I know that the server communicates with several servers, but I want to know which servers it communicates with through this system account explicitly.</p><p>I was looking in the filter "Conversation", and there was a lot of traffic but I couldn't see the account.</p><p>But ok, then I know it isn't possible. Right?</p></div><div id="comment-14453-info" class="comment-info"><span class="comment-age">(22 Sep '12, 17:15)</span> c0zzman</div></div></div><div id="comment-tools-14450" class="comment-tools"></div><div class="clear"></div><div id="comment-14450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14461"></span>

<div id="answer-container-14461" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14461-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This problem might be a bit tricky to solve, but under the right circumstances you might be able to get what you want. Since the notes server may have other communications going in and out that do not relate to the notes application you'll have to determine which communications are related. This is usually done by determining the port numbers in use, which is</p><ol><li>simple if the communication is incoming to the server, because then the application port is ususally well known or easily determined by doing a netstat lookup with any parameters necessary to tell you the process ID/process name of the application using a port</li><li>complex if the server is opening connections to other servers (which it makes the notes server to be the "client" in this communication), and for that ephemeral ports will usually be used.</li></ol><p>So depending on if your notes server is the "client" of the communications to other servers you will have a hard time correlating the communications to the notes application. Wireshark can't help you with this, because it will only see communication from port to port, but not which application it was on the system. Maybe Microsoft NetMon can help you here, because it can do just that if it runs on the notes server (assuming your Notes server is running a windows OS). For linux systems, the <a href="https://github.com/HoneProject/Linux-Sensor">Hone Project</a> could help (but I haven't tried it myself yet).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '12, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14461" class="comments-container"><span id="14468"></span><div id="comment-14468" class="comment"><div id="post-14468-score" class="comment-score"></div><div class="comment-text"><p>The manual method (if netmon can't be used) is to use "netstat -aon" and you'll see the process ID as the last column. Then you need to use something like Process Monitor (ex sysinternals tool) to find the info for that PID. I'm not 100% sure if the owner is exposed, but you should be able to verify pretty quickly. Good luck.</p></div><div id="comment-14468-info" class="comment-info"><span class="comment-age">(23 Sep '12, 17:10)</span> hansangb</div></div></div><div id="comment-tools-14461" class="comment-tools"></div><div class="clear"></div><div id="comment-14461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

