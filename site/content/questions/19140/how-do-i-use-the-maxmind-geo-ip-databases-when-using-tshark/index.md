+++
type = "question"
title = "how do I use the maxmind Geo IP databases when using tshark?"
description = '''Hi, How do I use the maxmind Geo IP databases when using tshark, using the terminal (or how do tell tshark to refer to the downloaded database files)? There is no gui on the system so I cannot add using wireshark. Thanks, qwerfdsa'''
date = "2013-03-04T18:54:00Z"
lastmod = "2013-03-04T21:54:00Z"
weight = 19140
keywords = [ "terminal", "geoip", "tshark", "command-line" ]
aliases = [ "/questions/19140" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how do I use the maxmind Geo IP databases when using tshark?](/questions/19140/how-do-i-use-the-maxmind-geo-ip-databases-when-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19140-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, How do I use the maxmind Geo IP databases when using tshark, using the terminal (or how do tell tshark to refer to the downloaded database files)? There is no gui on the system so I cannot add using wireshark.</p><p>Thanks, qwerfdsa</p></div><div id="question-tags" class="tags-container tags">terminal geoip tshark command-line</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '13, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/78fdb0b07eaa8e7ef156b2cc2a067252?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qwerfdsa&#39;s gravatar image" /><p>qwerfdsa<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qwerfdsa has no accepted answers">0%</span></p></div></div><div id="comments-container-19140" class="comments-container"></div><div id="comment-tools-19140" class="comment-tools"></div><div class="clear"></div><div id="comment-19140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19142"></span>

<div id="answer-container-19142" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19142-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will need to have a <code>~/.wireshark/geoip_db_paths</code> file; it should contain a line giving the absolute path name of the GeoIP database directory, in double-quotes. For example, mine has the line</p><pre><code>&quot;/Users/gharris/GeoIP&quot;</code></pre><p>because they're stored in a directory named <code>GeoIP</code> under my home directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '13, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19142" class="comments-container"></div><div id="comment-tools-19142" class="comment-tools"></div><div class="clear"></div><div id="comment-19142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

