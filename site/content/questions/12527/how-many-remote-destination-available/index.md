+++
type = "question"
title = "how many remote destination available?"
description = '''Hi Everybody How many remote destination will be available if I want to get reports from a PC ? Regards'''
date = "2012-07-09T06:46:00Z"
lastmod = "2012-07-11T07:06:00Z"
weight = 12527
keywords = [ "remote-monitoring" ]
aliases = [ "/questions/12527" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how many remote destination available?](/questions/12527/how-many-remote-destination-available)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12527-score" class="post-score" title="current number of votes">0</div><span id="post-12527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everybody</p><p>How many remote destination will be available if I want to get reports from a PC ?</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote-monitoring" rel="tag" title="see questions tagged &#39;remote-monitoring&#39;">remote-monitoring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '12, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/47a7e698e00a2e039822404128b814f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mm23&#39;s gravatar image" /><p><span>mm23</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mm23 has no accepted answers">0%</span></p></div></div><div id="comments-container-12527" class="comments-container"><span id="12532"></span><div id="comment-12532" class="comment"><div id="post-12532-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure what you are looking for. Is the question about the max. number of remote capture devices that can feed captured packets to Wireshark in parallel?</p></div><div id="comment-12532-info" class="comment-info"><span class="comment-age">(09 Jul '12, 11:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12565"></span><div id="comment-12565" class="comment"><div id="post-12565-score" class="comment-score"></div><div class="comment-text"><p>Dear Kurt,</p><p>Actually i am a new guy and trying to learn and want to run Wireshark on my local network due to analysing and monitoring.Are you thinking am i able to use Wireshark to cover it or i should be choise other application?</p><p>Best Regards</p></div><div id="comment-12565-info" class="comment-info"><span class="comment-age">(10 Jul '12, 10:45)</span> <span class="comment-user userinfo">mm23</span></div></div><span id="12566"></span><div id="comment-12566" class="comment"><div id="post-12566-score" class="comment-score"></div><div class="comment-text"><p>Additional: It means i want to run a server and try to get different reports from remote serivce on <a href="http://Wireshark.Is">Wireshark.Is</a> it possible ? how i have to manage it to get faster speed and lower throughput on LAN?</p></div><div id="comment-12566-info" class="comment-info"><span class="comment-age">(10 Jul '12, 10:48)</span> <span class="comment-user userinfo">mm23</span></div></div></div><div id="comment-tools-12527" class="comment-tools"></div><div class="clear"></div><div id="comment-12527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12589"></span>

<div id="answer-container-12589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12589-score" class="post-score" title="current number of votes">0</div><span id="post-12589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm sorry, but I still don't understand. What do you mean by "and try to get different reports from remote serivce"? What kind of reports?</p><p>Let me guess: You want to analyze a performance problem between two locations (or two systems on a LAN) and you want to figure out why the connections are slow. Right?</p><p>If so, you have several options:</p><ul><li>Sniff on a mirror port of your switch or use a TAP. That is the preferred method to get results that are not influenced by "something" on the affected systems itself. See here:</li></ul><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code></p></blockquote><ul><li><p>Sniff on the affected systems itself, either only on one side of the communication or on both sides.<br />
</p><ul><li><p>If you decide to sniff only one side, just run Wireshark on one of the affected systems. Please read the manual how to do that:</p><blockquote><p><code>http://www.wireshark.org/docs/wsug_html_chunked/</code></p></blockquote></li><li>If you decide to sniff on both sides, you can either run Wireshark on both machines or you can use the remote capture feature of WinPcap.</li></ul></li></ul><blockquote><p><code>http://www.winpcap.org/docs/docs_41b5/html/group__remote.html</code><br />
<code>http://www.wireshark.org/docs/wsug_html_chunked/ChCapInterfaceRemoteSection.html</code><br />
</p></blockquote><p>Does that answer your question?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '12, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12589" class="comments-container"><span id="12598"></span><div id="comment-12598" class="comment"><div id="post-12598-score" class="comment-score"></div><div class="comment-text"><p>Dear Kurt</p><p>I am working on a company that those are more than 50 nodes( LAPTOP and PC's).The connection between those are Wireless and Ethernet but the people who are working there think that the connection speed on network to use server's is too low therefore i thought maybe i will be able to use Wireshark to find out this problem which means i have to run a Wireshark on a PC ( like a server ) and use from the remote service on Wireshark to get online reports from all off the destination. Perhaps it will be better to aks you that is the Wireshark a client-server application ?</p><p>Regards</p></div><div id="comment-12598-info" class="comment-info"><span class="comment-age">(11 Jul '12, 02:55)</span> <span class="comment-user userinfo">mm23</span></div></div><span id="12604"></span><div id="comment-12604" class="comment"><div id="post-12604-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but the people who are working there think that the connection speed on network to use server's is too low</p></blockquote><p>In that case, I suggest to capture traffic on a mirror port of the switch where those server(s) is connected. However, there are no "simple" statistics in Wireshark that will tell you what is slow and why. You need a thorough understanding of the actual problem as user reports are often vague. You also need a good understanding of networking protocols. Wireshark is just a tool that can help in the process of analyzing the network traffic it's not a network health monitor tool or a application performance monitoring tool. There are commercial solutions for those things, but they are rather expensive.</p><p>If you feel that is all too complicated, there are several options (in the mentioned order) ;-)</p><ul><li>Dive into the wonderful world of network troubleshooting and learn how to do it yourself. Start with some Wireshark videos on Youtube. Just search for Wireshark. They will give you a good idea what you can do with wireshark and how.</li><li>Hire a consultant who is able to do it for you</li><li>Throw some money at the problem and buy better equipment (network, server) in the hope it will improve things. Most of the time it does not ;-))</li></ul></div><div id="comment-12604-info" class="comment-info"><span class="comment-age">(11 Jul '12, 04:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12632"></span><div id="comment-12632" class="comment"><div id="post-12632-score" class="comment-score"></div><div class="comment-text"><p>Dear Kurt</p><p>Thank you very much for your co-operation.</p><p>Regards</p></div><div id="comment-12632-info" class="comment-info"><span class="comment-age">(11 Jul '12, 07:06)</span> <span class="comment-user userinfo">mm23</span></div></div></div><div id="comment-tools-12589" class="comment-tools"></div><div class="clear"></div><div id="comment-12589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

