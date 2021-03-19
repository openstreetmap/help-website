+++
type = "question"
title = "How to detect ARP spoofing"
description = '''Hi all, can this be consider ARP sproofing ? How can I find ARP sproofing because when i filter by arp i couldn&#x27;t see it 192.168.60.7 was able to reach 192.168.100.1 then later there&#x27;s a request to ask who is 192.168.60.7 finally i can see 192.168.60.7 unable to reach 192.168.100.1 at packet 50428 '''
date = "2016-12-12T04:10:00Z"
lastmod = "2016-12-12T07:01:00Z"
weight = 58016
keywords = [ "arpspoofing" ]
aliases = [ "/questions/58016" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to detect ARP spoofing](/questions/58016/how-to-detect-arp-spoofing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58016-score" class="post-score" title="current number of votes">0</div><span id="post-58016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, can this be consider ARP sproofing ? How can I find ARP sproofing because when i filter by arp i couldn't see it</p><p>192.168.60.7 was able to reach 192.168.100.1</p><p>then later there's a request to ask who is 192.168.60.7</p><p>finally i can see 192.168.60.7 unable to reach 192.168.100.1 at packet 50428</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ARP_sproofing.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arpspoofing" rel="tag" title="see questions tagged &#39;arpspoofing&#39;">arpspoofing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '16, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/149d6f8eb0595bad31c406551c9654a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doran_lum&#39;s gravatar image" /><p><span>doran_lum</span><br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doran_lum has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '16, 21:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-58016" class="comments-container"></div><div id="comment-tools-58016" class="comment-tools"></div><div class="clear"></div><div id="comment-58016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58017"></span>

<div id="answer-container-58017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58017-score" class="post-score" title="current number of votes">0</div><span id="post-58017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your screenshot looks more like a normal arp cache update as it is discussed here: <a href="https://ask.wireshark.org/questions/57174/seeing-lots-of-arp-requests-even-though-the-hosts-have-the-mac-address-in-their-arp-cache-already">https://ask.wireshark.org/questions/57174/seeing-lots-of-arp-requests-even-though-the-hosts-have-the-mac-address-in-their-arp-cache-already</a></p><p>ARP spoof looks like this:</p><p>192.168.2.1 is at ab:ab:ab:ab:ab:ab</p><p>And</p><p>192.168.2.1 is at 10:10:10:10:10:10</p><p>Where the mac addresses are just examples.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '16, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-58017" class="comments-container"></div><div id="comment-tools-58017" class="comment-tools"></div><div class="clear"></div><div id="comment-58017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58020"></span>

<div id="answer-container-58020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58020-score" class="post-score" title="current number of votes">0</div><span id="post-58020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is how ARP-spoofing attack looks in Wireshark:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/arp_poison.JPG" alt="alt text" /></p><p>Wireshark warns you by the message "(duplicate use of &lt;ip&gt; detected!)". In my case I used Intercepter NG to make the attack.</p><p>You can use filter expression "arp.duplicate-address-detected" to quickly find if there are any such occurences in your trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '16, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p><span>Packet_vlad</span><br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '16, 07:03</strong> </span></p></div></div><div id="comments-container-58020" class="comments-container"></div><div id="comment-tools-58020" class="comment-tools"></div><div class="clear"></div><div id="comment-58020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

