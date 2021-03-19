+++
type = "question"
title = "Email attachment"
description = '''how to get the size of e-mail attachment? protocol is pop.. I have found the e-mail stream, I have also seen this: ------MIME delimiter for sendEmail-910493.736229004 Content-Type: application/pdf;  name=&quot;invitation.pdf&quot;  Content-Transfer-Encoding: base64 Content-Disposition: attachment; filename=&quot;i...'''
date = "2014-06-13T02:17:00Z"
lastmod = "2014-06-15T00:10:00Z"
weight = 33760
keywords = [ "incomingemail" ]
aliases = [ "/questions/33760" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Email attachment](/questions/33760/email-attachment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33760-score" class="post-score" title="current number of votes">0</div><span id="post-33760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to get the size of e-mail attachment? protocol is pop.. I have found the e-mail stream, I have also seen this: ------MIME delimiter for sendEmail-910493.736229004</p><p>Content-Type: application/pdf;</p><pre><code>    name=&quot;invitation.pdf&quot;</code></pre><p>Content-Transfer-Encoding: base64</p><p>Content-Disposition: attachment; filename="invitation.pdf"</p><p>but I dont know how to get the size of that attachment, does anyone know? any help is appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-incomingemail" rel="tag" title="see questions tagged &#39;incomingemail&#39;">incomingemail</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '14, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/0481ad9191f7aa22791404539802b06a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bishoy%20Atef&#39;s gravatar image" /><p><span>Bishoy Atef</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bishoy Atef has no accepted answers">0%</span></p></div></div><div id="comments-container-33760" class="comments-container"></div><div id="comment-tools-33760" class="comment-tools"></div><div class="clear"></div><div id="comment-33760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33770"></span>

<div id="answer-container-33770" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33770-score" class="post-score" title="current number of votes">1</div><span id="post-33770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bishoy Atef has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but I dont know how to get the size of that attachment, does anyone know? any help is appreciated.</p></blockquote><p>If there is no header that shows the length of the attachment (like "Content-Length"), you'll have to 'count' the bytes yourself, by doing the following:</p><ul><li>right click one of the POP3 frames</li><li>select "Follow TCP Stream"</li><li>in the pop-up windows, select the encoded bytes (base64 encoded) of the attachment</li><li>copy those bytes to the clipboard (CTRL-C)</li><li>go to <a href="http://www.motobit.com/util/base64-decoder-encoder.asp">http://www.motobit.com/util/base64-decoder-encoder.asp</a> or use the base64 decoder of your choice</li><li>paste the clipbaord into the blank white window</li><li>select the following options: 'decode the data from a Base64 string' and 'export to a binary file, filename:'</li><li>save the file 'base64.bin' when the pop-up appears.</li><li>check the file size of 'base64.bin'. <strong>That size is the answer to your question</strong></li></ul><p>You can test it with the following pop3 pcap file.</p><blockquote><p><a href="http://wiki.xplico.org/lib/exe/fetch.php?media=pcap:xplico.org_sample_capture_pop3_must_use_xplico_nc.cfg.pcap">http://wiki.xplico.org/lib/exe/fetch.php?media=pcap:xplico.org_sample_capture_pop3_must_use_xplico_nc.cfg.pcap</a></p></blockquote><p>Set the following display filter, to get the TCP stream with the attachment</p><blockquote><p>tcp.stream eq 2</p></blockquote><p>Then <strong>right-click</strong> one of the frames and select <strong>Follow TCP Stream</strong>. In the pop-up windows, click on <strong>Find</strong> and search for <strong>attachment</strong>. From the first occurrence, copy the attachment bytes.</p><pre><code>/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEP
ERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4e
.....
many more lines
.....
AhEBAxEB/8QAHAAAAQUBAQEAAAAAAAAAAAAABQIDBAYHAAEI/8QAThAAAgEDAwEGAwYEAwYEAwUJ
XHHV1dXVxx1dXV1ccdXV1dXHHV1dXVxx1dXV1ccdXV1dXHHV1dXVxx1dXV1ccdXV1dXHHV1dXVxx
1dXV1ccdXV1dXHHV1dXVxx1dXV1ccdXV1dXHHV1dXVxx1dXV1ccdXV1dXHH/2Q==
--00151747362a0e2e0d047a4eb121--  &lt;=== NOT this line !!!</code></pre><p>The last line is the end marker for the MIME encoded attachment. Don't copy that line. Then just follow the steps described above. You should get a file named base64.bin, with a size of ~ 71,5 KByte.</p><p>Alternatively, you can use other tools to extract the attachment from the POP3 stream (not sure which of the following actually do support POP3 - I believe Xplico).</p><p>Xplico - the tool that provided the POP3 sample capture file above.</p><blockquote><p><a href="http://www.xplico.org">http://www.xplico.org</a></p></blockquote><p>Some other tools (NetworkMiner, tcpxtract, etc.) here:</p><blockquote><p><a href="https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961">https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961</a></p></blockquote><p>NetWitness Investigator (now part of EMC, but still available as Freeware). Hint: Download and save that tool, as long as EMC is providing the download ;-))</p><blockquote><p><a href="http://download.netwitness.com">http://download.netwitness.com</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '14, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '14, 07:58</strong> </span></p></div></div><div id="comments-container-33770" class="comments-container"><span id="33812"></span><div id="comment-33812" class="comment"><div id="post-33812-score" class="comment-score"></div><div class="comment-text"><p>thank you very much for your reply, that really helps.</p></div><div id="comment-33812-info" class="comment-info"><span class="comment-age">(15 Jun '14, 00:10)</span> <span class="comment-user userinfo">Bishoy Atef</span></div></div></div><div id="comment-tools-33770" class="comment-tools"></div><div class="clear"></div><div id="comment-33770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

