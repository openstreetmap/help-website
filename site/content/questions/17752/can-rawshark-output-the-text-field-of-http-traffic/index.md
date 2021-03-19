+++
type = "question"
title = "Can rawshark output the text field of HTTP traffic?"
description = '''I&#x27;m trying to get rawshark to output the text of an HTTP stream. I&#x27;m running the following: cat wlan.pcap | rawshark -r - -d proto:radiotap -d proto:http -s -F tcp.dstport -F ip.src -F http.host -F tcp.data -F text  It outputs the tcp.dstport, ip.src, and http.host but fails to output tcp.data and t...'''
date = "2013-01-17T10:33:00Z"
lastmod = "2013-01-18T06:18:00Z"
weight = 17752
keywords = [ "rawshark" ]
aliases = [ "/questions/17752" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can rawshark output the text field of HTTP traffic?](/questions/17752/can-rawshark-output-the-text-field-of-http-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17752-score" class="post-score" title="current number of votes">0</div><span id="post-17752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to get rawshark to output the text of an HTTP stream. I'm running the following:</p><pre><code>cat wlan.pcap | rawshark -r - -d proto:radiotap -d proto:http -s -F tcp.dstport -F ip.src -F http.host -F tcp.data -F text</code></pre><p>It outputs the tcp.dstport, ip.src, and http.host but fails to output tcp.data and text reliably.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rawshark" rel="tag" title="see questions tagged &#39;rawshark&#39;">rawshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '13, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/9017f8af999ec51ae7fe6d7b5b5fc213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joeferner&#39;s gravatar image" /><p><span>joeferner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joeferner has no accepted answers">0%</span></p></div></div><div id="comments-container-17752" class="comments-container"></div><div id="comment-tools-17752" class="comment-tools"></div><div class="clear"></div><div id="comment-17752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17759"></span>

<div id="answer-container-17759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17759-score" class="post-score" title="current number of votes">0</div><span id="post-17759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One issue is that "tcp.data" is not there on every frame: see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8084">bug 8084</a> for details.</p><p>Unfortunately I don't think there's a field which contains the entire HTTP payload.</p><p>I don't know about the "text" field/issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '13, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-17759" class="comments-container"><span id="17775"></span><div id="comment-17775" class="comment"><div id="post-17775-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I guess I'll use tshark in the mean time. To bad tshark can't accept a piped in file.</p></div><div id="comment-17775-info" class="comment-info"><span class="comment-age">(18 Jan '13, 06:18)</span> <span class="comment-user userinfo">joeferner</span></div></div></div><div id="comment-tools-17759" class="comment-tools"></div><div class="clear"></div><div id="comment-17759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

