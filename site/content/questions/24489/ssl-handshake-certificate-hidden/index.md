+++
type = "question"
title = "SSL Handshake Certificate hidden"
description = '''i cannot figure out why when i apply the filter ssl.handshake.certificate to a trace i see nothing and others in the same unit with the same trace see the packets. is there a setting to ignore or hide these packets?'''
date = "2013-09-09T10:21:00Z"
lastmod = "2013-09-10T14:59:00Z"
weight = 24489
keywords = [ "ssl", "handshake", "hidden", "certificate", "openssl" ]
aliases = [ "/questions/24489" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Handshake Certificate hidden](/questions/24489/ssl-handshake-certificate-hidden)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24489-score" class="post-score" title="current number of votes">0</div><span id="post-24489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i cannot figure out why when i apply the filter ssl.handshake.certificate to a trace i see nothing and others in the same unit with the same trace see the packets. is there a setting to ignore or hide these packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-hidden" rel="tag" title="see questions tagged &#39;hidden&#39;">hidden</span> <span class="post-tag tag-link-certificate" rel="tag" title="see questions tagged &#39;certificate&#39;">certificate</span> <span class="post-tag tag-link-openssl" rel="tag" title="see questions tagged &#39;openssl&#39;">openssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '13, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/442f93f3d125b99268f8fcf4578b4f1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mhumphries73&#39;s gravatar image" /><p><span>mhumphries73</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mhumphries73 has no accepted answers">0%</span></p></div></div><div id="comments-container-24489" class="comments-container"></div><div id="comment-tools-24489" class="comment-tools"></div><div class="clear"></div><div id="comment-24489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="24490"></span>

<div id="answer-container-24490" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24490-score" class="post-score" title="current number of votes">0</div><span id="post-24490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is your session using a well-known ssl port number like 443? Otherwise you need to use the 'decode as' function and map the connection to SSL protocol</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-24490" class="comments-container"><span id="24492"></span><div id="comment-24492" class="comment"><div id="post-24492-score" class="comment-score"></div><div class="comment-text"><p>it is not however i have added the port (7043) to the http protocol information in preferences ( i also tried the decode as ) still nothing.</p></div><div id="comment-24492-info" class="comment-info"><span class="comment-age">(09 Sep '13, 13:20)</span> <span class="comment-user userinfo">mhumphries73</span></div></div><span id="24529"></span><div id="comment-24529" class="comment"><div id="post-24529-score" class="comment-score"></div><div class="comment-text"><p>can you add a screenshot of your wireshark showing the ssl packet and possibly provide the trace file on www.cloudshark.org</p></div><div id="comment-24529-info" class="comment-info"><span class="comment-age">(10 Sep '13, 09:17)</span> <span class="comment-user userinfo">mrEEde2</span></div></div></div><div id="comment-tools-24490" class="comment-tools"></div><div class="clear"></div><div id="comment-24490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24499"></span>

<div id="answer-container-24499" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24499-score" class="post-score" title="current number of votes">0</div><span id="post-24499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please make sure you have the following protocol settings configured:</p><ul><li>IP: disable "Validate the IPv4 checksum if possible"</li><li>TCP: disable "Validate the TCP checksum if possible"</li><li>TCP: enable "Allow subdissector to reassemble TCP streams"</li><li>SSL: enable "Reassemble SSL records spanning multiple TCP segments"</li><li>SSL: enable "Reassemble SSL Application Data spanning multiple SSL records" (not strictly needed for displaying the certificate message, but might be needed for decryption application data)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-24499" class="comments-container"><span id="24528"></span><div id="comment-24528" class="comment"><div id="post-24528-score" class="comment-score"></div><div class="comment-text"><p>•TCP: enable "Allow subdissector to reassemble TCP streams" had to be changed but that did not correct the issue :(</p></div><div id="comment-24528-info" class="comment-info"><span class="comment-age">(10 Sep '13, 09:02)</span> <span class="comment-user userinfo">mhumphries73</span></div></div><span id="24532"></span><div id="comment-24532" class="comment"><div id="post-24532-score" class="comment-score"></div><div class="comment-text"><p>One more setting that might be of influence (where there are retransmissions or duplicate packets in the trace):</p><p>TCP: enable "Do not call subdissectors for error packets"</p></div><div id="comment-24532-info" class="comment-info"><span class="comment-age">(10 Sep '13, 11:05)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-24499" class="comment-tools"></div><div class="clear"></div><div id="comment-24499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24524"></span>

<div id="answer-container-24524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24524-score" class="post-score" title="current number of votes">0</div><span id="post-24524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is there a setting to ignore or hide these packets?<br />
i have added the port (7043) to the http protocol information in preferences ( i also tried the decode as ) still nothing.</p></blockquote><p>maybe the SSL dissector is disabled on your system. Please check:</p><blockquote><p>Analyze -&gt; Enabled Protocols -&gt; SSL</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '13, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Sep '13, 07:20</strong> </span></p></div></div><div id="comments-container-24524" class="comments-container"><span id="24527"></span><div id="comment-24527" class="comment"><div id="post-24527-score" class="comment-score"></div><div class="comment-text"><p>verified that this setting is enabled</p></div><div id="comment-24527-info" class="comment-info"><span class="comment-age">(10 Sep '13, 08:28)</span> <span class="comment-user userinfo">mhumphries73</span></div></div><span id="24537"></span><div id="comment-24537" class="comment"><div id="post-24537-score" class="comment-score"></div><div class="comment-text"><p>as you have checked and tested several options, I suggest to compare the settings of your colleagues with your settings.</p><p>So, please get a copy of their Wireshark settings (%APPDATA%\Wireshark*) and compare that with your settings. You can use a visual diff tool for that, like WinMerge (<a href="http://winmerge.org">http://winmerge.org</a>)</p></div><div id="comment-24537-info" class="comment-info"><span class="comment-age">(10 Sep '13, 14:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24524" class="comment-tools"></div><div class="clear"></div><div id="comment-24524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

