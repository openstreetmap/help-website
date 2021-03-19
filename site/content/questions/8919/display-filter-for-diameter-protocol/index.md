+++
type = "question"
title = "display filter for diameter protocol."
description = '''i want to use display filter for diameter protocol for some values.. when i set display filter for  &quot;diameter.hopbyhopId=4545655567&quot; its a success.. but when i use display filter on session Id &#x27;diameter.Session-Id == aaa://10.34.77.63:4876;1328783436;1&quot; its shows segmentation fault.. but its the sam...'''
date = "2012-02-09T02:50:00Z"
lastmod = "2012-02-09T05:10:00Z"
weight = 8919
keywords = [ "development", "diameter", "wireshark", "display-filter" ]
aliases = [ "/questions/8919" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [display filter for diameter protocol.](/questions/8919/display-filter-for-diameter-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8919-score" class="post-score" title="current number of votes">0</div><span id="post-8919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to use display filter for diameter protocol for some values..</p><p>when i set display filter for "diameter.hopbyhopId=4545655567" its a success..</p><p>but when i use display filter on session Id 'diameter.Session-Id == aaa://10.34.77.63:4876;1328783436;1"</p><p>its shows segmentation fault.. but its the same value as shown by wireshark how to apply this..</p><p>help!</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '12, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-8919" class="comments-container"></div><div id="comment-tools-8919" class="comment-tools"></div><div class="clear"></div><div id="comment-8919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8921"></span>

<div id="answer-container-8921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8921-score" class="post-score" title="current number of votes">0</div><span id="post-8921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use the latest Wireshark version 1.6.5. If that doesn't work file a full bug report at <a href="https://bugs.wireshark.org">bugs.wireshark.org</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '12, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8921" class="comments-container"><span id="8922"></span><div id="comment-8922" class="comment"><div id="post-8922-score" class="comment-score"></div><div class="comment-text"><p>when i use the string</p><p>"diameter.avp.session_id" as display filter in windows wireshark.. it works fine</p><p>but when i use it in my code</p><p>rrfilter="diameter.avp.session_id" then try to compile it using dfilter_compile()</p><p>its shows segmentation fault..</p><p>why so? any idea?</p></div><div id="comment-8922-info" class="comment-info"><span class="comment-age">(09 Feb '12, 03:37)</span> <span class="comment-user userinfo">Sanny_D</span></div></div><span id="8927"></span><div id="comment-8927" class="comment"><div id="post-8927-score" class="comment-score"></div><div class="comment-text"><p>I've converted your "answer" to a comment, please read the <a href="http://ask.wireshark.org/faq/">FAQ</a> on how to use the site.</p><p>Can you also please indicate in your questions that you are using the Wireshark dissection engine in your own code and that the question isn't related to general use of Wireshark as a whole.</p></div><div id="comment-8927-info" class="comment-info"><span class="comment-age">(09 Feb '12, 05:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-8921" class="comment-tools"></div><div class="clear"></div><div id="comment-8921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

