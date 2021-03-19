+++
type = "question"
title = "Sen and Ack"
description = '''Need filter to find last Sen and Ack that communicates with certain server ( i have ip of that server)'''
date = "2014-11-08T06:17:00Z"
lastmod = "2014-11-08T08:07:00Z"
weight = 37692
keywords = [ "ack", "sen" ]
aliases = [ "/questions/37692" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Sen and Ack](/questions/37692/sen-and-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37692-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Need filter to find last Sen and Ack that communicates with certain server ( i have ip of that server)</p></div><div id="question-tags" class="tags-container tags">ack sen</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '14, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/29d70bebce4c49d83f21598a057ab9ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skrndelj&#39;s gravatar image" /><p>Skrndelj<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skrndelj has no accepted answers">0%</span></p></div></div><div id="comments-container-37692" class="comments-container"><span id="37693"></span><div id="comment-37693" class="comment"><div id="post-37693-score" class="comment-score"></div><div class="comment-text"><p>Sen ??, and Ack of what, tcp ?</p></div><div id="comment-37693-info" class="comment-info"><span class="comment-age">(08 Nov '14, 07:16)</span> grahamb ♦</div></div><span id="37694"></span><div id="comment-37694" class="comment"><div id="post-37694-score" class="comment-score"></div><div class="comment-text"><p>Number of Sq and Ack when im braking relationship with server . So last Sq and Ack from communication with that server .</p><p>I have source ip and destination ip</p></div><div id="comment-37694-info" class="comment-info"><span class="comment-age">(08 Nov '14, 07:20)</span> Skrndelj</div></div><span id="37695"></span><div id="comment-37695" class="comment"><div id="post-37695-score" class="comment-score"></div><div class="comment-text"><p>Nope, still doesn't make much sense to me, what is Sq? Please use the standard names for the items your asking for.</p><p>What is the protocol you're using with the server?</p></div><div id="comment-37695-info" class="comment-info"><span class="comment-age">(08 Nov '14, 07:38)</span> grahamb ♦</div></div><span id="37696"></span><div id="comment-37696" class="comment"><div id="post-37696-score" class="comment-score"></div><div class="comment-text"><p>Its TCP protocol Seq and Ack is what i am after</p><p>Seq ( Sequence number ) Ack ( Acknowledgment number</p></div><div id="comment-37696-info" class="comment-info"><span class="comment-age">(08 Nov '14, 07:41)</span> Skrndelj</div></div></div><div id="comment-tools-37692" class="comment-tools"></div><div class="clear"></div><div id="comment-37692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37697"></span>

<div id="answer-container-37697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37697-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's no filter to show you the last, you can only select frames that match a filter, you'll have to manually find the last one.</p><p>For acks sent to the server use:</p><p><code>tcp.flags.ack == 1 &amp;&amp; ip.dst == server.ip</code></p><p>For acks from the server use:</p><p><code>tcp.flags.ack == 1 &amp;&amp; ip.src == server.ip</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '14, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37697" class="comments-container"></div><div id="comment-tools-37697" class="comment-tools"></div><div class="clear"></div><div id="comment-37697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

