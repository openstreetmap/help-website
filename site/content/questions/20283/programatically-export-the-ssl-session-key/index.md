+++
type = "question"
title = "programatically export the ssl session key"
description = '''i am new to wireshark and trying to get a little exposer. Is there any way to export SSL session key through command line. Please help me.... &#92;Thanks in advance... :)'''
date = "2013-04-10T07:08:00Z"
lastmod = "2013-04-10T08:11:00Z"
weight = 20283
keywords = [ "program", "export" ]
aliases = [ "/questions/20283" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [programatically export the ssl session key](/questions/20283/programatically-export-the-ssl-session-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20283-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>i am new to wireshark and trying to get a little exposer. Is there any way to export SSL session key through command line.</p><p>Please help me....</p><p>\Thanks in advance... :)</p></div><div id="question-tags" class="tags-container tags">program export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '13, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/f09a49225b6e11cb5a511934aeb24a66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amby&#39;s gravatar image" /><p>Amby<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amby has no accepted answers">0%</span></p></div></div><div id="comments-container-20283" class="comments-container"></div><div id="comment-tools-20283" class="comment-tools"></div><div class="clear"></div><div id="comment-20283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="20285"></span>

<div id="answer-container-20285" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20285-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @SYN-bit said, there is no CLI option to do that.</p><p>But, you could run tshark with a SSL debug file and then extract the SSL session keys from the debug file.</p><p>Use a command like this (not tested lately!).</p><blockquote><p><code>tshark -n -o "ssl.desegment_ssl_records: TRUE" -o "ssl.desegment_ssl_application_data: TRUE" -o "ssl.keys_list:x.x.x.x,443,http,rsa_private.key" -o "ssl.debug_file:ssl_debug.log" -r input.pcap -R "(tcp.port eq 443)"</code></p></blockquote><p>Please replace x.x.x.x with the IP address of your server.</p><p>After tshark has finished, parse the file ssl_debug.log (with your preferred scripting language) and extract the SSL session keys. Search for the string below and extract the consecutive lines, which is the SSL session key in HEX.</p><blockquote><p>ssl_save_session stored master secret</p></blockquote><p>Example:</p><pre><code>ssl_save_session stored master secret[48]:
f8 35 52 95 9e f0 dc 62 19 f6 c0 be cc 0c 32 fd 
84 d8 b1 2d 64 fa 51 b9 d6 25 2b 00 76 36 fd 4d 
20 a1 ea ff 6b 6a ed 56 b4 c2 fe f1 e8 87 65 2f </code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '13, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '13, 07:53</p></div></div><div id="comments-container-20285" class="comments-container"><span id="21143"></span><div id="comment-21143" class="comment"><div id="post-21143-score" class="comment-score"></div><div class="comment-text"><p>Guys i was able to generate SSL session key using the above hints that you gave i.e. by grepping "ssl_save_session stored session id" all i want to know that is there any chances that ssl session key what we generate from wire shark will not work to get the decrypted pcap data....</p></div><div id="comment-21143-info" class="comment-info"><span class="comment-age">(14 May '13, 21:52)</span> Amby</div></div><span id="21144"></span><div id="comment-21144" class="comment"><div id="post-21144-score" class="comment-score"></div><div class="comment-text"><blockquote><p>is there any chances that ssl session key what we generate from wire shark will not work to get the decrypted pcap data.</p></blockquote><p>yes, if the key extraction (with a script) fails (missing some bytes, etc.). Does it work, if you extract the key manually and then use it in Wireshark?</p></div><div id="comment-21144-info" class="comment-info"><span class="comment-age">(14 May '13, 23:40)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20285" class="comment-tools"></div><div class="clear"></div><div id="comment-20285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20287"></span>

<div id="answer-container-20287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20287-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @Kurt pointed out, the SSL session keys are available in the ssl-debug file (nice one Kurt), it just needs to be reformatted.</p><p>I did a little CLI mungling and came with the following oneliner (on multiple lines for readability):</p><pre><code>cat ssl_debug.log |\
 grep -A6 &quot;ssl_save_session stored session id&quot; |\
 sed -e &#39;s/ //g&#39; |\
 awk -F&#39;|&#39; &#39;$1 ~ &quot;ssl_save_sessionstoredsessionid&quot; {printf(&quot;RSA Session-ID:&quot;);next} 
            $1 ~ &quot;ssl_save_sessionstoredmastersecret&quot; {printf(&quot; Master-Key:&quot;);next} 
            $1 == &quot;--&quot; {printf(&quot;\n&quot;);next} 
            {printf(&quot;%s&quot;,$2)} 
            END {printf(&quot;\n&quot;)}&#39;</code></pre><p>Which transforms the following output in the ssl-debug file:</p><pre><code>ssl_save_session stored session id[32]:
| fb cf 32 21 28 ed 0a 00 b2 72 d6 ac 85 84 3f 50 |ûÏ2!(í..²rÖ¬..?P|
| de cc dd 94 ac 33 26 15 23 18 96 39 f5 ba 18 9a |ÞÌÝ.¬3&amp;.#..9õº..|
ssl_save_session stored master secret[48]:
| bd a6 ea 47 2f 6c 39 a9 fc fd 5d c7 9e b1 61 d1 |½¦êG/l9©üý]Ç.±aÑ|
| a4 ca e5 d9 24 fd de 80 0f 27 62 63 fd 6d f1 ee |¤ÊåÙ$ýÞ..&#39;bcýmñî|
| 8e d2 46 b5 a6 41 2e 32 8e b8 57 44 c9 bf 7c f2 |.ÒFµ¦A.2.¸WDÉ¿|ò|</code></pre><p>into:</p><pre><code>RSA Session-ID:fbcf322128ed0a00b272d6ac85843f50deccdd94ac33261523189639f5ba189a Master-Key:bda6ea472f6c39a9fcfd5dc79eb161d1a4cae5d924fdde800f276263fd6df1ee8ed246b5a6412e328eb85744c9bf7cf2</code></pre><p>Which is the format needed for Wireshark to be able to import the session keys to decrypt the SSL sessions in the file without the need for the private key.</p><p>(multiple session keys in the debug file will be converted)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '13, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '13, 08:27</p></div></div><div id="comments-container-20287" class="comments-container"><span id="20302"></span><div id="comment-20302" class="comment"><div id="post-20302-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt and SYN-bit for your quick responses. @SYN-bit can we generate the session key using batch scripting??</p></div><div id="comment-20302-info" class="comment-info"><span class="comment-age">(10 Apr '13, 22:10)</span> Amby</div></div><span id="20305"></span><div id="comment-20305" class="comment"><div id="post-20305-score" class="comment-score"></div><div class="comment-text"><p>(please use "add a comment" to respond to given answers, see the FAQ for details)</p><p>Yes, you can use bash scripting to extract the session keys from a bunch of tracefiles. You can loop through your files with a "for" loop and then for each file call the command from @Kurt's answer and then call my command sequence to extract the session keys from the ssl-debug file.</p></div><div id="comment-20305-info" class="comment-info"><span class="comment-age">(11 Apr '13, 01:13)</span> SYN-bit ♦♦</div></div><span id="20314"></span><div id="comment-20314" class="comment"><div id="post-20314-score" class="comment-score"></div><div class="comment-text"><blockquote><p>using batch scripting??</p></blockquote><p>by <strong>batch</strong> scripting, do you mean Windows batch scripting?</p><p>If yes, I recommend to look at powershell.<br />
If no, please follow the instructions of @SYN-bit.</p></div><div id="comment-20314-info" class="comment-info"><span class="comment-age">(11 Apr '13, 02:43)</span> Kurt Knochner ♦</div></div><span id="20315"></span><div id="comment-20315" class="comment"><div id="post-20315-score" class="comment-score"></div><div class="comment-text"><p>Nice catch @Kurt, I am not using windows much anymore, so I kinda have a bias in my answers.</p><p>@Amby, you could use <a href="http://www.cygwin.com/">Cygwin</a> on windows to have a bash shell and the then you can use my 'script' on a Windows machine too. But powershell should be able to do the ssame, I am just not familiar enough with it to convert my 'script' into powershell commands...</p></div><div id="comment-20315-info" class="comment-info"><span class="comment-age">(11 Apr '13, 02:54)</span> SYN-bit ♦♦</div></div><span id="20321"></span><div id="comment-20321" class="comment"><div id="post-20321-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am not using windows much anymore</p></blockquote><p>If VMware Workstation wasn't such a pain in the a.. on Linux (i.e. forced to recompile all modules after a kernel update, etc.), I would probably use Linux as a Desktop system ;-) Unless that changes, Windows 7 is my preferred VMWare Workstation Host, of course dual booted with Linux :-)</p></div><div id="comment-20321-info" class="comment-info"><span class="comment-age">(11 Apr '13, 03:22)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20287" class="comment-tools"></div><div class="clear"></div><div id="comment-20287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20284"></span>

<div id="answer-container-20284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20284-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately not, that has not (yet?) been implemented, so for now, you will need to use the Wireshark GUI to export the SSL session keys.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '13, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div></div><div id="comments-container-20284" class="comments-container"></div><div id="comment-tools-20284" class="comment-tools"></div><div class="clear"></div><div id="comment-20284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

