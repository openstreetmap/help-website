+++
type = "question"
title = "Question about Passive FTP"
description = '''I am aware that firewall will block the incoming data connection(the syn packet with source port 20) in case of Active FTP and therefore enterprises prefers to go with Passive where control and data will be initiated by client. My question is  Why in passive FTP the client opens data connection to a...'''
date = "2013-07-02T19:46:00Z"
lastmod = "2013-07-03T00:38:00Z"
weight = 22585
keywords = [ "ftp" ]
aliases = [ "/questions/22585" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Question about Passive FTP](/questions/22585/question-about-passive-ftp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22585-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am aware that firewall will block the incoming data connection(the syn packet with source port 20) in case of Active FTP and therefore enterprises prefers to go with Passive where control and data will be initiated by client.</p><p>My question is</p><p>Why in passive FTP the client opens data connection to a random port specified by the server rather than to port 20? If ,by any chance someone designs passive ftp server which will send port 20 (in PASV) for data connection will the firewall block that incoming syn-ack(Data connection)from server?</p><p>Thanks..</p></div><div id="question-tags" class="tags-container tags">ftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '13, 11:04</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22585" class="comments-container"></div><div id="comment-tools-22585" class="comment-tools"></div><div class="clear"></div><div id="comment-22585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22587"></span>

<div id="answer-container-22587" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22587-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Any recent firewall will read/inspect the content of the FTP control connection (Port 21 from client to server) and use the information in the PORT command to dynamically allow the data connection, no matter what port is used nor who opens the data connection (active or passive FTP). In the Linux Netfilter framework this mechanism is called a conntrack helper (connection tracking). Other vendors have their own names for it.</p><p>Passive FTP is only 'better', if you have an older firewall, as you can say:</p><ul><li>ALLOW client:* -&gt; server:21 (redundant)</li><li>ALLOW client:* -&gt; server:*</li></ul><p>which allows the dynamically chosen port of the FTP server for the data connection without need to inspect the control connection. However, that's not following the '<a href="http://en.wikipedia.org/wiki/Principle_of_least_privilege">principle of least privilege</a>' and thus should be avoided.</p><blockquote><p>Why in passive FTP the client opens data connection to a random port specified by the server rather than to port 20?</p></blockquote><p>That's how the FTP protocol is designed. If you want to know why, please contact the authors of the RFC (although J. Postel already died. Don't know about J. Reynolds).</p><blockquote><p>If ,by any chance someone designs passive ftp server which will send port 20 (in PASV) for data connection will the firewall block that incoming syn-ack(Data connection)from server?</p></blockquote><p>If that was the case, you will have to open your firewall for only two ports.</p><ul><li>ALLOW: client:* -&gt; server:21 (control connection)</li><li>ALLOW: client:* -&gt; server:20 (data connection)</li></ul><p>But as I said, with any recent firewall you only need this rule</p><ul><li>ALLOW: client:* -&gt; server:21 (control connection)</li></ul><p>The data connection will be allowed by the conntrack helper, no matter if ACTIVE or PASSIVE FTP is used.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '13, 08:41</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-22587" class="comments-container"><span id="22614"></span><div id="comment-22614" class="comment"><div id="post-22614-score" class="comment-score">1</div><div class="comment-text"><p>The following links may also be helpful:</p><ul><li>RFC 959, <a href="http://tools.ietf.org/html/rfc959">FILE TRANSFER PROTOCOL (FTP)</a></li><li><a href="http://www.inacon.de/ph/data/FTP/index.php">FTP Protocol Help</a>, provided by Inacon</li><li>Slacksite article: <a href="http://slacksite.com/other/ftp.html">Active FTP vs. Passive FTP, a Definitive Explanation</a></li></ul></div><div id="comment-22614-info" class="comment-info"><span class="comment-age">(03 Jul '13, 08:40)</span> cmaynard ♦♦</div></div><span id="23008"></span><div id="comment-23008" class="comment"><div id="post-23008-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-23008-info" class="comment-info"><span class="comment-age">(16 Jul '13, 05:51)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22587" class="comment-tools"></div><div class="clear"></div><div id="comment-22587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

