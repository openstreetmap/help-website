+++
type = "question"
title = "Wireshark on Windows 7 Hangs then Stops Working when Attempting to Select a Path for GeoIP Files"
description = '''This problems occurs on two Windows 7 machines available to me. Windows 7 Enterprise with Service Pack 1 and Windows 7 Ultimate with Service Pack 1. Wireshark Version 1.12.0 and does have &quot;with GeoIP&quot; in the About Box. Click Edit, Preferences..., Name Resolution, then Edit... on the button next to G...'''
date = "2014-08-28T14:49:00Z"
lastmod = "2014-08-28T15:27:00Z"
weight = 35851
keywords = [ "path", "gui", "geoip" ]
aliases = [ "/questions/35851" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on Windows 7 Hangs then Stops Working when Attempting to Select a Path for GeoIP Files](/questions/35851/wireshark-on-windows-7-hangs-then-stops-working-when-attempting-to-select-a-path-for-geoip-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35851-score" class="post-score" title="current number of votes">0</div><span id="post-35851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This problems occurs on two Windows 7 machines available to me. Windows 7 Enterprise with Service Pack 1 and Windows 7 Ultimate with Service Pack 1. Wireshark Version 1.12.0 and does have "with GeoIP" in the About Box.</p><p>Click Edit, Preferences..., Name Resolution, then Edit... on the button next to GeoIP database directories. Click New then attempt to select a drive letter or any other item displayed in the dropdownlistbox. Wireshark hangs then eventually a dialog box appears: "Wireshark has stopped working" "A problem caused the program to stop working correctly. Windows will close the program and notify you if a solution is available."</p><p>NOTE: The same happens when attempting to select SMI (MIB and PIB) paths. This appears to be a problem dealing with selecting drives &amp; paths in Windows and not specific to GeoIP.</p><p>Thanks, ds</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-geoip" rel="tag" title="see questions tagged &#39;geoip&#39;">geoip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '14, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/860aa5dc893bb7e9a4023e98dddea895?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DStackley&#39;s gravatar image" /><p><span>DStackley</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DStackley has no accepted answers">0%</span></p></div></div><div id="comments-container-35851" class="comments-container"></div><div id="comment-tools-35851" class="comment-tools"></div><div class="clear"></div><div id="comment-35851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35853"></span>

<div id="answer-container-35853" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35853-score" class="post-score" title="current number of votes">0</div><span id="post-35853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I can confirm this, only happens with the gtk version, so somethings broken in the gtk uat handler.</p><p>Can you check for an existing bug for this at the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a>, and if there isn't one, raise a new entry following the guidelines in the wiki <a href="http://wiki.wireshark.org/ReportingBugs">Reporting Bugs</a> page?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '14, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35853" class="comments-container"></div><div id="comment-tools-35853" class="comment-tools"></div><div class="clear"></div><div id="comment-35853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

