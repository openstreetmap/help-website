+++
type = "question"
title = "can&#x27;t run tcprewrite on 2 specific address - unable to parse as valid CIDR"
description = '''tcprewrite -N --pnat=10.0.0.39/32:10.0.0.39/32,192.168.1.1/32:192.168.1.1/32 -i ./upload.pcap -o ./upload_ip1.pcap and I get:   Unable to parse as a vaild CIDR: --pnat=10.0.0.39'''
date = "2017-09-11T03:02:00Z"
lastmod = "2017-09-11T23:39:00Z"
weight = 63579
keywords = [ "tcprewrite", "cidr" ]
aliases = [ "/questions/63579" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [can't run tcprewrite on 2 specific address - unable to parse as valid CIDR](/questions/63579/cant-run-tcprewrite-on-2-specific-address-unable-to-parse-as-valid-cidr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63579-score" class="post-score" title="current number of votes">0</div><span id="post-63579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>tcprewrite -N --pnat=10.0.0.39/32:10.0.0.39/32,192.168.1.1/32:192.168.1.1/32 -i ./upload.pcap -o ./upload_ip1.pcap</p><p>and I get: Unable to parse as a vaild CIDR: --pnat=10.0.0.39</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcprewrite" rel="tag" title="see questions tagged &#39;tcprewrite&#39;">tcprewrite</span> <span class="post-tag tag-link-cidr" rel="tag" title="see questions tagged &#39;cidr&#39;">cidr</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '17, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/b50e05a5f1954d250dd908dacce081c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kdani&#39;s gravatar image" /><p><span>kdani</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kdani has no accepted answers">0%</span></p></div></div><div id="comments-container-63579" class="comments-container"><span id="63582"></span><div id="comment-63582" class="comment"><div id="post-63582-score" class="comment-score"></div><div class="comment-text"><p>Note that tcprewrite doesn't come from the Wireshark developers; it's from <a href="http://tcpreplay.appneta.com">these people</a>.</p></div><div id="comment-63582-info" class="comment-info"><span class="comment-age">(11 Sep '17, 22:49)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-63579" class="comment-tools"></div><div class="clear"></div><div id="comment-63579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63580"></span>

<div id="answer-container-63580" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63580-score" class="post-score" title="current number of votes">1</div><span id="post-63580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kdani has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The parameter "-N" and "--pnat=" are the same (just long and short version). Therefore just specify one of them, e.g.</p><p><code>tcprewrite -N 10.0.0.39/32:10.0.0.39/32,192.168.1.1/32:192.168.1.1/32 -i ./upload.pcap -o ./upload_ip1.pcap</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '17, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-63580" class="comments-container"><span id="63583"></span><div id="comment-63583" class="comment"><div id="post-63583-score" class="comment-score"></div><div class="comment-text"><p>actually - the right answer would be to use only 1 pair - this code replace the ip with itself - but you are correct about using both -n and --pnat</p></div><div id="comment-63583-info" class="comment-info"><span class="comment-age">(11 Sep '17, 23:39)</span> <span class="comment-user userinfo">kdani</span></div></div></div><div id="comment-tools-63580" class="comment-tools"></div><div class="clear"></div><div id="comment-63580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

