+++
type = "question"
title = "calculating page load up time using Wireshark"
description = '''Hello, I&#x27;m using wireshark to calculate the page load up time for a website. I&#x27;m comparing the results from other online tools such as &quot;http://www.webpagetest.org&quot; and see the results don&#x27;t tally. My capture filters is: dst host 1.1.1.1 or src host 1.1.1.1  Further, my capture filter is !(tcp.flags....'''
date = "2015-08-14T00:38:00Z"
lastmod = "2015-08-15T02:38:00Z"
weight = 45093
keywords = [ "performance", "statistics", "loading" ]
aliases = [ "/questions/45093" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [calculating page load up time using Wireshark](/questions/45093/calculating-page-load-up-time-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45093-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm using wireshark to calculate the page load up time for a website. I'm comparing the results from other online tools such as "http://www.webpagetest.org" and see the results don't tally.</p><p>My capture filters is:</p><pre><code>dst host 1.1.1.1 or src host 1.1.1.1</code></pre><p>Further, my capture filter is</p><pre><code>!(tcp.flags.reset == 1) &amp;&amp; !(tcp.flags.fin == 1)</code></pre><p>I'm looking at page load up time through he following UI "statistics -&gt; summary" and reading the " time between first and last packet" values.</p><p>Differences in coming in seconds not ms between online test and wireshark test done from my computer. I'm using wireless NIC card.</p><p>Is there a way to tweak the param's on wireshark to bring more close to real results.</p></div><div id="question-tags" class="tags-container tags">performance statistics loading</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '15, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/a5e36ef8cc4416aa199a3a82dcb1deb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lazerz&#39;s gravatar image" /><p>lazerz<br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lazerz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Aug '15, 00:39</p></div></div><div id="comments-container-45093" class="comments-container"></div><div id="comment-tools-45093" class="comment-tools"></div><div class="clear"></div><div id="comment-45093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45134"></span>

<div id="answer-container-45134" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45134-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.webpagetest.org">http://www.webpagetest.org</a> loads a web page from servers in <strong>their datacenter</strong> (spread around the world), so packets are taking a <strong>totally different path</strong> compared to the test form your own PC. So, there <strong>has to be a difference</strong> in load time, unless you are sitting in one of the datacenters of webpagetest.org ;-))</p><blockquote><p>Is there a way to tweak the param's on wireshark to bring more close to real results.</p></blockquote><p>Please define <strong>real results</strong> after you've read what I have written above.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '15, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45134" class="comments-container"><span id="45138"></span><div id="comment-45138" class="comment"><div id="post-45138-score" class="comment-score"></div><div class="comment-text"><p>Thanks for analysis, but the fact is that from my pc/laptop the server I'm tried to reach is local as far as my geo-location is concerned. The difference is greater on my side and lower from results of "webpagetest.org". The fact the packets take different path is true of any "packet switched based network".</p><p>Other thing is I'm trying to figure out when I should close wireshark capturing.</p><p>I have workaround it like manually, as the wireshark is "ON" i keep a look on website page, as soon it loaded (which i check load-status icon at end of address bar) I close wireshark, then i see more accurate results.</p><p>But then I see that for complete page-load up perhaps the main index page is visible but at background there are other content e.g css,.theme files that are being downloaded from external sources (that are not visible on UI itself).</p><p>So, logically is it "ok" to close the wireshark as soon as the browser ended up loading the page. Thanks.</p></div><div id="comment-45138-info" class="comment-info"><span class="comment-age">(15 Aug '15, 04:00)</span> lazerz</div></div><span id="45139"></span><div id="comment-45139" class="comment"><div id="post-45139-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but the fact is that from my pc/laptop the server I'm tried to reach is local as far as my geo-location is concerned.</p></blockquote><p>That doesn't matter. Sometimes packets are taking long routes, even if the server is in a datacenter at the next corner of the street, because you and the datacenter are attached to totally different ISPs and there is no direct peering between those two. So, it really all depends on the number of hops between you and the server AND also the available bandwidth. If one (or both) of these is better for webpagetest.org, they will get better page load times than you. Furthermore: The definition of "page load time" is also important. I don't know how webpagetest.org defines that, so that could be a reason for the difference as well.</p><blockquote><p>So, logically is it "ok" to close the wireshark as soon as the browser ended up loading the page. Thanks.</p></blockquote><p>I don't know, because that depends on the page design. If some scripts are loading content in the background, even after the page "looks" done in the browser, then you would miss something if you close Wireshark too fast.</p></div><div id="comment-45139-info" class="comment-info"><span class="comment-age">(15 Aug '15, 04:09)</span> Kurt Knochner ♦</div></div><span id="45140"></span><div id="comment-45140" class="comment"><div id="post-45140-score" class="comment-score"></div><div class="comment-text"><p>I'm okay with second part of answer, but with first I expect the ISP routing follows basic principle of "shortest path first". I'm sure the traceroute done against same server from usa and one done within same geolocation will wary. Within same geolocation ISP core router will maintain the list of "routes" which are advertised as being closest to the destibation. So the knowledge or hops between closest neighbours couldn't and shouldn't be as far away or same as if the same routing path is taken from I.e usa. Also for address that are geolinked as per dist by ARIN etc router wouldn't do upstream lookup for resolution of those addresses doesn't make sense. I'm not talking external hosting or mobile IP.Traffic at best be rounded by tier 2 or 3 Levels ISP.</p></div><div id="comment-45140-info" class="comment-info"><span class="comment-age">(15 Aug '15, 05:07)</span> asad</div></div><span id="45142"></span><div id="comment-45142" class="comment"><div id="post-45142-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I expect the ISP routing follows basic principle of "shortest path first".</p></blockquote><p>despite your expectation, the 'shortest' path is sometimes elected to go via different continents, as it's the <strong>cheapest</strong> path for the ISP ;-)</p><p>Anyway, without any further information about</p><ul><li>the hop count</li><li>rtt</li><li>bandwidth</li><li>packet loss rate</li></ul><p>of your link and the link used by webpagetest.org this discussion will not produce any new insights, besides what I have already posted :-)</p></div><div id="comment-45142-info" class="comment-info"><span class="comment-age">(15 Aug '15, 08:11)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-45134" class="comment-tools"></div><div class="clear"></div><div id="comment-45134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

