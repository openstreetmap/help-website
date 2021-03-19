+++
type = "question"
title = "How to decrypt ssl traffic with centos TShark 1.10.3 ?"
description = '''link text i try it on the windows TShark (Wireshark) 1.99.9 (v1.99.9-0-g52a4a78 from master) no wireshark_ssl found and any pem file.... i want on centos decrypt ssl use by tshark.how?'''
date = "2015-09-07T00:57:00Z"
lastmod = "2015-09-07T16:33:00Z"
weight = 45652
keywords = [ "tshark", "centos" ]
aliases = [ "/questions/45652" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to decrypt ssl traffic with centos TShark 1.10.3 ?](/questions/45652/how-to-decrypt-ssl-traffic-with-centos-tshark-1103)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45652-score" class="post-score" title="current number of votes">0</div><span id="post-45652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="https://ask.wireshark.org/questions/4766/how-to-decrypt-ssl-traffic-with-tshark-16">link text</a></p><p>i try it on the windows TShark (Wireshark) 1.99.9 (v1.99.9-0-g52a4a78 from master) no wireshark_ssl found and any pem file....</p><p>i want on centos decrypt ssl use by tshark.how?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '15, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/a297d3fd8782bd82581536a255048422?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhylninc&#39;s gravatar image" /><p><span>zhylninc</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhylninc has no accepted answers">0%</span></p></div></div><div id="comments-container-45652" class="comments-container"></div><div id="comment-tools-45652" class="comment-tools"></div><div class="clear"></div><div id="comment-45652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45677"></span>

<div id="answer-container-45677" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45677-score" class="post-score" title="current number of votes">0</div><span id="post-45677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please take a look at the Wiki:</p><blockquote><p><a href="https://wiki.wireshark.org/SSL#Wireshark">https://wiki.wireshark.org/SSL#Wireshark</a></p></blockquote><p>If you search for "tshark", you'll find the following.</p><pre><code># tshark commands
tshark -o &quot;ssl.desegment_ssl_records: TRUE&quot; -o &quot;ssl.desegment_ssl_application_data: TRUE&quot; -o &quot;ssl.keys_list: 127.0.0.1,4443,http,/home/dirkx/xx/privkey.pem&quot; -o &quot;ssl.debug_file: /home/dirkx/.wireshark-log&quot; -i eth0 -R &quot;tcp.port == 4443&quot;</code></pre><p>So, if that does not work for you, please post the full tshark command you were running and the <strong>full</strong> error message printed by tshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45677" class="comments-container"></div><div id="comment-tools-45677" class="comment-tools"></div><div class="clear"></div><div id="comment-45677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

