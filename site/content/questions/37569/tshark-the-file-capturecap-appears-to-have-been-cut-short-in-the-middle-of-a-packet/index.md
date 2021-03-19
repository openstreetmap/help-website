+++
type = "question"
title = "tshark: The file &quot;capture.cap&quot; appears to have been cut short in the middle of a packet."
description = '''Hi All, is it possible to ignore this error and display the query results? I am just trying to obtain cipher information from connections using this command: tshark -r capture.cap -V -2R ssl.handshake.type==1 -T fields -e ip.src -e ssl.handshake.version -e ssl.handshake.ciphersuite tshark: The file ...'''
date = "2014-11-04T10:59:00Z"
lastmod = "2014-11-04T15:53:00Z"
weight = 37569
keywords = [ "ssl", "tshark", "error" ]
aliases = [ "/questions/37569" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: The file "capture.cap" appears to have been cut short in the middle of a packet.](/questions/37569/tshark-the-file-capturecap-appears-to-have-been-cut-short-in-the-middle-of-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37569-score" class="post-score" title="current number of votes">0</div><span id="post-37569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, is it possible to ignore this error and display the query results? I am just trying to obtain cipher information from connections using this command:</p><p>tshark -r capture.cap -V -2R ssl.handshake.type==1 -T fields -e ip.src -e ssl.handshake.version -e ssl.handshake.ciphersuite</p><p>tshark: The file "capture.cap" appears to have been cut short in the middle of a packet.</p><p>The file loads in the UI after displaying the same error messages and clicking OK, so I know the file is not corrupted. Let me know.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '14, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/f86f7ca5d84e2cc32500a7e4d4daa3b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StriclyFlava&#39;s gravatar image" /><p><span>StriclyFlava</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StriclyFlava has no accepted answers">0%</span></p></div></div><div id="comments-container-37569" class="comments-container"></div><div id="comment-tools-37569" class="comment-tools"></div><div class="clear"></div><div id="comment-37569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37571"></span>

<div id="answer-container-37571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37571-score" class="post-score" title="current number of votes">0</div><span id="post-37571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p>tshark -r capture.cap -V <strong>-q -Y</strong> -R ssl.handshake.type==1 -T fields -e ip.src -e ssl.handshake.version -e ssl.handshake.ciphersuite</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '14, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Nov '14, 13:23</strong> </span></p></div></div><div id="comments-container-37571" class="comments-container"><span id="37575"></span><div id="comment-37575" class="comment"><div id="post-37575-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, however, this syntax does not work, it is just displays all of the options. I am using version 1.12.1 in case that helps.</p><p>Thanks</p></div><div id="comment-37575-info" class="comment-info"><span class="comment-age">(04 Nov '14, 15:25)</span> <span class="comment-user userinfo">StriclyFlava</span></div></div><span id="37576"></span><div id="comment-37576" class="comment"><div id="post-37576-score" class="comment-score"></div><div class="comment-text"><p>sorry, I forgot to delete -R.</p><blockquote><p>tshark -r capture.cap -V -q -Y ssl.handshake.type==1 -T fields -e ip.src -e ssl.handshake.version -e ssl.handshake.ciphersuite</p></blockquote><p>Does that work better?</p></div><div id="comment-37576-info" class="comment-info"><span class="comment-age">(04 Nov '14, 15:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-37571" class="comment-tools"></div><div class="clear"></div><div id="comment-37571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

