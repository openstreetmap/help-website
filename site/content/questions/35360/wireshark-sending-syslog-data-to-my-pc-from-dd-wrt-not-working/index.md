+++
type = "question"
title = "Wireshark sending syslog data to my pc from dd-wrt, not working"
description = '''I was able to set this up on wall watcher using dd-wrt. setting the remote server to my ip. But in wireshark, the data comes in as: source is always dd-wrt and they protocol is Syslog I assume it is working correctly, because of that but, it is not parsing the data or showing anything useful etc. Wh...'''
date = "2014-08-10T06:02:00Z"
lastmod = "2014-08-10T06:13:00Z"
weight = 35360
keywords = [ "ddwrt", "dd-wrt", "syslog" ]
aliases = [ "/questions/35360" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark sending syslog data to my pc from dd-wrt, not working](/questions/35360/wireshark-sending-syslog-data-to-my-pc-from-dd-wrt-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35360-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was able to set this up on wall watcher using dd-wrt. setting the remote server to my ip. But in wireshark, the data comes in as: source is always dd-wrt and they protocol is Syslog I assume it is working correctly, because of that but, it is not parsing the data or showing anything useful etc.</p><p>What is going on? how can I fix</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ddwrt dd-wrt syslog</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '14, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/14e8ff606c6f737f476604034a184baa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="catcurio&#39;s gravatar image" /><p>catcurio<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="catcurio has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Aug '14, 06:03</p></div></div><div id="comments-container-35360" class="comments-container"></div><div id="comment-tools-35360" class="comment-tools"></div><div class="clear"></div><div id="comment-35360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35362"></span>

<div id="answer-container-35362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35362-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm sorry, but I don't understand what you are asking for:</p><p>So, here are some questions in return:</p><ul><li>What is 'wall watcher'? I only know whale watching ;-)</li><li>What kind of data do you send to your 'remote server'?</li><li>What kind of protocol are you using (you mentioned syslog)?</li></ul><blockquote><p>but, it is not parsing the data or showing anything useful etc.</p></blockquote><p>I guess that's your real question, right?</p><p>If so, my answer would be:</p><ul><li>maybe because the data is <strong>encrypted</strong></li><li>or because it's not syslog traffic, although the same port is being used.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '14, 06:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-35362" class="comments-container"><span id="35365"></span><div id="comment-35365" class="comment"><div id="post-35365-score" class="comment-score"></div><div class="comment-text"><p>HI Thanks for your response. Wallwatcher captures network traffic from routers.</p><p>I just realized that maybe wireshark works in a different way and this cannot be done. I think wireshark will capture data through my wireless adapter and not from router? I guess it cannot take the syslog info from the router? (I used this tutorial below to capture using wall watcher, can wireshark do same thing?) <a href="http://www.makeuseof.com/tag/paranoid-monitoring-networks-comings-goings-wallwatcher-ddwrt/">http://www.makeuseof.com/tag/paranoid-monitoring-networks-comings-goings-wallwatcher-ddwrt/</a></p><p>Thanks for your help.</p></div><div id="comment-35365-info" class="comment-info"><span class="comment-age">(10 Aug '14, 06:26)</span> catcurio</div></div><span id="35370"></span><div id="comment-35370" class="comment"><div id="post-35370-score" class="comment-score"></div><div class="comment-text"><p>O.K. <a href="http://www.wallwatcher1.com">Wallwatcher</a> looks like a syslog server that receives firewall log messages (iptables, pf, etc.) from several devices and then it does some statistics and graphing on that data.</p><p>So, you should be able to see and 'decode' the syslog data, but Wireshark won't be able to create the same usage graphs as Wallwatcher, as Wireshark does not care about the messages being transmitted via syslog, hence it does not analyse the syslog messages.</p><p>If you want to have that, you'll have to add some code to Wireshark. See the Lua integration of Wireshark: <a href="http://wiki.wireshark.org/Lua">http://wiki.wireshark.org/Lua</a></p></div><div id="comment-35370-info" class="comment-info"><span class="comment-age">(10 Aug '14, 06:56)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-35362" class="comment-tools"></div><div class="clear"></div><div id="comment-35362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

