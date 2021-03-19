+++
type = "question"
title = "filters for Torpig / Sinowal etc"
description = '''Could someone tell me where to set the filters on to see on what machine is a rootkit ? For example. Customer has 100+ pc&#x27;s all have antivirus. Now 1 machine has a torpig virus. running wireshark on the server to check packages for 24 hours. Now i would like to filter it to quickly see it. Did tcp.d...'''
date = "2012-05-09T07:32:00Z"
lastmod = "2012-05-09T11:31:00Z"
weight = 10839
keywords = [ "sinowal", "torpig" ]
aliases = [ "/questions/10839" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [filters for Torpig / Sinowal etc](/questions/10839/filters-for-torpig-sinowal-etc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10839-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could someone tell me where to set the filters on to see on what machine is a rootkit ?</p><p>For example. Customer has 100+ pc's all have antivirus. Now 1 machine has a torpig virus. running wireshark on the server to check packages for 24 hours.</p><p>Now i would like to filter it to quickly see it. Did tcp.dstport == 80 as filter and http.request.method==POST seeing that the rootkits ask for that. But its still alot to go through.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">sinowal torpig</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '12, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/f8234963119c043b834fb66b68f41d41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jotronics&#39;s gravatar image" /><p>Jotronics<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jotronics has no accepted answers">0%</span></p></div></div><div id="comments-container-10839" class="comments-container"></div><div id="comment-tools-10839" class="comment-tools"></div><div class="clear"></div><div id="comment-10839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10849"></span>

<div id="answer-container-10849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10849-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>trying to detect a trojan, just by looking at the network traffic is hard if you don't know how it behaves (IP addresses it contacts - C&amp;C servers -, what kind of data "pattern" it uses, etc.)</p><p>Just looking for POST requests for a whole network, won't help you, as there will be loads of regular POST requests from your users (logging in somewhere, etc.).</p><p>So, what can you do?</p><p>Luckily, there are a papers available that describ in detail how Tropig works and what servers it tries to contact.</p><blockquote><p><strong><code>http://fserror.com/pdf/Torpig.pdf</code></strong><br />
<strong><code>http://www.cs.ucsb.edu/~seclab/projects/torpig/torpig.pdf</code></strong><br />
</p></blockquote><p>Within one document you'll find a list of possible C&amp;C servers:</p><ul><li><a href="http://kolipso.info">kolipso.info</a></li><li>194.146.207.133</li><li><a href="http://ret9unj.com">ret9unj.com</a></li><li><a href="http://alzan.info">alzan.info</a></li><li>194.146.207.18</li><li><a href="http://tsforme.com">tsforme.com</a></li><li><a href="http://useforme.com">useforme.com</a></li></ul><p>I suggest you look for any data directed to those servers in the first place.</p><p><strong>Display Filter:</strong><br />
Resolve the names above to ip addresses and then use this filter</p><blockquote><p><strong><code>ip.addr eq x.x.x.x or ip.addr x.x.x.x or ip.addr x.x.x.x</code></strong><br />
</p></blockquote><p><strong>HOWEVER</strong>: Torpig uses "Domain/DNS flux", so the servers above might have changed and you won't see any traffic.</p><p>Basically, this is just something to get you started and I hope it gave you an idea how to continue.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '12, 12:05</p></div></div><div id="comments-container-10849" class="comments-container"><span id="10873"></span><div id="comment-10873" class="comment"><div id="post-10873-score" class="comment-score"></div><div class="comment-text"><p>Kurt thank you for your information. This was the key to finding the 1 pc in 1000 ;)</p><p>Sorting the data on IP# and scrolling quickly through all the data you suddenly see all strange domainnames with the same ip#</p><p>That was the new updated torpig rootkit. Removed the pc from the network for deeper analysis.</p><p>Examples of new domain names : <a href="http://tkdut.com">tkdut.com</a> <a href="http://xctwniban.com">xctwniban.com</a> <a href="http://zoxini.com">zoxini.com</a> <a href="http://lqtmd.com">lqtmd.com</a> <a href="http://kjehip.com">kjehip.com</a> <a href="http://biraxwdqd.com">biraxwdqd.com</a></p><p>Shame cannot attach a picture to it so other ppl with the same question could see an example.</p><p>-Milo</p></div><div id="comment-10873-info" class="comment-info"><span class="comment-age">(10 May '12, 01:05)</span> Jotronics</div></div><span id="10875"></span><div id="comment-10875" class="comment"><div id="post-10875-score" class="comment-score"></div><div class="comment-text"><p>You might want to accept Kurts answer if it helped you ;-)</p></div><div id="comment-10875-info" class="comment-info"><span class="comment-age">(10 May '12, 01:32)</span> Jasper ♦♦</div></div><span id="10878"></span><div id="comment-10878" class="comment"><div id="post-10878-score" class="comment-score"></div><div class="comment-text"><p>Congrats, you developed yourself a good way to detect "domain flux" malware. Filter on 'dns.request' and sort for the source IP. If there are clients that resolves "strange" names, that could be a trojan. You could post the picture on flickr.</p></div><div id="comment-10878-info" class="comment-info"><span class="comment-age">(10 May '12, 01:42)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-10849" class="comment-tools"></div><div class="clear"></div><div id="comment-10849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

