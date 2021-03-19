+++
type = "question"
title = "SSL decryption log file"
description = '''I&#x27;m totally new to Wireshark, and I don&#x27;t know much about network protocols in general. Here&#x27;s my situation: I&#x27;m trying to decrypt an SSL packet capture session. The traffic I&#x27;m trying to decrypt comes from the internet, and goes to an application running on my PC. I&#x27;ve found a number of different p...'''
date = "2013-03-16T13:34:00Z"
lastmod = "2013-03-16T15:08:00Z"
weight = 19570
keywords = [ "ssl" ]
aliases = [ "/questions/19570" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SSL decryption log file](/questions/19570/ssl-decryption-log-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm totally new to Wireshark, and I don't know much about network protocols in general. Here's my situation: I'm trying to decrypt an SSL packet capture session. The traffic I'm trying to decrypt comes from the internet, and goes to an application running on my PC. I've found a number of different private keys and certificate files in the application directory, and I'm not really sure which one would be the right one to use, but that's kind of beside the point right now.<br />
</p><p>I've searched a lot here, and I've found a bunch of questions that begin with the asker posting their SSL debug log file. I've noticed that all of these logs begin with something like the following:</p><pre><code>ssl_association_remove removing TCP 443 - data handle xx
Private key imported: KeyID xxxx...
ssl_load_key: swapping p and q parameters and recomputing u
ssl_init IPv4 addr &#39;192.xxx.xxx.xxx&#39; (xxx.xxx.xxx.xxx) port &#39;443&#39; filename &#39;C:\x.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file C:\x.pem successfully loaded.
association_add TCP port 443 protocol data handle xx</code></pre><p>My log file, however, doesn't have that. It just begins with 1 blank line, and then:</p><pre><code>dissect_ssl enter frame #8 (first time)</code></pre><p>So my question is, what is the significance of the absence of the information in the larger of the 2 log snippets above? I'm guessing this may have something to do with why I can't get the SSL decryption to work, so I figured I'd ask about it, and that it might be a good first step in figuring all this out. Thanks a lot.</p><p>Edit: just to give you bit more of an idea of my level of knowledge, I've been reading the SSL entry on Wikipedia, and I read Sake Blok's presentation on SSL decryption (<a href="http://sharkfest.wireshark.org/sharkfest.12/presentations/MB-1_SSL_Troubleshooting_with%20_Wireshark_Software.pdf).">http://sharkfest.wireshark.org/sharkfest.12/presentations/MB-1_SSL_Troubleshooting_with%20_Wireshark_Software.pdf).</a> I thought his presentation was informative, but there was a lot of stuff that went over my head, because I know so little about all this.</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '13, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/f1e3f650da5cc31a11f1d32ab15e69f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sandwiches9&#39;s gravatar image" /><p>sandwiches9<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sandwiches9 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Mar '13, 14:34</p></div></div><div id="comments-container-19570" class="comments-container"></div><div id="comment-tools-19570" class="comment-tools"></div><div class="clear"></div><div id="comment-19570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19572"></span>

<div id="answer-container-19572" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19572-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I thought his presentation was informative, ...</p></blockquote><p>Thank you :-)</p><blockquote><p>... but there was a lot of stuff that went over my head, because I know so little about all this.</p></blockquote><p>Then lets start at the beginning. It looks like you did not configure wireshark to use the private key.</p><p>If you go to "Edit -&gt; Preferences" then click on the triangle in front of Protocols and then scroll down to SSL and click on it. You will now see the SSL protocol preferences. In the preferences you will see a button "Edit" next to "RSA keys list". When you click on it, you can then add a new key by clicking on "new".</p><p>In the pop-up window, please enter:</p><ul><li>IP address ==&gt; IP address of your server which has SSL enabled</li><li>Port ==&gt; Most likely 443 or else the port on which you have your server running</li><li>Protocol ==&gt; http (unless you have some other protocol encrypted with SSL, you can always use "data" to tell wireshark to not dissect the data that is decrypted)</li><li>Key File: The location of the private key that corresponds to the certificate on the server (you need to get this key from the server)</li><li>Password: (leave empty, unless you point to a password protected pkcs12 certificate/key file in "Key File")</li></ul><p>If you have those properly filled and pressed OK (twice), then you should see the SSL debug lines that you quoted too...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19572" class="comments-container"><span id="19574"></span><div id="comment-19574" class="comment"><div id="post-19574-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info! I had done all that already, BUT it turned out the problem was that in the pop-up window, for the IP address, I had put '192.168.10.0/24' (hoping that it would apply to the entire '192.168.10.x' range). I just tried to put in the actual IP (instead of the '0/24' at the end), and I now get the debug lines that were missing before. Of course, it figures that decryption still doesn't work, but I'll work on it some more, and maybe I'll ask another question about it tomorrow. Thanks again!</p></div><div id="comment-19574-info" class="comment-info"><span class="comment-age">(16 Mar '13, 15:25)</span> sandwiches9</div></div></div><div id="comment-tools-19572" class="comment-tools"></div><div class="clear"></div><div id="comment-19572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

