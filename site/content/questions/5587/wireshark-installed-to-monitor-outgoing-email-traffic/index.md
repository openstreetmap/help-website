+++
type = "question"
title = "Wireshark installed to monitor outgoing email traffic"
description = '''I have a network with about 20 pcs running mainly XP. We got blacklisted and can&#x27;t send email out anymore. Internet provider said we are infected by the torpig virus. I installed wireshark on a pc to monitor traffice and I have 4 days of data but don&#x27;t know what to look for. Canyone help with this? ...'''
date = "2011-08-09T09:19:00Z"
lastmod = "2011-08-09T09:30:00Z"
weight = 5587
keywords = [ "torpig" ]
aliases = [ "/questions/5587" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark installed to monitor outgoing email traffic](/questions/5587/wireshark-installed-to-monitor-outgoing-email-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a network with about 20 pcs running mainly XP. We got blacklisted and can't send email out anymore. Internet provider said we are infected by the torpig virus. I installed wireshark on a pc to monitor traffice and I have 4 days of data but don't know what to look for. Canyone help with this? ISP said it was made through an IP 91.19.36.89</p></div><div id="question-tags" class="tags-container tags">torpig</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '11, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/35bf510f3f57000a1c33afda4d65ae5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sts&#39;s gravatar image" /><p>sts<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sts has no accepted answers">0%</span></p></div></div><div id="comments-container-5587" class="comments-container"></div><div id="comment-tools-5587" class="comment-tools"></div><div class="clear"></div><div id="comment-5587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5589"></span>

<div id="answer-container-5589" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5589-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Uh oh...</p><p>According to <a href="http://www.google.de/url?sa=t&amp;source=web&amp;cd=1&amp;ved=0CBwQFjAA&amp;url=http%3A%2F%2Fwww.cs.ucsb.edu%2F~seclab%2Fprojects%2Ftorpig%2Ftorpig.pdf&amp;rct=j&amp;q=torpig%20virus%20network%20pattern&amp;ei=al9BTqvsCIvKtAbLxa3XBw&amp;usg=AFQjCNE_nwDkiKXAoxtOZk1qUPyqV1wBFw&amp;cad=rja">this</a> document, section 5.1, Torpig communicates via HTTP POST requests that are pretty cryptic - meaning, that there is no human readable part in the post request, just HEX patterns.</p><p>In your case I'd filter out all packets that do POST request, like this: <code>http.request.method==POST</code> (put that into the filter entry bar just on top of the packet list, after loading one of your trace files). Then, do a comparision by eye to see if you can detect those cryptic patterns (the human eye is pretty good at this, so just scroll through the filtered packets).</p><p>If you see any, your provider was probably right. Then you need to determine which station it is on your network and take it down, backup all vital data, and reinstall it. Most forensic experts do not advise to try and clean the infected system unless you're a forensic expert yourself, because it is pretty hard to tell if you "got it all". Instead, do the reinstall and start with a clean slate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '11, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-5589" class="comments-container"></div><div id="comment-tools-5589" class="comment-tools"></div><div class="clear"></div><div id="comment-5589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

