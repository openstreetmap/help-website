+++
type = "question"
title = "text2pcap hex conversion issue"
description = '''Hi,not able to convert hex offset to pcap through text2pcap when there is pattern like  0000 0002 4500 0148 6833 0000 8011 bab6,actually i am taking output from juniper monitor traffic output command and it provides output in above ascii format.Please refere link http://kb.juniper.net/InfoCenter/ind...'''
date = "2014-05-21T04:19:00Z"
lastmod = "2014-05-23T00:39:00Z"
weight = 32946
keywords = [ "text2pcap" ]
aliases = [ "/questions/32946" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [text2pcap hex conversion issue](/questions/32946/text2pcap-hex-conversion-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32946-score" class="post-score" title="current number of votes">0</div><span id="post-32946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,not able to convert hex offset to pcap through text2pcap when there is pattern like 0000 0002 4500 0148 6833 0000 8011 bab6,actually i am taking output from juniper monitor traffic output command and it provides output in above ascii format.Please refere link <a href="http://kb.juniper.net/InfoCenter/index?page=content&amp;id=KB23952,">http://kb.juniper.net/InfoCenter/index?page=content&amp;id=KB23952,</a> in link it says put a space after each of 2 hex character.Is it possible through text2pcap.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '14, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-32946" class="comments-container"></div><div id="comment-tools-32946" class="comment-tools"></div><div class="clear"></div><div id="comment-32946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32947"></span>

<div id="answer-container-32947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32947-score" class="post-score" title="current number of votes">0</div><span id="post-32947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I can't access your link as it requires registration.</p><p>The format of text2pcap is clearly specified in the <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">man page</a> for the program, an offset of more than 2 digits, a space, then byte values as 2 hex digits separated by a space. You'll have to arrange your input text into the required format.</p><p>There is more info in text2pcap in the Wireshark <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolstext2pcap.html">docs</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '14, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-32947" class="comments-container"><span id="33012"></span><div id="comment-33012" class="comment"><div id="post-33012-score" class="comment-score"></div><div class="comment-text"><p>Thanks graham,i thihnk via xxd tool we can do this</p></div><div id="comment-33012-info" class="comment-info"><span class="comment-age">(23 May '14, 00:39)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-32947" class="comment-tools"></div><div class="clear"></div><div id="comment-32947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

