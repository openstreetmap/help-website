+++
type = "question"
title = "Command line capture filter syntax"
description = '''I want to start wireshark from the command line using a capture filter so that when wireshark starts it begins capturing immediately and is only capturing packets that I am interested in. I thought the -f would be the ticket but I am not sure what is going on here? It seems to be thinking that -f is...'''
date = "2011-10-26T08:33:00Z"
lastmod = "2011-10-26T09:56:00Z"
weight = 7083
keywords = [ "capture-filter", "command-line", "wireshark" ]
aliases = [ "/questions/7083" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Command line capture filter syntax](/questions/7083/command-line-capture-filter-syntax)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7083-score" class="post-score" title="current number of votes">0</div><span id="post-7083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to start wireshark from the command line using a capture filter so that when wireshark starts it begins capturing immediately and is only capturing packets that I am interested in. I thought the -f would be the ticket but I am not sure what is going on here? It seems to be thinking that -f is a capture file? Thanks</p><pre><code>C:\Program Files\Wireshark&gt;wireshark -i 2 -k -f tcp port==443

C:\Program Files\Wireshark&gt;

wireshark: You can&#39;t specify both a live capture and a capture file to be read.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '11, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/e27efc5db7208bd0813baa5f1f2381ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grunt&#39;s gravatar image" /><p><span>Grunt</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grunt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '11, 09:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-7083" class="comments-container"></div><div id="comment-tools-7083" class="comment-tools"></div><div class="clear"></div><div id="comment-7083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7085"></span>

<div id="answer-container-7085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7085-score" class="post-score" title="current number of votes">1</div><span id="post-7085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have a quoting issue and a syntax issue. As the capture filter includes spaces you must quote it, and to filter on tcp port 443, the capture filter would be <code>tcp port 443</code>. Your command line then becomes:</p><p><code>wireshark -i 2 -k -f "tcp port 443"</code></p><p>If you are just capturing for later analysis then you may want to look into dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '11, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-7085" class="comments-container"></div><div id="comment-tools-7085" class="comment-tools"></div><div class="clear"></div><div id="comment-7085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

