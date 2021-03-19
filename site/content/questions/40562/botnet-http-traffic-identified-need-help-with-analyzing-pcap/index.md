+++
type = "question"
title = "Botnet HTTP Traffic identified - need help with analyzing pcap"
description = '''Hello, We currently had an incident with a internal workstation sending traffic to a known botnet (Alarm from our Proxy appliance); I pulled the pcap from our Shark appliance and I am trying to analyze why our web proxy would identify this as botnet traffic.  Is there anything suspicious about this ...'''
date = "2015-03-14T09:05:00Z"
lastmod = "2015-03-19T14:48:00Z"
weight = 40562
keywords = [ "http", "botnet" ]
aliases = [ "/questions/40562" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Botnet HTTP Traffic identified - need help with analyzing pcap](/questions/40562/botnet-http-traffic-identified-need-help-with-analyzing-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40562-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>We currently had an incident with a internal workstation sending traffic to a known botnet (Alarm from our Proxy appliance); I pulled the pcap from our Shark appliance and I am trying to analyze why our web proxy would identify this as botnet traffic.<br />
</p><p>Is there anything suspicious about this communication that stands out that I am possibly missing? to me I see that the machine is making get request with a long string value to a known IP address that is involved with botnet traffic. I am just trying to take this one step further to better understand these types of events going forward.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/pcap2.JPG" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/pcap1_ciSTQbi.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">http botnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '15, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/d5c5a4d0ce3bcb005561f55794ea5a8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cvs278&#39;s gravatar image" /><p>cvs278<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cvs278 has no accepted answers">0%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '15, 09:09</p></div></div><div id="comments-container-40562" class="comments-container"></div><div id="comment-tools-40562" class="comment-tools"></div><div class="clear"></div><div id="comment-40562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40578"></span>

<div id="answer-container-40578" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40578-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, the GET request is highly unusual, as it has a high entropy and no readable parts at all. Its most likely an encryption of some kind, which isn't likely to happen for a "normal" web page.</p><p>Also, the request goes to an IP address, not an FQDN, so there is probably no DNS entry for the ressource that is accessed. This is either a very lazy administrator who doesn't care if anyone uses his web page (very unlikely) or someone who doesn't want to risk registering a DNS domain because it could help identify him. Or he just doesn't care because all the site is doing is receiving botnet traffic, so he doesn't have to register it - the botnet clients know the IP address.</p><p>On the positive side: <a href="http://www.ipvoid.com/scan/188.138.96.202/">IPvoid</a> doesn't blacklist the IP address, and says it's a server in the serverloft.com range: loft7301.serverloft.com. Calling up that server opens a nondescript search form, so there's no way of telling what it is used for.</p><p>So, in the end it's hard to say, but the page itself doesn't look that bad. I was too lazy to try and see what your GET request would do, because I don't want to type in all the characters. Also, it should only be done from a system that you can discard afterwards, in case it gets infected (e.g. do it from a VM that you can reset to a snapshot).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '15, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-40578" class="comments-container"></div><div id="comment-tools-40578" class="comment-tools"></div><div class="clear"></div><div id="comment-40578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40700"></span>

<div id="answer-container-40700" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40700-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I did a brief search and found others seeing the same kind of traffic to that server.</p><p>The response to the following request is "scrambled/encrypted" as well.</p><blockquote><p><a href="http://188.138.96.202/9J53BCBR8pGOKAgwBHQgrgvztOiAFoO5RHeI+3wdMkoINuo4CdHmf+LBVqYfnFev2MxNCQ1XgJqh0Brltcm70CmTFnwUbI9Leqz0/Gp3fszxClaGSCEjGPfcwQ1ejVM7XFu/rnTLghNBUG4xYxtm+I9qr3Syp/6TkiyRPHKrn6aQ6L2rYp4uUrZYFK3mIh4E/f17pQIxvqeQ6j9ea345IhpaxdcuyDrHiqAkk6ZPxFvzCxXgzt1Tpfm1x/OGk1sAHfpFEj35PDJiW7MM8ktNeVBs">http://188.138.96.202/9J53BCBR8pGOKAgwBHQgrgvztOiAFoO5RHeI+3wdMkoINuo4CdHmf+LBVqYfnFev2MxNCQ1XgJqh0Brltcm70CmTFnwUbI9Leqz0/Gp3fszxClaGSCEjGPfcwQ1ejVM7XFu/rnTLghNBUG4xYxtm+I9qr3Syp/6TkiyRPHKrn6aQ6L2rYp4uUrZYFK3mIh4E/f17pQIxvqeQ6j9ea345IhpaxdcuyDrHiqAkk6ZPxFvzCxXgzt1Tpfm1x/OGk1sAHfpFEj35PDJiW7MM8ktNeVBs</a></p></blockquote><p>Response:</p><pre><code>2eRXb7Mg5t5TlvkZBKEhn4DdCuyA5lfQBg4ZIudvkzuCQurtFbAsf/6+xs0pDq99uUKzYgI/ZZQmuVLiso1EpNCWf/wkJstV35U76OU0KSuDXs1QkshEcBtj9XC1H5BLyfT/oTIuEGmkFesCjWMGvVCwzVGt2ofLReQuZzmJzVt/VXUqodSUbZPGUyjf9xqgUpQCvwO2x4cfH3aFKM/rD8gBklsCCvsib31wu2unjk8fo+OTruVf4oYi7TDsk/aaKhkkKLygK7uLpIKG</code></pre><p>Looks like a covert communication channel, beeing used for whatever. Could be malware or some sort of tunneling proxy. BTW: If you change a single char of the request, you'll get a 404!<br />
</p><p>Does not look "normal" to me ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '15, 14:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Mar '15, 14:51</p></div></div><div id="comments-container-40700" class="comments-container"></div><div id="comment-tools-40700" class="comment-tools"></div><div class="clear"></div><div id="comment-40700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

