+++
type = "question"
title = "Is there a way to add a comment to packets in command line?"
description = '''I was reading this wireshark user guide and found that you can add comments to a pcapng capture file, but so far I haven&#x27;t been able to do it, I tried everything but nothing seems to work, can someone explain me how to do it? bash $ tshark -r e.pcapng -comment hey tshark: The specified packet count ...'''
date = "2015-04-30T07:45:00Z"
lastmod = "2015-04-30T10:03:00Z"
weight = 41974
keywords = [ "comment", "tshark", "packet", "command-line" ]
aliases = [ "/questions/41974" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to add a comment to packets in command line?](/questions/41974/is-there-a-way-to-add-a-comment-to-packets-in-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41974-score" class="post-score" title="current number of votes">0</div><span id="post-41974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I was reading this wireshark <a href="https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html">user guide</a> and found that you can add comments to a pcapng capture file, but so far I haven't been able to do it, I tried everything but nothing seems to work, can someone explain me how to do it?</p><p><strong>bash $</strong> tshark -r e.pcapng -comment hey</p><p>tshark: The specified packet count "omment" isn't a decimal number</p><hr /><p>This is the part of the page that shows that it is possible:</p><p><strong>capture-comment</strong> &lt;<em>comment</em>&gt;</p><p><strong>add a capture comment to the newly created</strong></p><p><strong>output file (only for pcapng)</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-comment" rel="tag" title="see questions tagged &#39;comment&#39;">comment</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '15, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/ef71a3d5b055d8b0c017bfd462acf573?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pier&#39;s gravatar image" /><p><span>pier</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pier has no accepted answers">0%</span></p></div></div><div id="comments-container-41974" class="comments-container"></div><div id="comment-tools-41974" class="comment-tools"></div><div class="clear"></div><div id="comment-41974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41976"></span>

<div id="answer-container-41976" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41976-score" class="post-score" title="current number of votes">0</div><span id="post-41976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pier has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you cannot add comments to existing files. I just tried, and this is what happenend:</p><pre><code>[D:\Traces]tshark -r &quot;HTTP Sample Test.pcapng&quot; --capture-comment &quot;Test for Q&amp;A&quot; -w &quot;HTTP Sample Test commented.pcapng&quot;
tshark: A capture comment was specified, but a capture isn&#39;t being done.
There&#39;s no support for adding a capture comment to an existing capture file.

[D:\Traces]</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '15, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '15, 07:54</strong> </span></p></div></div><div id="comments-container-41976" class="comments-container"><span id="41977"></span><div id="comment-41977" class="comment"><div id="post-41977-score" class="comment-score"></div><div class="comment-text"><p>I tried capturing a new file but still nothing, I'm using a raspberry pi by the way with raspbian (linux) so I don't know if I don't have that option =P</p><blockquote><p><strong>bash$</strong> sudo tshark -c 3 -i wlan0 --capture-comment "Test for Q&amp;A" -w e.pcapng</p><p>tshark: invalid option -- '-'</p><p>TShark 1.8.2</p><p>Dump and analyze network traffic.</p></blockquote></div><div id="comment-41977-info" class="comment-info"><span class="comment-age">(30 Apr '15, 08:05)</span> <span class="comment-user userinfo">pier</span></div></div><span id="41979"></span><div id="comment-41979" class="comment"><div id="post-41979-score" class="comment-score"></div><div class="comment-text"><p>This works on Windows with 1.12.4</p></div><div id="comment-41979-info" class="comment-info"><span class="comment-age">(30 Apr '15, 08:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41981"></span><div id="comment-41981" class="comment"><div id="post-41981-score" class="comment-score"></div><div class="comment-text"><p>yeah, I just checked the man page and it seems that that option is not available for linux distributions, at least not mine =P</p></div><div id="comment-41981-info" class="comment-info"><span class="comment-age">(30 Apr '15, 09:06)</span> <span class="comment-user userinfo">pier</span></div></div><span id="41985"></span><div id="comment-41985" class="comment"><div id="post-41985-score" class="comment-score">1</div><div class="comment-text"><p>You'll need a more up to date version. If .deb based you can try the <a href="https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable">wireshark-dev ppa</a>.</p></div><div id="comment-41985-info" class="comment-info"><span class="comment-age">(30 Apr '15, 10:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41976" class="comment-tools"></div><div class="clear"></div><div id="comment-41976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41978"></span>

<div id="answer-container-41978" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41978-score" class="post-score" title="current number of votes">0</div><span id="post-41978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>although not on the command line, you can do it in Wireshark</p><blockquote><p>Statistics -&gt; Summary -&gt; Capture File Comments</p></blockquote><p>If you save the file, the comments will be added to the pcapgng file.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '15, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Apr '15, 08:10</strong> </span></p></div></div><div id="comments-container-41978" class="comments-container"></div><div id="comment-tools-41978" class="comment-tools"></div><div class="clear"></div><div id="comment-41978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

