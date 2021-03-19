+++
type = "question"
title = "Is there any way to directly capture in CSV using tshark?"
description = '''Hello All, I have been trying to capture a wireshark trace from tshark but i need to capture the output in CSV directly instead of first saving in pcap and then converting it. Could anyone help here in this case? I have already used this command but it doesnt seem to help here tshark.exe -r &quot;C:&#92;aa_0...'''
date = "2015-08-26T02:52:00Z"
lastmod = "2015-08-27T14:07:00Z"
weight = 45363
keywords = [ "output", "csv", "tshark", "trace", "capture" ]
aliases = [ "/questions/45363" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there any way to directly capture in CSV using tshark?](/questions/45363/is-there-any-way-to-directly-capture-in-csv-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45363-score" class="post-score" title="current number of votes">0</div><span id="post-45363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I have been trying to capture a wireshark trace from tshark but i need to capture the output in CSV directly instead of first saving in pcap and then converting it. Could anyone help here in this case?</p><p>I have already used this command but it doesnt seem to help here tshark.exe -r "C:\aa_00001_20150826125423.pcap" -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e _ws.col.info -E header=y -E separator=, -E quote=d -E occurrence=f &gt; "C:\test11.csv"</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '15, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/02276086edbece4c74826bae17384888?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rahul527&#39;s gravatar image" /><p><span>rahul527</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rahul527 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Aug '15, 04:58</strong> </span></p></div></div><div id="comments-container-45363" class="comments-container"><span id="45365"></span><div id="comment-45365" class="comment"><div id="post-45365-score" class="comment-score"></div><div class="comment-text"><p>What is your problem exactly with this command?</p></div><div id="comment-45365-info" class="comment-info"><span class="comment-age">(26 Aug '15, 03:44)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-45363" class="comment-tools"></div><div class="clear"></div><div id="comment-45363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45423"></span>

<div id="answer-container-45423" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45423-score" class="post-score" title="current number of votes">0</div><span id="post-45423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The command you are using is to read an existing .pcap file, whereas your question is about creating a new capture file as a .csv?</p><p>This works completely fine for me(Tested on Linux):</p><pre><code>tshark -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e _ws.col.info -E header=y -E separator=&quot;,&quot; -E quote=d -E occurrence=f &gt; file.csv</code></pre><p>The output looks like this:</p><pre><code>&quot;1&quot;,&quot;Aug 27, 2015 22:23:20.192158000BST&quot;,&quot;xx:xx:xx:xx:xx:xx&quot;,&quot;xx:xx:xx:xx:xx:xx&quot;,&quot;192.168.0.8&quot;,&quot;157.56.192.xxx&quot;,&quot;6&quot;,</code></pre><p>The -r argument you used is exclusively for reading existing files.</p><p>Edit:</p><p>Also in your code the <code>-E separator=,</code> may be incorrect. You might need to put any string value in "" to represent text. Otherwise the application is looking for an argument called <code>separator=,</code> which doesn't exist depending on version type (My wireshark version wouldn't accept it).</p><p>Hope this helps, let me know if you need a hand with anything else. :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/6706dcd3c17a4d870b3a0d633c541c92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbm&#39;s gravatar image" /><p><span>tbm</span><br />
<span class="score" title="29 reputation points">29</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '15, 14:31</strong> </span></p></div></div><div id="comments-container-45423" class="comments-container"></div><div id="comment-tools-45423" class="comment-tools"></div><div class="clear"></div><div id="comment-45423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

