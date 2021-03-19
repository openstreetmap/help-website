+++
type = "question"
title = "SHUTR Protocol (Suppressed Headers for Uplink Traffic Reduction)"
description = '''Hello forum, I was trying to gather some info about Qualcomm&#x27;s SHUTR protocol, and this is the only thing google threw back: &quot;SHUTR is a HTTP protocol extension designed to reduce the size of HTTP request headers sent by a mobile user agent. SHUTR speeds up page downloads and reduces network data tr...'''
date = "2013-11-24T17:07:00Z"
lastmod = "2013-11-25T04:13:00Z"
weight = 27328
keywords = [ "shutr" ]
aliases = [ "/questions/27328" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SHUTR Protocol (Suppressed Headers for Uplink Traffic Reduction)](/questions/27328/shutr-protocol-suppressed-headers-for-uplink-traffic-reduction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27328-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello forum, I was trying to gather some info about Qualcomm's SHUTR protocol, and this is the only thing google threw back:</p><p>"SHUTR is a HTTP protocol extension designed to reduce the size of HTTP request headers sent by a mobile user agent. SHUTR speeds up page downloads and reduces network data traffic, overall improving the mobile Web experience on Snapdragon processor-based devices."</p><p>Does anyone know how this works? I assume they would be trying to eliminate redundant Header bytes in HTTP POSTS, like in "Request URI", "User Agent", "Cookies" or "Referer". This would allow me to send more POSTS</p><p>Which makes a lot of sense, especially when combined with small CWND on the user side that prevent the server from achieving a full BDP (the more TCP ACKs I can piggy back on HTTP Posts, the better for the server to get into a "warm" TCP state closer to the RWIN). Am I correct?</p><p>Also, what type of compression would they use?</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">shutr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '13, 17:07</strong></p><img src="https://secure.gravatar.com/avatar/599929aa65406761d15533f022ed2d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ctxsvc&#39;s gravatar image" /><p>ctxsvc<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ctxsvc has one accepted answer">33%</span></p></div></div><div id="comments-container-27328" class="comments-container"></div><div id="comment-tools-27328" class="comment-tools"></div><div class="clear"></div><div id="comment-27328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27340"></span>

<div id="answer-container-27340" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27340-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The only things that google returns for SHUTR are press releases and a few sentences about the way it might work. So, bad luck, no information available.</p><blockquote><p>I assume they would be trying to eliminate redundant Header bytes in HTTP POSTS, like in "Request URI", "User Agent", "Cookies" or "Referer". This would allow me to send more POSTS</p></blockquote><p>I agree, but it will be for all requests not just POST requests.</p><blockquote><p>Am I correct?</p></blockquote><p>I agree. The 'savings' for TCP are certainly one effect of SHUTR. However, unless we find a detailed description, we can only speculate!</p><blockquote><p>Also, what type of compression would they use?</p></blockquote><p>I don't know what they are doing, but I don't believe it's 'compression', as the call the method: <strong>Suppressed</strong> Headers for Uplink Traffic Reduction.</p><p>I can (again) only speculate, but here is how I would do it, to reduce the amount of HTTP request headers.</p><ul><li>define a set of possible values for the typical headers in HTTP requests (User-Agent, Content-Type for POST, Connection:, Host:, etc.)</li><li>Then encode those headers in a 'compressed' way</li></ul><p>Example</p><p>Instead of sending:</p><pre><code>GET /test.html HTTP/1.1
Cookie: test=abc123; path=/; domain=.domain.com;
User-agent: MobileDevice/1.0 SnapDragon QC4 4.2.1
Host: test.domain.com
Connection: Keep-Alive</code></pre><p>You would send this for the first time:</p><pre><code>GET /test.html HTTP/1.1
X-SHUTR: 1.0:0x2732372,0x83787483,0x87939929,0x74837843
Cookie: test=abc123; path=/; domain=.domain.com;
User-agent: MobileDevice/1.0 SnapDragon QC4 4.2.1
Host: test.domain.com
Connection: Keep-Alive</code></pre><p>Where the SHUTR 'values' are placeholders for the headers, in the order they appear.</p><p><strong>0x2732372</strong> = placeholder for the string: "Cookie: test=abc123; path=/; domain=.domain.com;"<br />
<strong>0x83787483</strong> = placeholder for the string: "User-agent: MobileDevice/1.0 SnapDragon QC4 4.2.1"</p><p>etc.</p><p>Both the client and the server build a 'string-table' and are then able to use the placeholders instead of the strings.</p><p>The second time if you need to send the same headers again, you would just send the SHUTR values (placeholders) for those strings.</p><pre><code>GET /test2.html HTTP/1.1
X-SHUTR: 1.0:0x2732372,0x83787483,0x87939929,0x74837843</code></pre><p><strong>UPDATE</strong>: While I was editing my post a few minutes ago, I thought: If there is no general information available, maybe they have a patent or something.</p><p>Bingo!</p><blockquote><p><a href="http://www.google.com/patents/WO2011066585A1">http://www.google.com/patents/WO2011066585A1</a></p></blockquote><p>I did not fully read the patent text, but from the keywords I've seen, it looks like I 're-invented' their method ;-))</p><p>&lt;rant&gt; If that is the case (and I believe so), I question the whole patent system once again. Is something worth a patent, that can be 'invented' by a guy in a Q&amp;A site within 5 minutes, while he answers a question? No way!!! Reason: Because that's how others have solved a similar problem before, like byte caching in WAN accelerators (that's why I came up with that method rather fast). It's not O.K. (in my eyes) to receive a patent for a technique that others have used before, just because you apply it in a slightly modified way for a certain protocol! &lt;/rant&gt;</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '13, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '13, 06:15</p></div></div><div id="comments-container-27340" class="comments-container"></div><div id="comment-tools-27340" class="comment-tools"></div><div class="clear"></div><div id="comment-27340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

