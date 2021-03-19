+++
type = "question"
title = "Configuring DICOM Protocol within 2.0.x"
description = '''Configuring new version of Wireshark for DICOM protocol differs from previous versions. In prior versions there was either all TCP ports or Heuristic mode box that could be checked. 2.0.x does not contain a configuration item like that, there is a single line for PORT. Are there wildcard characters ...'''
date = "2015-12-31T12:33:00Z"
lastmod = "2016-01-05T09:15:00Z"
weight = 48777
keywords = [ "dicom" ]
aliases = [ "/questions/48777" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Configuring DICOM Protocol within 2.0.x](/questions/48777/configuring-dicom-protocol-within-20x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48777-score" class="post-score" title="current number of votes">0</div><span id="post-48777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Configuring new version of Wireshark for DICOM protocol differs from previous versions. In prior versions there was either all TCP ports or Heuristic mode box that could be checked. 2.0.x does not contain a configuration item like that, there is a single line for PORT. Are there wildcard characters or a port range that needs to be entered to achieve the same result as heuristic mode?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dicom" rel="tag" title="see questions tagged &#39;dicom&#39;">dicom</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '15, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/33f3550b74419776d296a984aabb85b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BPOWELL&#39;s gravatar image" /><p><span>BPOWELL</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BPOWELL has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Dec '15, 15:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-48777" class="comments-container"><span id="48837"></span><div id="comment-48837" class="comment"><div id="post-48837-score" class="comment-score"></div><div class="comment-text"><p>Selecting Analyze--Enabled Protocols--DICOM---DICOM over TCP has no effect on the display of packets.</p></div><div id="comment-48837-info" class="comment-info"><span class="comment-age">(04 Jan '16, 07:04)</span> <span class="comment-user userinfo">BPOWELL</span></div></div></div><div id="comment-tools-48777" class="comment-tools"></div><div class="clear"></div><div id="comment-48777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48781"></span>

<div id="answer-container-48781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48781-score" class="post-score" title="current number of votes">0</div><span id="post-48781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For DICOM, 2.0.x has:</p><ul><li>a port range preference, "DICOM Ports range";</li><li>a heuristic dissector, disabled by default, which can be enabled in the "Enabled protocols" dialog from Analyze -&gt; Enabled protocols - search for "dicom" and check the box next to "DICOM over TCP".</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '15, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-48781" class="comments-container"><span id="48838"></span><div id="comment-48838" class="comment"><div id="post-48838-score" class="comment-score"></div><div class="comment-text"><p>Selecting Analyze--Enabled Protocols--DICOM---DICOM over TCP has no effect on the display of packets.</p></div><div id="comment-48838-info" class="comment-info"><span class="comment-age">(04 Jan '16, 07:06)</span> <span class="comment-user userinfo">BPOWELL</span></div></div><span id="48846"></span><div id="comment-48846" class="comment"><div id="post-48846-score" class="comment-score"></div><div class="comment-text"><p>This is working fine with the DICOM capture found in <a href="https://bugs.wireshark.org/bugzilla/attachment.cgi?id=1819">https://bugs.wireshark.org/bugzilla/attachment.cgi?id=1819</a> or <a href="https://bugs.wireshark.org/bugzilla/attachment.cgi?id=10032">https://bugs.wireshark.org/bugzilla/attachment.cgi?id=10032</a> for example</p><p>Could you provide your capture file?</p></div><div id="comment-48846-info" class="comment-info"><span class="comment-age">(04 Jan '16, 09:47)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="48874"></span><div id="comment-48874" class="comment"><div id="post-48874-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the feedback, my guess is some of the residual settings from the prior version may have been causing my issue. I performed an uninstall and removed everything. Installing from scratch, making the protocol change and then applying the coloring rules I have seems to have corrected my problem. I seem to be able to now consistently open captures and have them decoded as I would expect.</p></div><div id="comment-48874-info" class="comment-info"><span class="comment-age">(05 Jan '16, 09:15)</span> <span class="comment-user userinfo">BPOWELL</span></div></div></div><div id="comment-tools-48781" class="comment-tools"></div><div class="clear"></div><div id="comment-48781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

