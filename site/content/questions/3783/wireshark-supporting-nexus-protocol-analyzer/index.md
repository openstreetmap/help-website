+++
type = "question"
title = "wireshark supporting NEXUS protocol analyzer?"
description = '''Hi, Does the wireshark support log files of NEXUS protocol analyzer? thanks'''
date = "2011-04-28T03:28:00Z"
lastmod = "2011-05-24T15:55:00Z"
weight = 3783
keywords = [ "nexus", "support" ]
aliases = [ "/questions/3783" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark supporting NEXUS protocol analyzer?](/questions/3783/wireshark-supporting-nexus-protocol-analyzer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3783-score" class="post-score" title="current number of votes">0</div><span id="post-3783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Does the wireshark support log files of NEXUS protocol analyzer?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nexus" rel="tag" title="see questions tagged &#39;nexus&#39;">nexus</span> <span class="post-tag tag-link-support" rel="tag" title="see questions tagged &#39;support&#39;">support</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '11, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/7cd42793b9dc6b3ce6985cffbcaa3485?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="solarisan&#39;s gravatar image" /><p><span>solarisan</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="solarisan has no accepted answers">0%</span></p></div></div><div id="comments-container-3783" class="comments-container"><span id="3793"></span><div id="comment-3793" class="comment"><div id="post-3793-score" class="comment-score">1</div><div class="comment-text"><p>Can you be more specific? Are you referring to the NexusINSIGHT 3G analyzer, the Cisco Nexus switches, or something else named "Nexus" that generates capture files?</p></div><div id="comment-3793-info" class="comment-info"><span class="comment-age">(28 Apr '11, 10:45)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div><span id="4201"></span><div id="comment-4201" class="comment"><div id="post-4201-score" class="comment-score"></div><div class="comment-text"><p>yes Nexus Insight</p></div><div id="comment-4201-info" class="comment-info"><span class="comment-age">(24 May '11, 11:57)</span> <span class="comment-user userinfo">solarisan</span></div></div><span id="4206"></span><div id="comment-4206" class="comment"><div id="post-4206-score" class="comment-score">1</div><div class="comment-text"><p>See Chris Maynard's (cmaynard) answer, then. (No, it does not support them.)</p></div><div id="comment-4206-info" class="comment-info"><span class="comment-age">(24 May '11, 15:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-3783" class="comment-tools"></div><div class="clear"></div><div id="comment-3783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3791"></span>

<div id="answer-container-3791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3791-score" class="post-score" title="current number of votes">1</div><span id="post-3791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, they are not yet supported. The <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOOpenSection.html#ChIOInputFormatsSection">Wireshark user guide</a> lists the current capture file formats supported and the <a href="http://www.wireshark.org/docs/relnotes/wireshark-1.5.1.html#NewCapture">Wireshark 1.5.1 release notes</a> lists any new ones that might have been added in the development branch, which will become supported in the next stable branch. The <a href="http://www.wireshark.org/faq.html#q1.12">FAQ</a> also provides some information regarding capture file formats.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '11, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3791" class="comments-container"></div><div id="comment-tools-3791" class="comment-tools"></div><div class="clear"></div><div id="comment-3791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

