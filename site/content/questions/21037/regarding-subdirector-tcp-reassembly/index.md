+++
type = "question"
title = "Regarding subdirector tcp reassembly"
description = '''I am little confused about this reassembly option in wireshark.What exactly we achieve by enabling/disabling this option?'''
date = "2013-05-08T09:33:00Z"
lastmod = "2013-05-08T22:44:00Z"
weight = 21037
keywords = [ "reassembly", "tcp" ]
aliases = [ "/questions/21037" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Regarding subdirector tcp reassembly](/questions/21037/regarding-subdirector-tcp-reassembly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21037-score" class="post-score" title="current number of votes">0</div><span id="post-21037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am little confused about this reassembly option in wireshark.What exactly we achieve by enabling/disabling this option?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '13, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-21037" class="comments-container"></div><div id="comment-tools-21037" class="comment-tools"></div><div class="clear"></div><div id="comment-21037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21048"></span>

<div id="answer-container-21048" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21048-score" class="post-score" title="current number of votes">1</div><span id="post-21048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Reassembly means that Wireshark will gather all TCP (or whatever protocol the reassembly is used for, but it's usually TCP) segments that are part of a request or answer and combine them for the next layer dissector. Think of an HTTP page being transmitted - it will not fit into one single packet in most cases, so it spans multiple TCP segments. The HTTP dissector needs the whole content in one piece, not just single segments, so TCP can assemble all segments into the complete HTTP answer and have the dissector take a look at the result instead.</p><p>Reassembly in my opinion is useful for content reconstruction, but not so much when troubleshooting timing behavior and other issues. So I usually have TCP reassembly turned off and only turn it on when I need to take a look at the content that was transferred.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '13, 20:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21048" class="comments-container"><span id="21049"></span><div id="comment-21049" class="comment"><div id="post-21049-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper! Understood/</p></div><div id="comment-21049-info" class="comment-info"><span class="comment-age">(08 May '13, 22:44)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div></div><div id="comment-tools-21048" class="comment-tools"></div><div class="clear"></div><div id="comment-21048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

