+++
type = "question"
title = "Extract an attachment from a sniffed SMTP session"
description = '''While going through an Intrusion Analysis course I have encountered a demo on how to use Wireshark to extract an attachment from a sniffed SMTP session. For some reason even though I follow the process indicated in the lecture, which appears more than reasonable to me, I always end up with the creat...'''
date = "2017-05-02T10:24:00Z"
lastmod = "2017-05-02T13:53:00Z"
weight = 61169
keywords = [ "base64", "smtp", "attachment", "tcp", "linux" ]
aliases = [ "/questions/61169" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extract an attachment from a sniffed SMTP session](/questions/61169/extract-an-attachment-from-a-sniffed-smtp-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61169-score" class="post-score" title="current number of votes">0</div><span id="post-61169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While going through an Intrusion Analysis course I have encountered a demo on how to use Wireshark to extract an attachment from a sniffed SMTP session. For some reason even though I follow the process indicated in the lecture, which appears more than reasonable to me, I always end up with the creation of a corrupted attachment (PDF). Please refer to the below packet capture</p><p><a href="https://www.dropbox.com/s/y8s0zl3fvrcoict/carve-smtp.pcap?dl=0">https://www.dropbox.com/s/y8s0zl3fvrcoict/carve-smtp.pcap?dl=0</a></p><p>The process described in the lecture boils down to 5 points</p><p><strong>1)</strong> Use Analyze &gt; Follow TCP Stream to see the conversation</p><p><strong>2)</strong> Save the whole conversation in raw format (the attachment is obviously inside, base64 encoded). Let’s call it carve.raw</p><p><strong>3)</strong> Carve out everything apart from the base64 encoding</p><p><strong>4)</strong> Remove the ^M characters in the file (result of different line endings used in Windows and Linux) and save it. It can be done quickly in vi with</p><pre><code>:%s/^M//g</code></pre><p><strong>5)</strong> Use base64 to decode the encoded attachment in this way</p><pre><code>base64 -d carve.raw &gt; attached.pdf</code></pre><p>(it is said that the attachment is a PDF)</p><p>Point 5 is where I immediately understand that something is wrong as the output I get is</p><blockquote><p>base64: invalid input</p></blockquote><p>Nevertheless, the attachment file is created and, when I try to open it, I receive the information that the file is corrupted.</p><p>Does anybody know what I am missing?</p><p>P.S: Even though I would like to keep this exercise “low-level” (as manual as possible), I have tried to extract the file with Foremost as well and it failed to identify anything.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-base64" rel="tag" title="see questions tagged &#39;base64&#39;">base64</span> <span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span> <span class="post-tag tag-link-attachment" rel="tag" title="see questions tagged &#39;attachment&#39;">attachment</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '17, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/f4f56e956625e14b8d65d397f52ecb47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="squalodelfilo&#39;s gravatar image" /><p><span>squalodelfilo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="squalodelfilo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 May '17, 12:38</strong> </span></p></div></div><div id="comments-container-61169" class="comments-container"></div><div id="comment-tools-61169" class="comment-tools"></div><div class="clear"></div><div id="comment-61169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61172"></span>

<div id="answer-container-61172" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61172-score" class="post-score" title="current number of votes">0</div><span id="post-61172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="squalodelfilo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The steps described are ok. However a possible bug may playing tricks on youl.</p><p>After "Follow TCP Stream" I switched the view to one flow direction =&gt; '10.10.10.10:34573 -&gt; 10.10.10.25:25' and saved this content as ASCII to file (carve.b64).</p><p>When opening this file in an editor the content is duplicated, the first one with ^M, the second one without it. This looks like a Wireshark bug for me.</p><p>After removing everything before and after the second base64 part and saving it, I can run base64 -d without any problem.</p><p>I get a PDF file showing the dos2unix manpage.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '17, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-61172" class="comments-container"><span id="61174"></span><div id="comment-61174" class="comment"><div id="post-61174-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I had overlooked that second part. I managed to decode it successfully.</p></div><div id="comment-61174-info" class="comment-info"><span class="comment-age">(02 May '17, 13:53)</span> <span class="comment-user userinfo">squalodelfilo</span></div></div></div><div id="comment-tools-61172" class="comment-tools"></div><div class="clear"></div><div id="comment-61172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

