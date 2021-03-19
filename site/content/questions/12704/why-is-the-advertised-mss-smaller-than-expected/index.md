+++
type = "question"
title = "Why is the advertised MSS smaller than expected"
description = '''The client NIC is set to MTU of 4000 and supposedly the switches along the paths. The SYN is showing a 1380 MSS instead of 3960. What is the cause?'''
date = "2012-07-13T02:52:00Z"
lastmod = "2012-07-24T17:24:00Z"
weight = 12704
keywords = [ "mss", "mtu" ]
aliases = [ "/questions/12704" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the advertised MSS smaller than expected](/questions/12704/why-is-the-advertised-mss-smaller-than-expected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12704-score" class="post-score" title="current number of votes">0</div><span id="post-12704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The client NIC is set to MTU of 4000 and supposedly the switches along the paths. The SYN is showing a 1380 MSS instead of 3960. What is the cause?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mss" rel="tag" title="see questions tagged &#39;mss&#39;">mss</span> <span class="post-tag tag-link-mtu" rel="tag" title="see questions tagged &#39;mtu&#39;">mtu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '12, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p><span>ws2006</span><br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted <strong>13 Jul '12, 05:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-12704" class="comments-container"></div><div id="comment-tools-12704" class="comment-tools"></div><div class="clear"></div><div id="comment-12704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12710"></span>

<div id="answer-container-12710" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12710-score" class="post-score" title="current number of votes">0</div><span id="post-12710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are several possibilities why the MSS is different than the MTU. Please check the items below and provide some more details about your environment.</p><ol><li>how did you check that the MTU is really set to 4000?</li><li>an application can set the MSS via setsockopt (TCP_MAXSEG). If that works, depends on the OS, kernel parameters, etc. Maybe your application does that. What is the MSS if you use a "standard" tcp client like: <strong><code>telnet ask.wireshark.org 80</code></strong>?</li><li>iptables (TCPMSS target) can modify the MSS value. Other security devices can do that as well.</li><li>what is your OS?</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '12, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '12, 16:42</strong> </span></p></div></div><div id="comments-container-12710" class="comments-container"><span id="12765"></span><div id="comment-12765" class="comment"><div id="post-12765-score" class="comment-score"></div><div class="comment-text"><ol><li>The network team verified the MTU on the switches are set to 4000 and the server NIC was changed to 4000. Both client and server side are set to 4000 and can ping with 4000 mtu. The client is announcing 1380 MSS in the SYN and the server responding with 3960 in the SYN-ACK. The OS is Solaris. When the Server do initiate the connection, his SYN is 3960 as MSS and the client MSS is 1380 in the SYN-ACK. So it is the client not announcing the 3960 MSS.</li></ol></div><div id="comment-12765-info" class="comment-info"><span class="comment-age">(16 Jul '12, 07:55)</span> <span class="comment-user userinfo">ws2006</span></div></div><span id="12770"></span><div id="comment-12770" class="comment"><div id="post-12770-score" class="comment-score"></div><div class="comment-text"><p>is the client solaris?<br />
Can you post the output of <code>ifconfig -a</code>?<br />
what is the MSS if you use telnet instead of your application?</p></div><div id="comment-12770-info" class="comment-info"><span class="comment-age">(16 Jul '12, 08:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12775"></span><div id="comment-12775" class="comment"><div id="post-12775-score" class="comment-score"></div><div class="comment-text"><p>please (additionally) post the output of these commands on the client.</p><blockquote><p><code>ndd /dev/tcp tcp_mss_def</code><br />
<code>ndd /dev/tcp tcp_mss_max</code><br />
<code>ndd /dev/tcp tcp_mss_def_ipv4</code><br />
<code>ndd /dev/tcp tcp_mss_max_ipv4</code><br />
</p></blockquote><p>Maybe there is a limit defined, that explains the behaviour.</p></div><div id="comment-12775-info" class="comment-info"><span class="comment-age">(16 Jul '12, 11:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12710" class="comment-tools"></div><div class="clear"></div><div id="comment-12710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12822"></span>

<div id="answer-container-12822" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12822-score" class="post-score" title="current number of votes">0</div><span id="post-12822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you made the capture on the server or very close to the server. The MSS value in the TCP options of a SYN or SYN/ACK packet can be altered by network devices in between the client and the server.</p><p>One reason to do this is when a VPN device tunnels TCP traffic, it will lower the MSS value to make sure there is no need to fragment the packet after the packet is encapsulated.</p><p>Cisco FWSM and ACE modules do lower the MSS by default to 1380, but you can change this by the following settings:</p><ul><li>sysopt connection tcpmss &lt;0-65535&gt;</li><li>mtu &lt;interface&gt; &lt;mtu-value&gt;</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '12, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-12822" class="comments-container"><span id="12978"></span><div id="comment-12978" class="comment"><div id="post-12978-score" class="comment-score"></div><div class="comment-text"><p>Yes, the capture was at the sender side on the server vlan. Thanks.</p></div><div id="comment-12978-info" class="comment-info"><span class="comment-age">(24 Jul '12, 17:24)</span> <span class="comment-user userinfo">ws2006</span></div></div></div><div id="comment-tools-12822" class="comment-tools"></div><div class="clear"></div><div id="comment-12822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

