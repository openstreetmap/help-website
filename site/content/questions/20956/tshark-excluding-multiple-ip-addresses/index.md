+++
type = "question"
title = "tshark: excluding multiple ip addresses ?"
description = '''I can&#x27;t work out the correct syntax for excluding multiple ip addresses with tshark. I&#x27;m running tshark on a centos 6 server which is command line only. I can exclude a single ip address from the scoll by using: /usr/sbin/tshark -R &quot;ip.addr!=176.31.239.201&quot; &amp;lt;-- this command excludes 176.31.239.20...'''
date = "2013-05-05T06:49:00Z"
lastmod = "2013-05-05T06:52:00Z"
weight = 20956
keywords = [ "tshark" ]
aliases = [ "/questions/20956" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: excluding multiple ip addresses ?](/questions/20956/tshark-excluding-multiple-ip-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20956-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't work out the correct syntax for excluding multiple ip addresses with tshark. I'm running tshark on a centos 6 server which is command line only. I can exclude a single ip address from the scoll by using:</p><p>/usr/sbin/tshark -R "ip.addr!=176.31.239.201" &lt;-- this command excludes 176.31.239.201 but I'd also like to exclude several other ip addresses but nothing works.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '13, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/a3aeb3e02b7672911169cf411c38dd0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuronetv&#39;s gravatar image" /><p>neuronetv<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuronetv has no accepted answers">0%</span></p></div></div><div id="comments-container-20956" class="comments-container"></div><div id="comment-tools-20956" class="comment-tools"></div><div class="clear"></div><div id="comment-20956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20957"></span>

<div id="answer-container-20957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20957-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's usually better to build a filter that includes the stuff you don't want, and then negate it with a "not ()", e.g. like this:</p><p>"ip.addr==176.31.239.201" -&gt; "not (ip.addr==176.31.239.201)"</p><p>That way you can simply deduct a filter that includes everything you need, e.g.</p><p>"ip.addr==176.31.239.201 or ip.addr==192.168.0.1 or ip.addr==10.10.10.10" -&gt; "not (ip.addr==176.31.239.201 or ip.addr==192.168.0.1 or ip.addr==10.10.10.10)"</p><p>The reason why your filters didn't work is probably caused by the fact that there are TWO IP addresses in each packet, and your "!=" filter will always match one of the two, so all packets are still shown. Use the "not" technique to get around that problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '13, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '13, 06:54</p></div></div><div id="comments-container-20957" class="comments-container"></div><div id="comment-tools-20957" class="comment-tools"></div><div class="clear"></div><div id="comment-20957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

