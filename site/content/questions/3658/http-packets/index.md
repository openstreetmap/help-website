+++
type = "question"
title = "HTTP packets"
description = '''What is relation between number of HTTP packets and number of objects in a web page?'''
date = "2011-04-20T13:42:00Z"
lastmod = "2011-04-20T23:59:00Z"
weight = 3658
keywords = [ "packets", "http" ]
aliases = [ "/questions/3658" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP packets](/questions/3658/http-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3658-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is relation between number of HTTP packets and number of objects in a web page?</p></div><div id="question-tags" class="tags-container tags">packets http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '11, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/0d1f835bfa8cc91838057ef65fc4d1c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A%20B&#39;s gravatar image" /><p>A B<br />
<span class="score" title="1 reputation points">1</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A B has no accepted answers">0%</span></p></div></div><div id="comments-container-3658" class="comments-container"><span id="3660"></span><div id="comment-3660" class="comment"><div id="post-3660-score" class="comment-score"></div><div class="comment-text"><p>So how can I count number of objects?just trace the source code of web page?</p></div><div id="comment-3660-info" class="comment-info"><span class="comment-age">(20 Apr '11, 13:49)</span> A B</div></div></div><div id="comment-tools-3658" class="comment-tools"></div><div class="clear"></div><div id="comment-3658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3659"></span>

<div id="answer-container-3659" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3659-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>None.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3659" class="comments-container"></div><div id="comment-tools-3659" class="comment-tools"></div><div class="clear"></div><div id="comment-3659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3665"></span>

<div id="answer-container-3665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3665-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might try to filter on GET/POST requests, for example using</p><pre><code>http.request.method==GET or http.request.method==POST</code></pre><p>Since every object needs to be requested by either GET or POST request that filter should allow you to find out how many objects were requested in a trace file. If your trace file contains more than one page you have to exclude those packets of pages you don't want. If you're lucky your webbrowser used one single TCP session (by using HTTP1.1 keep-alive) that contains all elements of one page allowing you to filter on. If not, you're in for some additional filtering work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3665" class="comments-container"><span id="3669"></span><div id="comment-3669" class="comment"><div id="post-3669-score" class="comment-score"></div><div class="comment-text"><p>When keep-alives are used, most browsers usually open up multiple TCP sessions. In the past 2 were opened max to not overload the server. Nowadays browsers open up more sessions at the same time to make sure objects are fetched in parallel.</p><p>I just checked my firefox setting (open about:config) and the setting "network.http.max-connections-per-server" is set to 15 by default now.</p></div><div id="comment-3669-info" class="comment-info"><span class="comment-age">(21 Apr '11, 00:15)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-3665" class="comment-tools"></div><div class="clear"></div><div id="comment-3665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3667"></span>

<div id="answer-container-3667" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3667-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>A rough indication on how many objects were on a page is to use the "http.rerefer" field. When a browser requests an object that is part of a page, it sets the Referer: header to the URL of the page on which the object was requested.</p><p>So I just tried opening www.facebook.com and filtered for <code>http.referer == "http://www.facebook.com/"</code> and that gave me 44 objects (you can quickly count the amount of objects by looking at the status bar where it says (Packets: XXX, Displayed 44, Marked XX, Dropped XX).</p><p>Please note that your original request will not be in the list (as the Referer: field will be empty when you manually type in an URL). Also be aware that any click on the page will also use the page URL in the Referer: field, even when going to another website.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Apr '11, 00:01</p></div></div><div id="comments-container-3667" class="comments-container"><span id="3686"></span><div id="comment-3686" class="comment"><div id="post-3686-score" class="comment-score"></div><div class="comment-text"><p>Are you sure about it?if I have a webpage with one picture which is stored in my own server I think that the request for the picture wont have referrer but it is an object.</p></div><div id="comment-3686-info" class="comment-info"><span class="comment-age">(21 Apr '11, 10:32)</span> A B</div></div><span id="3687"></span><div id="comment-3687" class="comment"><div id="post-3687-score" class="comment-score"></div><div class="comment-text"><p>If the image is referenced by an <img src="xxx" /> from within a html page, requesting the html page will make the browser request the image xxx and when it does, it should have a "Referer:" header.</p><p>You could check this within firefox with http-fox (or Firebug) for instance.</p><p>There is one way to find out for sure and that's to request the page, make a trace with wireshark and look in the http-headers of each request.</p></div><div id="comment-3687-info" class="comment-info"><span class="comment-age">(21 Apr '11, 13:56)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-3667" class="comment-tools"></div><div class="clear"></div><div id="comment-3667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

