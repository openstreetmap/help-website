+++
type = "question"
title = "Why Doesn&#x27;t This Filter Work?"
description = '''I want to see results where neither the destination, nor the source are the specified address; here is my filter. ip.src != 192.168.1.119 &amp;amp;&amp;amp; ip.dst != 192.168.1.119 To my surprise, it returns some results with the that IP, such as this one: 157 238.065591 192.168.1.1 192.168.1.119 ICMP Desti...'''
date = "2010-11-23T16:50:00Z"
lastmod = "2010-11-23T23:49:00Z"
weight = 1093
keywords = [ "filter", "logic" ]
aliases = [ "/questions/1093" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why Doesn't This Filter Work?](/questions/1093/why-doesnt-this-filter-work)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1093-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to see results where neither the destination, nor the source are the specified address; here is my filter. ip.src != 192.168.1.119 &amp;&amp; ip.dst != 192.168.1.119</p><p>To my surprise, it returns some results with the that IP, such as this one: 157 238.065591 192.168.1.1 192.168.1.119 ICMP Destination unreachable (Port unreachable)</p><p>The destination on this result is clearly one the filter should have blocked. What's up?</p></div><div id="question-tags" class="tags-container tags">filter logic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '10, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/3b8a4f21d2910124c8a2e4a70a46c186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ActualRandy&#39;s gravatar image" /><p>ActualRandy<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ActualRandy has no accepted answers">0%</span></p></div></div><div id="comments-container-1093" class="comments-container"></div><div id="comment-tools-1093" class="comment-tools"></div><div class="clear"></div><div id="comment-1093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1095"></span>

<div id="answer-container-1095" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1095-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use <code>!ip.addr==192.168.1.119</code> and that will work.</p><p>Laura</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 17:06</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-1095" class="comments-container"><span id="1098"></span><div id="comment-1098" class="comment"><div id="post-1098-score" class="comment-score"></div><div class="comment-text"><p>Hi Laura -</p><p>You are correct, your filter does work, and I still don't understand why my filter doesn't work - I suspect it is a bug. But, of course, that wouldn't be your responsibility!</p></div><div id="comment-1098-info" class="comment-info"><span class="comment-age">(23 Nov '10, 17:30)</span> ActualRandy</div></div><span id="1099"></span><div id="comment-1099" class="comment"><div id="post-1099-score" class="comment-score"></div><div class="comment-text"><p>Filtering OUT based on IP address plagues everyone (see section 6.4.4 of the Wireshark User Manual). The developers even put in a sample display filter on that one with a note not to use != and made the yellow background. They tried to do everything short of flying/driving to your office/home, walking up to your desk and slapping you on the wrist. Grin.</p></div><div id="comment-1099-info" class="comment-info"><span class="comment-age">(23 Nov '10, 18:45)</span> lchappell ♦</div></div></div><div id="comment-tools-1095" class="comment-tools"></div><div class="clear"></div><div id="comment-1095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1105"></span>

<div id="answer-container-1105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1105-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem with a logical filter like <code>"ip.src != 192.168.1.119 &amp;&amp; ip.dst != 192.168.1.119"</code> is that while it may work for packets that only have one <code>ip.src</code> and <code>ip.dst</code>, it won't work like expected when there are more occurrences of those fields.</p><p>The maining of <code>"ip.src!=192.168.1.119"</code> is: "Match all packets where there is a field ip.src with a value other than 192.168.1.119".</p><p>In your case, the ICMP message contains to IP layers. Wheneven a system sends out an ICMP port unreachable message, it includes the IP header of the original packet that could not be delivered. That packet most probably had the ip.src and ip.dst reversed from the ip.src and ip.dst of the icmp message.</p><p>So there now is a field ip.src that does not match 192.168.1.119 and also a field ip.dst that does not match 192.168.1.119.</p><p>When you use <code>"!ip.addr==192.168.1.119"</code> it means there is not a field ip.addr with value 192.168.1.119. So that will work on all four fields ip.addr in your packet.</p><p>As Laura said, be careful with these filters, when a filter turns yellow, Wireshark tells you to pay attention. And the <a href="http://wiki.wireshark.org/">Wiki</a> and the <a href="http://www.wireshark.org/docs/wsug_html_chunked/">User's guide</a> are always great places to explore.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1105" class="comments-container"></div><div id="comment-tools-1105" class="comment-tools"></div><div class="clear"></div><div id="comment-1105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

