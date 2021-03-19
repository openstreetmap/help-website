+++
type = "question"
title = "How can I map SAP x0c8 to SNA protocol ?"
description = '''Per wireshark - Internals - Dissector tables - Integer tables SNA dissector is being called for LLC SAP 4, 8 12, 64 only.  There are some SNA stacks that receive SNA NLP frames on DSAP 0xc8.  Here is a sample capture file showing SNA NLP traffic in both directions.  sna_nlp.sap_c8.pcapng Can the 0xC...'''
date = "2015-09-26T23:34:00Z"
lastmod = "2015-09-27T06:03:00Z"
weight = 46189
keywords = [ "dsap", "sap", "snasw", "sna" ]
aliases = [ "/questions/46189" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I map SAP x0c8 to SNA protocol ?](/questions/46189/how-can-i-map-sap-x0c8-to-sna-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46189-score" class="post-score" title="current number of votes">0</div><span id="post-46189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Per wireshark - Internals - Dissector tables - Integer tables SNA dissector is being called for LLC SAP 4, 8 12, 64 only.</p><p>There are some SNA stacks that receive SNA NLP frames on DSAP 0xc8.</p><p>Here is a sample capture file showing SNA NLP traffic in both directions.</p><p><a href="https://www.ibm.com/developerworks/community/wikis/form/api/wiki/6ca65ea6-46b2-4aea-9bea-5bbcb0f2e06b/page/779148f0-9959-4221-8693-022779f2543e/attachment/48d8a37d-4dab-4c29-8c84-6ce16061fdee/media/sna_nlp.sap_c8.pcapng">sna_nlp.sap_c8.pcapng</a></p><p>Can the 0xC8/200 SAP value be included for SAP dissection ?</p><p>How can I dissect those frames using LUA (being a LUA script layman) ?</p><p>Thanks and regards Matthias</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dsap" rel="tag" title="see questions tagged &#39;dsap&#39;">dsap</span> <span class="post-tag tag-link-sap" rel="tag" title="see questions tagged &#39;sap&#39;">sap</span> <span class="post-tag tag-link-snasw" rel="tag" title="see questions tagged &#39;snasw&#39;">snasw</span> <span class="post-tag tag-link-sna" rel="tag" title="see questions tagged &#39;sna&#39;">sna</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '15, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Sep '15, 02:28</strong> </span></p></div></div><div id="comments-container-46189" class="comments-container"><span id="46190"></span><div id="comment-46190" class="comment"><div id="post-46190-score" class="comment-score"></div><div class="comment-text"><p>The link does not work correctly for me...</p></div><div id="comment-46190-info" class="comment-info"><span class="comment-age">(27 Sep '15, 00:01)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46191"></span><div id="comment-46191" class="comment"><div id="post-46191-score" class="comment-score"></div><div class="comment-text"><p>Sorry for this. I updated the link</p></div><div id="comment-46191-info" class="comment-info"><span class="comment-age">(27 Sep '15, 02:29)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-46189" class="comment-tools"></div><div class="clear"></div><div id="comment-46189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46192"></span>

<div id="answer-container-46192" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46192-score" class="post-score" title="current number of votes">0</div><span id="post-46192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If it's not a user settable item, it should go through the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark bug system</a>. You can file an enhancement bug there, and please attach the sample capture as well. This makes development and test much easier. If it's a simple change as it seems to be, it could be quickly implemented.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '15, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46192" class="comments-container"><span id="46193"></span><div id="comment-46193" class="comment"><div id="post-46193-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I opened an enhancement bug 11551 <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11551">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11551</a> .</p></div><div id="comment-46193-info" class="comment-info"><span class="comment-age">(27 Sep '15, 06:03)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-46192" class="comment-tools"></div><div class="clear"></div><div id="comment-46192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

