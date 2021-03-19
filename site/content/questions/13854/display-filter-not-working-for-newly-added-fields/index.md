+++
type = "question"
title = "Display Filter not working for newly added fields"
description = '''My plugin postdissector dissects, and displays, newly added suboptions in the tcp options field. But I just noticed that I&#x27;m unable to filter these fields when I type tcp.options.foo in the filter bar(but tcp.options,foo still appears in the drop down box). When I type tcp.options.foo, it shows abso...'''
date = "2012-08-23T21:46:00Z"
lastmod = "2012-08-28T21:46:00Z"
weight = 13854
keywords = [ "tcp-options", "postdissector", "display-filter" ]
aliases = [ "/questions/13854" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display Filter not working for newly added fields](/questions/13854/display-filter-not-working-for-newly-added-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13854-score" class="post-score" title="current number of votes">0</div><span id="post-13854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My plugin postdissector dissects, and displays, newly added suboptions in the tcp options field. But I just noticed that I'm unable to filter these fields when I type tcp.options.foo in the filter bar(but tcp.options,foo still appears in the drop down box). When I type tcp.options.foo, it shows absolutely no packets. However, the filter seems to work just fine when I try to filter something like, say, tcp.options. What's the reason for this?</p><p>Edit: No one has any ideas? :(</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-options" rel="tag" title="see questions tagged &#39;tcp-options&#39;">tcp-options</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '12, 21:46</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p><span>SidR</span><br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Aug '12, 02:31</strong> </span></p></div></div><div id="comments-container-13854" class="comments-container"></div><div id="comment-tools-13854" class="comment-tools"></div><div class="clear"></div><div id="comment-13854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13897"></span>

<div id="answer-container-13897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13897-score" class="post-score" title="current number of votes">0</div><span id="post-13897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, there is only one postdissector as a "reference" (packet-prp.c). Did you check that? Maybe it helps to track down your problem.</p><p>BTW: is it possible to post the code of your post dissector (on <a href="http://pastebin.com">pastebin.com</a> or so...)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '12, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13897" class="comments-container"><span id="13909"></span><div id="comment-13909" class="comment"><div id="post-13909-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your reply Kurt. Just checked the packet-prp.c file, but I'm still unable to figure out where the problem might be.</p><p>I have pasted a part of my plugin post-dissector code here: <a href="http://pastebin.com/1kJ4fLHm">http://pastebin.com/1kJ4fLHm</a></p><p>I'm sorry that I had to remove most of the data structures for my suboptions (which include some proprietary information), nevertheless all the essential parts have been included. I also recompiled my code with the above, but the problem persists.</p></div><div id="comment-13909-info" class="comment-info"><span class="comment-age">(27 Aug '12, 02:08)</span> <span class="comment-user userinfo">SidR</span></div></div><span id="13950"></span><div id="comment-13950" class="comment"><div id="post-13950-score" class="comment-score"></div><div class="comment-text"><p>Can anyone please tell me why the display filter does not work for the above code?</p></div><div id="comment-13950-info" class="comment-info"><span class="comment-age">(28 Aug '12, 21:46)</span> <span class="comment-user userinfo">SidR</span></div></div></div><div id="comment-tools-13897" class="comment-tools"></div><div class="clear"></div><div id="comment-13897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

