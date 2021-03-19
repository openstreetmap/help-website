+++
type = "question"
title = "How to debug a wireshark dissector ?"
description = '''I just want to debug some part of my custom dissector with printf. But I don&#x27;t know where the stdout is redirect, and the only answer that I found is to open a &quot;debug console window&quot;, but I don&#x27;t have this option in my wireshark. I need help. '''
date = "2011-03-20T08:20:00Z"
lastmod = "2011-03-20T09:09:00Z"
weight = 2937
keywords = [ "development", "debug", "dissector" ]
aliases = [ "/questions/2937" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to debug a wireshark dissector ?](/questions/2937/how-to-debug-a-wireshark-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2937-score" class="post-score" title="current number of votes">0</div><span id="post-2937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just want to debug some part of my custom dissector with printf. But I don't know where the stdout is redirect, and the only answer that I found is to open a "debug console window", but I don't have this option in my wireshark.</p><p>I need help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '11, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/a8e5c9438725b82bdee34d32a2068b80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chronidev&#39;s gravatar image" /><p><span>chronidev</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chronidev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Mar '11, 08:20</strong> </span></p></div></div><div id="comments-container-2937" class="comments-container"></div><div id="comment-tools-2937" class="comment-tools"></div><div class="clear"></div><div id="comment-2937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2943"></span>

<div id="answer-container-2943" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2943-score" class="post-score" title="current number of votes">1</div><span id="post-2943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chronidev has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From your comment I assume you don't run on Windows, that's good.</p><p>As you said, output goes to stdout. So open up a console window and start Wireshark from there. I actually do that always, having setup a desktop file which opens a console first then launches Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '11, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2943" class="comments-container"><span id="2945"></span><div id="comment-2945" class="comment"><div id="post-2945-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I think it's because we are Sunday, I had forgotten to make the "make install". Sorry.</p></div><div id="comment-2945-info" class="comment-info"><span class="comment-age">(20 Mar '11, 09:09)</span> <span class="comment-user userinfo">chronidev</span></div></div></div><div id="comment-tools-2943" class="comment-tools"></div><div class="clear"></div><div id="comment-2943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2938"></span>

<div id="answer-container-2938" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2938-score" class="post-score" title="current number of votes">3</div><span id="post-2938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>open a "debug console window", but I don't have this option in my wireshark.</p></blockquote><p>In Wireshark do Edit ! Preferences and select "Always (debugging)" from the drop-down menu on the "Open a console window" preference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '11, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-2938" class="comments-container"><span id="2942"></span><div id="comment-2942" class="comment"><div id="post-2942-score" class="comment-score"></div><div class="comment-text"><p>With the latest svn tree I don't have this option in the preference box.</p></div><div id="comment-2942-info" class="comment-info"><span class="comment-age">(20 Mar '11, 08:35)</span> <span class="comment-user userinfo">chronidev</span></div></div></div><div id="comment-tools-2938" class="comment-tools"></div><div class="clear"></div><div id="comment-2938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

