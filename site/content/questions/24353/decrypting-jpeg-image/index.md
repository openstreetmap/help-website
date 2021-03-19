+++
type = "question"
title = "Decrypting jpeg image"
description = '''I have extracted the output of a pcap file, where it has encrypted jpeg image inside a word .doc &amp;amp; also .jpeg. How can I extract the same ? '''
date = "2013-09-04T09:29:00Z"
lastmod = "2013-09-05T04:36:00Z"
weight = 24353
keywords = [ "jpeg", "extracting" ]
aliases = [ "/questions/24353" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting jpeg image](/questions/24353/decrypting-jpeg-image)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24353-score" class="post-score" title="current number of votes">0</div><span id="post-24353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have extracted the output of a pcap file, where it has encrypted jpeg image inside a word .doc &amp; also .jpeg. How can I extract the same ?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jpeg" rel="tag" title="see questions tagged &#39;jpeg&#39;">jpeg</span> <span class="post-tag tag-link-extracting" rel="tag" title="see questions tagged &#39;extracting&#39;">extracting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '13, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/e3b0323745a98f44e1e5de8a081bf52c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vj%20kumar&#39;s gravatar image" /><p><span>vj kumar</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vj kumar has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-24353" class="comments-container"><span id="24354"></span><div id="comment-24354" class="comment"><div id="post-24354-score" class="comment-score"></div><div class="comment-text"><p>can you rephrase your question? It is a bit hard to understand what you're trying to accomplish, and what the problem is.</p></div><div id="comment-24354-info" class="comment-info"><span class="comment-age">(04 Sep '13, 13:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="24356"></span><div id="comment-24356" class="comment"><div id="post-24356-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, I have got a captured pcap of a mail transaction. I have followed the SMTP's and obtained details about the mail, wherein it contains 4 encrypted files compressed in.rar format, which was also extracted with the mentioned . Now three files inside .rar has encrypted files..(picture.jpeg and file.docx contains a white image file)..now how can I decrypt the image file ?</p></div><div id="comment-24356-info" class="comment-info"><span class="comment-age">(04 Sep '13, 14:01)</span> <span class="comment-user userinfo">vj kumar</span></div></div></div><div id="comment-tools-24353" class="comment-tools"></div><div class="clear"></div><div id="comment-24353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24358"></span>

<div id="answer-container-24358" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24358-score" class="post-score" title="current number of votes">0</div><span id="post-24358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>it <strong>contains</strong> 4 <strong>encrypted files</strong> compressed <strong>in.rar</strong> format, .... now how can I decrypt the image file ?</p></blockquote><p>by opening the rar file with WinRar and by entering the encryption key when WinRar asks for it!?!</p><p>If the rar file is not encrypted itself, you'll have to ask the sender of the email how he/she encrypted the files and also for the key. With that information you should be able to decrypt the files.</p><p>BTW: Obviously you already managed to extract the rar file from the SMTP conversation. So, how is this problem related to Wireshark?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '13, 15:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24358" class="comments-container"><span id="24369"></span><div id="comment-24369" class="comment"><div id="post-24369-score" class="comment-score"></div><div class="comment-text"><p>Kurt, the problem doesn't exist with the wireshark...And moreover I have no clue to whome this pcap beloongs to..:).... Encrypted here, I'm not mentioning the "file.rar" password encryption, but its the "image.jpeg" &amp; "file.docx" which is obtained after extracting the file.rar. May be I can tell you the image is hidden inside the file.docx. I can just see a blank white space. So how this can be decrypted and I can see the image ?</p></div><div id="comment-24369-info" class="comment-info"><span class="comment-age">(04 Sep '13, 21:08)</span> <span class="comment-user userinfo">vj kumar</span></div></div><span id="24375"></span><div id="comment-24375" class="comment"><div id="post-24375-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Kurt, the problem doesn't exist with the wireshark...</p></blockquote><p>hm... well, this is a Q&amp;A site for Wireshark. So, if there is no problem with Wireshark, it might be the wrong place to ask !?!</p><blockquote><p>May be I can tell you the image is hidden inside the file.<strong>docx</strong>. I <strong>can just see a blank white space</strong>. So how this can be decrypted and I can see the image ?</p></blockquote><p>That sounds like a Microsoft Office problem to me and I'm sure you will get an answer in a Microsoft Word forum.</p></div><div id="comment-24375-info" class="comment-info"><span class="comment-age">(05 Sep '13, 04:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24358" class="comment-tools"></div><div class="clear"></div><div id="comment-24358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

