+++
type = "question"
title = "Dissector based  on two asn files"
description = '''Hey, i&#x27;m realy new in building dissectors in Wireshark. Now i&#x27;m trying to create a dissector based on an asn file. I used the example to understand the basic functions of asn2wrs and i think i understood it. But now i don&#x27;t know what files do i need to create, if i have a asn file, witch is based on...'''
date = "2014-08-27T00:58:00Z"
lastmod = "2014-08-27T06:04:00Z"
weight = 35788
keywords = [ "asn2wrs" ]
aliases = [ "/questions/35788" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector based on two asn files](/questions/35788/dissector-based-on-two-asn-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35788-score" class="post-score" title="current number of votes">0</div><span id="post-35788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey, i'm realy new in building dissectors in Wireshark. Now i'm trying to create a dissector based on an asn file. I used the example to understand the basic functions of asn2wrs and i think i understood it. But now i don't know what files do i need to create, if i have a asn file, witch is based on an other asn file. If i look at the Makefile of the foo example, i don't know hat i have to change if i have to use two asn files. Can someone help me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-asn2wrs" rel="tag" title="see questions tagged &#39;asn2wrs&#39;">asn2wrs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '14, 00:58</strong></p><img src="https://secure.gravatar.com/avatar/f65ac046295141d9f33ce4ac1770b5a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Venturina&#39;s gravatar image" /><p><span>Venturina</span><br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Venturina has no accepted answers">0%</span></p></div></div><div id="comments-container-35788" class="comments-container"></div><div id="comment-tools-35788" class="comment-tools"></div><div class="clear"></div><div id="comment-35788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35793"></span>

<div id="answer-container-35793" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35793-score" class="post-score" title="current number of votes">1</div><span id="post-35793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You just need to add your various ASN.1 source files to the ASN_FILE_LIST defined in Makefile.common. As an example, you can take a look at the asn1/ulp folder that includes 3 ASN.1 files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '14, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '14, 03:32</strong> </span></p></div></div><div id="comments-container-35793" class="comments-container"><span id="35795"></span><div id="comment-35795" class="comment"><div id="post-35795-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that works. But now i get many errors if i run the top level Make. one of them ist error:unknown type name 'asn1_ctx_t'. Did i forgot an include in my template? Or where is this type defined?</p></div><div id="comment-35795-info" class="comment-info"><span class="comment-age">(27 Aug '14, 04:56)</span> <span class="comment-user userinfo">Venturina</span></div></div><span id="35803"></span><div id="comment-35803" class="comment"><div id="post-35803-score" class="comment-score"></div><div class="comment-text"><h1 id="include-epan-asn1.h">include &lt;epan asn1.h=""&gt;</h1><p>probably, look at other asn1 based dissectors.</p></div><div id="comment-35803-info" class="comment-info"><span class="comment-age">(27 Aug '14, 06:04)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-35793" class="comment-tools"></div><div class="clear"></div><div id="comment-35793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

