+++
type = "question"
title = "Measure login latency"
description = '''We have a issue by latency when logging in to our network . It takes between 5-10 minutes from the computer is startet until I am logged in.  I have done a wireshark capture from start of the computer until the login process is finished. How is the best way to analyze the traffic to determine the la...'''
date = "2011-03-01T01:06:00Z"
lastmod = "2011-03-01T14:13:00Z"
weight = 2593
keywords = [ "latency", "login", "measure" ]
aliases = [ "/questions/2593" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Measure login latency](/questions/2593/measure-login-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2593-score" class="post-score" title="current number of votes">0</div><span id="post-2593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a issue by latency when logging in to our network . It takes between 5-10 minutes from the computer is startet until I am logged in.</p><p>I have done a wireshark capture from start of the computer until the login process is finished. How is the best way to analyze the traffic to determine the latency. I wish to find out if the latency belongs to LAN switching, applications &amp; Protocols,server traffic(late response).</p><p>Our environment is Windows XP 3(workstation), mixed novell(file &amp; print) and microsoft AD. Computers are members of AD.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-login" rel="tag" title="see questions tagged &#39;login&#39;">login</span> <span class="post-tag tag-link-measure" rel="tag" title="see questions tagged &#39;measure&#39;">measure</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '11, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/e1fed57eac9b10e2b57950c810766efb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AMO&#39;s gravatar image" /><p><span>AMO</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AMO has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-2593" class="comments-container"></div><div id="comment-tools-2593" class="comment-tools"></div><div class="clear"></div><div id="comment-2593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2594"></span>

<div id="answer-container-2594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2594-score" class="post-score" title="current number of votes">0</div><span id="post-2594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first things you need to find out are:</p><ul><li>Is every users PC affected? Or just a groups of users (if so, what do they have in common)? Or one particular PC?</li><li>Since when does the problem occur (were there any changes)? Or did it slowly creep in?</li><li>Is the problem there all the time? Or maybe just in the morning when everybody logs in at about the same time?</li></ul><p>That will give you an idea of where the problem might lie. And it also will give you clues anout where to look for in your trace file. Especially if not all users are affected, a comparison between the trace files of a bad and a good login session if valuable.</p><p>When analyzing the trace file at hand. I would look at the following things:</p><ul><li>File size (Summary window). How much data is exchanged during the login process</li><li>Delays. Where do delays between packets occur. Does the client not send any data after receiving data from the server or does the server receive data and not respond quickly. Add up the individual delays to get an indication whether the client or the server(s) are causing most of the delay.</li><li>Look for retransmissions. Do they occur often, then you may have a network problem like a duplex mismatch somewhere along the line.</li></ul><p>It's not easy to give a list of actions to take to pinpoint the problem as there are just to many variables. It's a combination of experience and 'art' to analyze trace files :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '11, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2594" class="comments-container"></div><div id="comment-tools-2594" class="comment-tools"></div><div class="clear"></div><div id="comment-2594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2607"></span>

<div id="answer-container-2607" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2607-score" class="post-score" title="current number of votes">0</div><span id="post-2607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another great features in Wireshark that helps in your quest is the Service Response Time: (Statistics -&gt; Service Response Time ...)</p><ul><li>Are the SMB / LDAP / DCE-RPC response times what you expect?</li><li>Check the service response time from a trace captured close to the server. Most SMB transactions should complete within a millisecond or two.</li><li>Check the service response time from a trace captured close to the client. This shows the real waiting time for the user</li></ul><p>You might want to check, if users wait for the PC to boot (i. e. power on until login box shows) or for the login (i. e. clicked OK, then wait until the desktop is ready).</p><p>The time from power on to login box can identified as followed: First locate the DHCP request (filter <strong>bootp</strong>) and set a time reference to the DHCP discover or request.</p><p>Next look out for a Kerberos message where the message-type is AS-REQ and the client name is the user. A good filter is <strong>kerberos.msg.typ == 10</strong> If the client principal matches the user name you have identified the time when the user clicked the OK button in the login-box.</p><p>The time from login to "Desktop ready" can be influenced by a number of factors. Roaming can be a pain, if a user decides to keep his collection of ISO images under "My Documents". Another factor to consider is the number of policies, that are applied.</p><hr /><p>NB: The AS-REQ is also shown, if a local service is started with the username</p><p>NB2: Depending on your configuration the login box can show up before all policies are loaded</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '11, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '17, 07:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-2607" class="comments-container"><span id="2617"></span><div id="comment-2617" class="comment"><div id="post-2617-score" class="comment-score"></div><div class="comment-text"><p>The most interesting part is from that point when username and password is entered and Ok is pressed. And then look at the packets from that point and to desktop ready. I will try to set a timereference.</p><p>This latency occurs for several hundreds computers. So I do not believe that collection of huge files under "My documents" cause the problem. We do not use roaming profiles.</p><p>As you mention, I will also try to look at service responsetime from a trace close to the client. Interesting tip I will try: Statistics -&gt; Service Response Time ...</p><p>I appreciate any tip from you.</p></div><div id="comment-2617-info" class="comment-info"><span class="comment-age">(01 Mar '11, 12:03)</span> <span class="comment-user userinfo">AMO</span></div></div><span id="2621"></span><div id="comment-2621" class="comment"><div id="post-2621-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment" to adhere to the Q&amp;A nature of this site)</p></div><div id="comment-2621-info" class="comment-info"><span class="comment-age">(01 Mar '11, 14:13)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-2607" class="comment-tools"></div><div class="clear"></div><div id="comment-2607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

