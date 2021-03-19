+++
type = "question"
title = "How to use tshark to output a tcpdump  into text-formatted file"
description = '''Hello All, The following command will export a view of the packet details rather than a one-line summary of the packet into a text file: tshark -V -r input &amp;gt; output.txt My question is how can I export a view of the packet details AND a one-line summary of the packet into a text file? Thanks.'''
date = "2012-09-27T20:19:00Z"
lastmod = "2012-10-09T10:40:00Z"
weight = 14581
keywords = [ "tshark" ]
aliases = [ "/questions/14581" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use tshark to output a tcpdump into text-formatted file](/questions/14581/how-to-use-tshark-to-output-a-tcpdump-into-text-formatted-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14581-score" class="post-score" title="current number of votes">0</div><span id="post-14581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>The following command will export a view of the packet details <strong>rather than</strong> a one-line summary of the packet into a text file: tshark -V -r input &gt; <a href="http://output.txt">output.txt</a></p><p>My question is how can I export a view of the packet details <strong>AND</strong> a one-line summary of the packet into a text file?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '12, 20:19</strong></p><img src="https://secure.gravatar.com/avatar/cd57e360702cc9f1c2d3f26661ec776e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylin&#39;s gravatar image" /><p><span>ylin</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylin has no accepted answers">0%</span></p></div></div><div id="comments-container-14581" class="comments-container"></div><div id="comment-tools-14581" class="comment-tools"></div><div class="clear"></div><div id="comment-14581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14590"></span>

<div id="answer-container-14590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14590-score" class="post-score" title="current number of votes">0</div><span id="post-14590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you "print" to a file (or in 1.8+, "Export Specified Packet Dissections"-&gt;"As plain text") from the GUI you can get both. I am not aware of a way to do this from tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '12, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Sep '12, 06:24</strong> </span></p></div></div><div id="comments-container-14590" class="comments-container"><span id="14591"></span><div id="comment-14591" class="comment"><div id="post-14591-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff,</p><p>The reason I want to use tshark is I want to automate this process not opening Wireshark GUI. Is there some way we can do it?</p></div><div id="comment-14591-info" class="comment-info"><span class="comment-age">(28 Sep '12, 07:07)</span> <span class="comment-user userinfo">ylin</span></div></div><span id="14825"></span><div id="comment-14825" class="comment"><div id="post-14825-score" class="comment-score"></div><div class="comment-text"><p>As I said, I am not aware of a way to do it. However, it looks like Ed Beroset took an interest in this request and opened <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7782">bug 7782</a> to add the functionality.</p></div><div id="comment-14825-info" class="comment-info"><span class="comment-age">(09 Oct '12, 10:40)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-14590" class="comment-tools"></div><div class="clear"></div><div id="comment-14590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

