+++
type = "question"
title = "can I modify packets using Wireshark?"
description = '''Can wireshark be used to modify packets by intercepting them midway. I have used WebScarab web application proxy to intercept browser requests and alter them before passing them on to their actual target website. But I do not know whether I can do a similar operation with wireshark. If not which too...'''
date = "2015-03-06T17:43:00Z"
lastmod = "2015-03-09T08:53:00Z"
weight = 40334
keywords = [ "intercept", "modify" ]
aliases = [ "/questions/40334" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can I modify packets using Wireshark?](/questions/40334/can-i-modify-packets-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40334-score" class="post-score" title="current number of votes">0</div><span id="post-40334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can wireshark be used to modify packets by intercepting them midway. I have used WebScarab web application proxy to intercept browser requests and alter them before passing them on to their actual target website. But I do not know whether I can do a similar operation with wireshark. If not which tool can help me do that? Pls help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-intercept" rel="tag" title="see questions tagged &#39;intercept&#39;">intercept</span> <span class="post-tag tag-link-modify" rel="tag" title="see questions tagged &#39;modify&#39;">modify</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '15, 17:43</strong></p><img src="https://secure.gravatar.com/avatar/efa67ffd82b0026fa37b1a4accae201a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anand&#39;s gravatar image" /><p><span>Anand</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anand has no accepted answers">0%</span></p></div></div><div id="comments-container-40334" class="comments-container"></div><div id="comment-tools-40334" class="comment-tools"></div><div class="clear"></div><div id="comment-40334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40339"></span>

<div id="answer-container-40339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40339-score" class="post-score" title="current number of votes">0</div><span id="post-40339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No it can't. Wireshark captures packets as-is, and does not modify them. I would use a tool like <a href="http://www.telerik.com/fiddler">Fiddler</a> to intercept and modify requests and responses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '15, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40339" class="comments-container"><span id="40387"></span><div id="comment-40387" class="comment"><div id="post-40387-score" class="comment-score"></div><div class="comment-text"><p>Thank you. Downloaded Fiddler and trying out now.</p></div><div id="comment-40387-info" class="comment-info"><span class="comment-age">(09 Mar '15, 08:53)</span> <span class="comment-user userinfo">Anand</span></div></div></div><div id="comment-tools-40339" class="comment-tools"></div><div class="clear"></div><div id="comment-40339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

