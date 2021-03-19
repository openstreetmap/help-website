+++
type = "question"
title = "Colorize with Filter problem"
description = '''Can someone confirm that &quot;Colorize with Filter&quot; does not colorize all captured packets as expected in Wireshark 1.4.x (it works well in Wireshark 1.2.11). I have tested it with Windows 32 and 64 bit Versions on multiple PCs. To reproduce capture some tcp traffic. Then open the context menu on a sour...'''
date = "2010-11-29T01:43:00Z"
lastmod = "2010-12-02T00:29:00Z"
weight = 1147
keywords = [ "colorize" ]
aliases = [ "/questions/1147" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Colorize with Filter problem](/questions/1147/colorize-with-filter-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1147-score" class="post-score" title="current number of votes">0</div><span id="post-1147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone confirm that "Colorize with Filter" does not colorize all captured packets as expected in Wireshark 1.4.x (it works well in Wireshark 1.2.11). I have tested it with Windows 32 and 64 bit Versions on multiple PCs. To reproduce capture some tcp traffic. Then open the context menu on a source port in the packet details pane and select a color under "Colorize with Filter".</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-colorize" rel="tag" title="see questions tagged &#39;colorize&#39;">colorize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '10, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/69d82b0f2bbc8297b86ee1354bcb5bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bcookie&#39;s gravatar image" /><p><span>bcookie</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bcookie has no accepted answers">0%</span></p></div></div><div id="comments-container-1147" class="comments-container"></div><div id="comment-tools-1147" class="comment-tools"></div><div class="clear"></div><div id="comment-1147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1148"></span>

<div id="answer-container-1148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1148-score" class="post-score" title="current number of votes">1</div><span id="post-1148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just tested it myself and you are right, there is a problem with it. The building of the internal coloring rule does take place, but the update of the packet list somehow is not performed. When you open the coloring rules and click on "OK" without editing the rules, the packet list is updated and the coloring applied.</p><p>I will take a look at this and give an update when it's fixed (somewhere this week I expect).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '10, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1148" class="comments-container"><span id="1149"></span><div id="comment-1149" class="comment"><div id="post-1149-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for the workaround and the fast response. This will help until fixed.</p></div><div id="comment-1149-info" class="comment-info"><span class="comment-age">(29 Nov '10, 02:39)</span> <span class="comment-user userinfo">bcookie</span></div></div><span id="1162"></span><div id="comment-1162" class="comment"><div id="post-1162-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" into a "comment" to adhere to the Q&amp;A style of this website.</p></div><div id="comment-1162-info" class="comment-info"><span class="comment-age">(29 Nov '10, 13:39)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="1167"></span><div id="comment-1167" class="comment"><div id="post-1167-score" class="comment-score"></div><div class="comment-text"><p>OK, this has been fixed in SVN 35074 and is scheduled to be included in 1.4.3.</p><p>You can also download an automated development build from http://www.wireshark.org/download/automated/ (use version 35074 or higher which will be available in a couple of hours)</p></div><div id="comment-1167-info" class="comment-info"><span class="comment-age">(29 Nov '10, 14:51)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="1207"></span><div id="comment-1207" class="comment"><div id="post-1207-score" class="comment-score"></div><div class="comment-text"><p>Sake - there also seems to be a problem with moving to another profile and the coloring rules being updated. The export from one profile and import to another doesn't seem to be updating properly. I'll play with it more tomorrow time permitting. Things are crazy and yes - I still owe you an email or two (lots of things changing here lately - pulling 16-hour days... eek).</p></div><div id="comment-1207-info" class="comment-info"><span class="comment-age">(02 Dec '10, 00:29)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-1148" class="comment-tools"></div><div class="clear"></div><div id="comment-1148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

