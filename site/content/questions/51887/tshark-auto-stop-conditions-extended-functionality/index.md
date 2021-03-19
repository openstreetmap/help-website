+++
type = "question"
title = "tshark auto stop conditions -- extended functionality?"
description = '''Is it possible to have Tshark auto stop capturing when a certain string is captured? I&#x27;ve read through the documentation but I didn&#x27;t see any options that would make this possible. Here&#x27;s what I&#x27;m using now: tshark.exe -a duration:15 -a filesize:2400 -i 5 -w c:&#92;dumps&#92;dump.dat -f &quot;tcp port 22557&quot; The...'''
date = "2016-04-22T20:55:00Z"
lastmod = "2016-04-23T13:02:00Z"
weight = 51887
keywords = [ "tshark", "autostop" ]
aliases = [ "/questions/51887" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark auto stop conditions -- extended functionality?](/questions/51887/tshark-auto-stop-conditions-extended-functionality)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51887-score" class="post-score" title="current number of votes">0</div><span id="post-51887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to have Tshark auto stop capturing when a certain string is captured? I've read through the documentation but I didn't see any options that would make this possible.</p><p>Here's what I'm using now:</p><p>tshark.exe -a duration:15 -a filesize:2400 -i 5 -w c:\dumps\dump.dat -f "tcp port 22557"</p><p>The -a options tell tshark to capture for 15 seconds or until the capture file reaches 2400KB.</p><p>Is there some other option that tells Tshark to stop capturing when a certain string is received?</p><p>like -{?} "stopcapturingwhenyouseethis"</p><p>Are there some other options I can use in conjunction with one another to achieve this sort of functionality?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-autostop" rel="tag" title="see questions tagged &#39;autostop&#39;">autostop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '16, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/fd0269c467a7c438032719409342e047?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eltzwabo&#39;s gravatar image" /><p><span>eltzwabo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eltzwabo has no accepted answers">0%</span></p></div></div><div id="comments-container-51887" class="comments-container"></div><div id="comment-tools-51887" class="comment-tools"></div><div class="clear"></div><div id="comment-51887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51888"></span>

<div id="answer-container-51888" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51888-score" class="post-score" title="current number of votes">2</div><span id="post-51888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="eltzwabo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>At the moment no stop condition is available directly. What you can do is to let dumpcap, rather than tshark, record the captures into ring-buffered files like you've already been doing, and use a regularly triggered or constantly running script to process each new file by tshark searching for your "stop condition" in it. The script then kills the dumpcap, and possibly sends you an e-mail or an snmp trap, when such a tshark run finds the stop condition in the file.</p><p>The best scripting language for MS Windows for this purpose is your favourite one, because the task is so simple that you'll waste least time on implementing it if you use a language you already know.</p><p>The reason why it makes more sense to use dumpcap than tshark to capture "until the lightning strikes" is described in <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/comment-page-1/#HowTo:%20dumpcap">this nice article</a> by <span>@Jasper</span>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '16, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51888" class="comments-container"><span id="51898"></span><div id="comment-51898" class="comment"><div id="post-51898-score" class="comment-score"></div><div class="comment-text"><p>This is not necessarily the case anymore. I tend to still use <code>dumpcap</code> myself for long-running captures, but at least in theory <code>tshark</code> should be as capable as <code>dumpcap</code> now, at least in terms of memory usage. See: <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a>.</p></div><div id="comment-51898-info" class="comment-info"><span class="comment-age">(23 Apr '16, 13:02)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-51888" class="comment-tools"></div><div class="clear"></div><div id="comment-51888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

