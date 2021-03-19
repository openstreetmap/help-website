+++
type = "question"
title = "Decrypting SSL in SSL"
description = '''Hi all, I am challenged with the analysis of an SSL VPN Gateway. Users ultimately access an HTTPS server in the inside network. This session is encapsulated in another SSL layer on the outside. As I have both SSL keys (VPN gateway and HTTPS server) traffic can be decrypted. (Thanks, Wireshark, I lov...'''
date = "2010-12-09T00:57:00Z"
lastmod = "2010-12-10T08:30:00Z"
weight = 1296
keywords = [ "ssl", "ssltunnel" ]
aliases = [ "/questions/1296" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting SSL in SSL](/questions/1296/decrypting-ssl-in-ssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1296-score" class="post-score" title="current number of votes">0</div><span id="post-1296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am challenged with the analysis of an SSL VPN Gateway.</p><p>Users ultimately access an HTTPS server in the inside network. This session is encapsulated in another SSL layer on the outside.</p><p>As I have both SSL keys (VPN gateway and HTTPS server) traffic can be decrypted. (Thanks, Wireshark, I love this feature.)</p><p>Decrypted traffic on the outside of the gateway matches the encrypted traffic from the inside.</p><p>I want to compare HTTP response times from both sides of the gateway, thus deducting the latency.</p><p>Is there a way to peel off the inner layer of SSL? Or could I save decrypted contents as decrypted pcap file?</p><p>Any help is appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-ssltunnel" rel="tag" title="see questions tagged &#39;ssltunnel&#39;">ssltunnel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '10, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-1296" class="comments-container"></div><div id="comment-tools-1296" class="comment-tools"></div><div class="clear"></div><div id="comment-1296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1304"></span>

<div id="answer-container-1304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1304-score" class="post-score" title="current number of votes">0</div><span id="post-1304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is not possible to strip a layer or save decrypted traffic as pcap. The only option would be to do decryption two times for the outside traffic. I'm not sure though if the current implementation would support that or gets itself mixed up. What is the carried protocol within the SSL session to the SSL-VPN gateway?</p><p>If IP is carried, you could try the following key list when analyzing the outside traffic:</p><pre><code>&lt;ip-vpn-gateway&gt;,&lt;port&gt;,ip,&lt;sslvpn-key&gt;;&lt;ip-https-server&gt;,443,http,&lt;https-key&gt;</code></pre><p>If not, could you give a schematic of the encapsulation that is done by the SSL-VPN?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '10, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1304" class="comments-container"><span id="1311"></span><div id="comment-1311" class="comment"><div id="post-1311-score" class="comment-score"></div><div class="comment-text"><p>The external traffic carries HTTPS over HTTPS. The SSL gateway strips the outer layer and is a transparent proxy for the internal HTTPS session.</p><p>I tried to force a decode and entered both keys. Alas, it didn't work.</p></div><div id="comment-1311-info" class="comment-info"><span class="comment-age">(10 Dec '10, 04:28)</span> <span class="comment-user userinfo">packethunter</span></div></div><span id="1314"></span><div id="comment-1314" class="comment"><div id="post-1314-score" class="comment-score"></div><div class="comment-text"><p>A long shot, but if the SSL-VPN gateway acts as a HTTP proxy (which can be seen by the "CONNECT &lt;https-server&gt;" header at the beginning of the encapsulated traffic (after doing one layer of decryption), then it might be possible to decrypt both layers with the following keys_list:</p><p>&lt;ip-vpn-gateway&gt;,&lt;port&gt;,http,&lt;sslvpn-key&gt;;&lt;ip-vpn-gateway&gt;,0,http,&lt;https-key&gt;</p><p>This will treat the decrypted traffic as http, see the CONNECT, switches over to SSL for a second time and by the wildcard port find the https-key.</p><p>Then again... it's a long shot :-)</p></div><div id="comment-1314-info" class="comment-info"><span class="comment-age">(10 Dec '10, 08:30)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-1304" class="comment-tools"></div><div class="clear"></div><div id="comment-1304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

