+++
type = "question"
title = "Global variable misused in the code"
description = '''Two days ago i got this problem when i add a global varible to the original wireshark source code, it tells me there is a compile error like this:   in load_cap_file:  tshark.c:2585: undefined reference to &#x27;fp&#x27;, tshark.c:2840:undefined reference to &#x27;fp&#x27; ...  recursive error .... Infact, i just add a...'''
date = "2012-11-18T18:54:00Z"
lastmod = "2012-11-22T00:43:00Z"
weight = 16029
keywords = [ "variable", "global", "undefined", "reference" ]
aliases = [ "/questions/16029" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Global variable misused in the code](/questions/16029/global-variable-misused-in-the-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16029-score" class="post-score" title="current number of votes">0</div><span id="post-16029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Two days ago i got this problem when i add a global varible to the original wireshark source code, it tells me there is a compile error like this:<br />
</p><p>in load_cap_file: tshark.c:2585: undefined reference to 'fp', tshark.c:2840:undefined reference to 'fp' ... recursive error ....</p><p>Infact, i just add a global varible <strong>FILE* fp=NULL；</strong>in the file packet.c, and then <strong>extern FILE* fp;</strong> in the tshark.c . In the tshark.c file, there are some code related to the 'fp', and tshark.c will call 'dissect_packet' function in packet.c, 'fp' is also used in the function 'dissect_packet', i don't know where did i make a mistake?Is there anyone can tell me?Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-variable" rel="tag" title="see questions tagged &#39;variable&#39;">variable</span> <span class="post-tag tag-link-global" rel="tag" title="see questions tagged &#39;global&#39;">global</span> <span class="post-tag tag-link-undefined" rel="tag" title="see questions tagged &#39;undefined&#39;">undefined</span> <span class="post-tag tag-link-reference" rel="tag" title="see questions tagged &#39;reference&#39;">reference</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '12, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/18b671a9df9f8c8d67a5fce658c10e81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rodman&#39;s gravatar image" /><p><span>rodman</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rodman has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-16029" class="comments-container"></div><div id="comment-tools-16029" class="comment-tools"></div><div class="clear"></div><div id="comment-16029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16035"></span>

<div id="answer-container-16035" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16035-score" class="post-score" title="current number of votes">0</div><span id="post-16035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not all symbols are exported from libwireshark anymore. They have to be explicitly listed in libwireshark.def.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '12, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16035" class="comments-container"><span id="16185"></span><div id="comment-16185" class="comment"><div id="post-16185-score" class="comment-score"></div><div class="comment-text"><p>I have solved this problem using the method you told me, many thanks!</p></div><div id="comment-16185-info" class="comment-info"><span class="comment-age">(21 Nov '12, 17:34)</span> <span class="comment-user userinfo">rodman</span></div></div><span id="16194"></span><div id="comment-16194" class="comment"><div id="post-16194-score" class="comment-score"></div><div class="comment-text"><p>If an answer solves your problem please accept it by clicking the checkmark icon next to the answer. This benefits other users of the site who may have similar issues.</p></div><div id="comment-16194-info" class="comment-info"><span class="comment-age">(22 Nov '12, 00:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-16035" class="comment-tools"></div><div class="clear"></div><div id="comment-16035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

