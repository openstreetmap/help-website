+++
type = "question"
title = "https traffic times out"
description = '''Yesterday a couple of users reported a problem accessing https://www.firstrepublic.com. The site worked fine in the past. One user is on the internal lan behind a sonicwall firewall. The second user is outside the corporate firewall and is behind a cisco small business router. They both connect to t...'''
date = "2014-08-05T18:07:00Z"
lastmod = "2014-08-06T06:04:00Z"
weight = 35237
keywords = [ "out", "https", "times" ]
aliases = [ "/questions/35237" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [https traffic times out](/questions/35237/https-traffic-times-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35237-score" class="post-score" title="current number of votes">0</div><span id="post-35237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Yesterday a couple of users reported a problem accessing <a href="https://www.firstrepublic.com">https://www.firstrepublic.com</a>. The site worked fine in the past. One user is on the internal lan behind a sonicwall firewall. The second user is outside the corporate firewall and is behind a cisco small business router. They both connect to the same ISP. When you attempt to connect to the site it times out. On rare occasions after a long delay the site does open in text view. If I connect a laptop directly to my WAN switch and assign it an ipaddress I can connect fine. Thing that doesn't make sense is the two users are behind different firewalls and started having the problem exact same time. If I connect directly to the WAN I can connect fine. No changes have been made, I am the only admin and was away on vacation last week. I can access other sites with no problems, including banking and credit card sites. So far it appears to be isolated to this one site. We can first republic and they are not aware of any problems.</p><p>I don't see any errors in the firewall logs. I uploaded a tracefile. If someone would bekind enough to look at it perhaps they can point me in the right direction. The source ip is 192.168.1.76 the dest is 72.3.176.221</p><p>I can ping and tracert to the website, it's only accessing it with a browser, IE, Chrome or Firefox that I have a problem. Let me know if you need additional information. Thanks in advance.</p><p><a href="https://onedrive.live.com/redir.aspx?cid=949862ff5b8a7a62&amp;page=self&amp;resid=949862FF5B8A7A62!108&amp;parId=949862FF5B8A7A62!105&amp;authkey=!Atcpjsj_KZsRGzE&amp;Bpub=SDX.SkyDrive&amp;Bsrc=Share">https://onedrive.live.com/redir.aspx?cid=949862ff5b8a7a62&amp;page=self&amp;resid=949862FF5B8A7A62!108&amp;parId=949862FF5B8A7A62!105&amp;authkey=!Atcpjsj_KZsRGzE&amp;Bpub=SDX.SkyDrive&amp;Bsrc=Share</a></p><p>Robert</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-out" rel="tag" title="see questions tagged &#39;out&#39;">out</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-times" rel="tag" title="see questions tagged &#39;times&#39;">times</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '14, 18:07</strong></p><img src="https://secure.gravatar.com/avatar/9ac06e048db50cbb1f84e68e5517f0f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgm34&#39;s gravatar image" /><p><span>rgm34</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgm34 has no accepted answers">0%</span></p></div></div><div id="comments-container-35237" class="comments-container"><span id="35263"></span><div id="comment-35263" class="comment"><div id="post-35263-score" class="comment-score"></div><div class="comment-text"><p>There was packet loss. The SSL handshake was successful, but the client (192.168.1.76) never received a few of the data packets from the server. It tries to get them by sending duplicate ACKs, and sending keep-alives to keep the connection open. But it never got the missing segments, so it terminated the connection.</p><p>The question is where are these packets getting dropped? That's a very difficult question to answer if your trace is limited to one side of the connection.</p></div><div id="comment-35263-info" class="comment-info"><span class="comment-age">(06 Aug '14, 05:20)</span> <span class="comment-user userinfo">smp</span></div></div></div><div id="comment-tools-35237" class="comment-tools"></div><div class="clear"></div><div id="comment-35237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35265"></span>

<div id="answer-container-35265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35265-score" class="post-score" title="current number of votes">0</div><span id="post-35265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Robert,</p><p>If you could get matching traces from the outside of the firewall and the laptop at least you would be able to narrow the problem a little. Each side of the firewall would be even better.</p><p>As SMP says, the current trace just shows that you are dropping packets somewhere, or we are not seeing them all. Perhaps you have some strange asymmetric routing going on which could be identified with matching traces from each side of the firewall.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '14, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35265" class="comments-container"></div><div id="comment-tools-35265" class="comment-tools"></div><div class="clear"></div><div id="comment-35265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

