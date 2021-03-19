+++
type = "question"
title = "All the http protocol packets captured are ssl protected"
description = '''I used to get packets in wireshark, where http protocols were not encrypted but recently every packet with application data in my wireshark captured packets is ssl encrypted. There is not even one packet where I can see http protocol(ie when I filter with http, the result is always empty). It&#x27;s prot...'''
date = "2013-06-30T12:40:00Z"
lastmod = "2013-07-01T02:52:00Z"
weight = 22487
keywords = [ "ssl", "http" ]
aliases = [ "/questions/22487" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [All the http protocol packets captured are ssl protected](/questions/22487/all-the-http-protocol-packets-captured-are-ssl-protected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22487-score" class="post-score" title="current number of votes">0</div><span id="post-22487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I used to get packets in wireshark, where http protocols were not encrypted but recently every packet with application data in my wireshark captured packets is ssl encrypted. There is not even one packet where I can see http protocol(ie when I filter with http, the result is always empty). It's protocol is always TLsv1.1 and the data is encrypted, for every packet thats supposed to be http. So basically I cannot see the header information. Can anyone reply as to why this is happening. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '13, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/a7f84c53ea39d7c60cdefdf0984c9b3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="athina&#39;s gravatar image" /><p><span>athina</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="athina has no accepted answers">0%</span></p></div></div><div id="comments-container-22487" class="comments-container"><span id="22493"></span><div id="comment-22493" class="comment"><div id="post-22493-score" class="comment-score"></div><div class="comment-text"><p>What are the source and destination ports of the SSL packets you're seeing?</p></div><div id="comment-22493-info" class="comment-info"><span class="comment-age">(30 Jun '13, 17:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="22498"></span><div id="comment-22498" class="comment"><div id="post-22498-score" class="comment-score"></div><div class="comment-text"><p>the server's port(source/ dest) is generally https(443) and my computer's (57715 , 57810, etc). The ip addresses are of google, facebook, or quora. Everything is in https mode and ssl encrypted. Any ideas as to why this is happening?</p></div><div id="comment-22498-info" class="comment-info"><span class="comment-age">(30 Jun '13, 21:54)</span> <span class="comment-user userinfo">athina</span></div></div></div><div id="comment-tools-22487" class="comment-tools"></div><div class="clear"></div><div id="comment-22487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="22488"></span>

<div id="answer-container-22488" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22488-score" class="post-score" title="current number of votes">0</div><span id="post-22488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is the traffic always between yur IP address and one specific remote address? Then are you running some kind of SSL-VPN software?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '13, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22488" class="comments-container"><span id="22497"></span><div id="comment-22497" class="comment"><div id="post-22497-score" class="comment-score"></div><div class="comment-text"><p>There are multiple ip addresses from/to where the packets are encrypted. Even when I refresh my browser with websites like google.com, yahoo.com, etc, the dns packets are captured but there is no http protocol packet, only ssl encrypted packets which does say that the application data is http, but that data is encypted and I cannot read the header info. I have typed some of those ips into my browser and it took me to websites like google.com. So basically every http protocol is being ssl encrypted. I have no VPN, but I did run a server on this computer(now turned off). Any ideas why this might be happening?</p></div><div id="comment-22497-info" class="comment-info"><span class="comment-age">(30 Jun '13, 21:40)</span> <span class="comment-user userinfo">athina</span></div></div><span id="22501"></span><div id="comment-22501" class="comment"><div id="post-22501-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any ideas why this might be happening?</p></blockquote><p>See my answer.</p></div><div id="comment-22501-info" class="comment-info"><span class="comment-age">(30 Jun '13, 23:20)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-22488" class="comment-tools"></div><div class="clear"></div><div id="comment-22488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22500"></span>

<div id="answer-container-22500" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22500-score" class="post-score" title="current number of votes">0</div><span id="post-22500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>the server's port(source/ dest) is generally https(443) and my computer's (57715 , 57810, etc). The ip addresses are of google, facebook, or quora. Everything is in https mode and ssl encrypted. Any ideas as to why this is happening?</p></blockquote><p>Because whatever software on your computer is contacting those hosts (browser, or whatever) either</p><ol><li>is using an https:// URL, which means it's asking for HTTP-over-SSL;</li><li>the site is set up to redirect ordinary HTTP requests to the https:// URL, so it uses SSL.</li></ol><p>In case 1, all your HTTP traffic will be over SSL. In case 2, the initial HTTP request will not be over SSL, and the response to it will not be over SSL, but that response will just tell the browser (or other client software) to use an https:// URL, and all <em>subsequent</em> HTTP traffic will be over SSL.</p><p>For example, my Facebook account is set up to switch to SSL by default, so even if I go to <a href="http://www.facebook.com">http://www.facebook.com</a>, it will switch to <a href="https://www.facebook.com">https://www.facebook.com</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '13, 23:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22500" class="comments-container"><span id="22502"></span><div id="comment-22502" class="comment"><div id="post-22502-score" class="comment-score"></div><div class="comment-text"><p>I think its not 1 because: the browser shows https in the address bar for some and not for others. Besides I have tried both safari and chrome. For example after the site in loaded the address bar shows both kinds of url :</p><p>a) <a href="http://www.nytimes.com/">http://www.nytimes.com/</a> b) <a href="https://accounts.google.com/ServiceLogin?service=mail&amp;passive=true&amp;rm=false&amp;continue=http://mail.google.com/mail/&amp;scc=1&amp;ltmpl=default&amp;ltmplcache=2">https://accounts.google.com/ServiceLogin?service=mail&amp;passive=true&amp;rm=false&amp;continue=http://mail.google.com/mail/&amp;scc=1&amp;ltmpl=default&amp;ltmplcache=2</a></p><p>I think it shouldn't be 2 because : If the initial http request is not over SSL then if I filtered wireshark capture with the keyword http, some result should have appeared but the result is completely empty. Is it possible that the initial ssl request happens over tcp?</p></div><div id="comment-22502-info" class="comment-info"><span class="comment-age">(01 Jul '13, 00:39)</span> <span class="comment-user userinfo">athina</span></div></div></div><div id="comment-tools-22500" class="comment-tools"></div><div class="clear"></div><div id="comment-22500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22505"></span>

<div id="answer-container-22505" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22505-score" class="post-score" title="current number of votes">0</div><span id="post-22505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can anyone reply as to why this is happening. Thanks!</p></blockquote><p>because you (probably) installed a plug-in into your browser (Firefox, Chrome) that does <a href="http://en.wikipedia.org/wiki/Opportunistic_encryption">opportunistic encryption</a>, like <a href="https://addons.mozilla.org/de/firefox/addon/https-finder/">HTTPS Finder</a> or <a href="https://www.eff.org/https-everywhere">HTTPS Everywhere</a></p><p>The same holds true for any other browser. After a (recent) system update that browser version might try to find encrypted versions of a web site and then only use SSL/TLS to those sites.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22505" class="comments-container"></div><div id="comment-tools-22505" class="comment-tools"></div><div class="clear"></div><div id="comment-22505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

