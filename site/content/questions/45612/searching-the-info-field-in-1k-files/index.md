+++
type = "question"
title = "Searching the Info Field in 1k files"
description = '''Hi guys, I got a problem with the info field. I need to search for log files which contain :&quot;Retransmission&quot; in the info field in about 1k logs. However, i already know that the frame doesnt contain the information &quot;Retransmission&quot;. Do you guys know any workaround to filter the log-files with the in...'''
date = "2015-09-03T02:20:00Z"
lastmod = "2015-09-04T01:03:00Z"
weight = 45612
keywords = [ "info", "tcp_retransmission", "searching" ]
aliases = [ "/questions/45612" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Searching the Info Field in 1k files](/questions/45612/searching-the-info-field-in-1k-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45612-score" class="post-score" title="current number of votes">0</div><span id="post-45612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I got a problem with the info field.</p><p>I need to search for log files which contain :"Retransmission" in the info field in about 1k logs.<br />
However, i already know that the frame doesnt contain the information "Retransmission".</p><p>Do you guys know any workaround to filter the log-files with the info field : [Retransmission] in any part of the logfile?</p><p>if you need any more information pls let me know.<br />
thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-tcp_retransmission" rel="tag" title="see questions tagged &#39;tcp_retransmission&#39;">tcp_retransmission</span> <span class="post-tag tag-link-searching" rel="tag" title="see questions tagged &#39;searching&#39;">searching</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '15, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/4782c252432cec34f4c297e008f800eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schmiddi&#39;s gravatar image" /><p><span>schmiddi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schmiddi has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-45612" class="comments-container"></div><div id="comment-tools-45612" class="comment-tools"></div><div class="clear"></div><div id="comment-45612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45617"></span>

<div id="answer-container-45617" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45617-score" class="post-score" title="current number of votes">1</div><span id="post-45617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nothing that can't be solved with a for loop :)</p><p><code>for file in *.pcap; do tshark -r $file -Y tcp.analysis.retransmission -w $file_ret.pcapng; done</code></code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '15, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Sep '15, 08:47</strong> </span></p></div></div><div id="comments-container-45617" class="comments-container"><span id="45627"></span><div id="comment-45627" class="comment"><div id="post-45627-score" class="comment-score"></div><div class="comment-text"><p>wow , thx! it worked.</p></div><div id="comment-45627-info" class="comment-info"><span class="comment-age">(04 Sep '15, 01:03)</span> <span class="comment-user userinfo">schmiddi</span></div></div></div><div id="comment-tools-45617" class="comment-tools"></div><div class="clear"></div><div id="comment-45617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

