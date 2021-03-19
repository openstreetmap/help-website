+++
type = "question"
title = "Develop a SIP&amp;RTP display filter"
description = '''Hi, I&#x27;m trying to find out the way to make a display filter that includes two different, but related, protocols. I mean, SIP messages contains information about RTP ports. What I am doing now is:  Filter a SIP flow Analyse which ports RTP is using Add this information to the display filter Filter ag...'''
date = "2012-11-21T04:27:00Z"
lastmod = "2012-11-22T04:56:00Z"
weight = 16154
keywords = [ "sip", "rtp", "dissector", "display-filter" ]
aliases = [ "/questions/16154" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Develop a SIP&RTP display filter](/questions/16154/develop-a-siprtp-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16154-score" class="post-score" title="current number of votes">0</div><span id="post-16154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to find out the way to make a display filter that includes two different, but related, protocols. I mean, SIP messages contains information about RTP ports. What I am doing now is:</p><ol><li>Filter a SIP flow</li><li>Analyse which ports RTP is using</li><li>Add this information to the display filter</li><li>Filter again.</li></ol><p>I'd like to develop a filter to do it automatically but I've seen nothing similar. Should I develop a chained-dissector, a post-dissector or should I develop inside display filter?</p><p>I've taken a look at this: <a href="http://wiki.wireshark.org/Lua/Examples#Dump_VoIP_calls_into_separate_files">http://wiki.wireshark.org/Lua/Examples#Dump_VoIP_calls_into_separate_files</a></p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '12, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/5aa3e602fe20c86ecbe0c2bf2353efef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robin&#39;s gravatar image" /><p><span>Robin</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robin has no accepted answers">0%</span></p></div></div><div id="comments-container-16154" class="comments-container"></div><div id="comment-tools-16154" class="comment-tools"></div><div class="clear"></div><div id="comment-16154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16199"></span>

<div id="answer-container-16199" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16199-score" class="post-score" title="current number of votes">1</div><span id="post-16199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Robin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://wiki.wireshark.org/Mate">MATE</a> is your friend here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 04:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16199" class="comments-container"><span id="16207"></span><div id="comment-16207" class="comment"><div id="post-16207-score" class="comment-score"></div><div class="comment-text"><p>I've just read the description, it seems to fit perfect. Thank you so much!</p></div><div id="comment-16207-info" class="comment-info"><span class="comment-age">(22 Nov '12, 04:56)</span> <span class="comment-user userinfo">Robin</span></div></div></div><div id="comment-tools-16199" class="comment-tools"></div><div class="clear"></div><div id="comment-16199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

