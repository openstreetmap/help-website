+++
type = "question"
title = "Slowness Issue"
description = '''Hello, Lately our users are complaining of our ERP system, saying it&#x27;s super slow and they can&#x27;t get work done. Our previous application developer says that it&#x27;s most likely the network as he doesn&#x27;t see anything unusual on the sql server. Our networking team thinks it&#x27;s the application itself. I&#x27;m ...'''
date = "2016-05-23T12:37:00Z"
lastmod = "2016-05-25T12:16:00Z"
weight = 52838
keywords = [ "applicaitondelay", "network", "slowness" ]
aliases = [ "/questions/52838" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slowness Issue](/questions/52838/slowness-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52838-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Lately our users are complaining of our ERP system, saying it's super slow and they can't get work done. Our previous application developer says that it's most likely the network as he doesn't see anything unusual on the sql server. Our networking team thinks it's the application itself. I'm trying to build a case with hard facts to determine where this slowness is coming from (or if it's a case of one user complains, so they all complain). I ran a wireshark capture, and found that there are multiple times where there's a [RST, ACK] Connection reset warning. I'm trying to determine if this is anything of significance on my journey to finding this "slowness" issue, but have no wireshark experience. Do you know what a connection reset (RST) is and why it's happening? I haven't found much using google.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">applicaitondelay network slowness</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '16, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/89d0fa24f0d43ef501b18f52a0f905ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slownessissue&#39;s gravatar image" /><p>slownessissue<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slownessissue has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 May '16, 11:33</p></div></div><div id="comments-container-52838" class="comments-container"><span id="52840"></span><div id="comment-52840" class="comment"><div id="post-52840-score" class="comment-score"></div><div class="comment-text"><p>It is much more a TCP question than a Wireshark question.</p><p>An RST flag in TCP normally indicates an emergency dropping of that TCP session. In addition to the session participants (the client and the server), the source of such packet may also be some security equipment (firewall) between them, e.g. due to recognition of a signature of some kind of attack in the session, which may happen even if the session is actually harmless. So the first thing to do would be to capture at both the client PC and the server to see whether those RST packets really come from one of them (so can be seen at both ends) or from some box in between them. Next, I would watch how much time had elapsed since the last packet of that session which went in the opposite direction before the RST packet was sent (as the application may have reset the session as it gave up waiting for some response from the other side).</p></div><div id="comment-52840-info" class="comment-info"><span class="comment-age">(23 May '16, 13:50)</span> sindy</div></div><span id="52849"></span><div id="comment-52849" class="comment"><div id="post-52849-score" class="comment-score"></div><div class="comment-text"><p>Could you share us a trace on public accessible place, like cloudshark or Dropbox... If you worry about privacy, use TraceWrangler (<a href="https://www.tracewrangler.com">https://www.tracewrangler.com</a>) to randomize all IP addresses and remove the TCP payload (verify it looks good before uploading, "good" meaning IPs are different and the packets have no TCP payload anymore). Please make sure that you include the TCP handshake.</p></div><div id="comment-52849-info" class="comment-info"><span class="comment-age">(23 May '16, 23:45)</span> Christian_R</div></div><span id="52865"></span><div id="comment-52865" class="comment"><div id="post-52865-score" class="comment-score"></div><div class="comment-text"><p>Christian_R,</p><p>Here are the captures. The IP's that you'll be wanting to look at are 192.168.1.131 and 192.168.1.130 (they're our SQL/app servers).</p><p><a href="https://www.dropbox.com/s/hzysfvg2ozgxdtu/packet%20capture%20nsweetland.pcapng?dl=0">https://www.dropbox.com/s/hzysfvg2ozgxdtu/packet%20capture%20nsweetland.pcapng?dl=0</a></p><p><a href="https://www.dropbox.com/s/8lp8emt90okdqfw/nick%20capture%202.pcapng?dl=0">https://www.dropbox.com/s/8lp8emt90okdqfw/nick%20capture%202.pcapng?dl=0</a></p><p>Thanks.</p></div><div id="comment-52865-info" class="comment-info"><span class="comment-age">(24 May '16, 08:11)</span> slownessissue</div></div><span id="52866"></span><div id="comment-52866" class="comment"><div id="post-52866-score" class="comment-score"></div><div class="comment-text"><p>On which port is the SQLite server listening or do you use http?</p></div><div id="comment-52866-info" class="comment-info"><span class="comment-age">(24 May '16, 10:35)</span> Christian_R</div></div><span id="52867"></span><div id="comment-52867" class="comment"><div id="post-52867-score" class="comment-score"></div><div class="comment-text"><p>By using the steps here in method 1 (<a href="https://sqlandme.com/2013/05/01/sql-server-finding-tcp-port-number-sql-instance-is-listening-on/)">https://sqlandme.com/2013/05/01/sql-server-finding-tcp-port-number-sql-instance-is-listening-on/)</a> I'm showing port 1433 as a statically configured listening port.</p></div><div id="comment-52867-info" class="comment-info"><span class="comment-age">(24 May '16, 11:22)</span> slownessissue</div></div><span id="52871"></span><div id="comment-52871" class="comment not_top_scorer"><div id="post-52871-score" class="comment-score"></div><div class="comment-text"><p>Can't see that port in the trace.</p></div><div id="comment-52871-info" class="comment-info"><span class="comment-age">(24 May '16, 12:32)</span> Christian_R</div></div><span id="52873"></span><div id="comment-52873" class="comment not_top_scorer"><div id="post-52873-score" class="comment-score"></div><div class="comment-text"><p>It's possible it may run over http still somehow, but I don't know enough about the application to determine this. After running a packet trace of someone logging into the desktop based application, I'm seeing a bunch of http/1.1 responses though.</p></div><div id="comment-52873-info" class="comment-info"><span class="comment-age">(24 May '16, 13:26)</span> slownessissue</div></div><span id="52874"></span><div id="comment-52874" class="comment not_top_scorer"><div id="post-52874-score" class="comment-score"></div><div class="comment-text"><p>I think the network looks very calm. Some http responses took long time.</p></div><div id="comment-52874-info" class="comment-info"><span class="comment-age">(24 May '16, 13:48)</span> Christian_R</div></div><span id="52919"></span><div id="comment-52919" class="comment not_top_scorer"><div id="post-52919-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the feedback. Can you tell me which packets you saw that took a long time? I will note this down.</p><p>Thanks</p></div><div id="comment-52919-info" class="comment-info"><span class="comment-age">(25 May '16, 08:31)</span> slownessissue</div></div></div><div id="comment-tools-52838" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-52838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52933"></span>

<div id="answer-container-52933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52933-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should set the filter to:</p><pre><code>tcp.port==80 and (ip.addr==192.168.1.131 or ip.addr==192.168.1.130)</code></pre><p>Then choose in the Edit -&gt; Preferences dialog window under protocols the TCP protocol. There you should enable TCP reasembly in this case.</p><p>Then choose in the same preferences dialog "User Interface" -&gt; columns In that window you push the "Add" button and choose as Field type "Custom" As "Field name" you should use <code>http.time</code> After that you close Preferences dialog. Now you have a new column with http Response time and you can sort the trace by that column.</p><p>After that you can do a "Follow TCp Stream" at the frames with high http.time.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/25-05-_2016_20-56-42.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '16, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div></div><div id="comments-container-52933" class="comments-container"></div><div id="comment-tools-52933" class="comment-tools"></div><div class="clear"></div><div id="comment-52933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

