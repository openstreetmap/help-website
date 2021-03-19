+++
type = "question"
title = "when running wireshark i came across what seems to be Bad TCP."
description = ''' i was watching because my internet seemed a tad slow after somoene threatened to dos/ddos me. Does this look abit sus? i Tracked the ip back to Santa monica California, which is not im my country. Something called Edgecast Networks. i don&#x27;t overly believe that this would be the ip of someone trying...'''
date = "2015-12-02T02:42:00Z"
lastmod = "2015-12-02T05:46:00Z"
weight = 48181
keywords = [ "bad", "tcp" ]
aliases = [ "/questions/48181" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [when running wireshark i came across what seems to be Bad TCP.](/questions/48181/when-running-wireshark-i-came-across-what-seems-to-be-bad-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48181-score" class="post-score" title="current number of votes">0</div><span id="post-48181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://i.imgur.com/TJf303k.png" alt="alt text" /></p><p>i was watching because my internet seemed a tad slow after somoene threatened to dos/ddos me. Does this look abit sus? i Tracked the ip back to Santa monica California, which is not im my country. Something called Edgecast Networks. i don't overly believe that this would be the ip of someone trying to ddos me. however i was just wondering if anyone can make sense of it.</p><p>i Am new to using Wireshark so sorry if i seem dumb when it comes to this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bad" rel="tag" title="see questions tagged &#39;bad&#39;">bad</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/3bdcd1fa96f01a10ca2f03f3e876b913?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gunshin101&#39;s gravatar image" /><p><span>gunshin101</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gunshin101 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Dec '15, 02:46</strong> </span></p></div></div><div id="comments-container-48181" class="comments-container"><span id="48182"></span><div id="comment-48182" class="comment"><div id="post-48182-score" class="comment-score"></div><div class="comment-text"><p>Hard to tell without the tracefile. Could you provide us a trace on a public accessible place like dropbox or cloudshark?</p><p>Sometimes the error message(New Fragment overlaps...) is caused by frame slicing. Do you use frame slicing?</p></div><div id="comment-48182-info" class="comment-info"><span class="comment-age">(02 Dec '15, 02:54)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="48194"></span><div id="comment-48194" class="comment"><div id="post-48194-score" class="comment-score"></div><div class="comment-text"><p>What <strong>can</strong> be told without the tracefile, by the screenshot, is that these particular packets are not part of a traditional DoS (or even DDoS) attack to your PC as it was your PC which has first asked the remote site for contents (see the destination IP of the http GET). The response which comes is broken (or got broken under way) for some reason.</p><p>A traditional DoS targeted to your PC would be quite complex to do as the PC is connected to the internet via a NAT device, so if someone would want to take it down using a targeted (D)DoS, they would have to use other computers in the same LAN for the purpose (which is not impossible but it is not the case here).</p><p>But it could be that the web site which your browser has asked for legal contents has been hijacked and is now responding with malicious contents to clients like your PC, in hope to exploit some tcp bug. The clients become accessible for such attacker because they've open a pinhole on their firewall by sending the http GET request.</p><p>For deeper analysis, you'd need to post the trace to some public place and give a link to it here, as <span></span><span>@Christian_R</span> asked you to.</p></div><div id="comment-48194-info" class="comment-info"><span class="comment-age">(02 Dec '15, 05:46)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48181" class="comment-tools"></div><div class="clear"></div><div id="comment-48181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

