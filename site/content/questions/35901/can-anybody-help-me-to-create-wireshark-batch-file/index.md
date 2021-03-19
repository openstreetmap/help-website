+++
type = "question"
title = "Can anybody help me to create wireshark batch file?"
description = '''I need to create bat file recording all data from two hosts (192.168.1.200 or 192.168.1.201) and:  store in subfolder (C:&#92;CDR) as file name_date_starthour.txt  each 1Mb start with windows and restart after crash  Can someone help me? my first bat: wireshark -B 10 -i any -f &quot;192.168.1.200 and 192.168...'''
date = "2014-09-01T02:10:00Z"
lastmod = "2014-09-01T11:26:00Z"
weight = 35901
keywords = [ "batch" ]
aliases = [ "/questions/35901" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can anybody help me to create wireshark batch file?](/questions/35901/can-anybody-help-me-to-create-wireshark-batch-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35901-score" class="post-score" title="current number of votes">0</div><span id="post-35901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to create bat file recording all data from two hosts (192.168.1.200 or 192.168.1.201) and:</p><ul><li>store in subfolder (C:\CDR) as file name_date_starthour.txt</li><li>each 1Mb</li><li>start with windows and restart after crash</li></ul><p>Can someone help me?</p><p>my first bat: wireshark -B 10 -i any -f "192.168.1.200 and 192.168.1.201" -k \ -b filesize:10240 -w E:\CDR\wireshark_<code>date +%m%d</code></p><p>not working (invalid argument: +d')</p><p>with hints from: <a href="https://ask.wireshark.org/questions/16576/how-to-save-the-capture-options">https://ask.wireshark.org/questions/16576/how-to-save-the-capture-options</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '14, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/3690418a10f47a981a8999ff8bab8a9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="invoso&#39;s gravatar image" /><p><span>invoso</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="invoso has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Sep '14, 15:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-35901" class="comments-container"></div><div id="comment-tools-35901" class="comment-tools"></div><div class="clear"></div><div id="comment-35901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35904"></span>

<div id="answer-container-35904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35904-score" class="post-score" title="current number of votes">0</div><span id="post-35904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You don't need the "_date +%m%d" part at the end, because the -b parameter will add full date and time to the filename automatically. Try with "-w E:\CDR\wireshark.pcapng" at the end instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Sep '14, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35904" class="comments-container"><span id="35908"></span><div id="comment-35908" class="comment"><div id="post-35908-score" class="comment-score"></div><div class="comment-text"><p>wireshark return: "you can't specify both a live capture and a capture file to be read"</p><p>Is possible to run two different instances of wireshark on one machine?</p></div><div id="comment-35908-info" class="comment-info"><span class="comment-age">(01 Sep '14, 05:18)</span> <span class="comment-user userinfo">invoso</span></div></div><span id="35910"></span><div id="comment-35910" class="comment"><div id="post-35910-score" class="comment-score"></div><div class="comment-text"><p>yes, but you should use two dumpcap instances instead. Wireshark doesn't capture packets anyway, it starts a dumpcap process each time. See <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div id="comment-35910-info" class="comment-info"><span class="comment-age">(01 Sep '14, 06:11)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="35916"></span><div id="comment-35916" class="comment"><div id="post-35916-score" class="comment-score"></div><div class="comment-text"><p>Why wireshark return: "you can't specify both a live capture and a capture file to be read"?</p></div><div id="comment-35916-info" class="comment-info"><span class="comment-age">(01 Sep '14, 11:26)</span> <span class="comment-user userinfo">invoso</span></div></div></div><div id="comment-tools-35904" class="comment-tools"></div><div class="clear"></div><div id="comment-35904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

