+++
type = "question"
title = "Are tshark statistics slow?"
description = '''Previous post I use one tshark instance to sniff for 30 sec a network interface before a web server: tshark -a duration:30 -f &quot;(tcp dst port 8080) &amp;amp;&amp;amp; (tcp[13]=0x02 or tcp[((tcp[12:1] &amp;amp; 0xf0) &amp;gt;&amp;gt; 2):4] = 0x47455420)&quot; -w sniff.pcap  to capture packets with TCP.SYN and/or HTTP.GET requ...'''
date = "2012-01-26T14:53:00Z"
lastmod = "2012-01-28T07:57:00Z"
weight = 8638
keywords = [ "slow", "stats", "tshark" ]
aliases = [ "/questions/8638" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Are tshark statistics slow?](/questions/8638/are-tshark-statistics-slow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8638-score" class="post-score" title="current number of votes">0</div><span id="post-8638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="http://ask.wireshark.org/questions/8029/counting-incoming-tcp-open-http-get-requests-to-a-web-server">Previous post</a></p><p>I use one tshark instance to sniff for 30 sec a network interface before a web server:<br />
</p><pre><code>tshark -a duration:30 -f &quot;(tcp dst port 8080) &amp;&amp; (tcp[13]=0x02 or tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420)&quot; -w sniff.pcap</code></pre><p>to capture packets with TCP.SYN and/or HTTP.GET requests.<br />
</p><p>Following that, I call tshark to gather statistics from the capture file:<br />
</p><pre><code>tshark -r sniff.pcap -qz &quot;io,stat,0,COUNT(tcp.flags)tcp.flags==0x02&quot; -z &quot;io,stat,0,COUNT(http.request.method)http.request.method==&quot;GET&quot;&quot;</code></pre><p>Both these calls are made from a Java program using <em>Runtime.exec()</em> method in different threads.<br />
The concept is that capturing happens for 30 sec, then the next 30-sec-capturing starts, while in another thread statistics are gathered from the first capture.<br />
<strong>The problem is that the statistics call almost never runs to completion in the 30 sec window until its next call (sometimes takes minutes)</strong>.<br />
<br />
Is this delay something expected? Is there a way to speed the statistics up?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-stats" rel="tag" title="see questions tagged &#39;stats&#39;">stats</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '12, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/b6ab78997ac26efb7a11ea254f8bcc76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adonies&#39;s gravatar image" /><p><span>adonies</span><br />
<span class="score" title="12 reputation points">12</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adonies has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jan '12, 13:40</strong> </span></p></div></div><div id="comments-container-8638" class="comments-container"><span id="8644"></span><div id="comment-8644" class="comment"><div id="post-8644-score" class="comment-score"></div><div class="comment-text"><p>The first thing I'd do is run the tshark "gather statistics" command manually on one of the capture files to see how long it takes.</p><p>I'd then try manually running the tshark capture and the analysis simultaneously (two sub-processes ?) and see how that works.</p><p>This will give some info to verify that there's an issue with tshark being slow as opposed to some other problem (like some problem using threads or something).</p></div><div id="comment-8644-info" class="comment-info"><span class="comment-age">(26 Jan '12, 20:47)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="8656"></span><div id="comment-8656" class="comment"><div id="post-8656-score" class="comment-score"></div><div class="comment-text"><p>I ran tshark stats manually (windows command prompt) on one of the capture files and it completed in ~ 5sec the first time and half that time each time afterwards.</p><p>I ran tshark capture and stats manually as separate concurrent processes (separate windows command prompts) and saw no significant effect on the stats gathering time, which was less than 5 sec each and every time.</p></div><div id="comment-8656-info" class="comment-info"><span class="comment-age">(27 Jan '12, 13:44)</span> <span class="comment-user userinfo">adonies</span></div></div><span id="8665"></span><div id="comment-8665" class="comment"><div id="post-8665-score" class="comment-score"></div><div class="comment-text"><p>So: it sounds like the issue is not with tshark but with the the way it's being invoked in Java (or something) ??</p></div><div id="comment-8665-info" class="comment-info"><span class="comment-age">(28 Jan '12, 07:57)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-8638" class="comment-tools"></div><div class="clear"></div><div id="comment-8638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

