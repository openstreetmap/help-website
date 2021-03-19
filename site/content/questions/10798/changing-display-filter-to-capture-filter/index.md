+++
type = "question"
title = "Changing Display Filter to Capture Filter"
description = '''In a previous question, I received some excellent explanation for a display filter. Now, I would like to use that filter with tshark. When I use the current one with tshark, I get a message that says it&#x27;s a valid display filter but not a valid capture filter. What are the differences? The display fi...'''
date = "2012-05-08T21:54:00Z"
lastmod = "2012-05-10T02:01:00Z"
weight = 10798
keywords = [ "capture-filter", "tshark" ]
aliases = [ "/questions/10798" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Changing Display Filter to Capture Filter](/questions/10798/changing-display-filter-to-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10798-score" class="post-score" title="current number of votes">0</div><span id="post-10798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a previous question, I received some excellent explanation for a display filter. Now, I would like to use that filter with tshark. When I use the current one with tshark, I get a message that says it's a valid display filter but not a valid capture filter. What are the differences?</p><p>The display filter suggested was</p><pre><code>udp.port==9565 or udp.port==9570 or udp.port==6000 or tcp.port==9946 or tcp.port==9988 or tcp.port==42124 or (tcp.port&gt;=10000 and tcp.port&lt;=20000)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '12, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/b47fc9ff10b938b2c04a2f791094637b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Perceptus&#39;s gravatar image" /><p><span>Perceptus</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Perceptus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '12, 00:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-10798" class="comments-container"></div><div id="comment-tools-10798" class="comment-tools"></div><div class="clear"></div><div id="comment-10798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10804"></span>

<div id="answer-container-10804" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10804-score" class="post-score" title="current number of votes">2</div><span id="post-10804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Perceptus has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As answer in the other question.</p><p>The syntax of display filters is totally different from the syntax of capture filters.</p><p>You can use this capture filter.</p><blockquote><p><code>(udp and (port 9565 or port 9570 or port 6000)) or (tcp and (port 9946 or port 9988 port 42124 or portrange 10000-20000))</code><br />
</p></blockquote><p><strong>portrange</strong> works at least with 1.6.2. (just tested). If it does not work with an earlier versions (not checked), please upgrade.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '12, 00:32</strong> </span></p></div></div><div id="comments-container-10804" class="comments-container"><span id="10846"></span><div id="comment-10846" class="comment"><div id="post-10846-score" class="comment-score"></div><div class="comment-text"><p>Do you have a link for where I can find out this information? Your answer is exactly what I was looking for. I tried to search the online documentation for the information you gave but I keep ending up on Display Filters instead.</p></div><div id="comment-10846-info" class="comment-info"><span class="comment-age">(09 May '12, 10:43)</span> <span class="comment-user userinfo">Perceptus</span></div></div><span id="10847"></span><div id="comment-10847" class="comment"><div id="post-10847-score" class="comment-score"></div><div class="comment-text"><p>take a look at the man page of pcap-filter:</p><blockquote><p><code>http://www.manpagez.com/man/7/pcap-filter/</code></p></blockquote></div><div id="comment-10847-info" class="comment-info"><span class="comment-age">(09 May '12, 11:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10851"></span><div id="comment-10851" class="comment"><div id="post-10851-score" class="comment-score"></div><div class="comment-text"><p>Have a look at the docs page on the Wireshark web site:</p><p><a href="http://www.wireshark.org/docs/man-pages/wireshark-filter.html">Display Filters</a></p><p><a href="http://wiki.wireshark.org/CaptureFilters">Capture Filters</a></p></div><div id="comment-10851-info" class="comment-info"><span class="comment-age">(09 May '12, 12:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="10854"></span><div id="comment-10854" class="comment"><div id="post-10854-score" class="comment-score"></div><div class="comment-text"><p>portrange works with 0.9 and later. :-)</p><p>I.e., whether portrange works is a function of the version of libpcap/WinPcap, not a function of the version of Wireshark. Libpcap 0.9 and later have support for it; I'm not sure which version of WinPcap was the first one based on libpcap 0.9.x, but WinPcap 4.0 and later are based on libpcap 0.9.x and later, so WinPcap 4.x should support portrange.</p></div><div id="comment-10854-info" class="comment-info"><span class="comment-age">(09 May '12, 14:41)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="10855"></span><div id="comment-10855" class="comment not_top_scorer"><div id="post-10855-score" class="comment-score"></div><div class="comment-text"><p>tshark -f '(udp (port 9565 or port 9570 or port 6000)) or (tcp (port 9946 or port 9988 port 42124 or portrange 10000-20000))' -i eth0 -w c:\capture.cap keeps saying</p><p>tshark: Capture filters were specified both with "-f" and with additional command-line arguments</p><p>What am I missing?</p></div><div id="comment-10855-info" class="comment-info"><span class="comment-age">(09 May '12, 16:39)</span> <span class="comment-user userinfo">Perceptus</span></div></div><span id="10858"></span><div id="comment-10858" class="comment not_top_scorer"><div id="post-10858-score" class="comment-score"></div><div class="comment-text"><p>The capture filter is invalid, which might be causing that misleading error message. There should be an <code>or</code> right before <code>port 42124</code>.</p><p><code> tshark '(udp and (port 9565 or port 9570 or port 6000)) or (tcp and (port 9946 or port 9988 or port 42124 or portrange 10000-20000))'</code></p></div><div id="comment-10858-info" class="comment-info"><span class="comment-age">(09 May '12, 16:52)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="10880"></span><div id="comment-10880" class="comment"><div id="post-10880-score" class="comment-score">1</div><div class="comment-text"><p>It's the stupidity of M$ DOS box. If you use " instead of ', it will work, e.g. tshark -f "(udp ...)".</p><p>BTW: eth0 is not a valid interface name on windows. Get the list of interfaces with 'dumpcap -D -M' and then use the interface ID, e.g. tshark -i 2.</p></div><div id="comment-10880-info" class="comment-info"><span class="comment-age">(10 May '12, 02:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-10804" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-10804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

