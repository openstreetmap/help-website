+++
type = "question"
title = "how to capture traffic for a specific program?"
description = '''If I suspect a certain program or programs is a keylogger, can i capture just packets coming going in and out of that program? or possibly slect multiple programs and capture only data coming to/from them? I don&#x27;t know if it&#x27;s possible for programs to pass use your browser to transfer data, is it po...'''
date = "2011-04-26T12:02:00Z"
lastmod = "2015-01-14T20:42:00Z"
weight = 3725
keywords = [ "browser", "programs" ]
aliases = [ "/questions/3725" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture traffic for a specific program?](/questions/3725/how-to-capture-traffic-for-a-specific-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3725-score" class="post-score" title="current number of votes">2</div><span id="post-3725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I suspect a certain program or programs is a keylogger, can i capture just packets coming going in and out of that program? or possibly slect multiple programs and capture only data coming to/from them?</p><p>I don't know if it's possible for programs to pass use your browser to transfer data, is it possible? so maybe it won't help much but I'd like to get some info on that</p><p>Thanx in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-browser" rel="tag" title="see questions tagged &#39;browser&#39;">browser</span> <span class="post-tag tag-link-programs" rel="tag" title="see questions tagged &#39;programs&#39;">programs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '11, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/8a6d18f5a4b2cd3dade46658caf6d4f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fiftyeight&#39;s gravatar image" /><p><span>fiftyeight</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fiftyeight has no accepted answers">0%</span></p></div></div><div id="comments-container-3725" class="comments-container"></div><div id="comment-tools-3725" class="comment-tools"></div><div class="clear"></div><div id="comment-3725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3734"></span>

<div id="answer-container-3734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3734-score" class="post-score" title="current number of votes">3</div><span id="post-3734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might be able to achieve close to what you want by first using something like <a href="http://en.wikipedia.org/wiki/Netstat"><code>netstat</code></a> to find the source and destination IP:port pairs that the program of interest is using. On Windows (with cygwin installed for grep), the following should produce some useful output:</p><pre><code>netstat -bn | grep -B 1 &lt;program&gt;</code></pre><p>... where <code>&lt;program&gt;</code> should be substituted for the actual program name of interest.</p><p>Keep in mind though that <code>netstat</code> will only give you a snapshot of connections at the time the command was run.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '11, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3734" class="comments-container"><span id="34398"></span><div id="comment-34398" class="comment"><div id="post-34398-score" class="comment-score"></div><div class="comment-text"><p>On Ubuntu/Linux, that was <code>sudo netstat -n --program|grep &lt;program&gt;</code> for me.</p></div><div id="comment-34398-info" class="comment-info"><span class="comment-age">(04 Jul '14, 01:35)</span> <span class="comment-user userinfo">Vics</span></div></div></div><div id="comment-tools-3734" class="comment-tools"></div><div class="clear"></div><div id="comment-3734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3738"></span>

<div id="answer-container-3738" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3738-score" class="post-score" title="current number of votes">1</div><span id="post-3738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On windows you can use <a href="http://www.microsoft.com/downloads/en/details.aspx?FamilyID=983b941d-06cb-4658-b7f6-3088333d062f">Netmon</a> which can categorize traffic by application.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '11, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3738" class="comments-container"><span id="3743"></span><div id="comment-3743" class="comment"><div id="post-3743-score" class="comment-score"></div><div class="comment-text"><p>It indeed shows the processes and seems like a good program, the problem is it doesn't show the process' path, is there a way to do it?</p></div><div id="comment-3743-info" class="comment-info"><span class="comment-age">(27 Apr '11, 07:28)</span> <span class="comment-user userinfo">fiftyeight</span></div></div><span id="3744"></span><div id="comment-3744" class="comment"><div id="post-3744-score" class="comment-score">1</div><div class="comment-text"><p>Good point Sake. And that reminds me - there is a bug filed in Wireshark's bugzilla, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1184">bug 1184</a>, to add this capability to Wireshark. Gerald did some early work on this way back in 2001, but it hasn't received any TLC since then.</p></div><div id="comment-3744-info" class="comment-info"><span class="comment-age">(27 Apr '11, 07:30)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="3746"></span><div id="comment-3746" class="comment"><div id="post-3746-score" class="comment-score"></div><div class="comment-text"><p>@fiftyeight, I haven't used netmon in a long time, so I don't know if it can provide the process' path or not, but in a pinch, maybe something like <code>netstat -bnv</code> will help you?</p></div><div id="comment-3746-info" class="comment-info"><span class="comment-age">(27 Apr '11, 07:53)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="3747"></span><div id="comment-3747" class="comment"><div id="post-3747-score" class="comment-score"></div><div class="comment-text"><p>Well, I don't think you can show the full path in netmon itself, but next to the executable name, there is the process ID in parentices. If you add the columns "PID" and "Image Path Name" to your Task Manager Processes list, you're all set to look up the path of the executable.</p></div><div id="comment-3747-info" class="comment-info"><span class="comment-age">(27 Apr '11, 08:18)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="3748"></span><div id="comment-3748" class="comment"><div id="post-3748-score" class="comment-score">1</div><div class="comment-text"><p>You might also try using <a href="http://technet.microsoft.com/en-us/sysinternals/bb896653">Process Explorer</a> in addition to or instead of Task Manager. There's also <a href="http://technet.microsoft.com/en-us/sysinternals/bb896645">Process Monitor</a>.</p></div><div id="comment-3748-info" class="comment-info"><span class="comment-age">(27 Apr '11, 08:31)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="3759"></span><div id="comment-3759" class="comment not_top_scorer"><div id="post-3759-score" class="comment-score"></div><div class="comment-text"><p>guess a combination of all these can do the job, but for some reason netstat, and also TCPView and CurrPorts which I have tried list some processes as unknown and I don't really understand why, guess I'll need to do some more research,</p><p>I also found a program called SocketSniff that seems to monitor the data coming out of a specific process</p><p>the answers here have been gr8, thanks a lot!</p></div><div id="comment-3759-info" class="comment-info"><span class="comment-age">(27 Apr '11, 12:39)</span> <span class="comment-user userinfo">fiftyeight</span></div></div><span id="39138"></span><div id="comment-39138" class="comment not_top_scorer"><div id="post-39138-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@cmaynard</span> repeated your answer here. <a href="http://askubuntu.com/a/573943/368900">http://askubuntu.com/a/573943/368900</a></p></div><div id="comment-39138-info" class="comment-info"><span class="comment-age">(14 Jan '15, 20:42)</span> <span class="comment-user userinfo">jtmoon1979</span></div></div></div><div id="comment-tools-3738" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-3738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

