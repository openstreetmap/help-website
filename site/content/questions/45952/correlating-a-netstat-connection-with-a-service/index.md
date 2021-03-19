+++
type = "question"
title = "Correlating a netstat connection with a service"
description = '''Hello all, I have some servers in my network talking to what looks like a Microsoft server in washington on port 443. I&#x27;v tracked down the PID in netstat however it looks like the PID belongs to almost a dozen services Wuauserv, winmgmt, themes, ShellHWDetection, SesionEnv, SENS, Schedule, Profsvc, ...'''
date = "2015-09-18T13:45:00Z"
lastmod = "2015-09-19T01:29:00Z"
weight = 45952
keywords = [ "netstat", "wireshark" ]
aliases = [ "/questions/45952" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Correlating a netstat connection with a service](/questions/45952/correlating-a-netstat-connection-with-a-service)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45952-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I have some servers in my network talking to what looks like a Microsoft server in washington on port 443.</p><p>I'v tracked down the PID in netstat however it looks like the PID belongs to almost a dozen services</p><p>Wuauserv, winmgmt, themes, ShellHWDetection, SesionEnv, SENS, Schedule, Profsvc, LanmanServer, CertPropSvc, BITS and AppInfo. I'm currently stuck at trying to figure out what service is specifically</p><p>Would you know of any applications that would help align an ip/port in netstat to a specific service?</p><p>Thanks for your help!</p></div><div id="question-tags" class="tags-container tags">netstat wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '15, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/c034c6b570e0946788de634bb2af43b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="forkbomb&#39;s gravatar image" /><p>forkbomb<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="forkbomb has no accepted answers">0%</span></p></div></div><div id="comments-container-45952" class="comments-container"></div><div id="comment-tools-45952" class="comment-tools"></div><div class="clear"></div><div id="comment-45952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45955"></span>

<div id="answer-container-45955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45955-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I know the build in commands</p><pre><code>tasklist /svc

tasklist /v

netstat -b</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '15, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-45955" class="comments-container"></div><div id="comment-tools-45955" class="comment-tools"></div><div class="clear"></div><div id="comment-45955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45959"></span>

<div id="answer-container-45959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45959-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>The easiest way to do this is with Sysinternal Process Explorer which you can freely download from Microsoft. Once you've started Process Explorer you'll get a tree diagram showing all of the processes. Look down the PID column to find the process that interests you.</p><p><img src="http://www.tribelabzero.com/procexplorer1.png" alt="alt text" /></p><p>Next select the TCP/IP tab and you'll see which TCP and UDP ports the process is using and the associated services.</p><p><img src="http://www.tribelabzero.com/procexplorer2.png" alt="alt text" /></p><p>As you can see, the Local Address shows the port number. I hope this helps.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '15, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 19 Sep '15, 01:30</p></div></div><div id="comments-container-45959" class="comments-container"><span id="46041"></span><div id="comment-46041" class="comment"><div id="post-46041-score" class="comment-score"></div><div class="comment-text"><p>THANK YOU!</p><p>I found the issue, device setup manager was reaching out to microsoft &amp; akamai servers. However, this is slightly concerning. Is this normal behavior for this service? It seems like it is 'Enables the detection , download and installation of device-related software' however just wanted to get a second opinion.</p></div><div id="comment-46041-info" class="comment-info"><span class="comment-age">(21 Sep '15, 17:08)</span> forkbomb</div></div></div><div id="comment-tools-45959" class="comment-tools"></div><div class="clear"></div><div id="comment-45959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

