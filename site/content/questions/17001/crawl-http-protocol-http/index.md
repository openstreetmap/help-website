+++
type = "question"
title = "[closed] Crawl HTTP protocol (关于抓取HTTP协议的问题)"
description = '''非常抱歉，我的英语不是很好，所以只能写中文了。在使用wireshark过程中我遇到一个问题，就是我想在抓包之前设置过滤，只抓取HTTP协议的数据包，为什么我在对网卡进行设置的时候在过滤条件中输入HTTP显示的就是经色，这表示这个设置不对的，但是输入TCP之类的都可以。我想问一下这是什么原因？  (As translated by Google): I&#x27;m sorry, my English is not very good, and we can only write Chinese. Use wireshark process, I encountered a problem, is tha...'''
date = "2012-12-17T17:59:00Z"
lastmod = "2012-12-18T21:35:00Z"
weight = 17001
keywords = [ "http" ]
aliases = [ "/questions/17001" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Crawl HTTP protocol (关于抓取HTTP协议的问题)](/questions/17001/crawl-http-protocol-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17001-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>非常抱歉，我的英语不是很好，所以只能写中文了。在使用wireshark过程中我遇到一个问题，就是我想在抓包之前设置过滤，只抓取HTTP协议的数据包，为什么我在对网卡进行设置的时候在过滤条件中输入HTTP显示的就是经色，这表示这个设置不对的，但是输入TCP之类的都可以。我想问一下这是什么原因？</p><blockquote><p>(As translated by Google): I'm sorry, my English is not very good, and we can only write Chinese. Use wireshark process, I encountered a problem, is that I would like to set up filters in Ethereal before, only to grab the HTTP protocol packet, why when I set the NIC to input HTTP is shown by the color filter conditions this means that the settings wrong, but can enter the TCP like. I would like to ask what reason?</p></blockquote></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 17:59</strong></p><img src="https://secure.gravatar.com/avatar/52c284b06d387ac702f48ee644e6f442?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jun&#39;s gravatar image" /><p>jun<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 20 Dec '12, 23:24</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-17001" class="comments-container"><span id="17009"></span><div id="comment-17009" class="comment"><div id="post-17009-score" class="comment-score"></div><div class="comment-text"><p>Sounds like a display filter versus capture filter question.</p></div><div id="comment-17009-info" class="comment-info"><span class="comment-age">(17 Dec '12, 23:53)</span> Jaap ♦</div></div></div><div id="comment-tools-17001" class="comment-tools"></div><div class="clear"></div><div id="comment-17001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question of http://ask.wireshark.org/questions/17118/issue-about-crawl-http" by Kurt Knochner 20 Dec '12, 23:24

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17046"></span>

<div id="answer-container-17046" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17046-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>您可以不使用 <strong>HTTP</strong>作为捕捉过滤器，因为这不是一个有效的libpcap的过滤器语法。而 <strong>TCP</strong>是一个有效的过滤器。</p><p>在这里看到：<a href="http://www.manpagez.com/man/7/pcap-filter/">http://www.manpagez.com/man/7/pcap-filter/</a></p><p>请使用此过滤器，而不是<strong>`TCP端口80</strong></p><p>此致 库尔特</p><p>You cannot use <strong>http</strong> as a capture filter, as that is not a valid libpcap filter syntax. whereas <strong>tcp</strong> is a valid filter.</p><p>See here: <a href="http://www.manpagez.com/man/7/pcap-filter/">http://www.manpagez.com/man/7/pcap-filter/</a></p><p>Please use this filter instead: <strong><code>tcp port 80</code></strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '12, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-17046" class="comments-container"><span id="17048"></span><div id="comment-17048" class="comment"><div id="post-17048-score" class="comment-score"></div><div class="comment-text"><p>如果使用tcp port 80这个过滤语法的话，那么他只能抓取经过80端口的HTTP协议哦，如果有些HTTP协调不是通过80端口的又要怎么抓呢？</p></div><div id="comment-17048-info" class="comment-info"><span class="comment-age">(18 Dec '12, 17:16)</span> jun</div></div></div><div id="comment-tools-17046" class="comment-tools"></div><div class="clear"></div><div id="comment-17046-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17050"></span>

<div id="answer-container-17050" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17050-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>这个要用 高级过滤器才行</p><p>抓Http GET 或者 HEAD (80 可以改为任意) tshark 'tcp port 80 and (((ip[2:2] - ((ip[0]&amp;0xf)&lt;&lt;2)) - ((tcp[12]&amp;0xf0)&gt;&gt;2)) != 0)' -R 'http.request.method == "GET" || http.request.method == "HEAD"</p><p>PS：LZ 怎么跑这里来问了 ？</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '12, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/8933507db30522e7ad869df02b61a7eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Missuniverse110&#39;s gravatar image" /><p>Missuniverse110<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Missuniverse110 has no accepted answers">0%</span></p></div></div><div id="comments-container-17050" class="comments-container"><span id="17051"></span><div id="comment-17051" class="comment"><div id="post-17051-score" class="comment-score"></div><div class="comment-text"><p>那个高级过滤器要另外安装吗？ 不在问在那里问，还有中文版的论坛吗？</p></div><div id="comment-17051-info" class="comment-info"><span class="comment-age">(18 Dec '12, 23:49)</span> jun</div></div><span id="17053"></span><div id="comment-17053" class="comment"><div id="post-17053-score" class="comment-score"></div><div class="comment-text"><p>能否请您重复安装过滤器的问题吗？</p><p>顺便说一句：有没有中国版网站。我建议英语问（询问你的同事），谷歌翻译增加了一些错误，这使得通信有点难。</p><p>Can you please repeat the question about installing the filter?</p><p>There is no chinese version of this site. I suggest to ask in english (ask a colleague of yours), as Google translate adds some errors, which makes communication somewhat hard.</p></div><div id="comment-17053-info" class="comment-info"><span class="comment-age">(19 Dec '12, 00:27)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-17050" class="comment-tools"></div><div class="clear"></div><div id="comment-17050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

