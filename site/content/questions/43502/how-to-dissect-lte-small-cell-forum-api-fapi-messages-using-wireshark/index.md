+++
type = "question"
title = "How to dissect LTE Small Cell Forum API (FAPI) messages  Using Wireshark?"
description = '''Hi all, Thank you for your valuable support. I want to know how to dissect LTE Small Cell Forum API (FAPI) messages using wireshark. Thanks and Regards, Sathish'''
date = "2015-06-24T06:27:00Z"
lastmod = "2015-06-24T12:02:00Z"
weight = 43502
keywords = [ "pcap", "lte", "dissectors" ]
aliases = [ "/questions/43502" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect LTE Small Cell Forum API (FAPI) messages Using Wireshark?](/questions/43502/how-to-dissect-lte-small-cell-forum-api-fapi-messages-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43502-score" class="post-score" title="current number of votes">0</div><span id="post-43502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Thank you for your valuable support.</p><p>I want to know how to dissect LTE Small Cell Forum API (FAPI) messages using wireshark.</p><p>Thanks and Regards, Sathish</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span> <span class="post-tag tag-link-dissectors" rel="tag" title="see questions tagged &#39;dissectors&#39;">dissectors</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '15, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/7ba5607f38325cbf87766b918e1d76a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sathish%20kannan&#39;s gravatar image" /><p><span>Sathish kannan</span><br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sathish kannan has no accepted answers">0%</span></p></div></div><div id="comments-container-43502" class="comments-container"><span id="43519"></span><div id="comment-43519" class="comment"><div id="post-43519-score" class="comment-score"></div><div class="comment-text"><p>I have written a dissector for one flavour of FAPI, which in my case was sent out over a UDP port. The stack we used sent out frames that were close to, but not exactly, what you find in LTE+eNB+L1+API+Definition.pdf. It was very useful, in terms of tracking information forward from UL/DL config requests to the MAC PDUs (for which I filled in the PHY attributes then called the MAC dissector), and linking back from the HARQ status, and setting appropriate expert info. Of course the capture files were enormous (not helped by some questionable choices made in FAPI implementation we used).</p><p>So it can be done, but due to differences between different vendors' FAPI implementations, and possible issues with releasing GPL code specific to their implementations, I'm not sure if the code I wrote may be shared. It was not trivial, around 3,500 lines of code.</p></div><div id="comment-43519-info" class="comment-info"><span class="comment-age">(24 Jun '15, 12:02)</span> <span class="comment-user userinfo">MartinM</span></div></div></div><div id="comment-tools-43502" class="comment-tools"></div><div class="clear"></div><div id="comment-43502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

