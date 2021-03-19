+++
type = "question"
title = "Selecting correct field with tshark for output file csv"
description = '''In Windows 7 I&#x27;m using tshark on the commandprompt to extract some information from pcaps and write them to csv files. In the csv file I want to write what is in the filter below, containing &quot;&quot;test&quot;&quot;&quot;. In the pcap itself and the &#x27;x509af.subject&#x27; field are multiple lines of x509sat.uTF8String values ...'''
date = "2017-02-02T08:14:00Z"
lastmod = "2017-02-02T08:38:00Z"
weight = 59244
keywords = [ "-tfields", "utf8string", "tshark" ]
aliases = [ "/questions/59244" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Selecting correct field with tshark for output file csv](/questions/59244/selecting-correct-field-with-tshark-for-output-file-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59244-score" class="post-score" title="current number of votes">0</div><span id="post-59244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Windows 7 I'm using tshark on the commandprompt to extract some information from pcaps and write them to csv files. In the csv file I want to write what is in the filter below, containing ""test""". In the pcap itself and the 'x509af.subject' field are multiple lines of x509sat.uTF8String values (in the ssl.handshake.certificate).</p><p>It looks like the output always shows the first value of the different uTF8Strings, but in this case I want to show the value of the 5th uTF8String. Just to be sure that the correct value has been printed to the csv file. I want "test" to show in the csv file, instead of a location which is currently showing.</p><p>Is there a way to tell tshark which uTF8String value can be printed to the csv file? Apparently the -Y filter does work, but the wrong field gets printed to the csv.</p><pre><code>tshark.exe -r C:\pcaps\test.pcap -T fields -Y &quot;ssl.handshake.certificate&quot; -Y &quot;x509sat.uTF8String == &quot;&quot;test&quot;&quot;&quot; -e frame.number -e frame.time -e ip.src -e ip.dst -e x509af.utcTime -e x509sat.uTF8String -E header=y -E separator=, -E quote=d -E occurrence=f &gt; C:\pcaps\test.csv</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link--tfields" rel="tag" title="see questions tagged &#39;-tfields&#39;">-tfields</span> <span class="post-tag tag-link-utf8string" rel="tag" title="see questions tagged &#39;utf8string&#39;">utf8string</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '17, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/1bd7aa9ec4636e9d234ddfb63bb15f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r00t070&#39;s gravatar image" /><p><span>r00t070</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r00t070 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Feb '17, 08:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-59244" class="comments-container"></div><div id="comment-tools-59244" class="comment-tools"></div><div class="clear"></div><div id="comment-59244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59245"></span>

<div id="answer-container-59245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59245-score" class="post-score" title="current number of votes">1</div><span id="post-59245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a -E option to select the occurrence of a field, but it only gives the options of first, last or all:</p><pre><code>-E &lt;fieldsoption&gt;=&lt;value&gt; set options for output when -T fields selected:
   ...
   occurrence=f|l|a      print first, last or all occurrences of each field</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '17, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59245" class="comments-container"></div><div id="comment-tools-59245" class="comment-tools"></div><div class="clear"></div><div id="comment-59245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

