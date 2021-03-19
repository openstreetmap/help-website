+++
type = "question"
title = "Re bilt attached file from RAW"
description = '''Bonjour, I&#x27;m preparing a degree level and i have to find user / password in clear text using POP.  Well, i did it, don&#x27;t have to be genius for that. But wanted to go further and find the attached file and rebild it. I tried with the magic number PK for .docx (delete all before PK, found by Follow TC...'''
date = "2015-09-30T08:39:00Z"
lastmod = "2015-10-15T14:09:00Z"
weight = 46281
keywords = [ ".docx", "magic_number", "attachment", "pk" ]
aliases = [ "/questions/46281" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Re bilt attached file from RAW](/questions/46281/re-bilt-attached-file-from-raw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46281-score" class="post-score" title="current number of votes">0</div><span id="post-46281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Bonjour,</p><p>I'm preparing a degree level and i have to find user / password in clear text using POP. Well, i did it, don't have to be genius for that. But wanted to go further and find the attached file and rebild it. I tried with the magic number PK for .docx (delete all before PK, found by Follow TCP Stream) but doesn't work for me. It seems that i have the begining "PK" but not "end" not the good one of course. I got the frames on the way out (while sending).</p><p>Can somebody tell me "where is the end" of the attached file. How should i proceed, which protocols to use to find it easier, where to put the analyser ...</p><p>And how to upload a file in Wireshark, please, would be easier for you with the file in front. PS: have two more questions, i'm not getting out... but one after another</p><p>best regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-.docx" rel="tag" title="see questions tagged &#39;.docx&#39;">.docx</span> <span class="post-tag tag-link-magic_number" rel="tag" title="see questions tagged &#39;magic_number&#39;">magic_number</span> <span class="post-tag tag-link-attachment" rel="tag" title="see questions tagged &#39;attachment&#39;">attachment</span> <span class="post-tag tag-link-pk" rel="tag" title="see questions tagged &#39;pk&#39;">pk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '15, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/75b1235cdca6afc5f90f1b32bcdd2cce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tome80&#39;s gravatar image" /><p><span>tome80</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tome80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '15, 10:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-46281" class="comments-container"><span id="46283"></span><div id="comment-46283" class="comment"><div id="post-46283-score" class="comment-score"></div><div class="comment-text"><p>You can share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc. and then edit your question with the link to the file.</p></div><div id="comment-46283-info" class="comment-info"><span class="comment-age">(30 Sep '15, 10:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="46309"></span><div id="comment-46309" class="comment"><div id="post-46309-score" class="comment-score"></div><div class="comment-text"><p>Any advice ? Do I do the rignt thing ?</p><ol><li>Follow TCP Stream</li><li>Save to RAW (last conversation)</li><li>Open with Hexaeditor</li><li>Cut before "PK"</li><li>Save to RAW</li><li>Base64 decode <a href="http://www.motobit.com/util/base64-decoder-encoder.asp">http://www.motobit.com/util/base64-decoder-encoder.asp</a></li><li>Save in .docx Doesn't work. I'm missing something cricial.</li></ol></div><div id="comment-46309-info" class="comment-info"><span class="comment-age">(01 Oct '15, 05:06)</span> <span class="comment-user userinfo">tome80</span></div></div><span id="46483"></span><div id="comment-46483" class="comment"><div id="post-46483-score" class="comment-score"></div><div class="comment-text"><p>Which TCP stream are you "following" in that pcap?</p></div><div id="comment-46483-info" class="comment-info"><span class="comment-age">(12 Oct '15, 15:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46580"></span><div id="comment-46580" class="comment"><div id="post-46580-score" class="comment-score"></div><div class="comment-text"><p>Bonsoir,</p><p>I follow the TCP Stream on pacjet 78 (DATA Fragment) where i can see the name of the attachment ...</p><p>check this link cause i changed the file (the other one i didnt remember where did i look for) so i made a new capture with my test accounts.</p><p><a href="https://www.cloudshark.org/captures/88d11775b31b">https://www.cloudshark.org/captures/88d11775b31b</a></p><p>thanks for your help</p><p>best regardes</p></div><div id="comment-46580-info" class="comment-info"><span class="comment-age">(15 Oct '15, 14:01)</span> <span class="comment-user userinfo">tome80</span></div></div></div><div id="comment-tools-46281" class="comment-tools"></div><div class="clear"></div><div id="comment-46281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46581"></span>

<div id="answer-container-46581" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46581-score" class="post-score" title="current number of votes">0</div><span id="post-46581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I can see this</p><p>Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document; name="Nutri group.docx" Content-Transfer-Encoding: base64 Content-Disposition: attachment; filename="Nutri group.docx"</p><p>and by editing from PK to the endn and then savig to .docx. I'can open the document. If PK is the begining and the end is not the end there must be some other "end" like "." the file is 1.56 Mo, maybe i should try only with few lines, but a real file is biggest chalenge.</p><p>best regardes</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '15, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/75b1235cdca6afc5f90f1b32bcdd2cce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tome80&#39;s gravatar image" /><p><span>tome80</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tome80 has no accepted answers">0%</span></p></div></div><div id="comments-container-46581" class="comments-container"></div><div id="comment-tools-46581" class="comment-tools"></div><div class="clear"></div><div id="comment-46581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

