+++
type = "question"
title = "store results locally and replicate to a server"
description = '''Hi,  DISCLAIMER - I&#x27;m not a developer, I&#x27;m an idea&#x27;s guy :-). I currently have a working system that i want to enhance, in order to do so i would employ the services of a freelance developer. My question is to ask for advice so i can then ask / tell a developer what i need to do. If you can help or ...'''
date = "2016-12-27T03:04:00Z"
lastmod = "2016-12-27T06:56:00Z"
weight = 58354
keywords = [ "tshark", "mysql" ]
aliases = [ "/questions/58354" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [store results locally and replicate to a server](/questions/58354/store-results-locally-and-replicate-to-a-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58354-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><hr /><p>DISCLAIMER - I'm not a developer, I'm an idea's guy :-). I currently have a working system that i want to enhance, in order to do so i would employ the services of a freelance developer.</p><p>My question is to ask for advice so i can then ask / tell a developer what i need to do. If you can help or or interested in the project please let me know...</p><hr /><p>I am currently using Tshark as a simple scanning tool to record Wireless MAC's, RSSI and date / time stamp them. This is all done via a RPI.</p><p>At the moment the data is captured and sent to my server @ AWS via a Json script, this is done in real time as soon as scan results are received... In a busy environment it generates quite a bit of traffic :-)</p><p>I have an issue in there when i loose internet connectivity i also loose all my scan results. Although this isn't a massive problem i would like to resolve it. Originally i was thinking of capturing the scan results, send them to a local running instance of SQL and then replicate the data from SQL to my server... somehow. Then if i loose internet connectivity the local DB will continue to store the data and when connectivity is back up and running the DB will send the everything it has cached to my server.</p><p>However reading several threads alot of people are saying that its not a good idea to store data in SQL... not sure why. It also doesn't seem that easy to get Tshark to save its data to SQL without scripting or some people have said to pipe it directly.</p><p>What i would like to ask the community for is idea's on the best way to achieve my goal of a locally store copy of the data that can replicate to a main server but also when my RPI is online it all does it in as close to real time as possible as per the current setup.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">tshark mysql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '16, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/73514d77c921e9443a1a3d4f425c2301?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pigsfoot&#39;s gravatar image" /><p>Pigsfoot<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pigsfoot has no accepted answers">0%</span></p></div></div><div id="comments-container-58354" class="comments-container"></div><div id="comment-tools-58354" class="comment-tools"></div><div class="clear"></div><div id="comment-58354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58362"></span>

<div id="answer-container-58362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58362-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're looking to replicate files across servers, then you might want to have a look at something like <a href="https://linux.die.net/man/1/rsync">rysnc</a> or <a href="https://www.cis.upenn.edu/~bcpierce/unison/">unison</a> or a number of other file replication services.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '16, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-58362" class="comments-container"><span id="58364"></span><div id="comment-58364" class="comment"><div id="post-58364-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the pointer @cmaynard, first thing i need to work out though is how do i store the data and if a DB is the way forward how do i get it in there.</p></div><div id="comment-58364-info" class="comment-info"><span class="comment-age">(27 Dec '16, 07:14)</span> Pigsfoot</div></div></div><div id="comment-tools-58362" class="comment-tools"></div><div class="clear"></div><div id="comment-58362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

