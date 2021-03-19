+++
type = "question"
title = "Can&#x27;t save the decrypted data in wireshark"
description = '''I tried to save the decrypted data as a pcap file. But when I opened it it&#x27;s still a encrypted one.Will it be possible to save the decrypted wireshark file? Thanks in Advance'''
date = "2013-05-21T00:21:00Z"
lastmod = "2013-05-21T05:57:00Z"
weight = 21341
keywords = [ "decryption", "ssl", "wireshark" ]
aliases = [ "/questions/21341" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can't save the decrypted data in wireshark](/questions/21341/cant-save-the-decrypted-data-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21341-score" class="post-score" title="current number of votes">0</div><span id="post-21341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to save the decrypted data as a pcap file. But when I opened it it's still a encrypted one.Will it be possible to save the decrypted wireshark file? Thanks in Advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '13, 00:21</strong></p><img src="https://secure.gravatar.com/avatar/3606fb2f161676306a345c0e2809e550?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalai&#39;s gravatar image" /><p><span>Kalai</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalai has no accepted answers">0%</span></p></div></div><div id="comments-container-21341" class="comments-container"></div><div id="comment-tools-21341" class="comment-tools"></div><div class="clear"></div><div id="comment-21341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21342"></span>

<div id="answer-container-21342" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21342-score" class="post-score" title="current number of votes">1</div><span id="post-21342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kalai has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Will it be possible to save the decrypted wireshark file?</p></blockquote><p>no, unfortunately that feature is not implemented. Wireshark will only show the decrypted data, but it is unable to save it into a (new) pcap file.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '13, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-21342" class="comments-container"><span id="21345"></span><div id="comment-21345" class="comment"><div id="post-21345-score" class="comment-score"></div><div class="comment-text"><p>Whith the new export PDU functionality it will be possible to implement. It's only implemeted for SIP and Diameter currently it will also "cut off" all the lower layers e.g. the layer above SSL could be output to a new file.</p></div><div id="comment-21345-info" class="comment-info"><span class="comment-age">(21 May '13, 05:57)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-21342" class="comment-tools"></div><div class="clear"></div><div id="comment-21342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

