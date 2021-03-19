+++
type = "question"
title = "getting &quot;Invalid capture filter &quot;subtype probereq&quot; for interface &#x27;Ethernet&quot; error when trying to save captures directly to csv file"
description = '''I wanted to store the captures directly to the csv file, for that I used the following command line tshark -T fields -E separator=&quot;,&quot; -E header=y -E quote=d -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto subtype probereq  but I am getting the following error:   C...'''
date = "2017-06-05T05:00:00Z"
lastmod = "2017-06-05T05:24:00Z"
weight = 61784
keywords = [ "capture", "csv", "tshark" ]
aliases = [ "/questions/61784" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [getting "Invalid capture filter "subtype probereq" for interface 'Ethernet" error when trying to save captures directly to csv file](/questions/61784/getting-invalid-capture-filter-subtype-probereq-for-interface-ethernet-error-when-trying-to-save-captures-directly-to-csv-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61784-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to store the captures directly to the csv file, for that I used the following command line</p><pre><code>tshark -T fields -E separator=&quot;,&quot; -E header=y -E quote=d -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto subtype probereq</code></pre><p>but I am getting the following error:</p><pre><code>  Capturing on &#39;Ethernet&#39;
tshark: Invalid capture filter &quot;subtype probereq&quot; for interface &#39;Ethernet&#39;.</code></pre><p>I also tried adding the name of the file to write in but it didn't help</p></div><div id="question-tags" class="tags-container tags">capture csv tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '17, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/87cc9cdbb338bd8869385782e33fb6fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dr_dr_&#39;s gravatar image" /><p>dr_dr_<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dr_dr_ has no accepted answers">0%</span></p></div></div><div id="comments-container-61784" class="comments-container"><span id="61816"></span><div id="comment-61816" class="comment"><div id="post-61816-score" class="comment-score"></div><div class="comment-text"><p>What network interface are you capturing on? What version, of what operating system, is the machine on which you're capturing running?</p></div><div id="comment-61816-info" class="comment-info"><span class="comment-age">(06 Jun '17, 20:24)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-61784" class="comment-tools"></div><div class="clear"></div><div id="comment-61784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61786"></span>

<div id="answer-container-61786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61786-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As the error message states, that is not a valid capture (or display or read) filter.</p><p>What is the filter you are using in the gui?</p><p>Try to add exactly the same filter, prefixed with either <code>-Y</code> or <code>-R</code>, and you might need quotes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '17, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61786" class="comments-container"></div><div id="comment-tools-61786" class="comment-tools"></div><div class="clear"></div><div id="comment-61786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

