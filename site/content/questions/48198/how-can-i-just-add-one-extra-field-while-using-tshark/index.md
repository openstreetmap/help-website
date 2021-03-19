+++
type = "question"
title = "How can I just add one extra field while using tshark"
description = '''Hi all.  I would like to just add one extra field in tshark&#x27;s output here is the command I execute  sudo tshark -p -t e -i mon0  below is the output 1449064211.939089 SmcNetwo_a7:11:a8 -&amp;gt; Broadcast 802.11 127 Beacon frame, SN=3671, FN=0, Flags=........, BI=100, SSID=TPE-Free how can I just add on...'''
date = "2015-12-02T07:05:00Z"
lastmod = "2015-12-02T07:19:00Z"
weight = 48198
keywords = [ "tshark" ]
aliases = [ "/questions/48198" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I just add one extra field while using tshark](/questions/48198/how-can-i-just-add-one-extra-field-while-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48198-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all.</p><p>I would like to just add one extra field in tshark's output</p><p>here is the command I execute</p><blockquote><p>sudo tshark -p -t e -i mon0</p></blockquote><p>below is the output</p><p>1449064211.939089 SmcNetwo_a7:11:a8 -&gt; Broadcast 802.11 127 Beacon frame, SN=3671, FN=0, Flags=........, BI=100, SSID=TPE-Free</p><p>how can I just add one extra field ?</p><p>if I specify a field. the output will only show one field and forget the original output</p><p>thanks in advanced !</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/6c02955223afaf0555e4a68df16cabd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Hsu&#39;s gravatar image" /><p>Tim Hsu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Hsu has no accepted answers">0%</span></p></div></div><div id="comments-container-48198" class="comments-container"></div><div id="comment-tools-48198" class="comment-tools"></div><div class="clear"></div><div id="comment-48198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48199"></span>

<div id="answer-container-48199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48199-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Presumably you're selecting the field to display with <code>-T fields -e field</code>? If so, you can add as many fields as you want with extra <code>-e field2 -e field3 ... -e fieldN</code> parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48199" class="comments-container"><span id="48200"></span><div id="comment-48200" class="comment"><div id="post-48200-score" class="comment-score"></div><div class="comment-text"><p>thanks for your answer. but how can I know these default field name?</p></div><div id="comment-48200-info" class="comment-info"><span class="comment-age">(02 Dec '15, 07:21)</span> Tim Hsu</div></div><span id="48202"></span><div id="comment-48202" class="comment"><div id="post-48202-score" class="comment-score"></div><div class="comment-text"><p>open the capture in wireshark, select a typical packet, go to the packet pane and expand all levels of detail which are interesting for you. Next, select the individual packet fields which interest you, one by one, and for each of them use right-click and choose "prepare a filter -&gt; ...and selected" from the context menu. This way, a string of <code>field1 == value1 &amp;&amp; field2 == value2 &amp;&amp; ...</code> builds up in the "display filter" field.</p><p>Now copy that string and edit it, keeping the field names and replacing the ==, &amp;&amp;, () and values with -e .</p></div><div id="comment-48202-info" class="comment-info"><span class="comment-age">(02 Dec '15, 07:32)</span> sindy</div></div></div><div id="comment-tools-48199" class="comment-tools"></div><div class="clear"></div><div id="comment-48199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

