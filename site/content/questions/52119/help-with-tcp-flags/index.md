+++
type = "question"
title = "help with tcp flags"
description = '''Hello, I&#x27;m learning how to use Wireshark and I need some help with my homework. I have to run wireshark on a file and filter on tcp traffic with both the S and F flags set (as well as any others).   I&#x27;m using the filter: tcp.flags but I&#x27;m not sure if this is correct. Help please.'''
date = "2016-05-01T01:16:00Z"
lastmod = "2016-05-01T04:15:00Z"
weight = 52119
keywords = [ "flags", "tcp" ]
aliases = [ "/questions/52119" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [help with tcp flags](/questions/52119/help-with-tcp-flags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52119-score" class="post-score" title="current number of votes">0</div><span id="post-52119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm learning how to use Wireshark and I need some help with my homework. I have to run wireshark on a file and filter on tcp traffic with both the S and F flags set (as well as any others). I'm using the filter: tcp.flags but I'm not sure if this is correct. Help please.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flags" rel="tag" title="see questions tagged &#39;flags&#39;">flags</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '16, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/36f1ad05cbe3b7e9e7120ca5c804f557?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ezra%20Nb&#39;s gravatar image" /><p><span>Ezra Nb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ezra Nb has no accepted answers">0%</span></p></div></div><div id="comments-container-52119" class="comments-container"></div><div id="comment-tools-52119" class="comment-tools"></div><div class="clear"></div><div id="comment-52119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52121"></span>

<div id="answer-container-52121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52121-score" class="post-score" title="current number of votes">0</div><span id="post-52121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, it's partially correct. Filtering on TCP flags tells Wireshark to show all packets that have a TCP flag field - which any TCP packet will, so you'll see them all.</p><p>What you need to filter for is specific flags, in your case SYN and FIN. To not give it all away just like that, here's an example how you'd filter on a PSH flag:</p><p><code>tcp.flags.push==1</code></p><p>Which means "check if the Push flag is set". Filtering for just "tcp.flags.push" would again mean "check if there's a push flag field" (which there is, always). So you need to adapt the push filter for your SYN and FIN flag problem - good luck :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '16, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52121" class="comments-container"></div><div id="comment-tools-52121" class="comment-tools"></div><div class="clear"></div><div id="comment-52121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

