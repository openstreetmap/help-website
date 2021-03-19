+++
type = "question"
title = "VPN and wireshark"
description = '''as i have been reading , when using a VPN most stuff on wireshark should be basically unreadable.. so.. when it comes to DNS why can i see everything that is happening on the dns side of things? it all comes through in plain text to wireshark eg: google.com or  152755 2108.687994000 192.168.1.2 10.3...'''
date = "2015-09-24T00:43:00Z"
lastmod = "2015-09-24T13:29:00Z"
weight = 46093
keywords = [ "vpn", "dns", "wireshark" ]
aliases = [ "/questions/46093" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VPN and wireshark](/questions/46093/vpn-and-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46093-score" class="post-score" title="current number of votes">0</div><span id="post-46093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>as i have been reading , when using a VPN most stuff on wireshark should be basically unreadable.. so.. when it comes to DNS why can i see everything that is happening on the dns side of things? it all comes through in plain text to wireshark eg: google.com or</p><pre><code>152755  2108.687994000  192.168.1.2 10.30.0.1   DNS 76  Standard query 0x381f  A dns.msftncsi.com</code></pre><p>and so forth i have no dns leaks.. tried on ipleak.net and a few others..dnsleaktest.com n so forth im using Airvpn and cyberghost sepeartly mind you, and it is plain as day the dns requests.. are they scrambled through the vpn tunnel and spat out so only wireshark and my pc can read these or if i can see them so can everybody else? im sorry i dont know how to post a screen dump so maybe ill post on imgur if thats ok thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '15, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/9879a78df052f5129960ce5a8f1dbb9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nitehawk&#39;s gravatar image" /><p><span>nitehawk</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nitehawk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Sep '15, 01:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46093" class="comments-container"><span id="46124"></span><div id="comment-46124" class="comment"><div id="post-46124-score" class="comment-score"></div><div class="comment-text"><p>im going to post to expire box as i cannot work cloudshark. ive posted a snippet of time with vpn running i usew firefox tried another browser..Edge but it gave me the same thing im beginning to think its normal..</p><p>Capture <a href="http://expirebox.com/download/a17e1b8c95156fda396f24a8989703a8.html">http://expirebox.com/download/a17e1b8c95156fda396f24a8989703a8.html</a></p><p>CMD routes <a href="http://expirebox.com/download/87b04020f1b69d031c13272bd179ef00.html">http://expirebox.com/download/87b04020f1b69d031c13272bd179ef00.html</a></p></div><div id="comment-46124-info" class="comment-info"><span class="comment-age">(24 Sep '15, 13:29)</span> <span class="comment-user userinfo">nitehawk</span></div></div></div><div id="comment-tools-46093" class="comment-tools"></div><div class="clear"></div><div id="comment-46093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46095"></span>

<div id="answer-container-46095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46095-score" class="post-score" title="current number of votes">0</div><span id="post-46095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Only traffic sent through the VPN tunnel will be encrypted. Depending on the tunnel configuration it will either scoop up all traffic or only traffic for a particular destination, I'm not familiar with either of the VPN systems you mention so don't know if they can be configured to route all traffic into the tunnel.</p><p>It would appear that at least some of your DNS traffic isn't being sent via the tunnel.</p><p>This isn't really a Wireshark question, more about your VPN Config. You'll probably get better support on the forums for the VPN's you are using.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-46095" class="comments-container"><span id="46096"></span><div id="comment-46096" class="comment"><div id="post-46096-score" class="comment-score"></div><div class="comment-text"><p>hi , thanks for your awnser , im asking if its normal.. all traffic is going through VPN with both.. im on windows 10 with native program for each provider (their vpn program)</p><p>so im just trying to figure out why i can see things in wireshark in plain text if its supposed to be encrypted.. unless dns does something diffrent maybe someone else might know.</p></div><div id="comment-46096-info" class="comment-info"><span class="comment-age">(24 Sep '15, 02:06)</span> <span class="comment-user userinfo">nitehawk</span></div></div><span id="46107"></span><div id="comment-46107" class="comment"><div id="post-46107-score" class="comment-score"></div><div class="comment-text"><p>The vpn client will modify your routing table to direct traffic into the tunnel (use <code>route print</code> from a command line prompt).</p><p>The network resolver built into Windows just issues DNS requests to the configured DNS servers, then it's up to the network routing as to where those requests are sent.</p><p>You'll probably have to post a capture file to get any further, showing this DNS request and some encrypted vpn traffic. You could also post the contents of your routing table when the vpn is running as a comment here.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox, and post the link back here?</p></div><div id="comment-46107-info" class="comment-info"><span class="comment-age">(24 Sep '15, 07:27)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-46095" class="comment-tools"></div><div class="clear"></div><div id="comment-46095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

