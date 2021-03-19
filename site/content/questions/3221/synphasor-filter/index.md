+++
type = "question"
title = "synphasor filter"
description = '''I&#x27;m capturing IEEE C37.118 packets with the synphasor filter and in the data frames where the measurement data should be shown it says &quot;Measurement data, no configuration frame found&quot; even though there is a configuration frame as the 3rd packet in the capture.  Is there a certain way to associate th...'''
date = "2011-03-29T21:42:00Z"
lastmod = "2013-02-19T01:09:00Z"
weight = 3221
keywords = [ "synphasor" ]
aliases = [ "/questions/3221" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [synphasor filter](/questions/3221/synphasor-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3221-score" class="post-score" title="current number of votes">0</div><span id="post-3221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm capturing IEEE C37.118 packets with the synphasor filter and in the data frames where the measurement data should be shown it says "Measurement data, no configuration frame found" even though there is a configuration frame as the 3rd packet in the capture. Is there a certain way to associate the configuration frame with the data frames in the capture? How is it done? Need help!</p><p>Thank you!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-synphasor" rel="tag" title="see questions tagged &#39;synphasor&#39;">synphasor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '11, 21:42</strong></p><img src="https://secure.gravatar.com/avatar/abbee233c9292ba7fe859116093d7afb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aginosian&#39;s gravatar image" /><p><span>aginosian</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aginosian has no accepted answers">0%</span></p></div></div><div id="comments-container-3221" class="comments-container"><span id="18727"></span><div id="comment-18727" class="comment"><div id="post-18727-score" class="comment-score"></div><div class="comment-text"><p>yes its found that wire-shark is not taking the frames in cases:</p><p>1.data channel is udp and command channel is tcp :udp_t 2. Wireshark started after pdc,pmu's started</p></div><div id="comment-18727-info" class="comment-info"><span class="comment-age">(18 Feb '13, 23:43)</span> <span class="comment-user userinfo">Gokul Cg</span></div></div><span id="18728"></span><div id="comment-18728" class="comment"><div id="post-18728-score" class="comment-score"></div><div class="comment-text"><p>Please raise a bug (if there isn't one already) at the <a href="http://bugs.wireshark.org">BugTracker</a>, and attach a capture file that illustrates the problem.</p></div><div id="comment-18728-info" class="comment-info"><span class="comment-age">(19 Feb '13, 01:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-3221" class="comment-tools"></div><div class="clear"></div><div id="comment-3221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

