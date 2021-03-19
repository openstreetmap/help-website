+++
type = "question"
title = "MODBUS/UDP Support"
description = '''One of our vendors implemented MODBUS/UDP in a system they delivered to us. We commonly use Wireshark to troubleshoot issues. However, I am now stuck using an old version of Wireshark because new versions no longer support MODBUS/UDP since it&#x27;s not an actual standard. I&#x27;ve found 1.6.4 Portable can s...'''
date = "2014-05-07T13:07:00Z"
lastmod = "2014-05-07T20:41:00Z"
weight = 32617
keywords = [ "modbus", "udp", "versions" ]
aliases = [ "/questions/32617" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [MODBUS/UDP Support](/questions/32617/modbusudp-support)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32617-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>One of our vendors implemented MODBUS/UDP in a system they delivered to us. We commonly use Wireshark to troubleshoot issues. However, I am now stuck using an old version of Wireshark because new versions no longer support MODBUS/UDP since it's not an actual standard. I've found 1.6.4 Portable can still dissect the MODBUS packets (and filter by MODBUS values), but it hangs sometimes when saving files. I know 1.10.0 on up will not dissect the MODBUS from UDP. The bug pages suggest using "Decode As..." but it's not even an option when I go to "Decode As..." anymore.</p><p>So, I have a couple questions: 1. What is the last version of Wireshark that could still dissect MODBUS/UDP? 2. Is there a work-around or some way to get a newer version to dissect MODBUS from within UDP?</p><p>Thank You.</p></div><div id="question-tags" class="tags-container tags">modbus udp versions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '14, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/7aa31b10303327434572773aabbc9b2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trashman&#39;s gravatar image" /><p>Trashman<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trashman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 May '14, 13:09</p></div></div><div id="comments-container-32617" class="comments-container"><span id="32619"></span><div id="comment-32619" class="comment"><div id="post-32619-score" class="comment-score"></div><div class="comment-text"><p>Update: Checked the last "old stable" version 1.8.14 (portable version). It dissects the MODBUS inside UDP, and it can also filter (though the filter syntax changed).</p></div><div id="comment-32619-info" class="comment-info"><span class="comment-age">(07 May '14, 13:55)</span> Trashman</div></div><span id="32620"></span><div id="comment-32620" class="comment"><div id="post-32620-score" class="comment-score"></div><div class="comment-text"><p>In case anyone asks, I've tried 1.10.0, 1.10.1, 1.10.5, and 1.10.7 both 64-bit full installs and 32-bit portable versions - none of them were able to dissect MODBUS from UDP. It appears I've answered question 1 myself, 1.8.14 supports it and appears to work well. I know it's always best to use the latest software, however, so I'd like to be able to use 1.10.x and future versions if anyone knows of a workaround.</p></div><div id="comment-32620-info" class="comment-info"><span class="comment-age">(07 May '14, 14:02)</span> Trashman</div></div></div><div id="comment-tools-32617" class="comment-tools"></div><div class="clear"></div><div id="comment-32617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32631"></span>

<div id="answer-container-32631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32631-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you may have seen, it looks like Wireshark MODBUS/UDP support was added and then removed some time later two times. (I didn't dig further to determine the exact Wireshark versions which included the support).</p><p>As you've noted, there's no support for MODBUS/UDP or MODBUS "decode as" over UDP in the current Wireshark 1.10 &amp; newer. I believe the bug comment you saw meant only that "decode as" to support MODBUS/UDP could be implemented if needed.</p><p>So: there's no workaround to dissect MODBUS/UDP with the current Wireshark.</p><p>If you like, you can submit an "enhancement request" at bugs.wireshark.org making the case to again add MODBUS/UDP support to Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '14, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-32631" class="comments-container"><span id="33102"></span><div id="comment-33102" class="comment"><div id="post-33102-score" class="comment-score"></div><div class="comment-text"><p>Hello, I have the same problem. We use Modbus UDP. I also use the old portable Version to make analysis from our Network, because the new Version doesn´t support Modbus UDP. Why is it not supported now ? Is it planned to support it again in the next version ?</p></div><div id="comment-33102-info" class="comment-info"><span class="comment-age">(27 May '14, 01:46)</span> Genesis</div></div><span id="33103"></span><div id="comment-33103" class="comment"><div id="post-33103-score" class="comment-score"></div><div class="comment-text"><p>See the answer provided by @Bill Meier above.</p></div><div id="comment-33103-info" class="comment-info"><span class="comment-age">(27 May '14, 02:06)</span> grahamb ♦</div></div></div><div id="comment-tools-32631" class="comment-tools"></div><div class="clear"></div><div id="comment-32631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

