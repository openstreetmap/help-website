+++
type = "question"
title = "Display filter with ip destination and port dest: what is wrong?"
description = '''tshark -r &quot;semAtaques.pcap&quot; -Tfields -e frame.time_epoch -e tcp.window_size_value -e ip.dst -Y &quot;ip.dst == 192.168.91.5&quot; -e tcp.port eq 80 &amp;gt;&amp;gt; winTime_10Abril_SemAtaques.txt '''
date = "2017-05-28T17:38:00Z"
lastmod = "2017-05-28T20:21:00Z"
weight = 61677
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/61677" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Display filter with ip destination and port dest: what is wrong?](/questions/61677/display-filter-with-ip-destination-and-port-dest-what-is-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61677-score" class="post-score" title="current number of votes">0</div><span id="post-61677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>tshark -r &quot;semAtaques.pcap&quot; -Tfields -e frame.time_epoch -e tcp.window_size_value -e ip.dst -Y &quot;ip.dst == 192.168.91.5&quot; -e tcp.port eq 80 &gt;&gt; winTime_10Abril_SemAtaques.txt</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '17, 17:38</strong></p><img src="https://secure.gravatar.com/avatar/5e26585f104939e9d0d1045d25254f1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foxmodem&#39;s gravatar image" /><p><span>foxmodem</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foxmodem has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 May '17, 08:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-61677" class="comments-container"></div><div id="comment-tools-61677" class="comment-tools"></div><div class="clear"></div><div id="comment-61677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61680"></span>

<div id="answer-container-61680" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61680-score" class="post-score" title="current number of votes">1</div><span id="post-61680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>-Y "ip.dst==192.168.91.5 &amp;&amp; tcp.port==80" for all packets to 192.168.91.5 with 80 as either source or destination port,</p><p>or</p><p>-Y "ip.dst==192.168.91.5 &amp;&amp; tcp.dstport==80" for all packets to 192.168.91.5 with 80 as the destination port.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '17, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-61680" class="comments-container"></div><div id="comment-tools-61680" class="comment-tools"></div><div class="clear"></div><div id="comment-61680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61678"></span>

<div id="answer-container-61678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61678-score" class="post-score" title="current number of votes">0</div><span id="post-61678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"-e tcp.port eq 80" is probably the problem - I guess you wanted to add that to the -Y parameter? If not, it should only be "-e tcp.port" without the compare operator.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '17, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61678" class="comments-container"><span id="61679"></span><div id="comment-61679" class="comment"><div id="post-61679-score" class="comment-score"></div><div class="comment-text"><p>I need to filter TCP port 80 too. How can I add it in the code? Thanks</p></div><div id="comment-61679-info" class="comment-info"><span class="comment-age">(28 May '17, 17:46)</span> <span class="comment-user userinfo">foxmodem</span></div></div><span id="61681"></span><div id="comment-61681" class="comment"><div id="post-61681-score" class="comment-score"></div><div class="comment-text"><p>Yes, he wanted to add that to the -Y parameter; Jim Aragon's answer shows how to do that.</p></div><div id="comment-61681-info" class="comment-info"><span class="comment-age">(28 May '17, 20:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-61678" class="comment-tools"></div><div class="clear"></div><div id="comment-61678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

