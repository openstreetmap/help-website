+++
type = "question"
title = "when is add_oid() funtion called?"
description = '''When is the add_oid() function that is present in epan&#92;dissectors&#92;oids.h called? Where particularly are the values for the funtion add_oid() passed?'''
date = "2012-01-12T07:13:00Z"
lastmod = "2012-01-15T05:27:00Z"
weight = 8335
keywords = [ "development" ]
aliases = [ "/questions/8335" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [when is add\_oid() funtion called?](/questions/8335/when-is-add_oid-funtion-called)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8335-score" class="post-score" title="current number of votes">0</div><span id="post-8335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When is the <code>add_oid()</code> function that is present in <code>epan\dissectors\oids.h</code> called? Where particularly are the values for the funtion <code>add_oid()</code> passed?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '12, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/92707c24fa77ae73d3dd88b6a93a32aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Premini%20Francis&#39;s gravatar image" /><p><span>Premini Francis</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Premini Francis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jan '12, 07:18</strong> </span></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span></p></div></div><div id="comments-container-8335" class="comments-container"></div><div id="comment-tools-8335" class="comment-tools"></div><div class="clear"></div><div id="comment-8335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8336"></span>

<div id="answer-container-8336" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8336-score" class="post-score" title="current number of votes">0</div><span id="post-8336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I presume you mean <code>oid_add()</code>. There is <code>no add_oid()</code> declared in <code>oids.h</code> (at least in the current dev Wireshark source).</p><p>A quick grep suggests that <code>oid_add()</code> is called only in <code>oids.c</code> so presumably examining that code will answer your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '12, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-8336" class="comments-container"><span id="8341"></span><div id="comment-8341" class="comment"><div id="post-8341-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply. But kindly look at the screen shot attached. There is add_oid() function in oids.c <img src="https://picasaweb.google.com/116549508739714619740/DropBox?authkey=Gv1sRgCJmmiqyki_2FDQ&amp;gsessionid=3iIReCuMozeKAIdDZpikLw#5696785111466073410" alt="alt text" /></p></div><div id="comment-8341-info" class="comment-info"><span class="comment-age">(12 Jan '12, 08:37)</span> <span class="comment-user userinfo">Premini Francis</span></div></div><span id="8343"></span><div id="comment-8343" class="comment"><div id="post-8343-score" class="comment-score"></div><div class="comment-text"><p>(I converted your answer to a comment; Please see the FAQ).</p><p>add_oid() is static in oids.c and is not declared in oids.h (at least in the dev Wireshark sources).</p><p>Thus add_oid() is called only within oids.c; looking at the calls should answer your question.</p></div><div id="comment-8343-info" class="comment-info"><span class="comment-age">(12 Jan '12, 08:48)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="8393"></span><div id="comment-8393" class="comment"><div id="post-8393-score" class="comment-score"></div><div class="comment-text"><p>how is packet_snmp.c and add_oid() function are linked together?</p></div><div id="comment-8393-info" class="comment-info"><span class="comment-age">(15 Jan '12, 05:27)</span> <span class="comment-user userinfo">Premini Francis</span></div></div></div><div id="comment-tools-8336" class="comment-tools"></div><div class="clear"></div><div id="comment-8336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

