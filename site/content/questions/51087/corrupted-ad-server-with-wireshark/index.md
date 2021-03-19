+++
type = "question"
title = "Corrupted AD server with Wireshark?"
description = '''Hi! I have runned Wireshark on our AD server as a background porcess in the last couple weeks with writing logs to files. A external IT manager warned me about this and said it&#x27;s danguraus because it can currupt our AD database or something like that. Is it not recommanded to run Wireshark over a lo...'''
date = "2016-03-22T06:48:00Z"
lastmod = "2016-03-22T10:13:00Z"
weight = 51087
keywords = [ "ad", "server" ]
aliases = [ "/questions/51087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Corrupted AD server with Wireshark?](/questions/51087/corrupted-ad-server-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51087-score" class="post-score" title="current number of votes">0</div><span id="post-51087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I have runned Wireshark on our AD server as a background porcess in the last couple weeks with writing logs to files. A external IT manager warned me about this and said it's danguraus because it can currupt our AD database or something like that.<br />
Is it not recommanded to run Wireshark over a longer period on AD server?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ad" rel="tag" title="see questions tagged &#39;ad&#39;">ad</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '16, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/93737ed46d1c9813687bb8d134024254?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jovial&#39;s gravatar image" /><p><span>Jovial</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jovial has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '16, 07:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-51087" class="comments-container"></div><div id="comment-tools-51087" class="comment-tools"></div><div class="clear"></div><div id="comment-51087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51089"></span>

<div id="answer-container-51089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51089-score" class="post-score" title="current number of votes">1</div><span id="post-51089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark itself is unlikely (impossible really) to corrupt the AD database, however it would be possible for Wireshark to fill a disk with capture files, leading other software to misbehave.</p><p>Apart from that Wireshark should not be used for long term captures, it will run out of memory, which may also cause other software to misbehave.</p><p>See the Wiki page on <a href="https://wiki.wireshark.org/KnownBugs/OutOfMemory">Out Of Memory</a> and numerous questions about it on this Q&amp;A site. For long term captures use dumpcap and ring buffers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '16, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51089" class="comments-container"><span id="51090"></span><div id="comment-51090" class="comment"><div id="post-51090-score" class="comment-score"></div><div class="comment-text"><p>Thank you for clearing it up for me! Wireshark normally use around 300mb ram because of the GUI of wireshark logs have been disabled. And HDD is set to overwrite old files with saving last 30GB of logs. Gues i'm in the clear to continue to run Wireshark than! :)</p><p>The reason why I run wireshark over a long period like this is because I use it to troubleshot virus activities in our network. (Get alerts from firewall with no information to find the source) Please let me know if you have other suggestion on software that might be more suited for this kind of operations :) Thanks!</p></div><div id="comment-51090-info" class="comment-info"><span class="comment-age">(22 Mar '16, 07:18)</span> <span class="comment-user userinfo">Jovial</span></div></div><span id="51099"></span><div id="comment-51099" class="comment"><div id="post-51099-score" class="comment-score"></div><div class="comment-text"><blockquote>the GUI of wireshark logs have been disabled</blockquote><p>I'm not sure what you mean here. If running the wireshark executable, the issue isn't the GUI, it's the retained state of requests and responses. tshark retains much the same sate (as it uses the same dissection engine) so isn't the answer either for long duration running.</p><p>There is no definitive answer either on how much traffic consumes how much memory, as it depends on the traffic capture itself.</p></div><div id="comment-51099-info" class="comment-info"><span class="comment-age">(22 Mar '16, 10:13)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-51089" class="comment-tools"></div><div class="clear"></div><div id="comment-51089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

