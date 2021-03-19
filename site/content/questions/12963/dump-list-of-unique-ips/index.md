+++
type = "question"
title = "Dump list of unique IP&#x27;s"
description = '''Im getting ddos&#x27;d by a large group of servers, large enough that sorting IP&#x27;s human wise is too large but small enough that I&#x27;d like to block all of them. My one second capture has each one hitting ~50-100 times and its consistently from these IP&#x27;s (It&#x27;s not from the same IP range) Any way i could d...'''
date = "2012-07-24T11:45:00Z"
lastmod = "2012-07-24T13:58:00Z"
weight = 12963
keywords = [ "ip", "dump", "text" ]
aliases = [ "/questions/12963" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Dump list of unique IP's](/questions/12963/dump-list-of-unique-ips)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12963-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Im getting ddos'd by a large group of servers, large enough that sorting IP's human wise is too large but small enough that I'd like to block all of them. My one second capture has each one hitting ~50-100 times and its consistently from these IP's (It's not from the same IP range)</p><p>Any way i could dump these into text?</p></div><div id="question-tags" class="tags-container tags">ip dump text</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '12, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/3f98d3c37034baa06752e543491ef240?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryanb213&#39;s gravatar image" /><p>ryanb213<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryanb213 has no accepted answers">0%</span></p></div></div><div id="comments-container-12963" class="comments-container"></div><div id="comment-tools-12963" class="comment-tools"></div><div class="clear"></div><div id="comment-12963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="12973"></span>

<div id="answer-container-12973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12973-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The following will create a list of Cisco ACL lines to block the IP's, if you need it in another syntax, I'm sure you will manage :-)</p><pre><code>tshark -r file.cap -R &quot;tcp.flags==2&quot; -T fields -e ip.src |\
  sort |\
  uniq |\
  awk &#39;{printf(&quot;deny ip host %s any\n&quot;,$1)}&#39;</code></pre><p>Hope this helps :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '12, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jul '12, 16:18</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-12973" class="comments-container"></div><div id="comment-tools-12973" class="comment-tools"></div><div class="clear"></div><div id="comment-12973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12966"></span>

<div id="answer-container-12966" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12966-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could use the statistics/endpoint function. There is a copy button that allows you to copy the list to the clipboard, from which you can paste it to a text editor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '12, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-12966" class="comments-container"><span id="12974"></span><div id="comment-12974" class="comment"><div id="post-12974-score" class="comment-score"></div><div class="comment-text"><p>Thank you, im new to wireshark but that solved my exact problem. I was getting saturated on my gbps line but i only needed 6 filter rules to block it.</p><p>Thank you!</p></div><div id="comment-12974-info" class="comment-info"><span class="comment-age">(24 Jul '12, 14:08)</span> ryanb213</div></div></div><div id="comment-tools-12966" class="comment-tools"></div><div class="clear"></div><div id="comment-12966-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12967"></span>

<div id="answer-container-12967" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12967-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please check if one of the following helps:</p><blockquote><p><code>tshark -r input.cap.pcapng -q -z hosts</code><br />
<code>tshark -r input.cap.pcapng -q -z ip_hosts,tree</code><br />
</p><p><code>windows: tshark -r input.cap.pcapng -q -z conv,tcp | find "192.168.x.x"</code><br />
<code>unix:    tshark -r input.cap.pcapng -q -z conv,tcp | grep "192.168.x.x"</code><br />
</p></blockquote><p>Where 192.168.x.x is the IP address of your attacked server.</p><p>Regards<br />
Kurt<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '12, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jul '12, 12:12</p></div></div><div id="comments-container-12967" class="comments-container"></div><div id="comment-tools-12967" class="comment-tools"></div><div class="clear"></div><div id="comment-12967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

