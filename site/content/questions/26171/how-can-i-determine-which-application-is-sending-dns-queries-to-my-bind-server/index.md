+++
type = "question"
title = "How can I determine which application is sending DNS queries to my Bind server?"
description = '''I&#x27;m trying to figure out how one would go about determining which application on my Linux box is sending a particular DNS query to my Bind server. I&#x27;ve been toying with the following command: $ tshark -i wlan0 -nn -e ip.src -e dns.qry.name -E separator=&quot;;&quot; -T fields port 53 192.168.1.20;ajax.googlea...'''
date = "2013-10-18T08:41:00Z"
lastmod = "2013-10-21T03:45:00Z"
weight = 26171
keywords = [ "dns" ]
aliases = [ "/questions/26171" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I determine which application is sending DNS queries to my Bind server?](/questions/26171/how-can-i-determine-which-application-is-sending-dns-queries-to-my-bind-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26171-score" class="post-score" title="current number of votes">0</div><span id="post-26171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to figure out how one would go about determining which application on my Linux box is sending a particular DNS query to my Bind server. I've been toying with the following command:</p><pre><code>$ tshark -i wlan0 -nn -e ip.src -e dns.qry.name -E separator=&quot;;&quot; -T fields port 53
192.168.1.20;ajax.googleapis.com
192.168.1.101;ajax.googleapis.com
192.168.1.20;pop.bizmail.yahoo.com</code></pre><p>How can I get this to show me the actual application (port and possibly PID)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/9421488baab01c1fd83a76e908d54350?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slm&#39;s gravatar image" /><p><span>slm</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slm has no accepted answers">0%</span></p></div></div><div id="comments-container-26171" class="comments-container"><span id="26191"></span><div id="comment-26191" class="comment"><div id="post-26191-score" class="comment-score"></div><div class="comment-text"><blockquote><p>on my Linux box</p></blockquote><p>what is your distribution and release? Depending on the kernel you are using, you could try to use Systemtap to trace gethostbyname().</p></div><div id="comment-26191-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26207"></span><div id="comment-26207" class="comment"><div id="post-26207-score" class="comment-score"></div><div class="comment-text"><p>I'm on Fedora. Can you explain how to do this a bit?</p></div><div id="comment-26207-info" class="comment-info"><span class="comment-age">(18 Oct '13, 19:52)</span> <span class="comment-user userinfo">slm</span></div></div></div><div id="comment-tools-26171" class="comment-tools"></div><div class="clear"></div><div id="comment-26171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26173"></span>

<div id="answer-container-26173" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26173-score" class="post-score" title="current number of votes">2</div><span id="post-26173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="slm has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With normal packet captures there is no way of identifying the application or PID from the packets, because all you can see is what port the packet was sent from.</p><p>If you capture on a host that is doing the communication you could try to use the <a href="https://github.com/HoneProject/Linux-Sensor">Hone Project</a> to get that kind of information. On Windows, <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Network Monitor</a> can do the same.</p><p>Otherwise you could try to use netstat on the box that does the name resolution and match it to the port numbers the DNS query uses, but since it is a UDP communication the port is open and closed almost instantly - so chances to do the netstat just in that millisecond where it is open is going to be like trying to win the lottery.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26173" class="comments-container"></div><div id="comment-tools-26173" class="comment-tools"></div><div class="clear"></div><div id="comment-26173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26234"></span>

<div id="answer-container-26234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26234-score" class="post-score" title="current number of votes">1</div><span id="post-26234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm on Fedora. Can you explain how to do this a bit?</p></blockquote><p>First install systemtap</p><blockquote><p><a href="https://sourceware.org/systemtap/wiki/SystemtapOnFedora">https://sourceware.org/systemtap/wiki/SystemtapOnFedora</a></p></blockquote><p>Then, if you kernel supports CONFIG_UTRACE, you can run the following script</p><pre><code>#!/usr/bin/env stap

probe process(&quot;/lib/x86_64-linux-gnu/libc.so.6&quot;).function(&quot;gethostbyname&quot;).call {
log(user_string($name)) }</code></pre><p>Please replace the path of libc with the one on your system!!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26234" class="comments-container"></div><div id="comment-tools-26234" class="comment-tools"></div><div class="clear"></div><div id="comment-26234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

