+++
type = "question"
title = "Constructing the HF declarations dynamically"
description = '''Hi all, I have a requirement to build some of the Wireshark data structures dynamically, like the HF Info data. I tried to do this and build the data structure and passed the same while registering the protocol. Everything went fine, compilation and installation as well. But, when i execute i could ...'''
date = "2013-11-14T10:22:00Z"
lastmod = "2013-11-15T01:19:00Z"
weight = 27014
keywords = [ "hf_register_info", "hf" ]
aliases = [ "/questions/27014" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Constructing the HF declarations dynamically](/questions/27014/constructing-the-hf-declarations-dynamically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27014-score" class="post-score" title="current number of votes">0</div><span id="post-27014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have a requirement to build some of the Wireshark data structures dynamically, like the HF Info data. I tried to do this and build the data structure and passed the same while registering the protocol. Everything went fine, compilation and installation as well. But, when i execute i could see the dissection happening, but when the select the fields under that protocol Wireshark crashes. It throws the following.</p><p><strong>Unhandled exception ("proto.c:4567: failed assertion "hfinfo-&gt;type==FT_PROTOCOL"", group=1, code=4)</strong></p><p>can we build these data structures dynamically, and if at all where should it be stored, is there any constraint.</p><p>One more questions with curiosity, is there any way Wireshark can read XML file which contains protocol information and generate plugin which can be used to dissect the incoming data.</p><p>Thanks in advance.</p><p>-Regards Kiran Kumar G</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hf_register_info" rel="tag" title="see questions tagged &#39;hf_register_info&#39;">hf_register_info</span> <span class="post-tag tag-link-hf" rel="tag" title="see questions tagged &#39;hf&#39;">hf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '13, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p><span>Kiran Kumar G</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div></div><div id="comments-container-27014" class="comments-container"><span id="27017"></span><div id="comment-27017" class="comment"><div id="post-27017-score" class="comment-score">1</div><div class="comment-text"><p>For which version of wireshark do you get Unhandled exception ("proto.c:4567: failed assertion "hfinfo-&gt;type==FT_PROTOCOL"", group=1, code=4? Check the lan in proto.c it might give you an idea of what goes wrong.</p><p>packet-diameter.c builds dynamic hf:s look there, it also reads XML.</p></div><div id="comment-27017-info" class="comment-info"><span class="comment-age">(14 Nov '13, 12:31)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="27027"></span><div id="comment-27027" class="comment"><div id="post-27027-score" class="comment-score"></div><div class="comment-text"><p>I am using Wireshark version 1.6.1</p></div><div id="comment-27027-info" class="comment-info"><span class="comment-age">(15 Nov '13, 00:22)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div></div><div id="comment-tools-27014" class="comment-tools"></div><div class="clear"></div><div id="comment-27014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27029"></span>

<div id="answer-container-27029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27029-score" class="post-score" title="current number of votes">0</div><span id="post-27029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is there any way Wireshark can read XML file which contains protocol information and generate plugin which can be used to dissect the incoming data</p></blockquote><p>No, but there is the <a href="http://wsgd.free.fr">Wireshark Generic Dissector</a> plugin, which lets you give protocol information in a syntax that doesn't suck the way XML would. :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '13, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27029" class="comments-container"></div><div id="comment-tools-27029" class="comment-tools"></div><div class="clear"></div><div id="comment-27029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

