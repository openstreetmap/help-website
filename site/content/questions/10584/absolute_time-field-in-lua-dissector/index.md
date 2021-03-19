+++
type = "question"
title = "absolute_time field in Lua dissector"
description = '''The function ProtoField.absolute_time is documented (11.10.6.14), but may be broken in some way. At least, when I try to call it, I get an error dialogue containing the message &quot;attempt to call field &#x27;?&#x27; (a nil value)&quot;, and pointing to the line with the absolute_time call, when starting wireshark. I...'''
date = "2012-05-02T04:11:00Z"
lastmod = "2012-05-02T09:51:00Z"
weight = 10584
keywords = [ "absolute_time", "lua" ]
aliases = [ "/questions/10584" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [absolute\_time field in Lua dissector](/questions/10584/absolute_time-field-in-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10584-score" class="post-score" title="current number of votes">0</div><span id="post-10584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The function ProtoField.absolute_time is documented (11.10.6.14), but may be broken in some way. At least, when I try to call it, I get an error dialogue containing the message "attempt to call field '?' (a nil value)", and pointing to the line with the absolute_time call, when starting wireshark.</p><p>I am using version 1.6.7.</p><p>Is this deliberate, or a bug?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-absolute_time" rel="tag" title="see questions tagged &#39;absolute_time&#39;">absolute_time</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '12, 04:11</strong></p><img src="https://secure.gravatar.com/avatar/e46f968132ae91eba78671e90e58399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brian%20Raven&#39;s gravatar image" /><p><span>Brian Raven</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brian Raven has no accepted answers">0%</span></p></div></div><div id="comments-container-10584" class="comments-container"></div><div id="comment-tools-10584" class="comment-tools"></div><div class="clear"></div><div id="comment-10584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10606"></span>

<div id="answer-container-10606" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10606-score" class="post-score" title="current number of votes">1</div><span id="post-10606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Brian Raven has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That function was added after 1.6 (that is, in the current trunk which is 1.7). The documentation you're looking at is probably the online WSUG which is, as per <a href="http://www.wireshark.org/docs/wsug_html_chunked/">the front page</a>, for 1.7 (not 1.6).</p><p>You might want to use the WSUG that came with your version of Wireshark (if it did, in fact, come with one).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '12, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-10606" class="comments-container"><span id="10607"></span><div id="comment-10607" class="comment"><div id="post-10607-score" class="comment-score"></div><div class="comment-text"><p>That explains it. I missed the "For Wireshark 1.7". I look forward to being able to add timestamps to my dissector, when 1.7 becomes stable.</p><p>Many thanks for the prompt response.</p></div><div id="comment-10607-info" class="comment-info"><span class="comment-age">(02 May '12, 09:43)</span> <span class="comment-user userinfo">Brian Raven</span></div></div><span id="10608"></span><div id="comment-10608" class="comment"><div id="post-10608-score" class="comment-score"></div><div class="comment-text"><p>As this is a Q&amp;A site, please don't forget to Accept the answer if it answered your question--see the FAQ.</p><p>Anyway, you're welcome!</p></div><div id="comment-10608-info" class="comment-info"><span class="comment-age">(02 May '12, 09:51)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-10606" class="comment-tools"></div><div class="clear"></div><div id="comment-10606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

