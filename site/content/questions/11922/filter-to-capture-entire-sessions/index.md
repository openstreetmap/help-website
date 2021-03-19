+++
type = "question"
title = "filter to capture entire sessions"
description = '''I have a application talking to a database using persistent sessions. From time to time new sessions are initiated and I want to capture only those ones. I could wait hours before seeing a new session, so I&#x27;m looking for a capture filter that will allow only interesting traffic to be saved on disk. ...'''
date = "2012-06-15T01:51:00Z"
lastmod = "2012-06-15T04:41:00Z"
weight = 11922
keywords = [ "session", "syn", "linux" ]
aliases = [ "/questions/11922" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [filter to capture entire sessions](/questions/11922/filter-to-capture-entire-sessions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11922-score" class="post-score" title="current number of votes">0</div><span id="post-11922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a application talking to a database using persistent sessions. From time to time new sessions are initiated and I want to capture only those ones. I could wait hours before seeing a new session, so I'm looking for a <strong>capture</strong> filter that will allow only interesting traffic to be saved on disk. Please point me to any linux command line tool and filter syntax I could use. Thanks in advance !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '12, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/8dd726762a46ec4db30f74d9a9936471?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gab&#39;s gravatar image" /><p><span>Gab</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gab has no accepted answers">0%</span></p></div></div><div id="comments-container-11922" class="comments-container"><span id="11923"></span><div id="comment-11923" class="comment"><div id="post-11923-score" class="comment-score"></div><div class="comment-text"><p>I forgot to tell output must be in pcap format.</p></div><div id="comment-11923-info" class="comment-info"><span class="comment-age">(15 Jun '12, 01:55)</span> <span class="comment-user userinfo">Gab</span></div></div></div><div id="comment-tools-11922" class="comment-tools"></div><div class="clear"></div><div id="comment-11922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11924"></span>

<div id="answer-container-11924" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11924-score" class="post-score" title="current number of votes">1</div><span id="post-11924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gab has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One option would be to filter out all ports that are already in use by the established connections:</p><ul><li><code>netstat -na | grep xxxx</code> where xxxx is your DB port</li><li>Look for all source ports used</li><li>Use this capture filter: <code>'port xxxx and not port 1111 and not port 2222 and not port 3333'</code>, where xxxx is the port your DB application is listening and 1111,2222,3333 are the (source) ports of the established connections. Combine the filter with IP addresses if necessary.</li></ul><blockquote><p>I forgot to tell output must be in pcap format.</p></blockquote><p>use option <code>-w</code> to write the file in pcap format. See man page.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '12, 02:15</strong> </span></p></div></div><div id="comments-container-11924" class="comments-container"><span id="11925"></span><div id="comment-11925" class="comment"><div id="post-11925-score" class="comment-score"></div><div class="comment-text"><p>I'm sniffing on a 3rd device connected to a network tap between client and server. This is the linux box I can run stuff onto. I don't have access to client nor server.</p></div><div id="comment-11925-info" class="comment-info"><span class="comment-age">(15 Jun '12, 03:29)</span> <span class="comment-user userinfo">Gab</span></div></div><span id="11926"></span><div id="comment-11926" class="comment"><div id="post-11926-score" class="comment-score"></div><div class="comment-text"><p>well, then netstat is not an option. Why do you need only new sessions?</p></div><div id="comment-11926-info" class="comment-info"><span class="comment-age">(15 Jun '12, 04:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11927"></span><div id="comment-11927" class="comment"><div id="post-11927-score" class="comment-score"></div><div class="comment-text"><p>Kurt, anyway that is a very good idea: the linux box runs a proprietary software tracking sessions. Such software keeps a table of inspected sessions and I can do the trick from there. Let's wait for other (simpler) alternatives, but I got a good starting point :)</p></div><div id="comment-11927-info" class="comment-info"><span class="comment-age">(15 Jun '12, 04:29)</span> <span class="comment-user userinfo">Gab</span></div></div><span id="11928"></span><div id="comment-11928" class="comment"><div id="post-11928-score" class="comment-score"></div><div class="comment-text"><p>O.K. you can do the "trick" with wireshark as well. Run wireshark with a filter on the DB port. Wait a few seconds/minutes and extract all source ports. Use that list to filter out all those ports in another wireshark session, as shown above.</p><p>BTW: What kind of proprietary session tracking software do you run on that linux box?</p></div><div id="comment-11928-info" class="comment-info"><span class="comment-age">(15 Jun '12, 04:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11924" class="comment-tools"></div><div class="clear"></div><div id="comment-11924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

