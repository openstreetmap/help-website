+++
type = "question"
title = "How to receive packets from unique IPs using wireshark ?"
description = '''Basically what I want is to stop displaying packets from a host if I have earlier received a packet from it. This will not only decrease the size of output but also make analyzing packets much more convenient. Is there a way to do this ?'''
date = "2015-06-19T05:17:00Z"
lastmod = "2015-06-19T17:34:00Z"
weight = 43364
keywords = [ "packet-capture", "wireshark" ]
aliases = [ "/questions/43364" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to receive packets from unique IPs using wireshark ?](/questions/43364/how-to-receive-packets-from-unique-ips-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43364-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Basically what I want is to stop displaying packets from a host if I have earlier received a packet from it. This will not only decrease the size of output but also make analyzing packets much more convenient. Is there a way to do this ?</p></div><div id="question-tags" class="tags-container tags">packet-capture wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '15, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/4541634d61685ddb3a8aa77299713c7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Backspace&#39;s gravatar image" /><p>Backspace<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Backspace has no accepted answers">0%</span></p></div></div><div id="comments-container-43364" class="comments-container"><span id="43390"></span><div id="comment-43390" class="comment"><div id="post-43390-score" class="comment-score"></div><div class="comment-text"><pre><code>Basically what I want is to stop displaying packets from a host if I have earlier received a packet from it.</code></pre><p><code></code></p><code></code><p><code></code></p><p><code></code></p><p>So I assume you need a display filter which excludes the host from displaying. Have you tried a filter like this:</p><pre><code>!(ip.addr==10.0.0.1)</code></pre></div><div id="comment-43390-info" class="comment-info"><span class="comment-age">(19 Jun '15, 15:00)</span> Christian_R</div></div></div><div id="comment-tools-43364" class="comment-tools"></div><div class="clear"></div><div id="comment-43364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43391"></span>

<div id="answer-container-43391" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43391-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Both capture filters and display filters are stateless, so they can't remember that a packet has been seen from a given host and either discard or filter out subsequent packets from the host. There's no other mechanism I know of in Wireshark to do what you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '15, 17:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-43391" class="comments-container"></div><div id="comment-tools-43391" class="comment-tools"></div><div class="clear"></div><div id="comment-43391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

