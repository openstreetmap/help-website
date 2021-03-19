+++
type = "question"
title = "extract an attachment email (SMTP)  .cap"
description = '''hey, I ve an e-mail capture (SMTP) with an attached photo (secret.rtf), how to extract this file ??  http://posting.org/image/pz9dzx9uh'''
date = "2014-05-26T12:12:00Z"
lastmod = "2014-06-02T04:02:00Z"
weight = 33094
keywords = [ "capture", "smtp", "extract", "attachment" ]
aliases = [ "/questions/33094" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [extract an attachment email (SMTP) .cap](/questions/33094/extract-an-attachment-email-smtp-cap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33094-score" class="post-score" title="current number of votes">0</div><span id="post-33094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hey,</p><p>I ve an e-mail capture (SMTP) with an attached photo (secret.rtf),</p><p>how to extract this file ??<br />
</p><p><a href="http://posting.org/image/pz9dzx9uh">http://posting.org/image/pz9dzx9uh</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-attachment" rel="tag" title="see questions tagged &#39;attachment&#39;">attachment</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '14, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/c9d613756951f311b4e93da5854e8ac4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mahfoudi%20Mohamed&#39;s gravatar image" /><p><span>Mahfoudi Moh...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mahfoudi Mohamed has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 May '14, 17:19</strong> </span></p></div></div><div id="comments-container-33094" class="comments-container"></div><div id="comment-tools-33094" class="comment-tools"></div><div class="clear"></div><div id="comment-33094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33195"></span>

<div id="answer-container-33195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33195-score" class="post-score" title="current number of votes">2</div><span id="post-33195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How use NetworkMiner ( <a href="http://sourceforge.net/projects/networkminer/">http://sourceforge.net/projects/networkminer/</a> )</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '14, 03:10</strong></p><img src="https://secure.gravatar.com/avatar/d62b869ec385c6bbc2c04dc7176e8ea8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexis%20La%20Goutte&#39;s gravatar image" /><p><span>Alexis La Go...</span><br />
<span class="score" title="110 reputation points">110</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexis La Goutte has one accepted answer">25%</span></p></div></div><div id="comments-container-33195" class="comments-container"><span id="33222"></span><div id="comment-33222" class="comment"><div id="post-33222-score" class="comment-score"></div><div class="comment-text"><p>hey, thanks for your reply<br />
</p><p>NetworkMiner<br />
(error opening pcap file ...) juste for .pcap (i've .cap) // pcapng.com gives Invalid PcapNg file</p><p>tcpxtract<br />
<span class="__cf_email__" data-cfemail="0f7d60607b4f646e6366">[email protected]</span>:#tcpxtract --file d.cap --output output //Couldn't open file d.cap: unknown file format</p><p>foremost <span class="__cf_email__" data-cfemail="a1d3ceced5e1cac0cdc8">[email protected]</span>:#foremost -v -i d.raw 0 FILES EXTRACTED</p><p>tcpflow -r d.cap tcpflow[3850]: unknown file format</p><p>...!!</p></div><div id="comment-33222-info" class="comment-info"><span class="comment-age">(30 May '14, 12:34)</span> <span class="comment-user userinfo">Mahfoudi Moh...</span></div></div><span id="33266"></span><div id="comment-33266" class="comment"><div id="post-33266-score" class="comment-score"></div><div class="comment-text"><p>NetworkMiner works great, you'll just have to convert the PcapNG file to PCAP first. Use Wireshark's File &gt; Save As and select libpcap format in the File format drop down list.</p><p>You can also convert the PcapNG file online at <a href="http://pcapng.com">http://pcapng.com</a></p><p>Kurt's suggestion to use editcap also works fine of course!</p></div><div id="comment-33266-info" class="comment-info"><span class="comment-age">(02 Jun '14, 04:02)</span> <span class="comment-user userinfo">Netresec_LJ</span></div></div></div><div id="comment-tools-33195" class="comment-tools"></div><div class="clear"></div><div id="comment-33195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33096"></span>

<div id="answer-container-33096" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33096-score" class="post-score" title="current number of votes">0</div><span id="post-33096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use Wireshark and do it manually: Select one frame of the SMTP conversation. Then right click it and select <strong>Follow TCP Stream</strong>. In the pop-up window, copy the encoded file (Windows selection and copy mechanisms - CTRL-C, etc.) and save the content to disk. Then use a decoder to extract the file itself (either local tool or online - search for "MIME UUDECODE BASE64 online").</p><p>Sample capture to test with:</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=sample-TNEF.pcap.gz">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=sample-TNEF.pcap.gz</a></p></blockquote><p><img src="https://osqa-ask.wireshark.org/upfiles/smtp_extract.png" alt="alt text" /></p><p>Alternatively please check my answer to the following question, for external tools.</p><blockquote><p><a href="http://ask.wireshark.org/questions/31557/how-to-extract-email-files/31565">http://ask.wireshark.org/questions/31557/how-to-extract-email-files/31565</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '14, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '14, 07:10</strong> </span></p></div></div><div id="comments-container-33096" class="comments-container"><span id="33231"></span><div id="comment-33231" class="comment"><div id="post-33231-score" class="comment-score"></div><div class="comment-text"><p>I just realized, that the link to my answer of another questions did not work. I fixed it.</p><p>In that answer you'll find some links to data extraction tools (including Networkminer). Some of them do support pcap-ng, some don't.</p><p>If you convert your pcap-ng to pcap, you can use anyone of the mentioned tools.</p><blockquote><p>editcap -F pcap input.pcapng output.pcap</p></blockquote></div><div id="comment-33231-info" class="comment-info"><span class="comment-age">(31 May '14, 07:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-33096" class="comment-tools"></div><div class="clear"></div><div id="comment-33096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

