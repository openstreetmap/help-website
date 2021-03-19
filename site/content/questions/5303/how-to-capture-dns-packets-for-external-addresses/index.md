+++
type = "question"
title = "How to capture DNS packets for external addresses"
description = '''Hello, As in the title, does anyone know how to capture the dns packets but only for external resources?  If I simply specify port 53, then it captures all the packets including the internal resources which are on 10.0.0.0/24 range. 10.0.0.0/24 is a range I need to exclude to capture only external r...'''
date = "2011-07-27T02:53:00Z"
lastmod = "2011-07-28T11:24:00Z"
weight = 5303
keywords = [ "range", "dns", "wireshark" ]
aliases = [ "/questions/5303" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture DNS packets for external addresses](/questions/5303/how-to-capture-dns-packets-for-external-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5303-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>As in the title, does anyone know how to capture the dns packets but only for external resources?</p><p>If I simply specify port 53, then it captures all the packets including the internal resources which are on 10.0.0.0/24 range. 10.0.0.0/24 is a range I need to exclude to capture only external resources.</p><p>I also tried port 53 and not dst net 10.0.0.0/24 but does not work.</p><p>Thanks in advance, Peter</p></div><div id="question-tags" class="tags-container tags">range dns wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '11, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/300a90b6ef9d786f34e3b4b5beeac9bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wooju&#39;s gravatar image" /><p>wooju<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wooju has no accepted answers">0%</span></p></div></div><div id="comments-container-5303" class="comments-container"><span id="5304"></span><div id="comment-5304" class="comment"><div id="post-5304-score" class="comment-score"></div><div class="comment-text"><p>Sorry, i specified wrong interface and the quare actually works.</p></div><div id="comment-5304-info" class="comment-info"><span class="comment-age">(27 Jul '11, 03:00)</span> wooju</div></div><span id="5306"></span><div id="comment-5306" class="comment"><div id="post-5306-score" class="comment-score"></div><div class="comment-text"><p>Ok, as I mentioned, the qury worked, but reqiarements changed a bit.</p><p>Is there a way I can exclude destination network 10.0.0.0/8 except of host 10.X.X.X ?</p><p>Curret code:</p><p><code>port 53 and not dst net 10.0.0.0/8</code></p><p>Thanks in advance</p></div><div id="comment-5306-info" class="comment-info"><span class="comment-age">(27 Jul '11, 03:16)</span> wooju</div></div></div><div id="comment-tools-5303" class="comment-tools"></div><div class="clear"></div><div id="comment-5303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5350"></span>

<div id="answer-container-5350" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5350-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can filter out the whole subnet except for one host with the following filter:</p><pre><code>port 53 and (host 10.1.1.1 or not net 10.0.0.0/8)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '11, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5350" class="comments-container"></div><div id="comment-tools-5350" class="comment-tools"></div><div class="clear"></div><div id="comment-5350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

