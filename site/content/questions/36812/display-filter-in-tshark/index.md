+++
type = "question"
title = "Display filter in tshark"
description = '''While creating different flows from pcap file (say trace.pcap) I am using following command tshark -r trace.pcap -T fields -e frame.number -e ip.src -e ip.dst=&quot;172.141.90.14&quot; -e tcp.srcport -e frame.len –E separator=, -E header=y It gives an error as::ip.dst is not a valid field. Can anyone help me ...'''
date = "2014-10-03T03:38:00Z"
lastmod = "2014-10-03T06:04:00Z"
weight = 36812
keywords = [ "pcap", "tshark" ]
aliases = [ "/questions/36812" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display filter in tshark](/questions/36812/display-filter-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36812-score" class="post-score" title="current number of votes">0</div><span id="post-36812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While creating different flows from pcap file (say trace.pcap) I am using following command</p><p>tshark -r trace.pcap -T fields -e frame.number -e ip.src -e ip.dst="172.141.90.14" -e tcp.srcport -e frame.len –E separator=, -E header=y</p><p>It gives an error as::ip.dst is not a valid field. Can anyone help me in tracing this issue.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '14, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/2ddc96220369cf708ec792a8bfd4a3ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="loneharoon&#39;s gravatar image" /><p><span>loneharoon</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="loneharoon has no accepted answers">0%</span></p></div></div><div id="comments-container-36812" class="comments-container"></div><div id="comment-tools-36812" class="comment-tools"></div><div class="clear"></div><div id="comment-36812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36813"></span>

<div id="answer-container-36813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36813-score" class="post-score" title="current number of votes">0</div><span id="post-36813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most likely it does not work because with display filter type syntax you need to use double equals, like</p><p><code>-e ip.dst=="172.141.90.14"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '14, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36813" class="comments-container"><span id="36815"></span><div id="comment-36815" class="comment"><div id="post-36815-score" class="comment-score"></div><div class="comment-text"><p>I tried both ways like -e ip.dst=="192.12.3.2" ,and -e "ip.dst==192.12.3.2".</p><p>But still it is showing <strong>(tshark.exe:3228): WARNING</strong> : 'ip.dst==192.12.3.2' isn't a valid field! tshark: Some fields aren't valid</p></div><div id="comment-36815-info" class="comment-info"><span class="comment-age">(03 Oct '14, 04:11)</span> <span class="comment-user userinfo">loneharoon</span></div></div><span id="36816"></span><div id="comment-36816" class="comment"><div id="post-36816-score" class="comment-score"></div><div class="comment-text"><p>Hm I guess than it is simply not possible to use filter syntax in combination with "-e", because it is just a field designation. If you try using "ip.st" without anything else it should work. In that case you need to filter with a read filter or display filter (by adding a -R or -Y parameter)</p></div><div id="comment-36816-info" class="comment-info"><span class="comment-age">(03 Oct '14, 04:20)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-36813" class="comment-tools"></div><div class="clear"></div><div id="comment-36813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36817"></span>

<div id="answer-container-36817" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36817-score" class="post-score" title="current number of votes">0</div><span id="post-36817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper said: "-e" is not for <em>filters</em> it's for <em>fields</em>. So you probably want something like:</p><pre><code>tshark -r trace.pcap -T fields -e frame.number -e ip.src -e ip.dst -e tcp.srcport -e frame.len –E separator=, -E header=y -Yip.dst=&quot;172.141.90.14&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '14, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36817" class="comments-container"></div><div id="comment-tools-36817" class="comment-tools"></div><div class="clear"></div><div id="comment-36817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

