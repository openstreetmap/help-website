+++
type = "question"
title = "command line option for &quot;Follow tcp stream&quot;"
description = '''Hi , Is there any command line option to generate &quot;Follow tcp stream&quot;(which is availabe in GUI) ,so that we can look at the messages which are exchanged between the apllications as a whole with out having the message broken in multiple parts. Basically i wanted to track all the payload which are get...'''
date = "2012-04-09T01:48:00Z"
lastmod = "2012-05-08T02:53:00Z"
weight = 10023
keywords = [ "tcp.stream" ]
aliases = [ "/questions/10023" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [command line option for "Follow tcp stream"](/questions/10023/command-line-option-for-follow-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10023-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi , Is there any command line option to generate "Follow tcp stream"(which is availabe in GUI) ,so that we can look at the messages which are exchanged between the apllications as a whole with out having the message broken in multiple parts. Basically i wanted to track all the payload which are getting exchanged between th applications..and write it to some file..so i need to find a commandline option which will does the same thing which "Follow tcp stream" GUI does.</p></div><div id="question-tags" class="tags-container tags">tcp.stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '12, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/54dfb1796a8beedf9843a326d673eaae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vikram&#39;s gravatar image" /><p>vikram<br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vikram has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Apr '12, 02:51</p></div></div><div id="comments-container-10023" class="comments-container"></div><div id="comment-tools-10023" class="comment-tools"></div><div class="clear"></div><div id="comment-10023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10773"></span>

<div id="answer-container-10773" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10773-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>As tshark 1.7.1 is not available on your platform (none of the big distributions provide it as a package), I recommend to use <strong>tcpflow</strong> (see also Wiki: <strong><a href="http://wiki.wireshark.org/Tools">http://wiki.wireshark.org/Tools</a></strong>). This tool will be provided by most of the linux distributions and it does extract the data of tcp sessions.</p><p>Example:</p><blockquote><p><code>tcpflow -r http.cap</code><br />
</p></blockquote><p>This creates several files, named by the IP Addresses and Ports of a conversation, e.g. <strong><code>080.190.158.009.00080-192.168.030.151.52612</code></strong></p><p>Sample output:</p><p><code>head -40 080.190.158.009.00080-192.168.030.151.52612</code></p><blockquote><p><code>HTTP/1.1 200 OK</code><br />
<code>Server: nginx</code><br />
<code>Date: Tue, 08 May 2012 09:45:18 GMT</code><br />
<code>Content-Type: text/html; charset=iso-8859-15</code><br />
<code>Connection: keep-alive</code><br />
<code>Keep-Alive: timeout=60</code><br />
<code>Vary: Accept-Encoding</code><br />
<code>Last-Modified: Tue, 08 May 2012 05:02:00 GMT</code><br />
<code>ETag: "49db9-5a77-4965c200"</code><br />
<code>Accept-Ranges: bytes</code><br />
<code>Content-Length: 23159</code><br />
<code>Cache-Control: max-age=14400</code><br />
<code>Expires: Tue, 08 May 2012 13:45:18 GMT</code><br />
<code>&lt;!DOCTYPE html PUBLIC "-//W4C//DTD HTML 4.01 Transitional//EN"&gt; &lt;html&gt; &lt;head&gt;       &lt;meta name="generator" content="HTML Tidy, see www.w3.org"&gt;       &lt;meta http-equiv="Content-Type" content=       "text/html; charset=iso-8859-15"&gt;       &lt;meta name="Author" content="LEO GmbH"&gt;       &lt;meta name="description" content="#meta_descr#"&gt;       &lt;meta name="keywords" content="#meta_keys#"&gt;</code><br />
<code>&lt;title&gt;WWW leo.org&lt;/title&gt;</code><br />
</p></blockquote><p>If you filter away the HTTP response headers, you will get what you are looking for.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '12, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '12, 02:57</p></div></div><div id="comments-container-10773" class="comments-container"><span id="11081"></span><div id="comment-11081" class="comment"><div id="post-11081-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Is there anyway to decrypt ssl using tcpflow command.I am aware of decrypting using tshark(with private key),i am trying to find if the same can be achived using tcpflow.</p></div><div id="comment-11081-info" class="comment-info"><span class="comment-age">(16 May '12, 22:59)</span> vikram</div></div><span id="11082"></span><div id="comment-11082" class="comment"><div id="post-11082-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, tcpflow has no option for ssl decryption. If you need that, you should use the latest tshark. Compiling it yourself it pretty easy, especially on Ubuntu.</p><blockquote><p><code>apt-get install build-dep wireshark</code><br />
</p></blockquote><p>Then get the source. Extract it and run these commands in the wireshark directory.</p><blockquote><p><code>./configure</code><br />
<code>./make install</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-11082-info" class="comment-info"><span class="comment-age">(17 May '12, 00:31)</span> Kurt Knochner ♦</div></div><span id="39666"></span><div id="comment-39666" class="comment"><div id="post-39666-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately <code>tcpflow</code> saves client and server tcp payloads in separate files. This means that you will lost the order of payloads :(</p></div><div id="comment-39666-info" class="comment-info"><span class="comment-age">(05 Feb '15, 06:48)</span> SuBCo</div></div></div><div id="comment-tools-10773" class="comment-tools"></div><div class="clear"></div><div id="comment-10773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10026"></span>

<div id="answer-container-10026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10026-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use the development version of tshark (1.7.1) and the <code>-z follow</code> option, e.g. <code>-z follow,tcp,ascii,1</code> will display the ASCII output of tcp conversation number 1 from the input.</p><p>The <code>-z follow</code> option was introduced in r40856 of trunk.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '12, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-10026" class="comments-container"><span id="10764"></span><div id="comment-10764" class="comment"><div id="post-10764-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb, Is there a linux version of tshark 1.7.1 availabe for download ,i am intrested in using the commnad line option of tshark to get the tcp stream and see the actual payload (XML in my case).</p></div><div id="comment-10764-info" class="comment-info"><span class="comment-age">(07 May '12, 22:14)</span> vikram</div></div><span id="10772"></span><div id="comment-10772" class="comment"><div id="post-10772-score" class="comment-score"></div><div class="comment-text"><p>Not that I'm aware of. Until your distribution provides a pre-compiled package you'll just have to compile it yourself.</p></div><div id="comment-10772-info" class="comment-info"><span class="comment-age">(08 May '12, 02:29)</span> grahamb ♦</div></div></div><div id="comment-tools-10026" class="comment-tools"></div><div class="clear"></div><div id="comment-10026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

