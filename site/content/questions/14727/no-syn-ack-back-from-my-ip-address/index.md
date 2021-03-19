+++
type = "question"
title = "No [SYN, ACK] back from my IP address"
description = '''I am using FileZilla on my PC. I never had a problem having people connecting to it. I had to move to another PC because of hardware problems. Now on the new machine I nor anyone can connect to FileZilla using my IP address. My ISP is Comcast and their second level people could not see any problems ...'''
date = "2012-10-04T22:53:00Z"
lastmod = "2012-10-09T23:59:00Z"
weight = 14727
keywords = [ "ftp" ]
aliases = [ "/questions/14727" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No \[SYN, ACK\] back from my IP address](/questions/14727/no-syn-ack-back-from-my-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14727-score" class="post-score" title="current number of votes">0</div><span id="post-14727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using FileZilla on my PC. I never had a problem having people connecting to it. I had to move to another PC because of hardware problems. Now on the new machine I nor anyone can connect to FileZilla using my IP address. My ISP is Comcast and their second level people could not see any problems on their side of the SMC router/modem. I have looked at the wireshark trace and All I see is router sending one or two ftp [syn]'s. and I see no ftp [syn, ack].<br />
</p><p>I have tested with my windows 7 firewall down, Avira down and malwarebytes disabled. Any one have any ideas. Personally I think that comcast is doing something. I think that they want me to pay for a static IP address from then. They know I am using No-IP for my static IP address.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '12, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/4d8a237b0f73bd0874358e490a36e033?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IchBin&#39;s gravatar image" /><p><span>IchBin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IchBin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-14727" class="comments-container"></div><div id="comment-tools-14727" class="comment-tools"></div><div class="clear"></div><div id="comment-14727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14782"></span>

<div id="answer-container-14782" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14782-score" class="post-score" title="current number of votes">1</div><span id="post-14782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, it depends on some things:</p><ol><li><p>Where do you see the SYN packets? At the client side or at the server (FileZilla) side?</p></li><li><p>Did it work with that IP address from Comcast before? Maybe they switched from individual IPs per customer to a NATed address. In that case, you cannot connect to your server anymore.</p></li><li><p>Did you import that same FileZilla settings on the new server?</p></li><li><p>Does FileZilla works if you connect from the local network?</p></li><li><p>Silly, but anyway: Did you set the correct default route on your new server?</p></li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14782" class="comments-container"><span id="14801"></span><div id="comment-14801" class="comment"><div id="post-14801-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply.</p><p><strong>Question 1:</strong></p><p>External Address: <strong>69.253.224.6</strong></p><p>IPV4 Address: <strong>10.1.10.147</strong>(Preferred)</p><p>Default Gateway &amp; DHP Server: <strong>10.1.10.1</strong></p><p>10.1.10.147 208.67.222.222 <strong>DNS</strong> query with conical name</p><p>208.67.222.222 10.1.10.147 <strong>DNS</strong> Returns the IP 69.253.224.6</p><p>10.1.10.147 69.253.224.6 <strong>TCP</strong> ftp [SYN] Seg=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1</p><p>10.1.10.147 69.253.224.6 <strong>TCP</strong> ftp [SYN] Seg=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1</p><p>10.1.10.147 69.253.224.6 <strong>TCP</strong> ftp [SYN] Seg=0 Win=8192 Len=0 MSS=1460 SACK_PERM=1</p><p><strong>Question 2:</strong></p><p>Yes.. on a different PC. On the New PC. Initially I noticed that the ports where locked. Comcast second level fixed that problem. Before I called support I was able to ping my address 69.253.224.6 but after the first call I could not even ping it but the ports where open. They mentioned they would try to bridge the router and modem. Not sure I know enough info to reply to this question.</p><p><strong>Question 3:</strong></p><p>I did not import the settings. I changed by hand.</p><p><strong>Question 4:</strong></p><p>Yes no problem. In fact I test accounts first using local host</p><p><strong>Question 5:</strong></p><p>If you mean 'Port forwarding' I did on the router. Not sure what you mean by correct default route on your new server?</p></div><div id="comment-14801-info" class="comment-info"><span class="comment-age">(08 Oct '12, 15:35)</span> <span class="comment-user userinfo">IchBin</span></div></div><span id="14806"></span><div id="comment-14806" class="comment"><div id="post-14806-score" class="comment-score"></div><div class="comment-text"><p>regarding question 1:</p><p>I'm not quite sure if I understand the problem. Do you see an <strong>incoming</strong> SYN packet on your FileZilla Server, if you connect to 69.253.224.6?</p><p>If NO, then either your Port-Forwarding does not work, or the IP 69.253.224.6 is now natted and connections from the Internet are not forwarded to your router.</p><p>If yes, and you're not seeing a SYN/ACK, something your local PC blocks the requests (Firewall, Endpoint Protection, AV, etc.).</p><p>BTW: What is the dump you posted? Is 10.1.10.147 your FileZilla Server? If so, why do you try to connect to your own external address from that server?</p><p>Can you please add some more information, like:</p><p>internal IP of FileZilla Server, external IP address, Port Forwarding settings, etc.</p><p>Regards<br />
Kurt</p></div><div id="comment-14806-info" class="comment-info"><span class="comment-age">(09 Oct '12, 01:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14849"></span><div id="comment-14849" class="comment"><div id="post-14849-score" class="comment-score"></div><div class="comment-text"><p>I did have the address you asked for but seems they are hard to see the way they were attached in last response to this thread. Sorry I typically do not get to this level of debugging.</p><ul><li>External Address (WAN DHCP IP Address): <strong>69.253.224.6</strong></li><li>IPV4 Address: <strong>10.1.10.147(Preferred)</strong></li><li>Default Gateway &amp; DHP Server: <strong>10.1.10.1</strong></li></ul><p>My Port Forwarding rules ( they match FileZilla )</p><ul><li>FileZilla - <strong>Port 20-21 (Public &amp; Private) TCP IP Address 10.1.10.147</strong></li><li>Passive - <strong>Ports 3850-3859 (Public &amp; Private) TCP IP Address 10.1.10.147</strong></li><li>FTPS - <strong>Ports 989-990 (Public &amp; Private) TCP IP Address 10.1.10.147</strong></li></ul><p>Attaching the Wire shark capture when trying to connect to 69.253.224.6 my external IP address.</p><p>I am not seeing a Source <strong>69.253.224.6</strong> to <strong>10.1.10.147</strong> with a FTP [SYN, ACK]</p><p>Definitely not going to see the third [ACK] from 10.1.10.147 if I do not see the second handshake.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/FileZilla_to_My_PC_server_(Bad).png" alt="alt text" /></p></div><div id="comment-14849-info" class="comment-info"><span class="comment-age">(09 Oct '12, 20:52)</span> <span class="comment-user userinfo">IchBin</span></div></div><span id="14859"></span><div id="comment-14859" class="comment"><div id="post-14859-score" class="comment-score"></div><div class="comment-text"><p>O.K. from your description, I conclude, that 10.1.10.147 is your internal FileZilla server. So, in the screenshot (frame 6/7) we see a connection initiation (SYN) from 10.1.10.147 -&gt; 69.253.224.6.</p><p>Sorry, but again: Why do you try to connect from the FileZilla server to it's own "mapped/NATed" address? That connection will be mapped back to the FileZilla server and that's probably not going to work, depending on the NAT configuration (source translation) of your router.</p><p>Reason:</p><blockquote><p>10.1.10.147:* -&gt; 69.253.224.6:21<br />
</p></blockquote><p>will be translated (port forwarded) to this (at your router):</p><blockquote><p>10.1.10.147:* -&gt; 10.1.10.147:21</p></blockquote><p>if no source translation takes place (at the router).</p><p>That will finally lead to problems at the FileZilla server (think about the 3-way handshake!). As that translated SYN request is not in your capture file, your either did not capture it (capture filter), or the router did not translate it.</p><p>Did you try to connect from the internet? Do you see incoming requests if someone connects to 69.253.224.6?</p></div><div id="comment-14859-info" class="comment-info"><span class="comment-age">(09 Oct '12, 23:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-14782" class="comment-tools"></div><div class="clear"></div><div id="comment-14782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

