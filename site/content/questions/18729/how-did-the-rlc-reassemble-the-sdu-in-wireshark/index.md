+++
type = "question"
title = "How did the rlc reassemble the SDU in wireshark?"
description = '''1,How did the rlc reassemble the code from mac in wireshark? you should tell me the main step of reassemble in wireshark. 2,Is the wireshark malloc memory for each rlc SDU? because when the wireshark decode a big *.pcap,it will occupy a big memory. is the wireshark reassemble the rlc code stream fro...'''
date = "2013-02-19T02:15:00Z"
lastmod = "2013-02-25T02:18:00Z"
weight = 18729
keywords = [ "reassemble", "rlc" ]
aliases = [ "/questions/18729" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How did the rlc reassemble the SDU in wireshark?](/questions/18729/how-did-the-rlc-reassemble-the-sdu-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18729-score" class="post-score" title="current number of votes">0</div><span id="post-18729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>1,How did the rlc reassemble the code from mac in wireshark? you should tell me the main step of reassemble in wireshark.</p><p>2,Is the wireshark malloc memory for each rlc SDU? because when the wireshark decode a big *.pcap,it will occupy a big memory.</p><p>is the wireshark reassemble the rlc code stream from mac like this step? 1,decode each rlc code and malloc new memory for each rlc SDU.</p><p>2,when user click the frame .wireshark will find the rlc SDU's which have the same logical channel id. and then reassemble those ,transport to up level.</p><p>3,so for each rlc decode,it need to search the memory which malloced by rlc. if the memory is big, then the time used to decode is long.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span> <span class="post-tag tag-link-rlc" rel="tag" title="see questions tagged &#39;rlc&#39;">rlc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '13, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-18729" class="comments-container"></div><div id="comment-tools-18729" class="comment-tools"></div><div class="clear"></div><div id="comment-18729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18736"></span>

<div id="answer-container-18736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18736-score" class="post-score" title="current number of votes">0</div><span id="post-18736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming its UMTS rlc you can read the code of packet-rlc.c to figure out how it's done and see if any improvments can be done. You should probably start out by trying the development version to see if there has been improvments done allready.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-18736" class="comments-container"><span id="18794"></span><div id="comment-18794" class="comment"><div id="post-18794-score" class="comment-score"></div><div class="comment-text"><p>how to get the development version?</p></div><div id="comment-18794-info" class="comment-info"><span class="comment-age">(20 Feb '13, 23:33)</span> <span class="comment-user userinfo">smilezuzu</span></div></div><span id="18797"></span><div id="comment-18797" class="comment"><div id="post-18797-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.wireshark.org/download.html#development_release">http://www.wireshark.org/download.html#development_release</a></p><p>Or <a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a></p></div><div id="comment-18797-info" class="comment-info"><span class="comment-age">(21 Feb '13, 00:49)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="18844"></span><div id="comment-18844" class="comment"><div id="post-18844-score" class="comment-score"></div><div class="comment-text"><p>I have download the development version,and compile it.but the rlc reassemble is not so good.is still bad.</p></div><div id="comment-18844-info" class="comment-info"><span class="comment-age">(25 Feb '13, 02:17)</span> <span class="comment-user userinfo">smilezuzu</span></div></div><span id="18845"></span><div id="comment-18845" class="comment"><div id="post-18845-score" class="comment-score"></div><div class="comment-text"><p>any body help me to fix the rlc reassemble process？</p></div><div id="comment-18845-info" class="comment-info"><span class="comment-age">(25 Feb '13, 02:18)</span> <span class="comment-user userinfo">smilezuzu</span></div></div></div><div id="comment-tools-18736" class="comment-tools"></div><div class="clear"></div><div id="comment-18736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

