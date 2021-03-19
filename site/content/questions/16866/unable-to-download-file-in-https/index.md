+++
type = "question"
title = "Unable to download file in HTTPS"
description = '''Hi  We are facing some issue in which client(browser IE8) intermittently fails to download file over HTTPS. First time it successfully downloads the file on subsequent attempt it downloads the file partially 50MB out of 133 MB and says download is successful. wireshark dump says that after some time...'''
date = "2012-12-14T04:21:00Z"
lastmod = "2012-12-14T10:35:00Z"
weight = 16866
keywords = [ "download", "https", "file", "intermittent" ]
aliases = [ "/questions/16866" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to download file in HTTPS](/questions/16866/unable-to-download-file-in-https)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16866-score" class="post-score" title="current number of votes">0</div><span id="post-16866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>We are facing some issue in which client(browser IE8) intermittently fails to download file over HTTPS. First time it successfully downloads the file on subsequent attempt it downloads the file partially 50MB out of 133 MB and says download is successful.</p><p>wireshark dump says that after some time client sends FIN, ACK</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-intermittent" rel="tag" title="see questions tagged &#39;intermittent&#39;">intermittent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '12, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/f8c9e56aea64888b46c5f01959eb6e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lodha13&#39;s gravatar image" /><p><span>lodha13</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lodha13 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '12, 04:22</strong> </span></p></div></div><div id="comments-container-16866" class="comments-container"></div><div id="comment-tools-16866" class="comment-tools"></div><div class="clear"></div><div id="comment-16866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16877"></span>

<div id="answer-container-16877" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16877-score" class="post-score" title="current number of votes">0</div><span id="post-16877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That sounds like a cache issue. Do you use any HTTP caches? If so, did you try to clear those caches?</p><p>If that does not solve the problem, we really need more information. If possible, post the capture file somewhere (one-click hoster or <a href="http://cloudshark.org">cloudshark.org</a>). Beware privacy issues with the content in the capture file!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16877" class="comments-container"><span id="16896"></span><div id="comment-16896" class="comment"><div id="post-16896-score" class="comment-score"></div><div class="comment-text"><p>Thanks for replying. Issue is only seen in HTTPS not in HTTP, I have cleared the browser cache but even then the issue occurs.</p><p>I understand that without network capture it is difficult to investigate but capture contains confidential information.</p><p>I can tell you about packet capture, Client is receiving data which can be seen by acknowledment number but just at 40.7 MB client sends FIN, ACK and then eventually closes the connection.</p><p>Sometimes client sends RST, ACK.</p><p>Can you tell me how client knows that it has received the complete file and it has to end the connection now.</p><p>I mean at 41.7 MB only that condition occurs which tells the client that it has received the complete file and has to end the connection. (just a thought)</p></div><div id="comment-16896-info" class="comment-info"><span class="comment-age">(14 Dec '12, 08:36)</span> <span class="comment-user userinfo">lodha13</span></div></div><span id="16902"></span><div id="comment-16902" class="comment"><div id="post-16902-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I understand that without network capture it is difficult to investigate but capture contains confidential information.</p></blockquote><p>If it's HTTPS (encrypted data, nobody can read it), how confidential can it be? ;-)) If you are concerned regarding the IP addresses, I suggest to use a pcap anonymization tool.</p><p>BTW: Do you have access to the server private key to decrypt the HTTPS data stream? If no, then you will probably have a hard time to analyze the problem. In that case I suggest to use Fiddler2 (google it) to analyze the problem.</p></div><div id="comment-16902-info" class="comment-info"><span class="comment-age">(14 Dec '12, 10:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16903"></span><div id="comment-16903" class="comment"><div id="post-16903-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Can you tell me how client knows that it has received the complete file and it has to end the connection now.</p></blockquote><p>well, if it's really the client who ends the connection (I can't confirm without a capture file), then 'something' within the client leads to this decision. This could be:</p><ul><li>a timeout condition on the client</li><li>the client thinks it has downloaded the whole file (due to a size information from the server when it requested the "file").</li><li>the client has no space left on disk to write the (temp) file</li><li>some security software at the client (AV, IDS, Endpoint Security) closes the connection as it believes to have found malware, an attack, etc.</li></ul><p>So, there are numerous reasons for that kind of behaviour.</p><p>Is this a plain file download or some web application with code on the client (Java, Javascript)?</p></div><div id="comment-16903-info" class="comment-info"><span class="comment-age">(14 Dec '12, 10:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16877" class="comment-tools"></div><div class="clear"></div><div id="comment-16877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

