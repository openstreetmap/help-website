+++
type = "question"
title = "Wireshark Features for bluetooth low energy"
description = '''Hi, I am evaluating different Bluetooth Low Energy sniffers. I was wondering the features that Wireshark provides for Bluetooth Low Energy:  Provide usage of filters? If so, if I enable the filters, does it still capture entire   traffic but only shows the filtered ones? Can the traffic be captured/...'''
date = "2016-06-22T17:12:00Z"
lastmod = "2016-06-23T00:26:00Z"
weight = 53620
keywords = [ "blesniffer" ]
aliases = [ "/questions/53620" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Features for bluetooth low energy](/questions/53620/wireshark-features-for-bluetooth-low-energy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53620-score" class="post-score" title="current number of votes">0</div><span id="post-53620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am evaluating different Bluetooth Low Energy sniffers.<br />
I was wondering the features that Wireshark provides for Bluetooth Low Energy:</p><ol><li>Provide usage of filters? If so, if I enable the filters, does it still capture entire traffic but only shows the filtered ones?</li><li>Can the traffic be captured/saved in a file?</li><li>Can this file be converted to a pdf file?</li><li>Can I download Wireshark sniffer -- windows 7, 64bit version?</li></ol><p>Thanks, Asha</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-blesniffer" rel="tag" title="see questions tagged &#39;blesniffer&#39;">blesniffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '16, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/dc52e8c323e4e9f79e3eeba39cb1b0bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashasingh18&#39;s gravatar image" /><p><span>ashasingh18</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashasingh18 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Jun '16, 00:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-53620" class="comments-container"></div><div id="comment-tools-53620" class="comment-tools"></div><div class="clear"></div><div id="comment-53620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53623"></span>

<div id="answer-container-53623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53623-score" class="post-score" title="current number of votes">0</div><span id="post-53623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'll try to give an itemised response.</p><ol><li>Wireshark contains a powerful general purpose filter engine (see <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">Users Guide</a>), which handles any dissected protocol. The display filter system influences only the frames shown, so all frames are captured. Capture can be filtered as well through the <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html">capture filter system</a></li><li>Captured frames can be saved <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChIOSaveSection.html">in various capture file formats</a></li><li>PDF output can be generated through <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChIOPrintSection.html">the print output system</a></li><li>Downloads are available through <a href="https://www.wireshark.org/#download">the projects download page</a></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '16, 00:26</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53623" class="comments-container"></div><div id="comment-tools-53623" class="comment-tools"></div><div class="clear"></div><div id="comment-53623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

