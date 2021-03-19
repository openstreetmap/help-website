+++
type = "question"
title = "Getting Router IPs with wireshark"
description = '''Okay, so an inconsiderate guy on a website that is prejudice toward me (Dislikes me for no reason) somehow got my ip using wireshark and DDoSed my router for around 5 to 10 minutes. I&#x27;ve only known 1 other person to know how to do this but he&#x27;s doesn&#x27;t want to tell me either, he also has proof that ...'''
date = "2013-07-13T13:44:00Z"
lastmod = "2013-07-13T14:38:00Z"
weight = 22934
keywords = [ "ip", "mac", "wireshark" ]
aliases = [ "/questions/22934" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting Router IPs with wireshark](/questions/22934/getting-router-ips-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22934-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Okay, so an inconsiderate guy on a website that is prejudice toward me (Dislikes me for no reason) somehow got my ip using wireshark and DDoSed my router for around 5 to 10 minutes. I've only known 1 other person to know how to do this but he's doesn't want to tell me either, he also has proof that he's done it. I'd like to know, how do you perform something like this? and the website was a virtual game so it had a client in a chat system and everything. I'm not going to abuse this technique I just want to know uncase it ever comes handy.</p></div><div id="question-tags" class="tags-container tags">ip mac wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '13, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/0e5dca265a5149344a5e0d9eaf6df0cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Crypttt&#39;s gravatar image" /><p>Crypttt<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Crypttt has no accepted answers">0%</span></p></div></div><div id="comments-container-22934" class="comments-container"></div><div id="comment-tools-22934" class="comment-tools"></div><div class="clear"></div><div id="comment-22934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22935"></span>

<div id="answer-container-22935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22935-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To find your IP address the guy attacking it needs to see a connection to it, or get access to logs that show your IP. For example if you're posting something on a forum, that forum will usually record the IP you're connecting with in it's databases. If the "bad guy" can gain access to the DB (or maybe he even runs it, which would be the easiest way for him) he can find your IP associated with a recent post you did. Recent, because as a normal user your public IP will be changed every once in a while, coming from a DHCP pool of your provider. If you've got a static address, any post will do.</p><p>The other way could be that if he interacts with you in any way directly, through chats, a game, whatever, he can looku p his own connection table ("netstat -an" on a command line) and find your IP in it.</p><p>DoSing is quite easy, there's tons of tools for that. DDoSing isn't that easy because your attack needs to be a little more sophisticated or may even require access to a botnet. A known example for a DoS tool is the Low Orbit Ion Cannon (LOIC), (at least) formerly used by anonymous.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '13, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22935" class="comments-container"></div><div id="comment-tools-22935" class="comment-tools"></div><div class="clear"></div><div id="comment-22935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

