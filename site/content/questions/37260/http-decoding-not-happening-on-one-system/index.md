+++
type = "question"
title = "HTTP decoding not happening on one system"
description = '''Dear Experts, We are facing a peculiar problem. We have a pcap which we are able to decode and see the HTTP messages on one system. But on the other system, this is not working.  We checked the ports configured and they are same on both systems.  Is there any other configuration to be checked?  Rega...'''
date = "2014-10-21T23:24:00Z"
lastmod = "2014-10-22T01:53:00Z"
weight = 37260
keywords = [ "http", "decoding" ]
aliases = [ "/questions/37260" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP decoding not happening on one system](/questions/37260/http-decoding-not-happening-on-one-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37260-score" class="post-score" title="current number of votes">0</div><span id="post-37260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Experts,</p><p>We are facing a peculiar problem. We have a pcap which we are able to decode and see the HTTP messages on one system. But on the other system, this is not working.</p><p>We checked the ports configured and they are same on both systems. Is there any other configuration to be checked?</p><p>Regards, Prashanth</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-decoding" rel="tag" title="see questions tagged &#39;decoding&#39;">decoding</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/229c0e8119c7468de2b30a08f103feaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prashanth&#39;s gravatar image" /><p><span>Prashanth</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prashanth has no accepted answers">0%</span></p></div></div><div id="comments-container-37260" class="comments-container"></div><div id="comment-tools-37260" class="comment-tools"></div><div class="clear"></div><div id="comment-37260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37263"></span>

<div id="answer-container-37263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37263-score" class="post-score" title="current number of votes">0</div><span id="post-37263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This can have a number of reasons, e.g.</p><ul><li>Decoding HTTP could be disabled. Check the "Analyze" -&gt; "Enabled Protocols" dialog to see if decoding HTTP is enabled</li><li>TCP reassembly can do unexpected things to your decoding. Check in "Edit" -&gt; "Preferences" -&gt; "Protocols" -&gt; "TCP" to see if "Allow subdissector to reassemble TCP streams" is the same on both systems</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37263" class="comments-container"></div><div id="comment-tools-37263" class="comment-tools"></div><div class="clear"></div><div id="comment-37263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

