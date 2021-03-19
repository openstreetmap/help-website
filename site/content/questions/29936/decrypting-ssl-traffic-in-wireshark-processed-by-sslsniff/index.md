+++
type = "question"
title = "Decrypting SSL Traffic in Wireshark processed by sslsniff"
description = '''Hi there, to analyze some application, which are using https to communicate i had set up a little proxy which redirects the traffic to sslsniff and forwards it afterwards. Currently i&#x27;m running sslsniff in authority mode with a self signed CA. In this mode sslsniff automatically generates mathing ce...'''
date = "2014-02-17T08:24:00Z"
lastmod = "2014-02-19T06:09:00Z"
weight = 29936
keywords = [ "ssl", "sslsniff", "wireshark" ]
aliases = [ "/questions/29936" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypting SSL Traffic in Wireshark processed by sslsniff](/questions/29936/decrypting-ssl-traffic-in-wireshark-processed-by-sslsniff)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29936-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>to analyze some application, which are using https to communicate i had set up a little proxy which redirects the traffic to sslsniff and forwards it afterwards.</p><p>Currently i'm running sslsniff in authority mode with a self signed CA. In this mode sslsniff automatically generates mathing certificates which are then signed with the own CA.</p><p>The tool works fine, unfortunately parsing the output is a little bit nasty, since sslsniff drops the traffic simply as a txt file instead of dumping all traffic in a valid pcap file.</p><p>Now i'm searching for a way to get that ssl cracked traffic dumped into a pcap file in order to decrypt it properly in wireshark with the SSL dissector. Therefore i need a valid private Key (i assume the private key from the generated certificate and not the one provided by the fake CA). In authority mode the generated ca is dumped at no place, so there is also no private key available to set it in wireshark ssl settings.</p><p>What can i do to get all this traffic decrypted in wireshark in this scenario?</p><p>Best Regards Bastian</p></div><div id="question-tags" class="tags-container tags">ssl sslsniff wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '14, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/1cd9e3324f5061cdcb2ea68cb5fe8a01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CipherSpec&#39;s gravatar image" /><p>CipherSpec<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CipherSpec has no accepted answers">0%</span></p></div></div><div id="comments-container-29936" class="comments-container"></div><div id="comment-tools-29936" class="comment-tools"></div><div class="clear"></div><div id="comment-29936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30004"></span>

<div id="answer-container-30004" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30004-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>In authority mode the generated ca is dumped at no place</strong>, so there is also no private key available to set it in wireshark ssl settings.</p></blockquote><p>That's right. So, you need a way to get the keying material. There are some options I can think of:</p><ul><li>use a different SSL interception tool, like <a href="http://www.telerik.com/fiddler">Fiddler</a> or other tools.</li><li>rewrite the code of <a href="http://www.thoughtcrime.org/software/sslsniff/">sslsniff</a> to dump the keying material</li><li>let your client (Browser) dump the session keys (see: <strong><a href="http://www.root9.net/2012/11/ssl-decryption-with-wireshark-private.html">SSLKEYLOGFILE</a></strong> and a <a href="http://ask.wireshark.org/questions/10730/how-to-config-master-key-and-session-id-in-wireshark">similar question</a>. Then use the dumped keys to decrypt the session with Wireshark.</li><li>hook the crypto API calls to dump the keys. There is a workaround on Linux for sslsniff. Looks kind of 'creepy', but it seems to work: <strong><a href="http://diablohorn.wordpress.com/2013/07/14/sslsniff-howto-dump-the-temporary-key/">http://diablohorn.wordpress.com/2013/07/14/sslsniff-howto-dump-the-temporary-key/</a></strong></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '14, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30004" class="comments-container"><span id="30710"></span><div id="comment-30710" class="comment"><div id="post-30710-score" class="comment-score"></div><div class="comment-text"><blockquote><p>hook the crypto API calls to dump the keys. There is a workaround on Linux for sslsniff. Looks kind of 'creepy', but it seems to work: <a href="http://diablohorn.wordpress.com/2013/07/14/sslsniff-howto-dump-the-temporary-key/">http://diablohorn.wordpress.com/2013/07/14/sslsniff-howto-dump-the-temporary-key/</a></p></blockquote><p>But in this case the creepy way has been the best way! Works like a charm and is very helpful.</p><blockquote><p>let your client (Browser) dump the session keys (see: SSLKEYLOGFILE and a similar question. Then use the dumped keys to decrypt the session with Wireshark.</p></blockquote><p>The problem here is that new versions of firefox do not dump the keys anymore. As well you cannot consider traffic which isn't transmitted via browser (e.g. TLS IMAP Traffic)</p><blockquote><p>rewrite the code of sslsniff to dump the keying material</p></blockquote><p>It seems that this step is absolutely necessary. Although the tool works fine the error handling as a little bit poor.</p><blockquote><p>use a different SSL interception tool, like Fiddler or other tools.</p></blockquote><p>Likewise possible, but fiddler is not very nice to handle at linux operating systems. So if can recommend the creepy way.</p><p>Thank you very much!</p></div><div id="comment-30710-info" class="comment-info"><span class="comment-age">(12 Mar '14, 02:09)</span> CipherSpec</div></div></div><div id="comment-tools-30004" class="comment-tools"></div><div class="clear"></div><div id="comment-30004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

