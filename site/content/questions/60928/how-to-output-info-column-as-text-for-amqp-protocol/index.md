+++
type = "question"
title = "How to output Info Column as text for AMQP protocol?"
description = '''I&#x27;ve got a Wireshark capture of AMQP traffic and when viewed in Wireshark the Info column has text such as: connection.start-ok connection.tune  etc. I&#x27;m trying to figure out how I can get that field as text output? This is what I&#x27;m using so far and the output it provides: tshark -V -d tcp.port==100...'''
date = "2017-04-20T11:09:00Z"
lastmod = "2017-04-20T11:13:00Z"
weight = 60928
keywords = [ "fields", "tshark", "amqp" ]
aliases = [ "/questions/60928" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to output Info Column as text for AMQP protocol?](/questions/60928/how-to-output-info-column-as-text-for-amqp-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60928-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got a Wireshark capture of AMQP traffic and when viewed in Wireshark the Info column has text such as:</p><pre><code>connection.start-ok
connection.tune</code></pre><p>etc.</p><p>I'm trying to figure out how I can get that field as text output? This is what I'm using so far and the output it provides:</p><pre><code>tshark -V -d tcp.port==10004,amqp -T fields -e tcp.srcport -e tcp.dstport -e amqp.connection.method -r file.pcapng

56372   10004   2
10004   56372   5
56372   10004   6,7
10004   56372   8</code></pre><p>So what I'd want is something like:</p><pre><code>56372   10004   connection.start-ok
10004   56372   connection.tune
56372   10004   connection.tune-ok,connection.open</code></pre><p>Any suggestions?</p><p>Thank-you.</p></div><div id="question-tags" class="tags-container tags">fields tshark amqp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '17, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/01f5d3e1b9776d6d6baab07b4126eed9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gctaylor11&#39;s gravatar image" /><p>gctaylor11<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gctaylor11 has no accepted answers">0%</span></p></div></div><div id="comments-container-60928" class="comments-container"></div><div id="comment-tools-60928" class="comment-tools"></div><div class="clear"></div><div id="comment-60928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60929"></span>

<div id="answer-container-60929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60929-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <code>-e _ws.col.Info</code> to display the contents of the Info column. In general, you can display the contents of any column using this method, just replace <code>Info</code> with the title of the column of interest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '17, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-60929" class="comments-container"><span id="60932"></span><div id="comment-60932" class="comment"><div id="post-60932-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the suggestion.<br />
</p><p>Any idea why</p><pre><code>-e _ws.col.Info</code></pre><p>Is blank for me?<br />
</p><pre><code># tshark -V -d tcp.port==10004,amqp -T fields  -e _ws.col.Info -e tcp.srcport -e tcp.dstport  -r /tmp/1.mcc.b.AG1-1.pcapng  | head -n 30</code></pre><p>I have tried tshark versions 1.8.10 and 1.10.14 on RHEL. I also tried on Windows(tshark v. 2.2.3) but got a different decoding error unrelated to original problem.<br />
</p><pre><code>Parameter &quot;tcp.port==10004&quot; doesn&#39;t follow the template &quot;&gt;layer_type==selector&gt;&quot;,&quot;&gt;decode_as_protocol&gt;&quot;</code></pre><p>(My left angle bracket malformation is not part of the problem. In the error they are displayed correct. )</p></div><div id="comment-60932-info" class="comment-info"><span class="comment-age">(20 Apr '17, 13:54)</span> gctaylor11</div></div><span id="60933"></span><div id="comment-60933" class="comment"><div id="post-60933-score" class="comment-score"></div><div class="comment-text"><p>For versions of Wireshark prior to <a href="https://www.wireshark.org/docs/relnotes/wireshark-1.12.0.html">Wireshark 1.12.0</a>, omit the <code>_ws.</code> prefix.</p></div><div id="comment-60933-info" class="comment-info"><span class="comment-age">(20 Apr '17, 14:44)</span> cmaynard ♦♦</div></div><span id="60934"></span><div id="comment-60934" class="comment"><div id="post-60934-score" class="comment-score"></div><div class="comment-text"><p>Thanks much! Works with 1.10.14.</p></div><div id="comment-60934-info" class="comment-info"><span class="comment-age">(20 Apr '17, 15:44)</span> gctaylor11</div></div></div><div id="comment-tools-60929" class="comment-tools"></div><div class="clear"></div><div id="comment-60929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

