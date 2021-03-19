+++
type = "question"
title = "Can Wireshark monitor bandwidth usage per application/process?"
description = '''I&#x27;m using Ubuntu 10.04 and I want to monitor and ideally log how much each application/process is uploading and downloading. Something like: Firefox has downloaded 50MB, Transmission has downloaded 500MB and uploaded 300MB, Ubuntu One has uploaded 5MB, etc. A per-session record would do, but actuall...'''
date = "2010-09-15T05:27:00Z"
lastmod = "2012-06-19T08:05:00Z"
weight = 82
keywords = [ "traffic", "monitoring", "log", "ubuntu" ]
aliases = [ "/questions/82" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark monitor bandwidth usage per application/process?](/questions/82/can-wireshark-monitor-bandwidth-usage-per-applicationprocess)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-82-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-82-score" class="post-score" title="current number of votes">0</div><span id="post-82-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using Ubuntu 10.04 and I want to monitor and ideally log how much each application/process is uploading and downloading. Something like: Firefox has downloaded 50MB, Transmission has downloaded 500MB and uploaded 300MB, Ubuntu One has uploaded 5MB, etc. A per-session record would do, but actually logging usage to a database/text file would be best.</p><p>Can Wireshark do this? (And on Windows?)</p><p>Suggestions for alternate tools that do exactly this also welcome :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '10, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/7a3a6b56c78ce76bf8293ba227e76ee6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d3vid&#39;s gravatar image" /><p><span>d3vid</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="d3vid has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '10, 15:02</strong> </span></p></div></div><div id="comments-container-82" class="comments-container"></div><div id="comment-tools-82" class="comment-tools"></div><div class="clear"></div><div id="comment-82-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="83"></span>

<div id="answer-container-83" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-83-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-83-score" class="post-score" title="current number of votes">0</div><span id="post-83-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can see this information in Wireshark by clicking on "Statistics" -&gt; "Conversations".<br />
</p><p>To see traffic between:</p><ul><li>Two specific hosts look at the "IPv4" or "IPv6" tab.</li><li>A specific session between two hosts the "TCP" tab.</li></ul><p>For all data for a specific host, look at "Statistics" -&gt; "End Points" then look at the tabs as above.</p><p>Wireshark may not be the best solution for long term trending of this information however. You may want to look at something like <a href="http://www.ntop.org/overview.html">NTop</a> or <a href="http://bandwidthd.sourceforge.net/">BandwidthD</a> which may be a better solution. Article with more options here: <a href="http://www.ubuntugeek.com/bandwidth-monitoring-tools-for-linux.html">http://www.ubuntugeek.com/bandwidth-monitoring-tools-for-linux.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/1d8eda08758411bec29092a0b8220126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter&#39;s gravatar image" /><p><span>Peter</span><br />
<span class="score" title="65 reputation points">65</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-83" class="comments-container"><span id="116"></span><div id="comment-116" class="comment"><div id="post-116-score" class="comment-score"></div><div class="comment-text"><p>Hmmm, I can pick out particular IP addresses and ports that I know, but not actual applications (e.g. is an HTTP conversation running from Firefox or from Chrome?). Am I missing something? Looking into those other options too, thanks Peter!</p></div><div id="comment-116-info" class="comment-info"><span class="comment-age">(15 Sep '10, 15:00)</span> <span class="comment-user userinfo">d3vid</span></div></div><span id="117"></span><div id="comment-117" class="comment"><div id="post-117-score" class="comment-score"></div><div class="comment-text"><p>You would have to get the browser version from the 'agent' field in the http packets. Your web server should be able to give you those stats.</p></div><div id="comment-117-info" class="comment-info"><span class="comment-age">(15 Sep '10, 15:05)</span> <span class="comment-user userinfo">Peter</span></div></div><span id="123"></span><div id="comment-123" class="comment"><div id="post-123-score" class="comment-score"></div><div class="comment-text"><p>Excellent, that solves it for browsers and anything else sending HTTP packets. I guess for other protocols it'll be on a case by case basis.</p><p>I've added an answer with tools I've found that address the application/process issue in a more general way.</p></div><div id="comment-123-info" class="comment-info"><span class="comment-age">(15 Sep '10, 15:54)</span> <span class="comment-user userinfo">d3vid</span></div></div></div><div id="comment-tools-83" class="comment-tools"></div><div class="clear"></div><div id="comment-83-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="122"></span>

<div id="answer-container-122" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-122-score" class="post-score" title="current number of votes">0</div><span id="post-122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like one alternative might be NetHogs. Old, Linux-only, shows current traffic not totals, but small, easy to run and does show per-process stats directly. http://nethogs.sourceforge.net/</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/7a3a6b56c78ce76bf8293ba227e76ee6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="d3vid&#39;s gravatar image" /><p><span>d3vid</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="d3vid has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '10, 15:55</strong> </span></p></div></div><div id="comments-container-122" class="comments-container"><span id="12041"></span><div id="comment-12041" class="comment"><div id="post-12041-score" class="comment-score"></div><div class="comment-text"><p>You might want to follow <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1184">bug 1184</a>. If it's ever implemented, then this could become possible in Wireshark.</p></div><div id="comment-12041-info" class="comment-info"><span class="comment-age">(18 Jun '12, 21:10)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="12043"></span><div id="comment-12043" class="comment"><div id="post-12043-score" class="comment-score"></div><div class="comment-text"><p><span>@cmaynard</span>: regarding your comments to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1184">bug 1184</a>:</p><p>would it be acceptable (according to the design principles):</p><ul><li>to have a separate process to retrieve the PID of a process for every new conversation, where at least one ip address is configured on the local system? This may be necessary due to privilege separation. Communication with that process through IPC.</li><li>that this feature is NOT implemented on every platform. In general: is it required to implement a wireshark feature on EVERY platform. How does a developer handle that, without access to a certain target platform?</li><li>to extend dumpcap to have this functionality</li></ul><p>Regards<br />
Kurt</p></div><div id="comment-12043-info" class="comment-info"><span class="comment-age">(18 Jun '12, 23:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12057"></span><div id="comment-12057" class="comment"><div id="post-12057-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt</span>, I haven't thought about how this might be implemented at all, so I'm not in a position to provide a meaningful answer here, but if you have some ideas, then perhaps mentioning them in the bug report would be more appropriate, as anyone interested in this who might be following it might have more feedback to offer than myself.</p><p>Regarding any requirement that it be implemented on EVERY platform ... I think it <a href="http://tools.ietf.org/html/rfc2119"><code>SHOULD</code></a> be implemented on every platform, but at least initially, I don't think it <a href="http://tools.ietf.org/html/rfc2119"><code>MUST</code></a> be implemented on every platform.</p></div><div id="comment-12057-info" class="comment-info"><span class="comment-age">(19 Jun '12, 07:55)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="12058"></span><div id="comment-12058" class="comment"><div id="post-12058-score" class="comment-score"></div><div class="comment-text"><p>O.K. I'll update the bug.</p></div><div id="comment-12058-info" class="comment-info"><span class="comment-age">(19 Jun '12, 08:05)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-122" class="comment-tools"></div><div class="clear"></div><div id="comment-122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

