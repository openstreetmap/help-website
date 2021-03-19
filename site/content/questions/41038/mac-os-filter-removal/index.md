+++
type = "question"
title = "Mac OS filter removal"
description = '''I am running Mountain lion 10.8 and cannot remove the displayed filter located on the top of the main screen to the right of expression. In my enclosed pic its &quot;ME-exclude my ip src DST&quot; i have uninstalled and it still appears. How can I remove the filter?! Screen shot'''
date = "2015-03-30T14:57:00Z"
lastmod = "2015-03-30T15:14:00Z"
weight = 41038
keywords = [ "filter" ]
aliases = [ "/questions/41038" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OS filter removal](/questions/41038/mac-os-filter-removal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41038-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Mountain lion 10.8 and cannot remove the displayed filter located on the top of the main screen to the right of expression. In my enclosed pic its "ME-exclude my ip src DST"</p><p>i have uninstalled and it still appears. How can I remove the filter?! <a href="https://osqa-ask.wireshark.org/upfiles/wireshark_filter_removal.tiff">Screen shot</a></p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '15, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/a26768b463fa78c6915bbea890fca049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mewireshark&#39;s gravatar image" /><p>mewireshark<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mewireshark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Mar '15, 15:00</p></div></div><div id="comments-container-41038" class="comments-container"></div><div id="comment-tools-41038" class="comment-tools"></div><div class="clear"></div><div id="comment-41038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41039"></span>

<div id="answer-container-41039" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41039-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go to</p><blockquote><p>Edit -&gt; Preferences -&gt; Filter Expressions</p></blockquote><p>Select the filter and click Remove.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '15, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41039" class="comments-container"><span id="41041"></span><div id="comment-41041" class="comment"><div id="post-41041-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt. any idea why it remained after performing an unistall as follows. #4 I rebooted instead. How do I uninstall?</p><pre><code>1.  Remove /Applications/Wireshark.app
2.  Remove /Library/Application Support/Wireshark
3.  Remove the wrapper scripts from /usr/local/bin
4.  Unload the org.wireshark.ChmodBPF.plist launchd job
5.  Remove /Library/LaunchDaemons/org.wireshark.ChmodBPF.plist
6.  Remove the access_bpf group.</code></pre></div><div id="comment-41041-info" class="comment-info"><span class="comment-age">(30 Mar '15, 19:45)</span> mewireshark</div></div><span id="41042"></span><div id="comment-41042" class="comment"><div id="post-41042-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-41042-info" class="comment-info"><span class="comment-age">(31 Mar '15, 01:56)</span> Jaap ♦</div></div><span id="41046"></span><div id="comment-41046" class="comment"><div id="post-41046-score" class="comment-score"></div><div class="comment-text"><blockquote><p>any idea why it remained after performing an unistall as follows</p></blockquote><p>Maybe because it's in your personal Wireshark preferences file, which probably survived the uninstall !?!</p><p>Did you try the steps I mentioned in my answer?</p></div><div id="comment-41046-info" class="comment-info"><span class="comment-age">(31 Mar '15, 03:18)</span> Kurt Knochner ♦</div></div><span id="41229"></span><div id="comment-41229" class="comment"><div id="post-41229-score" class="comment-score"></div><div class="comment-text"><p>Kurt is correct when he says "Maybe because it's in your personal Wireshark preferences file" - uninstalls of applications generally do <em>not</em> remove personal configuration files for those applications.</p></div><div id="comment-41229-info" class="comment-info"><span class="comment-age">(06 Apr '15, 10:35)</span> Guy Harris ♦♦</div></div><span id="41242"></span><div id="comment-41242" class="comment"><div id="post-41242-score" class="comment-score"></div><div class="comment-text"><p>thanks. I did not expect the hidden file to exist after uninstall.</p></div><div id="comment-41242-info" class="comment-info"><span class="comment-age">(07 Apr '15, 03:10)</span> mewireshark</div></div></div><div id="comment-tools-41039" class="comment-tools"></div><div class="clear"></div><div id="comment-41039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

