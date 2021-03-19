+++
type = "question"
title = "analysing packets in a cap file"
description = '''Im quite new to wireshark, in fact ive hardly used it.  Basically, we have been set the task to analyse sniffer data in a cap file we have been given. We are also expected to turn all the network packets back into files, web pages emails etc Does anyone have any idea how i can do this? as im complet...'''
date = "2012-05-11T09:59:00Z"
lastmod = "2012-05-11T10:33:00Z"
weight = 10945
keywords = [ "packets", "wireshark" ]
aliases = [ "/questions/10945" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [analysing packets in a cap file](/questions/10945/analysing-packets-in-a-cap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10945-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im quite new to wireshark, in fact ive hardly used it.</p><p>Basically, we have been set the task to analyse sniffer data in a cap file we have been given. We are also expected to turn all the network packets back into files, web pages emails etc</p><p>Does anyone have any idea how i can do this? as im completely confused. I would really appreciate the help</p></div><div id="question-tags" class="tags-container tags">packets wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '12, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/bd5dff6d184c46b781d2e30ac5fda197?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="algyptalian&#39;s gravatar image" /><p>algyptalian<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="algyptalian has no accepted answers">0%</span></p></div></div><div id="comments-container-10945" class="comments-container"></div><div id="comment-tools-10945" class="comment-tools"></div><div class="clear"></div><div id="comment-10945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10948"></span>

<div id="answer-container-10948" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10948-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>well, some of that can be done with this options:</p><ul><li>File -&gt; Export -&gt; Objects -&gt; HTTP</li><li>by applying the Display filter "http.request". Then right-click on one entry and choose "Follow TCP Stream".</li><li>by applying the display filter "smtp and tcp.flags eq 0x02". Then again: right-click -&gt; Follow TCP Stream</li></ul><p><strong>HOWEVER</strong>, what you get is the raw communication for that protocol on the network. Maybe not what your client expected to get, ALTHOUGH you can re-construct downloads and e-mails with that.</p><p>There are other tools as well, e.g. <strong>tcpflow, tcptrace</strong>. Please check the wiki:</p><blockquote><p><strong><code>http://wiki.wireshark.org/Tools</code></strong><br />
</p></blockquote><p>Wireshark was mainly developed as a network troubleshooting tool, whereas your request sounds like spying on users or finding evidence for whatever ;-)</p><p>In that case, you better use a tool suited for that purpose, e.g. <strong>NetworkMiner</strong> (free version available)</p><blockquote><p><strong><code>http://www.netresec.com/?page=NetworkMiner</code></strong><br />
</p></blockquote><p>For <strong>OpenSource</strong> lovers:</p><blockquote><p><strong><code>http://www.xplico.org/</code></strong><br />
<strong><code>http://www.xplico.org/screenshot</code></strong><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '12, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 May '12, 12:55</p></div></div><div id="comments-container-10948" class="comments-container"><span id="10950"></span><div id="comment-10950" class="comment"><div id="post-10950-score" class="comment-score"></div><div class="comment-text"><p>Thnaks a lot for the reply. I tried your suggestion in wireshark. I got a whole lot of files, some jpeg, some png, and other css files, but theres supposed to be an excel document which contains some information, however i didnt really manage to find that. How would i analyse the packet in network miner? as it wasnt really clear to me.</p></div><div id="comment-10950-info" class="comment-info"><span class="comment-age">(11 May '12, 15:50)</span> algyptalian</div></div><span id="10951"></span><div id="comment-10951" class="comment"><div id="post-10951-score" class="comment-score"></div><div class="comment-text"><p>ok so ive been messing around with network miner, specifically the keyword search facility. Ive pulled up words like "confidential" and a few interesting things came up. What i want to know is, is it possible to download all frame content, or perhaps, all things sent by a particular source/destination host? I mean, the posibilities of what i could find seem to be endless, but i could be wrong (its because i am very new to this software...)</p></div><div id="comment-10951-info" class="comment-info"><span class="comment-age">(11 May '12, 16:24)</span> algyptalian</div></div><span id="10957"></span><div id="comment-10957" class="comment"><div id="post-10957-score" class="comment-score"></div><div class="comment-text"><p>O.K. could you please specify in more detail what you are looking for?</p><ul><li>Is it an excel in a HTTP up-/download OR an e-mail (or both)?</li><li>Do you know the name of the Excel sheet?</li><li>Do you know some content of the execel sheet (confidential?)?</li><li>Is there a certain IP address you can concentrate your investigation on?</li></ul></div><div id="comment-10957-info" class="comment-info"><span class="comment-age">(12 May '12, 01:20)</span> Kurt Knochner ♦</div></div><span id="10959"></span><div id="comment-10959" class="comment"><div id="post-10959-score" class="comment-score"></div><div class="comment-text"><p>ive been doing further looking around, conversations are taking place on myspace, and also on <a href="http://aussiemail.com.au">aussiemail.com.au</a>...but this may not be all there is...the conversations/ transactions are taking place between 2 hosts, 192.168.143.13 &amp; 161.74.26.25...when i use the keyword search in networkminer, i saw parts of messages, some about confidential information, &amp; attachments being sent. This is going on between the 2 above ip addresses mentioned. so is there some sort of way i can view all the messages that they have sent to and from eachother, as well as attachments they may have sent?</p></div><div id="comment-10959-info" class="comment-info"><span class="comment-age">(12 May '12, 02:16)</span> algyptalian</div></div></div><div id="comment-tools-10948" class="comment-tools"></div><div class="clear"></div><div id="comment-10948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

