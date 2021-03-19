+++
type = "question"
title = "Capture Filters under Windows 2008 Server"
description = '''I recently updated to Wireshark 1.8.5 and now I can not get a capture filter to work. I go to Capture -&amp;gt; Capture Filters and select a saved filter (host xxx.xxx.xxx.xxx) and click OK. When I try to start the capture, it captures all packets on the interface. I have tried double clicking on the Ca...'''
date = "2013-02-15T06:56:00Z"
lastmod = "2013-02-15T09:03:00Z"
weight = 18654
keywords = [ "capture", "capture-filter", "capture-setup" ]
aliases = [ "/questions/18654" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filters under Windows 2008 Server](/questions/18654/capture-filters-under-windows-2008-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18654-score" class="post-score" title="current number of votes">0</div><span id="post-18654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently updated to Wireshark 1.8.5 and now I can not get a capture filter to work.</p><p>I go to Capture -&gt; Capture Filters and select a saved filter (host xxx.xxx.xxx.xxx) and click OK. When I try to start the capture, it captures all packets on the interface.</p><p>I have tried double clicking on the Capture Filter name in the dialog box. I have also tried to apply while a current capture is in process and when the capture is stopped - all to no avail.</p><p>The help documents for capture filters are not very clear on how to actually start a capture with a filter applied.</p><p>Do you have any suggestion?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-capture-setup" rel="tag" title="see questions tagged &#39;capture-setup&#39;">capture-setup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '13, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/a5192266a15ff06ea8ad67056fffacf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EagleTRL57&#39;s gravatar image" /><p><span>EagleTRL57</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EagleTRL57 has no accepted answers">0%</span></p></div></div><div id="comments-container-18654" class="comments-container"></div><div id="comment-tools-18654" class="comment-tools"></div><div class="clear"></div><div id="comment-18654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18656"></span>

<div id="answer-container-18656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18656-score" class="post-score" title="current number of votes">1</div><span id="post-18656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capture &gt; Capture Filters takes you to a dialog for adding, editing, deleting, and saving capture filters, not applying capture filters. In fact, when I do this with 1.8.5 PortableApps version,there is no "Ok" to click on, only Save or Cancel.</p><p>To apply a capture filter, go to Capture &gt; Options, double-click the interface you're going to capture on, and then enter your capture filter in the Capture Filter field. If you want to select a saved filter, you can click on the Capture Filter button to the left of the capture filter input area.</p><p>When your capture filter has been entered and the syntax is correct (green background), click OK. On the Capture Options dialog, make sure the interface is selected (the checkbox in the "Capture" column is checked) and click Start.</p><p>You cannot apply a capture filter during a running capture, only while capturing is stopped.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '13, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-18656" class="comments-container"><span id="18658"></span><div id="comment-18658" class="comment"><div id="post-18658-score" class="comment-score"></div><div class="comment-text"><p>Got it - thanks! I am not sure how I managed to get the filters applied before, but I don't remember doing those steps.</p></div><div id="comment-18658-info" class="comment-info"><span class="comment-age">(15 Feb '13, 08:59)</span> <span class="comment-user userinfo">EagleTRL57</span></div></div><span id="18659"></span><div id="comment-18659" class="comment"><div id="post-18659-score" class="comment-score"></div><div class="comment-text"><p>The capture dialog changed in 1.8.x to allow capturing from multiple interfaces.</p></div><div id="comment-18659-info" class="comment-info"><span class="comment-age">(15 Feb '13, 09:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-18656" class="comment-tools"></div><div class="clear"></div><div id="comment-18656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

