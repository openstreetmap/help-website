+++
type = "question"
title = "How to build a dissector based on cip.class (using dissector_add_uint) ?"
description = '''Hi,  I would like to build my own dissector based on the parameter severals values of cip.class. I used the function dissector_add_uint(&quot;cip.class&quot;,VALUE,handle), but it is not working. My dissector is never called. After research, I think it is because cip.class is not registered, right ? How can I...'''
date = "2014-02-04T07:06:00Z"
lastmod = "2014-02-05T03:36:00Z"
weight = 29430
keywords = [ "cip", "dissector_add_uint", "cip.class.iface", "dissector", "cip.class" ]
aliases = [ "/questions/29430" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to build a dissector based on cip.class (using dissector\_add\_uint) ?](/questions/29430/how-to-build-a-dissector-based-on-cipclass-using-dissector_add_uint)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29430-score" class="post-score" title="current number of votes">0</div><span id="post-29430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to build my own dissector based on the parameter severals values of cip.class. I used the function dissector_add_uint("cip.class",VALUE,handle), but it is not working. My dissector is never called.</p><p>After research, I think it is because cip.class is not registered, right ? How can I do for use this parameter ?</p><p>I see (by trying) that I can use cip.class.iface with value 0. But I don't know what is the attribute, it is never displayed and I don't find where it is read. Someone know where I can find this information ?</p><p>Thanks, IJK</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cip" rel="tag" title="see questions tagged &#39;cip&#39;">cip</span> <span class="post-tag tag-link-dissector_add_uint" rel="tag" title="see questions tagged &#39;dissector_add_uint&#39;">dissector_add_uint</span> <span class="post-tag tag-link-cip.class.iface" rel="tag" title="see questions tagged &#39;cip.class.iface&#39;">cip.class.iface</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-cip.class" rel="tag" title="see questions tagged &#39;cip.class&#39;">cip.class</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '14, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/e42a64162b93f10790ee2d388da6a264?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IJK&#39;s gravatar image" /><p><span>IJK</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IJK has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '14, 18:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-29430" class="comments-container"></div><div id="comment-tools-29430" class="comment-tools"></div><div class="clear"></div><div id="comment-29430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29454"></span>

<div id="answer-container-29454" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29454-score" class="post-score" title="current number of votes">0</div><span id="post-29454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I think you are mixing filter names and dissector tables. To be able to register in a dissector table the table has to be registered first. You can find existing tables and what's registered in them in the "internals" menu in the top menubar.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '14, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-29454" class="comments-container"></div><div id="comment-tools-29454" class="comment-tools"></div><div class="clear"></div><div id="comment-29454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

