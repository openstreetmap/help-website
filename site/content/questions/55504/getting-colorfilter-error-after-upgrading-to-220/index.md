+++
type = "question"
title = "Getting Colorfilter error after upgrading to 2.2.0"
description = '''After I upgraded to 2.2.0, I now get the following error in the Wireshark debug console when selecting one of my configuration profiles. My profiles did not change, and never had an issue with any earlier version. Has anyone else had this issue? 21:15:40 Warn Could not compile &quot;Checksum Errors&quot; in c...'''
date = "2016-09-12T19:25:00Z"
lastmod = "2016-09-12T22:52:00Z"
weight = 55504
keywords = [ "color-rules", "debug", "2.2.0" ]
aliases = [ "/questions/55504" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Getting Colorfilter error after upgrading to 2.2.0](/questions/55504/getting-colorfilter-error-after-upgrading-to-220)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55504-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After I upgraded to 2.2.0, I now get the following error in the Wireshark debug console when selecting one of my configuration profiles. My profiles did not change, and never had an issue with any earlier version.</p><p>Has anyone else had this issue?</p><p><strong>21:15:40 Warn Could not compile "Checksum Errors" in colorfilters file "C:\Dropbox\PROFILES-SETTINGS-SOURCEDATA\Wireshark\PersonalConfiguration\profiles\VoIP - SIP\colorfilters". eth.fcs_bad (type=Label) cannot participate in '==' comparison.</strong></p></div><div id="question-tags" class="tags-container tags">color-rules debug 2.2.0</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '16, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-55504" class="comments-container"></div><div id="comment-tools-55504" class="comment-tools"></div><div class="clear"></div><div id="comment-55504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55510"></span>

<div id="answer-container-55510" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55510-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>As indicated in the <a href="https://www.wireshark.org/docs/relnotes/wireshark-2.2.0.html">release notes</a>, the format for the checksum coloring rules was changed:</p><p>proto_tree_add_checksum was added as an API. This attempts to standardize how checksums are reported and filtered for within *Shark. There are no more individual "good" and "bad" filter fields, protocols now have a "checksum.status" field that records "Good", "Bad" and "Unverified" (neither good or bad). Color filters provided with Wireshark have been adjusted to the new display filter names, but custom ones may need to be updated.</p><p>So you need to update your profile accordingly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '16, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-55510" class="comments-container"><span id="55511"></span><div id="comment-55511" class="comment"><div id="post-55511-score" class="comment-score"></div><div class="comment-text"><p>This practically means to go through your colorization rules in that profile (file <code>cfilters</code> in the profile directory) using a text editor, search for <code>eth.cfs_bad</code> in it, and update the affected part of the failing rule(s) from old <code>eth.fcs_bad == true</code> to <code>!(eth.fcs.status == Good)</code> or another one better suiting your needs.</p></div><div id="comment-55511-info" class="comment-info"><span class="comment-age">(12 Sep '16, 22:57)</span> sindy</div></div><span id="55517"></span><div id="comment-55517" class="comment"><div id="post-55517-score" class="comment-score"></div><div class="comment-text"><p>A checksum status, such as <code>eth.fcs.status</code>, can have one of four values:</p><ul><li>"Good" - this means the checksum was checked and it's correct;</li><li>"Bad" - this means the checksum was checked and it's not correct;</li><li>"Unverified" - this means the checksum was present, but wasn't checked (for example, because not all the data the checksum covers was captured, so it's impossible to check it);</li><li>"Not present" - this means the checksum field was present, but has a special value meaning "no checksum" - 0 is used in some protocols to mean "no checksum was computed for this packet, so there's no checksum check to be done").</li></ul><p>So if you want to flag all packets with a bad checksum with a particular color, the filter expression would be something such as <code>eth.fcs.status == "Bad"</code>.</p></div><div id="comment-55517-info" class="comment-info"><span class="comment-age">(13 Sep '16, 01:49)</span> Guy Harris ♦♦</div></div><span id="55546"></span><div id="comment-55546" class="comment"><div id="post-55546-score" class="comment-score"></div><div class="comment-text"><p>Thank you to Pascal, sindy, and Guy for all of your help. I finally got all of my profiles cleaned up and working now. Thanks again!</p></div><div id="comment-55546-info" class="comment-info"><span class="comment-age">(13 Sep '16, 22:34)</span> Rooster_50</div></div></div><div id="comment-tools-55510" class="comment-tools"></div><div class="clear"></div><div id="comment-55510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

