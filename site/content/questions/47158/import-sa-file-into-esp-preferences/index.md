+++
type = "question"
title = "Import SA file into ESP preferences"
description = '''Hi there, I am looking to decrypt some IPSec traffic. I have the capture file, the associated .SA file and the encryption key. The problem is that from what I can see every single line of the 33 SAs has to be entered into the ESP preferences in Wireshark - piece by piece. Is there an easier way to g...'''
date = "2015-11-02T08:47:00Z"
lastmod = "2015-11-02T16:04:00Z"
weight = 47158
keywords = [ "sa", "ipsec", "decrypt", "esp" ]
aliases = [ "/questions/47158" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import SA file into ESP preferences](/questions/47158/import-sa-file-into-esp-preferences)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47158-score" class="post-score" title="current number of votes">0</div><span id="post-47158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I am looking to decrypt some IPSec traffic. I have the capture file, the associated .SA file and the encryption key. The problem is that from what I can see every single line of the 33 SAs has to be entered into the ESP preferences in Wireshark - piece by piece. Is there an easier way to get the information from the SA file to the ESP preferences - perhaps via an import or some other means? Having that many SAs means a whole lot of data to manually enter which makes for potential errors.</p><p>Any information would be appreciated.</p><p>Thanks,</p><p>Les</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sa" rel="tag" title="see questions tagged &#39;sa&#39;">sa</span> <span class="post-tag tag-link-ipsec" rel="tag" title="see questions tagged &#39;ipsec&#39;">ipsec</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-esp" rel="tag" title="see questions tagged &#39;esp&#39;">esp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '15, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/a74a5b95b8189417af34ba767b20efa6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LesJarvis&#39;s gravatar image" /><p><span>LesJarvis</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LesJarvis has no accepted answers">0%</span></p></div></div><div id="comments-container-47158" class="comments-container"></div><div id="comment-tools-47158" class="comment-tools"></div><div class="clear"></div><div id="comment-47158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47160"></span>

<div id="answer-container-47160" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47160-score" class="post-score" title="current number of votes">0</div><span id="post-47160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no import function, but you can create the file manually. See my answer to a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/22874/tshark-decrypt-esp-packets-with-command-line-arguments">https://ask.wireshark.org/questions/22874/tshark-decrypt-esp-packets-with-command-line-arguments</a><br />
</p></blockquote><p><strong>++UPDATE++</strong></p><p>After reading my own post again, I realized that the path to the file is not that clear.</p><p>It's the in user preferences directory. You'll see the path to that directory in the Help menu.</p><blockquote><p>Help -&gt; About Wireshark -&gt; Folder [Tab] -&gt; Personal Configuration<br />
</p></blockquote><p>Take that folder and add the file name <strong>esp_sa</strong> to it.</p><p>On Windows it's usually:</p><blockquote><p>%APPDATA%\Wireshark\esp_sa</p></blockquote><p>unless you are working with profiles in Wireshark, then it's</p><blockquote><p>%APPDATA%\Wireshark\xxxxx\esp_sa</p></blockquote><p>While xxxxx is the name of the profile.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '15, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Nov '15, 09:03</strong> </span></p></div></div><div id="comments-container-47160" class="comments-container"><span id="47169"></span><div id="comment-47169" class="comment"><div id="post-47169-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt - I appreciate the help! I was able to generate a working esp_sa file by exporting the appropriate data from Excel.</p><p>Les</p></div><div id="comment-47169-info" class="comment-info"><span class="comment-age">(02 Nov '15, 12:20)</span> <span class="comment-user userinfo">LesJarvis</span></div></div><span id="47173"></span><div id="comment-47173" class="comment"><div id="post-47173-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-47173-info" class="comment-info"><span class="comment-age">(02 Nov '15, 16:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47160" class="comment-tools"></div><div class="clear"></div><div id="comment-47160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

