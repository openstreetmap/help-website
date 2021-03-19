+++
type = "question"
title = "tshark equivalent of Wireshark commands"
description = '''Is there an equivalent command line in tshark that does the following.  Filters the packet to TCP only (tcp.port==5555) Follow TCP stream. Save the file as raw.  The process will enable us to view real time video stream via TCP.'''
date = "2016-05-09T22:25:00Z"
lastmod = "2016-05-18T19:49:00Z"
weight = 52379
keywords = [ "capture-filter", "tshark", "wireshark" ]
aliases = [ "/questions/52379" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark equivalent of Wireshark commands](/questions/52379/tshark-equivalent-of-wireshark-commands)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52379-score" class="post-score" title="current number of votes">0</div><span id="post-52379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there an equivalent command line in tshark that does the following.</p><ul><li>Filters the packet to TCP only (tcp.port==5555)</li><li>Follow TCP stream.</li><li>Save the file as raw.</li></ul><p>The process will enable us to view real time video stream via TCP.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '16, 22:25</strong></p><img src="https://secure.gravatar.com/avatar/caee4da3afe707dd184f806fedead31b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dr%20Dre&#39;s gravatar image" /><p><span>Dr Dre</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dr Dre has no accepted answers">0%</span></p></div></div><div id="comments-container-52379" class="comments-container"></div><div id="comment-tools-52379" class="comment-tools"></div><div class="clear"></div><div id="comment-52379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52387"></span>

<div id="answer-container-52387" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52387-score" class="post-score" title="current number of votes">0</div><span id="post-52387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>tshark -i eth0 -z "follow,tcp,raw,1" "tcp port 5555"</code> would come close, but still requires you to process the text output into a raw file. Better option would be to consult <a href="https://wiki.wireshark.org/Tools">the tools section</a> of the wiki. Here you may find tools more suitable for your purpose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '16, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52387" class="comments-container"><span id="52455"></span><div id="comment-52455" class="comment"><div id="post-52455-score" class="comment-score"></div><div class="comment-text"><p>Jaap,</p><p>Thanks for that. I have seen this command before. I thought I was just getting the syntax wrong. So I tried it again yesterday. When I use the command above wireshark, I get a notification saying that z follow is not an option.</p><p>Dre Dre.</p></div><div id="comment-52455-info" class="comment-info"><span class="comment-age">(11 May '16, 17:13)</span> <span class="comment-user userinfo">Dr Dre</span></div></div><span id="52457"></span><div id="comment-52457" class="comment"><div id="post-52457-score" class="comment-score"></div><div class="comment-text"><p><span>@Dr Dre</span>, because it's a command line option to tshark, not to Wireshark?</p></div><div id="comment-52457-info" class="comment-info"><span class="comment-age">(11 May '16, 22:28)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52458"></span><div id="comment-52458" class="comment"><div id="post-52458-score" class="comment-score"></div><div class="comment-text"><p>Sorrt Jaap, just clarifying. I did use this via tshark.</p></div><div id="comment-52458-info" class="comment-info"><span class="comment-age">(11 May '16, 22:53)</span> <span class="comment-user userinfo">Dr Dre</span></div></div><span id="52461"></span><div id="comment-52461" class="comment"><div id="post-52461-score" class="comment-score"></div><div class="comment-text"><p>What tshark version are we talking about here? I think it was already in by version 1.8.</p></div><div id="comment-52461-info" class="comment-info"><span class="comment-age">(12 May '16, 02:58)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="52750"></span><div id="comment-52750" class="comment"><div id="post-52750-score" class="comment-score"></div><div class="comment-text"><p>Jaap,</p><p>I just checked, the version I have on my Ubuntu is 1.6.7.</p><p>Dre Dre</p></div><div id="comment-52750-info" class="comment-info"><span class="comment-age">(18 May '16, 18:08)</span> <span class="comment-user userinfo">Dr Dre</span></div></div><span id="52752"></span><div id="comment-52752" class="comment not_top_scorer"><div id="post-52752-score" class="comment-score"></div><div class="comment-text"><p>I just changed the version of wireshark/tshark and the z follow command works. Having issues then with saving it to a file.</p></div><div id="comment-52752-info" class="comment-info"><span class="comment-age">(18 May '16, 19:49)</span> <span class="comment-user userinfo">Dr Dre</span></div></div></div><div id="comment-tools-52387" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-52387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

