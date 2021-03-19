+++
type = "question"
title = "tshark -T json  data insert mongodb ,report&quot; key frame.interface_id must not contain &#x27;.&#x27;&quot;"
description = '''tshark -r test.pcap -V -T json  json example: ================================== &quot;tcp&quot;: {  &quot;tcp.srcport&quot;: &quot;60818&quot;,  &quot;tcp.dstport&quot;: &quot;27017&quot;,  &quot;tcp.port&quot;: &quot;60818&quot;,  &quot;tcp.port&quot;: &quot;27017&quot;,  &quot;tcp.stream&quot;: &quot;18&quot;,  &quot;tcp.len&quot;: &quot;0&quot;,  ... ....  =================================== json data inert mongodb report ...'''
date = "2017-04-27T23:17:00Z"
lastmod = "2017-04-28T05:30:00Z"
weight = 61084
keywords = [ "json" ]
aliases = [ "/questions/61084" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -T json data insert mongodb ,report" key frame.interface\_id must not contain '.'"](/questions/61084/tshark-t-json-data-insert-mongodb-report-key-frameinterface_id-must-not-contain)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61084-score" class="post-score" title="current number of votes">0</div><span id="post-61084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>tshark -r test.pcap -V -T json 
json example:
==================================
&quot;tcp&quot;: {
          &quot;tcp.srcport&quot;: &quot;60818&quot;,
          &quot;tcp.dstport&quot;: &quot;27017&quot;,
          &quot;tcp.port&quot;: &quot;60818&quot;,
          &quot;tcp.port&quot;: &quot;27017&quot;,
          &quot;tcp.stream&quot;: &quot;18&quot;,
          &quot;tcp.len&quot;: &quot;0&quot;,
    ... ....

===================================
json data inert mongodb report {&quot;message&quot; : &quot;Error: key frame.interface_id must not contain &#39;.&#39;&quot;}</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '17, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/231823579f4fd4763beb4d26fba40775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newman01&#39;s gravatar image" /><p><span>newman01</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newman01 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '17, 01:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-61084" class="comments-container"></div><div id="comment-tools-61084" class="comment-tools"></div><div class="clear"></div><div id="comment-61084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61089"></span>

<div id="answer-container-61089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61089-score" class="post-score" title="current number of votes">1</div><span id="post-61089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If this is so, it should be reported as a bug in <a href="https://bugs.wireshark.org">the bug database</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '17, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61089" class="comments-container"><span id="61095"></span><div id="comment-61095" class="comment"><div id="post-61095-score" class="comment-score"></div><div class="comment-text"><p>The wiki page on <a href="https://wiki.wireshark.org/ReportingBugs">Reporting Bugs</a> might also be of help.</p></div><div id="comment-61095-info" class="comment-info"><span class="comment-age">(28 Apr '17, 03:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="61102"></span><div id="comment-61102" class="comment"><div id="post-61102-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13668">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13668</a></p><p>reported!</p></div><div id="comment-61102-info" class="comment-info"><span class="comment-age">(28 Apr '17, 05:30)</span> <span class="comment-user userinfo">newman01</span></div></div></div><div id="comment-tools-61089" class="comment-tools"></div><div class="clear"></div><div id="comment-61089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

