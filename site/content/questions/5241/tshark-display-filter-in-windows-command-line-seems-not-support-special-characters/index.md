+++
type = "question"
title = "tshark display filter in windows command-line seems not support special characters"
description = '''I wrote a tshark display filter as this:  http.request.uri contains &quot;search?q&quot;.  It works fine in wireshark with gui in windows. However I get a variety of errors in windows comand-line tshark, like this: D:&#92;&amp;gt;tshark -r http.pcap -R &quot;http.request.uri contains search?q&quot; tshark: &quot;?&quot; was unexpected i...'''
date = "2011-07-25T23:14:00Z"
lastmod = "2011-07-26T01:58:00Z"
weight = 5241
keywords = [ "windows", "tshark", "display-filter" ]
aliases = [ "/questions/5241" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark display filter in windows command-line seems not support special characters](/questions/5241/tshark-display-filter-in-windows-command-line-seems-not-support-special-characters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5241-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a tshark display filter as this:</p><pre><code>http.request.uri contains &quot;search?q&quot;.</code></pre><p>It works fine in wireshark with gui in windows. However I get a variety of errors in windows comand-line tshark, like this:</p><pre><code>D:\&gt;tshark -r http.pcap -R &quot;http.request.uri contains search?q&quot;
tshark: &quot;?&quot; was unexpected in this context.

D:\&gt;tshark -r http.pcap -R &#39;http.request.uri contains &quot;search?q&quot;&#39;
tshark: Read filters were specified both with &quot;-R&quot; and with additional command-line arguments</code></pre><p>When I remove the "?" from the string, the tshark can print the outcome, but it wasn't the result I want because it prints too much content. I just want the last message from the following list of messages:</p><pre><code>D:\&gt;tshark -r http.pcap -R &quot;http.request.uri contains search&quot;
  5   0.464031 192.168.20.171 -&gt; 74.125.53.139 HTTP 676 GET /complete/search?client=chrome&amp;hl=zh-CN&amp;q=http%3A%2F%2Fbing.com.cn HTTP/1.1
 62   2.329645 192.168.20.171 -&gt; 74.125.71.105 HTTP 787 GET /url?sa=p&amp;hl=zh-CN&amp;pref=hkredirect&amp;pval=yes&amp;q=http://www.google.com.hk/searchdomaincheck%3Fformat%3Ddomain%26type%3Dchrome&amp;ust=1305691041473287&amp;usg=AFQjCNGPbHPEXHcOxDHu2X0Q3r92XfkD7w HTTP/1.1
 65   2.465906 192.168.20.171 -&gt; 74.125.71.105 HTTP 649 GET /searchdomaincheck?format=domain&amp;type=chrome HTTP/1.1
249  10.925213 192.168.20.171 -&gt; 125.252.224.82 HTTP 862 GET /search?q=%E5%BF%85%E5%BA%94&amp;go=&amp;form=QBLH&amp;qs=n&amp;sk= HTTP/1.1</code></pre><p>It seems that the tshark diplay filter doesn't support the special characters like "?", "=". Is there any method that I can include those characters in the display filter?</p></div><div id="question-tags" class="tags-container tags">windows tshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '11, 23:14</strong></p><img src="https://secure.gravatar.com/avatar/e24a5509f067f40c32d883b032dcfb60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="calcel&#39;s gravatar image" /><p>calcel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="calcel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jul '11, 15:41</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5241" class="comments-container"><span id="5242"></span><div id="comment-5242" class="comment"><div id="post-5242-score" class="comment-score"></div><div class="comment-text"><p>What is the error message you receive?</p></div><div id="comment-5242-info" class="comment-info"><span class="comment-age">(26 Jul '11, 00:48)</span> multipleinte...</div></div></div><div id="comment-tools-5241" class="comment-tools"></div><div class="clear"></div><div id="comment-5241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5245"></span>

<div id="answer-container-5245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5245-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>In windows you have to use double double-quotes to escape the double-quote. The syntax will be:</p><pre><code>C:\Download&gt;tshark -r http.cap -R &quot;http.request.uri contains &quot;&quot;search?d&quot;&quot;&quot;
 31 7.071765000 192.168.20.10 -&gt; 67.228.110.120 HTTP 589 GET /search?d HTTP/1.1

C:\Download&gt;tshark -r http.cap -R &quot;http.request.uri contains &quot;&quot;search&quot;&quot;&quot;
 31 7.071765000 192.168.20.10 -&gt; 67.228.110.120 HTTP 589 GET /search?d HTTP/1.1
163 19.888136000 192.168.20.10 -&gt; 67.228.110.120 HTTP 587 GET /search HTTP/1.1

C:\Download&gt;</code></pre><p>Hope this helps :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5245" class="comments-container"><span id="5286"></span><div id="comment-5286" class="comment"><div id="post-5286-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. It does solve the problem.</p></div><div id="comment-5286-info" class="comment-info"><span class="comment-age">(26 Jul '11, 18:33)</span> calcel</div></div></div><div id="comment-tools-5245" class="comment-tools"></div><div class="clear"></div><div id="comment-5245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

