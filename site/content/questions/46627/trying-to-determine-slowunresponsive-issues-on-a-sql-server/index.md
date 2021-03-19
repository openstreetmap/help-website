+++
type = "question"
title = "Trying to determine slow/unresponsive issues on a SQL server"
description = '''Greetings, I work for a medium sized healthcare institute of about 700 employees. We run an EMR (Electronic Medical Records) system that is responsible for just about everything we do. It consists of two servers, one 2008 R2 Application Server and one 2008 R2 MS SQL Server. For a good while now we h...'''
date = "2015-10-16T11:48:00Z"
lastmod = "2015-10-19T12:46:00Z"
weight = 46627
keywords = [ "newbie", "zero-window", "help" ]
aliases = [ "/questions/46627" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to determine slow/unresponsive issues on a SQL server](/questions/46627/trying-to-determine-slowunresponsive-issues-on-a-sql-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46627-score" class="post-score" title="current number of votes">0</div><span id="post-46627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>I work for a medium sized healthcare institute of about 700 employees. We run an EMR (Electronic Medical Records) system that is responsible for just about everything we do. It consists of two servers, one 2008 R2 Application Server and one 2008 R2 MS SQL Server. For a good while now we have had several complaints of random slowness or lockups within the application which results in angry physicians and nurses and ultimately slows down the company as a whole by increasing visit times due to a slow system.</p><p>To the end use this issue looks like a drop in network connectivity but I have been able to debunk this by checking switch logs, event viewer logs, and other various traps and monitors I have setup throughout the network. The servers themselves appear to be generally OK but that is not exactly my area. But working with the systems administrators we feel that the issue is more or less with our SQL server.</p><p>I used Wireshark to take a capture of the traffic going across it but I'm really not well versed in Wireshark enough to understand fully what I am looking at. One thing does stand out is a bunch of the following...</p><p><img src="http://i21.photobucket.com/albums/b274/Zimeroski/errors_zps2warxn2h.png" alt="alt text" /></p><p>The destination 10.30.10.10 being our SQL database server and the source 192.168.75.4 is one of our terminal servers. I've researched a little on TCP zerowindow but I don't fully understand it or how to go about resolving it.</p><p>I would appreciate any help anyone could give. Thank you,</p><p>-Adam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-zero-window" rel="tag" title="see questions tagged &#39;zero-window&#39;">zero-window</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '15, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/597ecb386aab75e701309843a09689d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Adam%20Barnett&#39;s gravatar image" /><p><span>Adam Barnett</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Adam Barnett has no accepted answers">0%</span></p></img></div></div><div id="comments-container-46627" class="comments-container"><span id="46628"></span><div id="comment-46628" class="comment"><div id="post-46628-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace?</p></div><div id="comment-46628-info" class="comment-info"><span class="comment-age">(16 Oct '15, 11:54)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46636"></span><div id="comment-46636" class="comment"><div id="post-46636-score" class="comment-score"></div><div class="comment-text"><p>Here is an example of what I see.</p><p><a href="https://www.cloudshark.org/captures/18b46be08aac">https://www.cloudshark.org/captures/18b46be08aac</a></p></div><div id="comment-46636-info" class="comment-info"><span class="comment-age">(16 Oct '15, 14:23)</span> <span class="comment-user userinfo">Adam Barnett</span></div></div><span id="46637"></span><div id="comment-46637" class="comment"><div id="post-46637-score" class="comment-score"></div><div class="comment-text"><p>That are really large segments above 50k and greater (TCP Offload enabled). I don´t think that is the cause of your prob, but it makes it even harder to say something reliable.</p><p>From my point of view it would be better to take a trace at the 10.30.19.113. Because there is the prob and you can hopefully (RSC disbaled) see the segemnts like they are on the wire...</p></div><div id="comment-46637-info" class="comment-info"><span class="comment-age">(16 Oct '15, 15:13)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-46627" class="comment-tools"></div><div class="clear"></div><div id="comment-46627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46638"></span>

<div id="answer-container-46638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46638-score" class="post-score" title="current number of votes">2</div><span id="post-46638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your terminal server is not offering TCP window scaling therefore the offered TCP window-size cannot exceed 64k.<br />
So for starters you need to enable RCF1323 (should be automatically enabled with auto-tuning in windows.<br />
<a href="http://www.speedguide.net/articles/windows-7-vista-2008-tweaks-2574">TCP 1323 Options from</a> <a href="http://www.speedguide.net">http://www.speedguide.net</a></p><pre><code>HKEY LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters Tcp1323Opts=1

(DWORD, entry created automatically by Windows when you run the &quot;netsh int tcp set global autotuninglvl=...&quot; command, set to 0 by default).</code></pre><p>Setting this seems to have no effect, since auto-tuning uses the TCP 1323 scale factor and changes it on the fly, disregarding this setting. Additional testing may be required to determine it's effect if auto-tuning is turned off. Setting it to 1 is best for broadband connections.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_014.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-46638" class="comments-container"><span id="46639"></span><div id="comment-46639" class="comment"><div id="post-46639-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@mrEEde</span>: Do you have another nice link about this auto tuning behavior?</p></div><div id="comment-46639-info" class="comment-info"><span class="comment-age">(16 Oct '15, 23:54)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46692"></span><div id="comment-46692" class="comment"><div id="post-46692-score" class="comment-score"></div><div class="comment-text"><p>This is one of the outputs from the terminal server.</p><p>[1]: <a href="http://s21.photobucket.com/user/Zimeroski/media/2015-10-19_8-05-58_zpskernl5ml.png.html"><img src="http://i21.photobucket.com/albums/b274/Zimeroski/2015-10-19_8-05-58_zpskernl5ml.png" alt=" photo 2015-10-19_8-05-58_zpskernl5ml.png" /></a></p></div><div id="comment-46692-info" class="comment-info"><span class="comment-age">(19 Oct '15, 06:09)</span> <span class="comment-user userinfo">Adam Barnett</span></div></div><span id="46700"></span><div id="comment-46700" class="comment"><div id="post-46700-score" class="comment-score"></div><div class="comment-text"><p>So I'd say you need to enable Auto-Tuning. <a href="https://support.microsoft.com/en-us/kb/947239">https://support.microsoft.com/en-us/kb/947239</a></p></div><div id="comment-46700-info" class="comment-info"><span class="comment-age">(19 Oct '15, 09:28)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="46708"></span><div id="comment-46708" class="comment"><div id="post-46708-score" class="comment-score"></div><div class="comment-text"><p>Receive Window Auto-Tuning is set to normal on the SQL server and disabled on the terminal servers.</p><p>I will run this by the server folks first before I set it.</p></div><div id="comment-46708-info" class="comment-info"><span class="comment-age">(19 Oct '15, 12:46)</span> <span class="comment-user userinfo">Adam Barnett</span></div></div></div><div id="comment-tools-46638" class="comment-tools"></div><div class="clear"></div><div id="comment-46638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

