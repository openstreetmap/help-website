+++
type = "question"
title = "Commandline Capture Filter for only GET Requests that contain &quot;.exe&quot; or &quot;.jar&quot;  ?"
description = '''Currently I am using tshark with the command below to capture only packets which contain a GET request. Problem is the capture file is still to big, and reducing capture time is locked in at 1 hour captures. Does anyone know how I could modify the command below to capture only GET requests that cont...'''
date = "2015-01-01T21:11:00Z"
lastmod = "2015-01-08T08:57:00Z"
weight = 38848
keywords = [ "filter", "capture", "command", "tshark", "get" ]
aliases = [ "/questions/38848" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Commandline Capture Filter for only GET Requests that contain ".exe" or ".jar" ?](/questions/38848/commandline-capture-filter-for-only-get-requests-that-contain-exe-or-jar)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38848-score" class="post-score" title="current number of votes">0</div><span id="post-38848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Currently I am using tshark with the command below to capture only packets which contain a GET request. Problem is the capture file is still to big, and reducing capture time is locked in at 1 hour captures. Does anyone know how I could modify the command below to capture only GET requests that contain ".exe" or ".jar" somewhere in them. Or if someones knows of another command-line capture utility which can do this please let me know, thanks.</p><pre><code>cd D:\Desktop\test &amp;&amp; tshark -f &quot;port 80 and tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420&quot; -i 3 -b duration:3600 -b files:1 -w testing.cap</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-command" rel="tag" title="see questions tagged &#39;command&#39;">command</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '15, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p><span>zer0day</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div></div><div id="comments-container-38848" class="comments-container"></div><div id="comment-tools-38848" class="comment-tools"></div><div class="clear"></div><div id="comment-38848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38856"></span>

<div id="answer-container-38856" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38856-score" class="post-score" title="current number of votes">1</div><span id="post-38856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zer0day has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, that would require looping over the packet contents, and the mechanism used for capture filtering doesn't support loops (the filters are, on most OSes, interpreted in the kernel, so strict limits are placed on what they can do, so that, for example, a program can't cause an infinite loop) and doesn't have a pattern-matching primitive, so that's not possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '15, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-38856" class="comments-container"><span id="38860"></span><div id="comment-38860" class="comment"><div id="post-38860-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the the thorough clarification, at least now I can stop beating that dead horse.</p></div><div id="comment-38860-info" class="comment-info"><span class="comment-age">(02 Jan '15, 18:25)</span> <span class="comment-user userinfo">zer0day</span></div></div></div><div id="comment-tools-38856" class="comment-tools"></div><div class="clear"></div><div id="comment-38856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38873"></span>

<div id="answer-container-38873" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38873-score" class="post-score" title="current number of votes">1</div><span id="post-38873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Or if someones knows of another command-line capture utility which can do this please let me know, thanks.</p></blockquote><p>Take a look at <a href="http://ngrep.sourceforge.net/">ngrep</a>.</p><p>See also my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/23824/how-to-filter-packets-while-capturing-them-using-tcpdump-on-linux-based-on-a-diameter-avp-value">https://ask.wireshark.org/questions/23824/how-to-filter-packets-while-capturing-them-using-tcpdump-on-linux-based-on-a-diameter-avp-value</a></p></blockquote><p>Please read the <a href="http://ngrep.sourceforge.net/usage.html">ngrep man page</a> for the filter syntax.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '15, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jan '15, 03:32</strong> </span></p></div></div><div id="comments-container-38873" class="comments-container"><span id="38932"></span><div id="comment-38932" class="comment"><div id="post-38932-score" class="comment-score"></div><div class="comment-text"><p>The machine used to capture is of the Windows 7 (x64) variety, sorry I should have stated that. And I'm looking to reduce capture size by only capturing packets that are GET requests containing ".exe" or ".jar". Filtering is no problem post capture as I convert the .cap to a text file then pull out what I need with a Powershell script, just filtering was taking over an hour cause an hourly capture is 2GB-3GB. It ended up that my above command from my first post turned out to be sufficient enough capturing only GET requests then filtering with Powershell. Thanks for the effort though.</p></div><div id="comment-38932-info" class="comment-info"><span class="comment-age">(07 Jan '15, 18:29)</span> <span class="comment-user userinfo">zer0day</span></div></div><span id="38949"></span><div id="comment-38949" class="comment"><div id="post-38949-score" class="comment-score"></div><div class="comment-text"><p>ngrep is available on Windows as well. Just google for it.</p></div><div id="comment-38949-info" class="comment-info"><span class="comment-age">(08 Jan '15, 05:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="38961"></span><div id="comment-38961" class="comment"><div id="post-38961-score" class="comment-score"></div><div class="comment-text"><p>From the downloads page, "Windows 95, 98, NT, 2000, XP, 2003 x86 "</p></div><div id="comment-38961-info" class="comment-info"><span class="comment-age">(08 Jan '15, 07:22)</span> <span class="comment-user userinfo">zer0day</span></div></div><span id="38963"></span><div id="comment-38963" class="comment"><div id="post-38963-score" class="comment-score"></div><div class="comment-text"><p>Only because ngrep hasn't been updated since 2006, i.e. pre-Vista so the page hasn't been updated. Try it, I'd guess it will work on Win 7.</p></div><div id="comment-38963-info" class="comment-info"><span class="comment-age">(08 Jan '15, 08:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38966"></span><div id="comment-38966" class="comment"><div id="post-38966-score" class="comment-score">1</div><div class="comment-text"><p>It works on Win7 64Bit!</p><blockquote><p>ngrep -L<br />
ngrep -d 4 -s 0 -O http.pcap "GET /"</p></blockquote><p>See the man page for more options!</p></div><div id="comment-38966-info" class="comment-info"><span class="comment-age">(08 Jan '15, 08:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-38873" class="comment-tools"></div><div class="clear"></div><div id="comment-38873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

