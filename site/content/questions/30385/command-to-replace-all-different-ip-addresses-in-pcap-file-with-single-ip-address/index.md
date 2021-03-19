+++
type = "question"
title = "command to replace all different IP addresses in pcap file with single IP address"
description = '''I have a pcap file which has multiple IP addresses, I want to replace those multiple IP addresses with single address, is there any command to do so?'''
date = "2014-03-04T02:20:00Z"
lastmod = "2014-03-04T10:16:00Z"
weight = 30385
keywords = [ "tcprewrite" ]
aliases = [ "/questions/30385" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [command to replace all different IP addresses in pcap file with single IP address](/questions/30385/command-to-replace-all-different-ip-addresses-in-pcap-file-with-single-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30385-score" class="post-score" title="current number of votes">0</div><span id="post-30385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file which has multiple IP addresses, I want to replace those multiple IP addresses with single address, is there any command to do so?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcprewrite" rel="tag" title="see questions tagged &#39;tcprewrite&#39;">tcprewrite</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '14, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/2a443ec0e6b04037ebd22c41eb517bbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shubhangi&#39;s gravatar image" /><p><span>shubhangi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shubhangi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Mar '14, 02:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-30385" class="comments-container"></div><div id="comment-tools-30385" class="comment-tools"></div><div class="clear"></div><div id="comment-30385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30386"></span>

<div id="answer-container-30386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30386-score" class="post-score" title="current number of votes">0</div><span id="post-30386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Why do you want to replace all IP addresses with a single address? That would lead to a file with the IP talking to itself, which is not seen on networks and doesn't make any sense (except for localhost stuff, but you don't see that in a pcap usually).</p><p>If you want to replace IP addresses you can use <a href="http://tcpreplay.synfin.net/wiki/tcprewrite">tcprewrite</a>, <a href="http://bittwist.sourceforge.net/">bittwiste</a> or <a href="http://www.tracewrangler.com/">TraceWrangler</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30386" class="comments-container"><span id="30390"></span><div id="comment-30390" class="comment"><div id="post-30390-score" class="comment-score"></div><div class="comment-text"><p>sorry, I mean I want to replace multiple SOURCE IP addresses with a single SOURCE IP address using tcprewrite, can you help me out?</p></div><div id="comment-30390-info" class="comment-info"><span class="comment-age">(04 Mar '14, 03:59)</span> <span class="comment-user userinfo">shubhangi</span></div></div><span id="30408"></span><div id="comment-30408" class="comment"><div id="post-30408-score" class="comment-score"></div><div class="comment-text"><p>Hm.. that can lead to 'collisions' if different clients (different IPs) are using the same source port to one destination address. The resulting capture file will be useless, as you cannot distinguish the former differing streams.</p><p>So, why do you want to do that?</p></div><div id="comment-30408-info" class="comment-info"><span class="comment-age">(04 Mar '14, 09:43)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30413"></span><div id="comment-30413" class="comment"><div id="post-30413-score" class="comment-score"></div><div class="comment-text"><p>Not to mention most protocols are bi-directional, so you'd change from this:</p><p>A-&gt;B B-&gt;A A-&gt;B B-&gt;A</p><p>To this:</p><p>C-&gt;B B-&gt;A C-&gt;B B-&gt;A</p><p>(or C-&gt;A and C-&gt;B depending on whether all source addresses are changed or not)</p><p>Kinda silly. :)</p></div><div id="comment-30413-info" class="comment-info"><span class="comment-age">(04 Mar '14, 10:16)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-30386" class="comment-tools"></div><div class="clear"></div><div id="comment-30386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

