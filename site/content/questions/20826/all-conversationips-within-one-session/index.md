+++
type = "question"
title = "all conversation(ip&#x27;s) within one session"
description = '''how can we find out all conversation pertaining to one session,say for e.g.during a communication betweeen a-b,in between the session a also commmunicates with C lets say for authenticatioin,how could we find out this with just reading wireshark capture.Kishan'''
date = "2013-04-27T23:01:00Z"
lastmod = "2013-04-28T03:39:00Z"
weight = 20826
keywords = [ "iteoffe" ]
aliases = [ "/questions/20826" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [all conversation(ip's) within one session](/questions/20826/all-conversationips-within-one-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20826-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can we find out all conversation pertaining to one session,say for e.g.during a communication betweeen a-b,in between the session a also commmunicates with C lets say for authenticatioin,how could we find out this with just reading wireshark capture.Kishan</p></div><div id="question-tags" class="tags-container tags">iteoffe</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '13, 23:01</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-20826" class="comments-container"></div><div id="comment-tools-20826" class="comment-tools"></div><div class="clear"></div><div id="comment-20826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20829"></span>

<div id="answer-container-20829" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20829-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use the items in the statistics menu of Wireshark, e.g the conversation statistics which will give you a list of conversation between nodes. If you're interested in a timeline of who is talking to who you might also find the Flow Graph useful, which you can also find in the Statistics menu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '13, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20829" class="comments-container"><span id="20835"></span><div id="comment-20835" class="comment"><div id="post-20835-score" class="comment-score"></div><div class="comment-text"><p>Currently i am doing it the same way but i thought that there could be a more efficient way.</p></div><div id="comment-20835-info" class="comment-info"><span class="comment-age">(29 Apr '13, 02:14)</span> kishan pandey</div></div></div><div id="comment-tools-20829" class="comment-tools"></div><div class="clear"></div><div id="comment-20829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20830"></span>

<div id="answer-container-20830" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20830-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>all conversation pertaining to one session,</p></blockquote><p>unless you define a 'session', it's hard to tell what look for.</p><blockquote><p>during a communication betweeen a-b,in between the session a also commmunicates with C lets say for authenticatioin,how could we find out this with just reading wireshark capture</p></blockquote><p>As there could be several systems involved (a,b,c) and several protocols (authentication, etc.) the only way to match those 'related' connections to one 'session' is to understand the protocols and systems/infrastructure (auth server, etc.) involved. Without that protocol/infrastructure knowledge, you will be unable to tell if a connection from a -&gt; c is somehow related to your 'session' or just triggered by another action/application at the same time.</p><p>To sum it up: Wireshark is a tool that helps you to monitor the network communication. It has <strong>some</strong> statistics and <strong>some</strong> other modules that can help to analyze a problem, but the rest is the job of an analyst, meaning you need to have good knowledge of networking protocols, you need to know your network infrastructure very well and you need to know your applications very well.<br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '13, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Apr '13, 03:48</p></div></div><div id="comments-container-20830" class="comments-container"></div><div id="comment-tools-20830" class="comment-tools"></div><div class="clear"></div><div id="comment-20830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

