+++
type = "question"
title = "capture the logs for a particular windows service installed on the server"
description = '''Hi Team, We have installed wireshark on our one of the windows server, we need to capture the logs for a particular windows service installed on the server say &quot;MyService&quot;. We need to capture all activity log related to this windows service. Can we capture as explain above?.'''
date = "2016-02-09T02:05:00Z"
lastmod = "2016-02-09T02:38:00Z"
weight = 49990
keywords = [ "windows", "services" ]
aliases = [ "/questions/49990" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture the logs for a particular windows service installed on the server](/questions/49990/capture-the-logs-for-a-particular-windows-service-installed-on-the-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49990-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team, We have installed wireshark on our one of the windows server, we need to capture the logs for a particular windows service installed on the server say "MyService". We need to capture all activity log related to this windows service. Can we capture as explain above?.</p></div><div id="question-tags" class="tags-container tags">windows services</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '16, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/8803c4c0fa258c5baadac672457d4585?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SHAMBHU&#39;s gravatar image" /><p>SHAMBHU<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SHAMBHU has no accepted answers">0%</span></p></div></div><div id="comments-container-49990" class="comments-container"></div><div id="comment-tools-49990" class="comment-tools"></div><div class="clear"></div><div id="comment-49990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49991"></span>

<div id="answer-container-49991" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49991-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not directly. Wireshark captures traffic on one or more network interfaces, and can use capture filters to limit the traffic captured, but there is no traffic filter for a service or process ID.</p><p>If the service is (or can be configured to be) the only user of a particular port or protocol or network address or network interface, then capture filters can be used to isolate the traffic for the service.</p><p>Microsoft <a href="https://technet.microsoft.com/en-us/library/jj649776.aspx">Message Analyser</a> or Sysinternals <a href="https://technet.microsoft.com/en-us/sysinternals/processmonitor">Process Monitor</a> may allow you to capture the data you seek in a different format, some MA captures can be exported to Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49991" class="comments-container"><span id="49994"></span><div id="comment-49994" class="comment"><div id="post-49994-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb,</p><p>Thanks for your quick reply. But i observed when a windows service runs its entry goes to task manager under services tab with PID (Process ID) and as we have a wireshark filter tcp.port==1234 in this way can we not have the log for specific service only??</p></div><div id="comment-49994-info" class="comment-info"><span class="comment-age">(09 Feb '16, 02:52)</span> SHAMBHU</div></div><span id="49996"></span><div id="comment-49996" class="comment"><div id="post-49996-score" class="comment-score"></div><div class="comment-text"><p>The PID and tcp.port (or udp.port, or any other protocol port) are two distinct things and there is no static mapping between the two. If you know at which port of which protocol the service listens, you can capture only packets to/from that port, but you cannot determine the port number from the PID. Maybe some Windows utility does show you which process is bound to which socket.</p></div><div id="comment-49996-info" class="comment-info"><span class="comment-age">(09 Feb '16, 03:03)</span> sindy</div></div><span id="49998"></span><div id="comment-49998" class="comment"><div id="post-49998-score" class="comment-score"></div><div class="comment-text"><p>Hi sindy,</p><p>Thanks for correcting me. Means any how we can not retrieve log related to particular windows service using Wireshark. If not can you please tell me any other tool which can extract the log related to specific windows task on a given server where wireshark is installed.</p><p>Thanks for your support.</p></div><div id="comment-49998-info" class="comment-info"><span class="comment-age">(09 Feb '16, 03:18)</span> SHAMBHU</div></div><span id="49999"></span><div id="comment-49999" class="comment"><div id="post-49999-score" class="comment-score"></div><div class="comment-text"><p>As I said, Wireshark has no facilities for restricting captures to a particular PID, the other tools I mentioned do.</p></div><div id="comment-49999-info" class="comment-info"><span class="comment-age">(09 Feb '16, 03:19)</span> grahamb ♦</div></div><span id="50001"></span><div id="comment-50001" class="comment"><div id="post-50001-score" class="comment-score"></div><div class="comment-text"><p>@SHAMBHU, I am still a little bit confused by your use of the word "log". Do you want to</p><ul><li><p>capture packets sent and received over the network by that service? If so, use one of the tools suggested by @grahamb to <em>capture</em> the traffic, and you may then <em>analyse</em> the captures using Wireshark.</p></li><li><p>get the <em>application logs</em> (the text information generated by the service, commenting about its operation and eventual trouble encountered)? If so, Wireshark is not the tool for the task and you have to use Windows' tools to show only the log messages coming from that service instead of showing messages from all.</p></li></ul></div><div id="comment-50001-info" class="comment-info"><span class="comment-age">(09 Feb '16, 03:25)</span> sindy</div></div><span id="50002"></span><div id="comment-50002" class="comment not_top_scorer"><div id="post-50002-score" class="comment-score"></div><div class="comment-text"><p>Hi sindy/Grahamb,</p><p>I think m getting yours point, and @sindy: Log means i wanted to say is "Packets sent and received over the network by a particular service here in this case my window service name is say MYService" as u mention in first statement. I think then i have to go for a window utility definitely as per your suggestion.</p><p>Can u tell me the freely available utility to get my result? or any other idea by which i can capture the trace related to specific windows service on a particular server.</p></div><div id="comment-50002-info" class="comment-info"><span class="comment-age">(09 Feb '16, 03:34)</span> SHAMBHU</div></div><span id="50003"></span><div id="comment-50003" class="comment not_top_scorer"><div id="post-50003-score" class="comment-score"></div><div class="comment-text"><p>@SHAMBHU, your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>I gave a couple of links in my answer.</p></div><div id="comment-50003-info" class="comment-info"><span class="comment-age">(09 Feb '16, 03:36)</span> grahamb ♦</div></div><span id="50006"></span><div id="comment-50006" class="comment not_top_scorer"><div id="post-50006-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb,</p><p>Yes thanks for your support. Will proceed as per your suggestion.</p><p>Thanks</p></div><div id="comment-50006-info" class="comment-info"><span class="comment-age">(09 Feb '16, 04:07)</span> SHAMBHU</div></div></div><div id="comment-tools-49991" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-49991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

